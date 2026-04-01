# APIChronicAbsenteeismRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** | School year using spring-year convention (e.g. 2025 &#x3D; the 2024-2025 school year) | [optional] 
**school_chronic_absenteeism_rate** | **float** | ChronicAbsenteeism Rate at the School Level (Pro or Enterprise level only) | [optional] 
**district_chronic_absenteeism_rate** | **float** | ChronicAbsenteeism Rate at the District Level (Pro or Enterprise level only) | [optional] 
**state_chronic_absenteeism_rate** | **float** | ChronicAbsenteeism Rate at the State Level (Pro or Enterprise level only) | [optional] 

## Example

```python
from schooldigger.models.api_chronic_absenteeism_rate import APIChronicAbsenteeismRate

# TODO update the JSON string below
json = "{}"
# create an instance of APIChronicAbsenteeismRate from a JSON string
api_chronic_absenteeism_rate_instance = APIChronicAbsenteeismRate.from_json(json)
# print the JSON string representation of the object
print(APIChronicAbsenteeismRate.to_json())

# convert the object into a dict
api_chronic_absenteeism_rate_dict = api_chronic_absenteeism_rate_instance.to_dict()
# create an instance of APIChronicAbsenteeismRate from a dict
api_chronic_absenteeism_rate_from_dict = APIChronicAbsenteeismRate.from_dict(api_chronic_absenteeism_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


