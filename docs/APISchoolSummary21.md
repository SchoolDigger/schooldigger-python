# APISchoolSummary21

APISchool2Summary: A summary of a school record. For the full school record, call /schools/{id}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schoolid** | **str** | SchoolDigger School ID Number (12 digits) | [optional] 
**school_name** | **str** | School name | [optional] 
**phone** | **str** | School phone number | [optional] 
**url** | **str** | SchoolDigger URL for this school | [optional] 
**url_compare** | **str** | SchoolDigger URL for comparing this school to nearby schools | [optional] 
**address** | [**APILocation**](APILocation.md) |  | [optional] 
**distance** | **float** | Distance from nearLatitude/nearLongitude, boundaryLatitude/boundaryLongitude, or boundaryAddress (if supplied) | [optional] 
**locale** | **str** | NCES urban-centric locale classification (e.g. &#39;City: Large&#39;, &#39;Suburb: Midsize&#39;, &#39;Rural: Fringe&#39;). Categories: City (Large/Midsize/Small), Suburb (Large/Midsize/Small), Town (Fringe/Distant/Remote), Rural (Fringe/Distant/Remote). See https://nces.ed.gov/ccd/rural_locales.asp | [optional] 
**low_grade** | **str** | The low grade served by this school (PK &#x3D; Prekindergarten, K &#x3D; Kindergarten) | [optional] 
**high_grade** | **str** | The high grade served by this school | [optional] 
**school_level** | **str** | The level of school (Elementary, Middle, High, Private, Alternative) | [optional] 
**is_charter_school** | **str** | Indicates if school is a charter school (Yes/No/n-a) | [optional] 
**is_magnet_school** | **str** | Indicates if school is a magnet school (Yes/No/n-a) | [optional] 
**is_virtual_school** | **str** | Indicates if school is a virtual school (Yes/No/n-a) | [optional] 
**is_title_i_school** | **str** | Indicates if school is a Title I school (Yes/No/n-a) | [optional] 
**is_title_i_schoolwide_school** | **str** | Indicates if a school-wide Title I school (Yes/No/n-a) | [optional] 
**district** | [**APIDistrictSum**](APIDistrictSum.md) |  | [optional] 
**county** | [**APICounty**](APICounty.md) |  | [optional] 
**rank_history** | [**List[APIRankHistory]**](APIRankHistory.md) | SchoolDigger yearly rank history of the school. To retrieve all years, call /schools/{id}. | [optional] 
**rank_movement** | **int** | Returns the movement of rank for this school between current and previous year | [optional] 
**school_yearly_details** | [**List[APIYearlyDemographics]**](APIYearlyDemographics.md) | School Yearly metrics. To retrieve all years, call /schools/{id}. | [optional] 
**is_private** | **bool** | Indicates if school is a private school (Yes/No) | [optional] 
**private_days** | **int** | Days in the school year (private schools only) | [optional] 
**private_hours** | **float** | Hours in the school day (private schools only) | [optional] 
**private_has_library** | **bool** | Indicates if the school has a library (private schools only) | [optional] 
**private_coed** | **str** | Coed/Boys/Girls (private schools only) | [optional] 
**private_orientation** | **str** | Affiliation of the school (private schools only) | [optional] 

## Example

```python
from schooldigger.models.api_school_summary21 import APISchoolSummary21

# TODO update the JSON string below
json = "{}"
# create an instance of APISchoolSummary21 from a JSON string
api_school_summary21_instance = APISchoolSummary21.from_json(json)
# print the JSON string representation of the object
print(APISchoolSummary21.to_json())

# convert the object into a dict
api_school_summary21_dict = api_school_summary21_instance.to_dict()
# create an instance of APISchoolSummary21 from a dict
api_school_summary21_from_dict = APISchoolSummary21.from_dict(api_school_summary21_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


