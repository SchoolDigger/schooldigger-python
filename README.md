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
