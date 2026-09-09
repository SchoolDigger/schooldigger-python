# APIDistrictFull30

District detail record for API 3.0. Identical to 2.4 (APIDistrictFull21) except testScores, whose percent metrics  are a number or an APIReportedPercent object and whose rows are no longer limited to what the pre-2026 importers  produced (docs/suppressed-test-values-spec.md R6).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_scores** | [**List[APITestScoreWrapper30]**](APITestScoreWrapper30.md) | Standardized test score results with district and state comparisons. Each entry represents one test/subject/grade/year combination. District-level records do not include schoolTestScore. Percent metrics are a number when the state reported an exact value, otherwise an object describing a range, a suppressed value, a legacy stand-in or a derived value (see APIReportedPercent). Requires Pro or Enterprise API subscription. | [optional] 
**district_id** | **str** | SchoolDigger District ID Number (7 digits) | [optional] 
**district_name** | **str** | District name | [optional] 
**phone** | **str** | District phone number | [optional] 
**url** | **str** | SchoolDigger URL for this district | [optional] 
**address** | [**APILocation**](APILocation.md) |  | [optional] 
**low_grade** | **str** | The low grade served by this district (PK &#x3D; Prekindergarten, K &#x3D; Kindergarten) | [optional] 
**high_grade** | **str** | The high grade served by this district | [optional] 
**number_total_schools** | **int** |  | [optional] 
**number_primary_schools** | **int** |  | [optional] 
**number_middle_schools** | **int** |  | [optional] 
**number_high_schools** | **int** |  | [optional] 
**number_alternative_schools** | **int** |  | [optional] 
**boundary** | [**APIBoundary12**](APIBoundary12.md) |  | [optional] 
**finance** | [**List[APISchoolFinance]**](APISchoolFinance.md) | Yearly per-student spending data. Array is sorted most recent year first. spendingPerStudent is available at Pro level; detailed federal/state/local and personnel/non-personnel breakdowns require Enterprise level. | [optional] 
**graduation_rates** | [**List[APIGraduationRate]**](APIGraduationRate.md) | 4-year adjusted cohort graduation rates at district and state levels (Pro and Enterprise API level only). Array is sorted most recent year first. | [optional] 
**dropout_rates** | [**List[APIDropoutRate]**](APIDropoutRate.md) | Annual dropout rates at district and state levels (Pro and Enterprise API level only). Array is sorted most recent year first. | [optional] 
**chronic_absenteeism_rates** | [**List[APIChronicAbsenteeismRate]**](APIChronicAbsenteeismRate.md) | Chronic absenteeism rates (students missing 15+ days) at district and state levels (Pro and Enterprise API level only). Array is sorted most recent year first. Data availability varies by state. | [optional] 
**is_within_boundary** | **bool** | Indicates whether this district&#39;s boundary includes the specified location from nearLatitude/nearLongitude | [optional] 
**county** | [**APICounty**](APICounty.md) |  | [optional] 
**rank_history** | [**List[APILEARankHistory]**](APILEARankHistory.md) | SchoolDigger yearly rank history for this district, sorted most recent year first. Districts are ranked statewide regardless of level. | [optional] 
**district_yearly_details** | [**List[APILEAYearlyDetail]**](APILEAYearlyDetail.md) | Yearly enrollment and staffing details for this district. Array is sorted most recent year first. Includes detailed FTE staffing breakdowns by role (teachers by level, administrators, counselors, librarians, support staff). | [optional] 

## Example

```python
from schooldigger.models.api_district_full30 import APIDistrictFull30

# TODO update the JSON string below
json = "{}"
# create an instance of APIDistrictFull30 from a JSON string
api_district_full30_instance = APIDistrictFull30.from_json(json)
# print the JSON string representation of the object
print(APIDistrictFull30.to_json())

# convert the object into a dict
api_district_full30_dict = api_district_full30_instance.to_dict()
# create an instance of APIDistrictFull30 from a dict
api_district_full30_from_dict = APIDistrictFull30.from_dict(api_district_full30_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


