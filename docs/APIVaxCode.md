# APIVaxCode

A vaccine (antigen) or a vaccination status: a stable code and its display name (API 3.1). Antigen codes include ALL (all required vaccines), MMR, MEASLES, DTP_TD, TDAP, POLIO, HEPB, VARICELLA, MENACWY; status codes include IMMUNIZED, COMPLIANT, CONDITIONAL, NOT_UP_TO_DATE, EXEMPT_ANY, EXEMPT_MEDICAL, EXEMPT_NONMEDICAL, EXEMPT_RELIGIOUS, EXEMPT_PERSONAL. New codes can be added when a state publishes a new measure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Stable code, e.g. \&quot;MMR\&quot; (antigen) or \&quot;IMMUNIZED\&quot; (status) | [optional] 
**name** | **str** | Display name, e.g. \&quot;Measles, mumps, rubella (MMR)\&quot; | [optional] 
**group** | **str** | Statuses only: \&quot;coverage\&quot; (students who have the vaccines), \&quot;exemption\&quot; (students exempt) or \&quot;other\&quot; (conditional, not up to date, no record and similar) | [optional] 

## Example

```python
from schooldigger.models.api_vax_code import APIVaxCode

# TODO update the JSON string below
json = "{}"
# create an instance of APIVaxCode from a JSON string
api_vax_code_instance = APIVaxCode.from_json(json)
# print the JSON string representation of the object
print(APIVaxCode.to_json())

# convert the object into a dict
api_vax_code_dict = api_vax_code_instance.to_dict()
# create an instance of APIVaxCode from a dict
api_vax_code_from_dict = APIVaxCode.from_dict(api_vax_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


