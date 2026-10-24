# APIVaxGrade

A grade code and its name (API 3.1 vaccination lookups).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Grade code: \&quot;PK\&quot;, \&quot;KG\&quot;, \&quot;01\&quot;-\&quot;12\&quot;, or \&quot;14\&quot; &#x3D; all grades in the school | [optional] 
**name** | **str** | Grade name, e.g. \&quot;Kindergarten\&quot;, \&quot;All grades\&quot; | [optional] 

## Example

```python
from schooldigger.models.api_vax_grade import APIVaxGrade

# TODO update the JSON string below
json = "{}"
# create an instance of APIVaxGrade from a JSON string
api_vax_grade_instance = APIVaxGrade.from_json(json)
# print the JSON string representation of the object
print(APIVaxGrade.to_json())

# convert the object into a dict
api_vax_grade_dict = api_vax_grade_instance.to_dict()
# create an instance of APIVaxGrade from a dict
api_vax_grade_from_dict = APIVaxGrade.from_dict(api_vax_grade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


