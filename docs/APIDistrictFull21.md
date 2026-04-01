# APIDistrictFull21


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**test_scores** | [**List[APITestScoreWrapper]**](APITestScoreWrapper.md) | Standardized test score results with district and state comparisons. Each entry represents one test/subject/grade/year combination. District-level records do not include schoolTestScore. Requires Pro or Enterprise API subscription. | [optional] 

## Example

```python
from schooldigger.models.api_district_full21 import APIDistrictFull21

# TODO update the JSON string below
json = "{}"
# create an instance of APIDistrictFull21 from a JSON string
api_district_full21_instance = APIDistrictFull21.from_json(json)
# print the JSON string representation of the object
print(APIDistrictFull21.to_json())

# convert the object into a dict
api_district_full21_dict = api_district_full21_instance.to_dict()
# create an instance of APIDistrictFull21 from a dict
api_district_full21_from_dict = APIDistrictFull21.from_dict(api_district_full21_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


