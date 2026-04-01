# APISchoolFull22


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schoolid** | **str** | SchoolDigger School ID Number (12 digits) | [optional] 
**school_name** | **str** | School name | [optional] 
**phone** | **str** | School phone number | [optional] 
**url** | **str** | URL of the school&#39;s own public website (may be null if not available). This is NOT the SchoolDigger page — see urlSchoolDigger for that. | [optional] 
**url_school_digger** | **str** | SchoolDigger URL for this school | [optional] 
**url_compare_school_digger** | **str** | SchoolDigger URL for comparing this school to nearby schools | [optional] 
**address** | [**APILocation**](APILocation.md) |  | [optional] 
**locale** | **str** | NCES urban-centric locale classification (e.g. &#39;City: Large&#39;, &#39;Suburb: Midsize&#39;, &#39;Rural: Fringe&#39;). Categories: City (Large/Midsize/Small), Suburb (Large/Midsize/Small), Town (Fringe/Distant/Remote), Rural (Fringe/Distant/Remote). See https://nces.ed.gov/ccd/rural_locales.asp | [optional] 
**low_grade** | **str** | The low grade served by this school (PK &#x3D; Prekindergarten, K &#x3D; Kindergarten) | [optional] 
**high_grade** | **str** | The high grade served by this school | [optional] 
**school_level** | **str** | The level of school (Elementary, Middle, High, Private, Alternative) | [optional] 
**is_charter_school** | **str** | Indicates if school is a charter school (Yes/No/n-a) | [optional] 
**is_magnet_school** | **str** | Indicates if school is a magnet school (Yes/No/n-a) | [optional] 
**is_virtual_school** | **str** | Indicates if school is a virtual school (Yes/No/n-a) | [optional] 
**is_title_i_school** | **str** | Indicates if school is a Title I school (Yes/No/n-a) | [optional] 
**is_title_i_schoolwide_school** | **str** | Indicates if a school-wide Title I school (Yes/No/n-a) | [optional] 
**is_private** | **bool** | Indicates if school is a private school (Yes/No) | [optional] 
**private_days** | **int** | Days in the school year (private schools only) | [optional] 
**private_hours** | **float** | Hours in the school day (private schools only) | [optional] 
**private_has_library** | **bool** | Indicates if the school has a library (private schools only) | [optional] 
**private_coed** | **str** | Coed/Boys/Girls (private schools only) | [optional] 
**private_orientation** | **str** | Affiliation of the school (private schools only) | [optional] 
**nces_private_school_id** | **str** | The NCES ID of the school (private schools only) | [optional] 
**district** | [**APIDistrictSum**](APIDistrictSum.md) |  | [optional] 
**county** | [**APICounty**](APICounty.md) |  | [optional] 
**reviews** | [**List[APISchoolReview]**](APISchoolReview.md) | User-submitted reviews from SchoolDigger.com visitors. Each review includes a star rating (1-5), comment text (HTML encoded), date, and reviewer type (parent, student, teacher, principal, citizen). Reviews are unmoderated user content. | [optional] 
**finance** | [**List[APISchoolFinance]**](APISchoolFinance.md) | Yearly per-student spending data. Array is sorted most recent year first. spendingPerStudent is available at Pro level; detailed federal/state/local and personnel/non-personnel breakdowns require Enterprise level. | [optional] 
**graduation_rates** | [**List[APIGraduationRate]**](APIGraduationRate.md) | 4-year adjusted cohort graduation rates at school, district, and state levels (Pro and Enterprise API level only). Array is sorted most recent year first. | [optional] 
**dropout_rates** | [**List[APIDropoutRate]**](APIDropoutRate.md) | Annual dropout rates at school, district, and state levels (Pro and Enterprise API level only). Array is sorted most recent year first. | [optional] 
**chronic_absenteeism_rates** | [**List[APIChronicAbsenteeismRate]**](APIChronicAbsenteeismRate.md) | Chronic absenteeism rates (students missing 15+ days) at school, district, and state levels (Pro and Enterprise API level only). Array is sorted most recent year first. Data availability varies by state. | [optional] 
**rank_history** | [**List[APIRankHistory]**](APIRankHistory.md) | SchoolDigger yearly rank history for this school, sorted most recent year first. Schools are ranked within their state and level (Elementary, Middle, or High). Includes all available years — the full record returns more years than the summary in search results. | [optional] 
**rank_movement** | **int** | Returns the movement of rank for this school between current and previous year | [optional] 
**test_scores** | [**List[APITestScoreWrapper]**](APITestScoreWrapper.md) | Standardized test score results with school, district, and state comparisons. Each entry represents one test/subject/grade/year combination. Includes percent meeting standard and optional tier breakdowns (Enterprise level). Tests are state-specific (e.g. SBA, WCAS in WA; CAASPP in CA). Requires Pro or Enterprise API subscription. | [optional] 
**school_yearly_details** | [**List[APIYearlyDemographics]**](APIYearlyDemographics.md) | Yearly enrollment, demographics, and staffing for this school. Array is sorted most recent year first and includes all available years (back to 1988 for some schools). The full record returns more years than the summary in search results. | [optional] 

## Example

```python
from schooldigger.models.api_school_full22 import APISchoolFull22

# TODO update the JSON string below
json = "{}"
# create an instance of APISchoolFull22 from a JSON string
api_school_full22_instance = APISchoolFull22.from_json(json)
# print the JSON string representation of the object
print(APISchoolFull22.to_json())

# convert the object into a dict
api_school_full22_dict = api_school_full22_instance.to_dict()
# create an instance of APISchoolFull22 from a dict
api_school_full22_from_dict = APISchoolFull22.from_dict(api_school_full22_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


