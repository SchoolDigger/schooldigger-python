# APIDistrictAC


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**districtid** | **str** | SchoolDigger District ID Number (7 digits). Use /districts/{districtID} to retrieve the full district record | [optional] 
**district_name** | **str** | District name | [optional] 
**city** | **str** | District location city | [optional] 
**state** | **str** | District location state | [optional] 
**zip** | **str** | District location zip code | [optional] 
**low_grade** | **str** | The low grade served by this district (PK &#x3D; Prekindergarten, K &#x3D; Kindergarten) | [optional] 
**high_grade** | **str** | The high grade served by this district | [optional] 
**latitude** | **float** | District location latitude | [optional] 
**longitude** | **float** | District location longitude | [optional] 
**has_boundary** | **bool** | States whether there is an attendance boundary available for this District | [optional] 
**rank** | **int** | Statewide rank of this district | [optional] 
**rank_of** | **int** | Count of districts ranked at this state/level | [optional] 
**rank_stars** | **int** | The number of stars SchoolDigger awarded in the ranking of the district (0-5, 5 is best) | [optional] 

## Example

```python
from schooldigger.models.api_district_ac import APIDistrictAC

# TODO update the JSON string below
json = "{}"
# create an instance of APIDistrictAC from a JSON string
api_district_ac_instance = APIDistrictAC.from_json(json)
# print the JSON string representation of the object
print(APIDistrictAC.to_json())

# convert the object into a dict
api_district_ac_dict = api_district_ac_instance.to_dict()
# create an instance of APIDistrictAC from a dict
api_district_ac_from_dict = APIDistrictAC.from_dict(api_district_ac_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


