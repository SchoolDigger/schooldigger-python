# APIDistrictList21


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**district_list** | [**List[APIDistrictSummary21]**](APIDistrictSummary21.md) |  | [optional] 
**number_of_districts** | **int** | The total count of districts that match your query | [optional] 
**number_of_pages** | **int** | The total count of pages in your query list based on given per_page value | [optional] 

## Example

```python
from schooldigger.models.api_district_list21 import APIDistrictList21

# TODO update the JSON string below
json = "{}"
# create an instance of APIDistrictList21 from a JSON string
api_district_list21_instance = APIDistrictList21.from_json(json)
# print the JSON string representation of the object
print(APIDistrictList21.to_json())

# convert the object into a dict
api_district_list21_dict = api_district_list21_instance.to_dict()
# create an instance of APIDistrictList21 from a dict
api_district_list21_from_dict = APIDistrictList21.from_dict(api_district_list21_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


