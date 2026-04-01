# APISchoolAC23


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schoolid** | **str** | SchoolDigger School ID Number (12 digits). Use /schools/{schoolID} to retrieve the full school record | [optional] 
**school_name** | **str** | School name | [optional] 
**city** | **str** | School location city | [optional] 
**state** | **str** | School location state | [optional] 
**zip** | **str** | School location zip code (Pro, Enterprise, and Autocomplete Pro levels only) | [optional] 
**school_level** | **str** | The level of school (Elementary, Middle, High, Private, Alternative) | [optional] 
**low_grade** | **str** | The low grade served by this school (PK &#x3D; Prekindergarten, K &#x3D; Kindergarten)  (Pro, Enterprise, and Autocomplete Pro levels only) | [optional] 
**high_grade** | **str** | The high grade served by this school  (Pro, Enterprise, and Autocomplete Pro levels only) | [optional] 
**latitude** | **float** | School location latitude (Pro, Enterprise, and Autocomplete Pro levels only) | [optional] 
**longitude** | **float** | School location longitude (Pro, Enterprise, and Autocomplete Pro levels only) | [optional] 
**rank** | **int** | Statewide rank of this School  (Pro, Enterprise, and Autocomplete Pro levels only) | [optional] 
**rank_of** | **int** | Count of schools ranked at this state/level (Pro, Enterprise, and Autocomplete Pro levels only) | [optional] 
**rank_stars** | **int** | The number of stars SchoolDigger awarded in the ranking of the school (0-5, 5 is best) (Pro, Enterprise, and Autocomplete Pro levels only) | [optional] 
**nces_private_school_id** | **str** | The NCES ID of the school (private schools only) | [optional] 

## Example

```python
from schooldigger.models.api_school_ac23 import APISchoolAC23

# TODO update the JSON string below
json = "{}"
# create an instance of APISchoolAC23 from a JSON string
api_school_ac23_instance = APISchoolAC23.from_json(json)
# print the JSON string representation of the object
print(APISchoolAC23.to_json())

# convert the object into a dict
api_school_ac23_dict = api_school_ac23_instance.to_dict()
# create an instance of APISchoolAC23 from a dict
api_school_ac23_from_dict = APISchoolAC23.from_dict(api_school_ac23_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


