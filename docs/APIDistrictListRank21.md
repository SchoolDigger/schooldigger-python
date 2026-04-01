# APIDistrictListRank21


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_year** | **int** | Year this ranking list represents (2018 &#x3D; 2017-18) | [optional] 
**rank_year_compare** | **int** | Year rankings returned for comparison (2018 &#x3D; 2017-18) | [optional] 
**rank_years_available** | **List[int]** | The years for which SchoolDigger district rankings are available for this state | [optional] 
**number_of_districts** | **int** | The total count of districts in the entire rank list | [optional] 
**number_of_pages** | **int** | The total count of pages in your query list based on given per_page value | [optional] 
**district_list** | [**List[APIDistrictSummary21]**](APIDistrictSummary21.md) |  | [optional] 
**rank_compare_year** | **int** |  | [optional] 

## Example

```python
from schooldigger.models.api_district_list_rank21 import APIDistrictListRank21

# TODO update the JSON string below
json = "{}"
# create an instance of APIDistrictListRank21 from a JSON string
api_district_list_rank21_instance = APIDistrictListRank21.from_json(json)
# print the JSON string representation of the object
print(APIDistrictListRank21.to_json())

# convert the object into a dict
api_district_list_rank21_dict = api_district_list_rank21_instance.to_dict()
# create an instance of APIDistrictListRank21 from a dict
api_district_list_rank21_from_dict = APIDistrictListRank21.from_dict(api_district_list_rank21_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


