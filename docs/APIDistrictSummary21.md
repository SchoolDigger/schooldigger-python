# APIDistrictSummary21


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**district_id** | **str** | SchoolDigger District ID Number (7 digits). Use /districts/{districtID} to retrieve the entire district record | [optional] 
**district_name** | **str** | District name | [optional] 
**phone** | **str** | District phone number | [optional] 
**url** | **str** | SchoolDigger URL for this district | [optional] 
**address** | [**APILocation**](APILocation.md) |  | [optional] 
**location_is_within_boundary** | **bool** | Indicates whether this school&#39;s boundary includes the specified location from nearLatitude/nearLongitude or boundaryAddress (Enterprise API level) | [optional] 
**has_boundary** | **bool** | Indicates that an attendance boundary is available for this district. (To retrieve, look up district with /districts/{id}) | [optional] 
**distance** | **float** | Distance in miles from the nearLatitude/nearLongitude coordinates (only populated when proximity search parameters are provided) | [optional] 
**is_within_boundary** | **bool** | Indicates whether this district&#39;s boundary includes the specified location from nearLatitude/nearLongitude | [optional] 
**county** | [**APICounty**](APICounty.md) |  | [optional] 
**low_grade** | **str** | The low grade served by this district (PK &#x3D; Prekindergarten, K &#x3D; Kindergarten) | [optional] 
**high_grade** | **str** | The high grade served by this district | [optional] 
**number_total_schools** | **int** | Count of schools in the district | [optional] 
**number_primary_schools** | **int** | Count of schools designated as primary schools | [optional] 
**number_middle_schools** | **int** | Count of schools designated as middle schools | [optional] 
**number_high_schools** | **int** | Count of schools designated as high schools | [optional] 
**number_alternative_schools** | **int** | Count of schools designated as other/alternative schools | [optional] 
**rank_history** | [**List[APILEARankHistory]**](APILEARankHistory.md) | SchoolDigger yearly rank history of the district | [optional] 
**district_yearly_details** | [**List[APILEAYearlyDetail]**](APILEAYearlyDetail.md) | District yearly metrics | [optional] 

## Example

```python
from schooldigger.models.api_district_summary21 import APIDistrictSummary21

# TODO update the JSON string below
json = "{}"
# create an instance of APIDistrictSummary21 from a JSON string
api_district_summary21_instance = APIDistrictSummary21.from_json(json)
# print the JSON string representation of the object
print(APIDistrictSummary21.to_json())

# convert the object into a dict
api_district_summary21_dict = api_district_summary21_instance.to_dict()
# create an instance of APIDistrictSummary21 from a dict
api_district_summary21_from_dict = APIDistrictSummary21.from_dict(api_district_summary21_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


