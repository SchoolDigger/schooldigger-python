# APIGraduationRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** | School year using spring-year convention (e.g. 2025 &#x3D; the 2024-2025 school year) | [optional] 
**school_graduation_rate** | **float** | 4-Year Graduation Rate at the School Level (Pro or Enterprise level only) | [optional] 
**district_graduation_rate** | **float** | 4-Year Graduation Rate at the District Level (Pro or Enterprise level only) | [optional] 
**state_graduation_rate** | **float** | 4-Year Graduation Rate at the State Level (Pro or Enterprise level only) | [optional] 

## Example

```python
from schooldigger.models.api_graduation_rate import APIGraduationRate

# TODO update the JSON string below
json = "{}"
# create an instance of APIGraduationRate from a JSON string
api_graduation_rate_instance = APIGraduationRate.from_json(json)
# print the JSON string representation of the object
print(APIGraduationRate.to_json())

# convert the object into a dict
api_graduation_rate_dict = api_graduation_rate_instance.to_dict()
# create an instance of APIGraduationRate from a dict
api_graduation_rate_from_dict = APIGraduationRate.from_dict(api_graduation_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


