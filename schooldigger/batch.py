"""Helpers for the SchoolDigger async batch service (https://api.schooldigger.com/batches).

Hand-written, not generated: listed in .openapi-generator-ignore so regeneration
keeps it. Import it as a submodule:

    from schooldigger.batch import BatchClient, verify_signature

The batch service runs up to 2,000 API GET calls for you, paced at half your
plan's per-minute limit, and returns the results in parts of 20 items as
gzipped NDJSON. See https://developer.schooldigger.com/batch-requests-schooldigger-api
"""

import hashlib
import hmac
import json
import time
from typing import Any, Dict, Iterable, Iterator, List, NamedTuple, Optional, Union
from urllib.parse import quote, urlencode

from schooldigger.configuration import Configuration
from schooldigger.rest import RESTClientObject

__all__ = [
    "BatchClient",
    "BatchError",
    "BatchNotCompletedError",
    "BatchPart",
    "verify_signature",
    "ACTIVE_STATUSES",
]

DEFAULT_BASE_URL = "https://api.schooldigger.com"

#: Statuses during which a batch still runs (the status call sends Retry-After).
ACTIVE_STATUSES = ("queued", "running")

BatchItem = Union[str, Dict[str, str]]


class BatchError(Exception):
    """An error response from the batch service.

    Carries the service's error shape ``{code, message, description, help}``
    plus ``errors`` (submit validation) and the HTTP ``status``. The request URL
    (which holds the appKey) is never included.
    """

    def __init__(self, status: int, body: Any = None, text: Optional[str] = None) -> None:
        self.status = status
        self.body = body
        b = body if isinstance(body, dict) else {}
        self.code = b.get("code", status)
        self.message = b.get("message")
        self.description = b.get("description") or (text[:500] if text else None)
        self.help = b.get("help")
        self.errors: List[str] = list(b.get("errors") or [])
        super().__init__(f"HTTP {status}: {self.message or ''} {self.description or ''}".strip())


class BatchNotCompletedError(BatchError):
    """Raised by ``wait_for_batch`` when a batch ends ``failed``, ``canceled`` or ``expired``.

    ``batch`` holds the final status. Parts that were ready were yielded first.
    """

    def __init__(self, batch: Dict[str, Any]) -> None:
        self.batch = batch
        super().__init__(200, {"message": f"Batch {batch.get('batchId')} ended {batch.get('status')}"})


class BatchPart(NamedTuple):
    """One downloaded result part: its number and its decoded NDJSON lines.

    Each result is ``{"id", "path", "status", "body"}`` (plus ``"error"`` when
    the response wasn't JSON). ``body`` is the exact JSON the same GET returns.
    """

    part: int
    results: List[Dict[str, Any]]


