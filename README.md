# SchoolDigger Python SDK

Official Python client for the [SchoolDigger API](https://developer.schooldigger.com) — K-12 school data for 120,000+ U.S. schools.

## Installation

```bash
pip install schooldigger
```

## Quick Start

```python
import schooldigger

config = schooldigger.Configuration()
config.api_key["appID"] = "YOUR_APP_ID"
config.api_key["appKey"] = "YOUR_APP_KEY"

client = schooldigger.ApiClient(config)

# Search schools
api = schooldigger.SchoolsApi(client)
result = api.search_schools(st="WA", q="Lincoln")
for school in result.school_list:
    print(f"{school.school_name} — {school.address.city}, {school.address.state}")

# Get a specific school by SchoolDigger ID
school = api.get_school("530966001632")
print(f"Enrollment: {school.school_yearly_details[0].number_of_students}")
```

## API Classes

| Class | Methods |
|-------|---------|
| `SchoolsApi` | `search_schools()`, `get_school()` |
| `DistrictsApi` | `search_districts()`, `get_district()` |
| `RankingsApi` | `get_school_rankings()`, `get_district_rankings()` |
| `AutocompleteApi` | `autocomplete_schools()`, `autocomplete_districts()` |

## Test scores in API 3.0

This version of the SDK targets API 3.0. Pass `include_ranges=True` to `get_school` / `get_district`
(without it the record is identical to API 2.4). Each test-score percent
(`percent_met_standard`, `percent_tier1` ... `percent_tier5`) is **either a number or an
`APIReportedPercent` object** (`status` of `range`, `suppressed`, `legacyImputed` or `derived`,
with optional `value`, `low`, `high`), and is `None` when the state reported nothing. The SDK
exposes the union through `.actual_instance`:

```python
school = api.get_school("330004800609", include_ranges=True)
for ts in school.test_scores or []:
    v = ts.school_test_score.percent_met_standard if ts.school_test_score else None
    v = v.actual_instance if v is not None else None
    if v is None:
        text = "not reported"
    elif isinstance(v, (int, float)):
        text = f"{v}%"
    elif v.status == "suppressed":
        text = "suppressed by the state"
    elif v.low is not None and v.low <= 0:
        text = f"< {v.high}%"
    elif v.high is not None and v.high >= 100:
        text = f">= {v.low}%"
    elif v.low is not None:
        text = f"{v.low}-{v.high}%"
    else:
        text = f"{v.value}%"
    print(ts.year, ts.grade, ts.subject, text)
```

See [Data Quality and Suppression](https://developer.schooldigger.com/data-quality) for the full
vocabulary and rendering rule. API 2.4 and below (SDK 1.x) return only exact values.

## Authentication

All API calls require an `appID` and `appKey`. Get your free API key at [developer.schooldigger.com](https://developer.schooldigger.com).

## Documentation

- [API Reference](https://developer.schooldigger.com/docs)
- [Get your free API key](https://developer.schooldigger.com)
- [SchoolDigger.com](https://www.schooldigger.com)

## Plans

| Plan | Price | Highlights |
|------|-------|------------|
| DEV/TEST | Free | Enterprise-level access, 20 calls/day |
| Basic | $19.90/mo | 1 year of data |
| Pro | $89/mo | Boundaries, geo search, finance |
| Enterprise | $189/mo | Full depth, boundary containment |

## License

MIT
