# APISchoolListRank21


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_year** | **int** | Year this ranking list represents (2018 &#x3D; 2017-18) | [optional] 
**rank_year_compare** | **int** | Year rankings returned for comparison (2018 &#x3D; 2017-18) | [optional] 
**rank_years_available** | **List[int]** | The years for which SchoolDigger rankings are available for this state and level | [optional] 
**number_of_schools** | **int** | The total count of schools in this ranking list | [optional] 
**number_of_pages** | **int** | The total count of pages this ranking list based on given per_page value | [optional] 
**school_list** | [**List[APISchoolSummary21]**](APISchoolSummary21.md) | The schools in the ranking list | [optional] 

## Example

```python
from schooldigger.models.api_school_list_rank21 import APISchoolListRank21

# TODO update the JSON string below
json = "{}"
# create an instance of APISchoolListRank21 from a JSON string
api_school_list_rank21_instance = APISchoolListRank21.from_json(json)
# print the JSON string representation of the object
print(APISchoolListRank21.to_json())

# convert the object into a dict
api_school_list_rank21_dict = api_school_list_rank21_instance.to_dict()
# create an instance of APISchoolListRank21 from a dict
api_school_list_rank21_from_dict = APISchoolListRank21.from_dict(api_school_list_rank21_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


