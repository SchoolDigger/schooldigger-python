# APIAutocompleteSchoolResult23


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_matches** | [**List[APISchoolAC23]**](APISchoolAC23.md) | List of the schools that match the query | [optional] 

## Example

```python
from schooldigger.models.api_autocomplete_school_result23 import APIAutocompleteSchoolResult23

# TODO update the JSON string below
json = "{}"
# create an instance of APIAutocompleteSchoolResult23 from a JSON string
api_autocomplete_school_result23_instance = APIAutocompleteSchoolResult23.from_json(json)
# print the JSON string representation of the object
print(APIAutocompleteSchoolResult23.to_json())

# convert the object into a dict
api_autocomplete_school_result23_dict = api_autocomplete_school_result23_instance.to_dict()
# create an instance of APIAutocompleteSchoolResult23 from a dict
api_autocomplete_school_result23_from_dict = APIAutocompleteSchoolResult23.from_dict(api_autocomplete_school_result23_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


