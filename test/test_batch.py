# coding: utf-8
"""Tests for the hand-written batch helpers (schooldigger/batch.py).

The signature tests run offline. The live test submits a real 25-item batch and
runs only when SCHOOLDIGGER_BATCH_LIVE=1 and SCHOOLDIGGER_APP_ID /
SCHOOLDIGGER_APP_KEY are set (a paid-plan key; each item counts as one API call):

    SCHOOLDIGGER_BATCH_LIVE=1 python -m unittest test.test_batch -v
"""

import hashlib
import hmac
import json
import os
import time
import unittest
from urllib.parse import urlencode

import urllib3

from schooldigger.batch import BatchClient, BatchError, verify_signature


class TestVerifySignature(unittest.TestCase):
    APP_KEY = "0123456789abcdef0123456789abcdef"
    BODY = b'{"batchId":"b_0123456789ab","status":"completed","itemCount":3}'

    def header(self, body=BODY, app_key=APP_KEY):
        key = hashlib.sha256(app_key.encode()).hexdigest().encode()
        return "sha256=" + hmac.new(key, body, hashlib.sha256).hexdigest()

    def test_valid(self):
        self.assertTrue(verify_signature(self.BODY, self.header(), self.APP_KEY))

    def test_known_vector(self):
        # Fixed vector shared with the JS SDK's test (test/batch.test.js).
        self.assertEqual(self.header(), KNOWN_SIGNATURE)
        self.assertTrue(verify_signature(self.BODY, KNOWN_SIGNATURE, self.APP_KEY))
        self.assertTrue(verify_signature(self.BODY, KNOWN_SIGNATURE.upper().replace("SHA256=", "sha256="), self.APP_KEY))

    def test_str_body(self):
        self.assertTrue(verify_signature(self.BODY.decode(), self.header(), self.APP_KEY))

    def test_tampered_body(self):
        self.assertFalse(verify_signature(self.BODY + b" ", self.header(), self.APP_KEY))

    def test_wrong_key(self):
        self.assertFalse(verify_signature(self.BODY, self.header(app_key="other"), self.APP_KEY))

    def test_missing_header(self):
        self.assertFalse(verify_signature(self.BODY, None, self.APP_KEY))
        self.assertFalse(verify_signature(self.BODY, "", self.APP_KEY))


KNOWN_SIGNATURE = "sha256=54a7f7b0c067adfbdf8cce54d263b0c92c7b06ed628e7eca4ab709b8b180f9cc"


LIVE = (os.environ.get("SCHOOLDIGGER_BATCH_LIVE") == "1"
        and os.environ.get("SCHOOLDIGGER_APP_ID") and os.environ.get("SCHOOLDIGGER_APP_KEY"))


@unittest.skipUnless(LIVE, "set SCHOOLDIGGER_BATCH_LIVE=1 and SCHOOLDIGGER_APP_ID/KEY to run")
class TestBatchLive(unittest.TestCase):
    def test_batch_matches_single_gets(self):
        app_id, app_key = os.environ["SCHOOLDIGGER_APP_ID"], os.environ["SCHOOLDIGGER_APP_KEY"]
        http = urllib3.PoolManager()

        def single_get(path):
            sep = "&" if "?" in path else "?"
            r = http.request("GET", f"https://api.schooldigger.com{path}{sep}"
                             + urlencode({"appID": app_id, "appKey": app_key}))
            return r.status, json.loads(r.data)

        status, listing = single_get("/v3.1/schools?st=WA&districtID=5301110&perPage=50")
        self.assertEqual(status, 200)
        ids = [s["schoolid"] for s in listing["schoolList"]][:25]
        self.assertEqual(len(ids), 25)
        items = [{"id": f"s{i}", "path": f"/v3.1/schools/{sid}"} for i, sid in enumerate(ids)]

        client = BatchClient(app_id, app_key)
        with self.assertRaises(BatchError) as bad:
            client.submit_batch([{"id": "x", "path": "/v3.1/schools/1?appKey=no"}])
        self.assertEqual(bad.exception.status, 400)
        self.assertTrue(bad.exception.errors)

        started = time.monotonic()
        sub = client.submit_batch(items)
        batch_id = sub["batchId"]
        finished = False
        try:
            self.assertEqual(sub["status"], "queued")
            self.assertEqual(sub["itemCount"], 25)
            self.assertEqual(sub["partCount"], 2)
            parts = {}
            for part in client.wait_for_batch(batch_id, timeout=600):
                print(f"  part {part.part}: {len(part.results)} items at {time.monotonic() - started:.0f}s")
                parts[part.part] = part.results
            finished = True
            self.assertEqual(sorted(parts), [0, 1])
            final = client.get_batch(batch_id)
            self.assertEqual(final["status"], "completed")
            self.assertEqual(final["partsReady"], [0, 1])
            results = parts[0] + parts[1]
            self.assertEqual([r["id"] for r in results], [i["id"] for i in items])
            for item, res in zip(items, results):
                self.assertEqual(res["path"], item["path"])
                self.assertEqual(res["status"], 200, res.get("error"))
                st, single = single_get(item["path"])
                self.assertEqual(st, 200)
                self.assertEqual(res["body"], single, f"{item['path']} differs from a single GET")
            print(f"  batch {batch_id}: 25 items, 2 parts, all bodies equal single GETs "
                  f"({time.monotonic() - started:.0f}s)")
        finally:
            if not finished:
                try:
                    client.cancel_batch(batch_id)
                except BatchError:
                    pass


if __name__ == "__main__":
    unittest.main()
