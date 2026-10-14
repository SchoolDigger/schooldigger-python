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

Pass `include_ranges=True` to `get_school` / `get_district` (without it, test scores are
as in API 2.4). Each test-score percent
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

## Low-income measure in API 3.1

SDK 3.0 targets API 3.1. School records from `get_school`, `search_schools` and
`get_school_rankings` carry `low_income`: the school's one low-income measure, `type` `"FRL"`
(free/reduced-price lunch eligible), `"DC"` (directly certified for free meals; used where the
school reports no usable free/reduced count) or `"CEP"` (likely serves free meals to all
students under the Community Eligibility Provision; no `percent`), with `year`, `percent`,
`count`, `enrollment`, `community_eligibility_likely` and `statewide_free_meals`. It is `None`
when the school has no usable value. FRL and DC are not comparable: don't sort one against the
other.

```python
school = api.get_school("250309000385")
li = school.low_income
if li is None:
    print("no low-income figure")
elif li.type == "CEP":
    print(f"All students receive free meals (Community Eligibility, {li.year - 1}-{li.year % 100:02d})")
else:
    label = "Free/reduced lunch eligible" if li.type == "FRL" else "Directly certified for free meals"
    print(f"{label}: {li.percent}% ({li.year - 1}-{li.year % 100:02d})")
for y in school.school_yearly_details or []:
    print(y.year, y.free_reduced_lunch, y.direct_certification)
```

Each yearly detail has `free_reduced_lunch` (count and percent, or a `status` of
`communityEligibility`, `repeated` or `aboveEnrollment`) and `direct_certification`. SDK 3.0
renames the school models for API 3.1, a breaking change for code that imports them by name (`APISchoolFull31Ranges`, `APISchoolList31`,
`APISchoolSummary31`, `APISchoolListRank31`, `APISchoolSummaryRank31`). See
[Low-income measures](https://developer.schooldigger.com/data-quality#low-income).

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
