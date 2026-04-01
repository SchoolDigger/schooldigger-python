# APIAutocompleteDistrictResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**district_matches** | [**List[APIDistrictAC]**](APIDistrictAC.md) | List of the districts that match the query | [optional] 

## Example

```python
from schooldigger.models.api_autocomplete_district_result import APIAutocompleteDistrictResult

# TODO update the JSON string below
json = "{}"
# create an instance of APIAutocompleteDistrictResult from a JSON string
api_autocomplete_district_result_instance = APIAutocompleteDistrictResult.from_json(json)
# print the JSON string representation of the object
print(APIAutocompleteDistrictResult.to_json())

# convert the object into a dict
api_autocomplete_district_result_dict = api_autocomplete_district_result_instance.to_dict()
# create an instance of APIAutocompleteDistrictResult from a dict
api_autocomplete_district_result_from_dict = APIAutocompleteDistrictResult.from_dict(api_autocomplete_district_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