class BatchClient:
    """Client for the 4 batch routes. Uses urllib3, like the generated SDK.

    Pass ``app_id`` / ``app_key``, or a ``schooldigger.Configuration`` whose
    ``api_key["appID"]`` / ``api_key["appKey"]`` are set (its proxy and SSL
    settings are used too).
    """

    def __init__(
        self,
        app_id: Optional[str] = None,
        app_key: Optional[str] = None,
        *,
        configuration: Optional[Configuration] = None,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = 120,
    ) -> None:
        config = configuration or Configuration()
        self._app_id = app_id or config.api_key.get("appID")
        self._app_key = app_key or config.api_key.get("appKey")
        if not self._app_id or not self._app_key:
            raise ValueError("BatchClient needs an appID and appKey")
        self._base = base_url.rstrip("/")
        self._timeout = timeout
        self._pool = RESTClientObject(config).pool_manager

    # ---- the 4 routes ----

    def submit_batch(self, items: Iterable[BatchItem], callback_url: Optional[str] = None) -> Dict[str, Any]:
        """POST /batches. ``items`` are ``{"id", "path"}`` dicts or plain path strings
        (``"/v3.1/schools/064215006903"``; the id defaults to the item's index).
        Returns the 202 body: batchId, status, itemCount, partSize, partCount,
        estimatedSeconds, statusUrl.
        """
        body: Dict[str, Any] = {"items": [{"path": i} if isinstance(i, str) else dict(i) for i in items]}
        if callback_url:
            body["callbackUrl"] = callback_url
        r = self._request("POST", "/batches", body=json.dumps(body).encode("utf-8"))
        return self._json(r)

    def get_batch(self, batch_id: str) -> Dict[str, Any]:
        """GET /batches/{batchId}: the batch status (status, completedCount, partsReady, ...)."""
        return self._get_status(batch_id)[0]

    def get_batch_results(self, batch_id: str, part: int) -> List[Dict[str, Any]]:
        """GET /batches/{batchId}/results?part=N: one part, decoded from gzipped NDJSON.

        Raises ``BatchError`` with status 409 if the part isn't ready, 410 after retention.
        """
        r = self._request("GET", f"/batches/{quote(batch_id, safe='')}/results", {"part": str(part)})
        if r.status != 200:
            raise self._error(r)
        text = r.data.decode("utf-8")
        return [json.loads(line) for line in text.splitlines() if line.strip()]

    def cancel_batch(self, batch_id: str) -> Dict[str, Any]:
        """DELETE /batches/{batchId}: stop a queued or running batch. Returns its status."""
        return self._json(self._request("DELETE", f"/batches/{quote(batch_id, safe='')}"))

    # ---- polling ----

    def wait_for_batch(
        self,
        batch_id: str,
        *,
        timeout: Optional[float] = None,
        max_poll_seconds: float = 60,
    ) -> Iterator[BatchPart]:
        """Poll the batch (waiting ``Retry-After`` seconds between polls) and yield each
        part as soon as it is ready, in part order within each poll.

        Stops when the batch is ``completed``. If it ends ``failed``, ``canceled`` or
        ``expired``, the parts that were ready are yielded first, then
        ``BatchNotCompletedError`` is raised. ``timeout`` (seconds) raises
        ``TimeoutError``; the batch keeps running.
        """
        deadline = None if timeout is None else time.monotonic() + timeout
        done = set()
        while True:
            status, retry_after = self._get_status(batch_id)
            for part in sorted(p for p in status.get("partsReady", []) if p not in done):
                results = self.get_batch_results(batch_id, part)
                done.add(part)
                yield BatchPart(part, results)
            state = status.get("status")
            if state not in ACTIVE_STATUSES:
                if state == "completed":
                    return
                raise BatchNotCompletedError(status)
            wait = min(retry_after if retry_after is not None else 15, max_poll_seconds)
            if deadline is not None:
                left = deadline - time.monotonic()
                if left <= 0:
                    raise TimeoutError(f"Batch {batch_id} is still {state}")
                wait = min(wait, left)
            time.sleep(max(wait, 1))

    # ---- internals ----

    def _get_status(self, batch_id: str):
        r = self._request("GET", f"/batches/{quote(batch_id, safe='')}")
        status = self._json(r)
        ra = r.headers.get("Retry-After")
        try:
            retry_after = float(ra) if ra is not None else None
        except ValueError:
            retry_after = None
        return status, retry_after

    def _request(self, method: str, path: str, query: Optional[Dict[str, str]] = None, body: Optional[bytes] = None):
        params = {"appID": self._app_id, "appKey": self._app_key, **(query or {})}
        url = f"{self._base}{path}?{urlencode(params)}"
        headers = {"Accept": "application/json, application/x-ndjson", "Accept-Encoding": "gzip"}
        if body is not None:
            headers["Content-Type"] = "application/json"
        try:
            return self._pool.request(method, url, body=body, headers=headers, timeout=self._timeout, retries=False)
        except Exception as e:  # urllib3 errors embed the URL, which holds the appKey
            raise ConnectionError(f"{method} {self._base}{path} failed: {type(e).__name__}") from None

    def _json(self, r) -> Dict[str, Any]:
        if r.status >= 400:
            raise self._error(r)
        return json.loads(r.data.decode("utf-8"))

    @staticmethod
    def _error(r) -> BatchError:
        text = r.data.decode("utf-8", errors="replace") if r.data else ""
        try:
            body = json.loads(text) if text else None
        except ValueError:
            body = None
        return BatchError(r.status, body, None if body is not None else text)


def verify_signature(raw_body: bytes, signature_header: Optional[str], app_key: str) -> bool:
    """Check a callback's ``X-SchoolDigger-Signature`` header.

    The header is ``sha256=`` + hex HMAC-SHA256 of the raw request body, keyed by the
    UTF-8 bytes of the lowercase hex SHA-256 of your appKey. Pass the body bytes
    exactly as received (before any JSON parsing).
    """
    if not signature_header:
        return False
    if isinstance(raw_body, str):
        raw_body = raw_body.encode("utf-8")
    key = hashlib.sha256(app_key.encode("utf-8")).hexdigest().encode("utf-8")
    expected = "sha256=" + hmac.new(key, raw_body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature_header.strip().lower())
