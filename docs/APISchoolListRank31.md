# APISchoolListRank31

API 3.1 school ranking list (/v3.1/rankings/schools/{st}): the v2.1-v3.0 ranking list with lowIncome on each school.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_list** | [**List[APISchoolSummaryRank31]**](APISchoolSummaryRank31.md) | The schools in the ranking list, each with lowIncome | [optional] 
**rank_year** | **int** | Year this ranking list represents (2018 &#x3D; 2017-18) | [optional] 
**rank_year_compare** | **int** | Year rankings returned for comparison (2018 &#x3D; 2017-18) | [optional] 
**rank_years_available** | **List[int]** | The years for which SchoolDigger rankings are available for this state and level | [optional] 
**number_of_schools** | **int** | The total count of schools in this ranking list | [optional] 
**number_of_pages** | **int** | The total count of pages this ranking list based on given per_page value | [optional] 

## Example

```python
from schooldigger.models.api_school_list_rank31 import APISchoolListRank31

# TODO update the JSON string below
json = "{}"
# create an instance of APISchoolListRank31 from a JSON string
api_school_list_rank31_instance = APISchoolListRank31.from_json(json)
# print the JSON string representation of the object
print(APISchoolListRank31.to_json())

# convert the object into a dict
api_school_list_rank31_dict = api_school_list_rank31_instance.to_dict()
# create an instance of APISchoolListRank31 from a dict
api_school_list_rank31_from_dict = APISchoolListRank31.from_dict(api_school_list_rank31_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


