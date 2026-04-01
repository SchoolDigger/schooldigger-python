# APIDropoutRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** | School year using spring-year convention (e.g. 2025 &#x3D; the 2024-2025 school year) | [optional] 
**school_dropout_rate** | **float** | Dropout Rate at the School Level (Pro or Enterprise level only) | [optional] 
**district_dropout_rate** | **float** | Dropout Rate at the District Level (Pro or Enterprise level only) | [optional] 
**state_dropout_rate** | **float** | Dropout Rate at the State Level (Pro or Enterprise level only) | [optional] 

## Example

```python
from schooldigger.models.api_dropout_rate import APIDropoutRate

# TODO update the JSON string below
json = "{}"
# create an instance of APIDropoutRate from a JSON string
api_dropout_rate_instance = APIDropoutRate.from_json(json)
# print the JSON string representation of the object
print(APIDropoutRate.to_json())

# convert the object into a dict
api_dropout_rate_dict = api_dropout_rate_instance.to_dict()
# create an instance of APIDropoutRate from a dict
api_dropout_rate_from_dict = APIDropoutRate.from_dict(api_dropout_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


