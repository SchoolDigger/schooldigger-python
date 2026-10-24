# APIVaxFigure

One published vaccination measure (API 3.1): a school year, grade, vaccine and status, with the value at each level the state publishes it for. A level is absent when the state published nothing for it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** | School year (2026 &#x3D; 2025-26) | [optional] 
**grade** | **str** | Grade code: \&quot;PK\&quot;, \&quot;KG\&quot;, \&quot;01\&quot;-\&quot;12\&quot;, or \&quot;14\&quot; &#x3D; all grades in the school (names in vaccination.grades) | [optional] 
**antigen** | **str** | Vaccine code (names in vaccination.antigens); ALL &#x3D; all required vaccines | [optional] 
**status** | **str** | Status code (names and groups in vaccination.statuses) | [optional] 
**school** | [**APIVaxLevelValue**](APIVaxLevelValue.md) |  | [optional] 
**district** | [**APIVaxLevelValue**](APIVaxLevelValue.md) |  | [optional] 
**county** | [**APIVaxLevelValue**](APIVaxLevelValue.md) |  | [optional] 
**state** | [**APIVaxLevelValue**](APIVaxLevelValue.md) |  | [optional] 

## Example

```python
from schooldigger.models.api_vax_figure import APIVaxFigure

# TODO update the JSON string below
json = "{}"
# create an instance of APIVaxFigure from a JSON string
api_vax_figure_instance = APIVaxFigure.from_json(json)
# print the JSON string representation of the object
print(APIVaxFigure.to_json())

# convert the object into a dict
api_vax_figure_dict = api_vax_figure_instance.to_dict()
# create an instance of APIVaxFigure from a dict
api_vax_figure_from_dict = APIVaxFigure.from_dict(api_vax_figure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


