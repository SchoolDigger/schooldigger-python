# APISchoolList31

API 3.1 school list (/v3.1/schools): the v2.4 / v3.0 list with lowIncome on each school  (SchoolListSD2_API_11 supplies the measure).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_list** | [**List[APISchoolSummary31]**](APISchoolSummary31.md) | The schools that match your query, each with lowIncome | [optional] 
**number_of_schools** | **int** | The total count of schools that match your query | [optional] 
**number_of_pages** | **int** | The total count of pages in your query list based on given per_page value | [optional] 

## Example

```python
from schooldigger.models.api_school_list31 import APISchoolList31

# TODO update the JSON string below
json = "{}"
# create an instance of APISchoolList31 from a JSON string
api_school_list31_instance = APISchoolList31.from_json(json)
# print the JSON string representation of the object
print(APISchoolList31.to_json())

# convert the object into a dict
api_school_list31_dict = api_school_list31_instance.to_dict()
# create an instance of APISchoolList31 from a dict
api_school_list31_from_dict = APISchoolList31.from_dict(api_school_list31_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


