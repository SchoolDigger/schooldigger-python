# APISchoolList22


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_schools** | **int** | The total count of schools that match your query | [optional] 
**number_of_pages** | **int** | The total count of pages in your query list based on given per_page value | [optional] 
**school_list** | [**List[APISchoolSummary22]**](APISchoolSummary22.md) |  | [optional] 

## Example

```python
from schooldigger.models.api_school_list22 import APISchoolList22

# TODO update the JSON string below
json = "{}"
# create an instance of APISchoolList22 from a JSON string
api_school_list22_instance = APISchoolList22.from_json(json)
# print the JSON string representation of the object
print(APISchoolList22.to_json())

# convert the object into a dict
api_school_list22_dict = api_school_list22_instance.to_dict()
# create an instance of APISchoolList22 from a dict
api_school_list22_from_dict = APISchoolList22.from_dict(api_school_list22_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


