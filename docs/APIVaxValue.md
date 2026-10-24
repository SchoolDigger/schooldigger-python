# APIVaxValue

A vaccination value as the state published it (API 3.1). status: \"exact\" (pct), \"range\" (rangeLow / rangeHigh; e.g. 95-100 for a published \"95% or more\"), \"suppressed\" (the state withheld the percent, usually for small groups; see source.suppressionNote), \"redactedCount\" (the state withheld a student count, e.g. \"fewer than 10\": see source.suppressedCountText), \"countOnly\" (the state published a count of students, not a percent: see students / studentsTotal) or \"invalid\" (not given: the published value is outside 0-100, qualityFlag 1, or the state's own figures contradict it, e.g. a non-report printed as zeros, qualityFlag 2).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | \&quot;exact\&quot;, \&quot;range\&quot;, \&quot;suppressed\&quot;, \&quot;redactedCount\&quot;, \&quot;countOnly\&quot; or \&quot;invalid\&quot; | [optional] 
**pct** | **float** | Percent of students (0-100), as published; status \&quot;exact\&quot; only | [optional] 
**range_low** | **float** | Lower bound of a published range (0-100); status \&quot;range\&quot; only | [optional] 
**range_high** | **float** | Upper bound of a published range (0-100); status \&quot;range\&quot; only | [optional] 

## Example

```python
from schooldigger.models.api_vax_value import APIVaxValue

# TODO update the JSON string below
json = "{}"
# create an instance of APIVaxValue from a JSON string
api_vax_value_instance = APIVaxValue.from_json(json)
# print the JSON string representation of the object
print(APIVaxValue.to_json())

# convert the object into a dict
api_vax_value_dict = api_vax_value_instance.to_dict()
# create an instance of APIVaxValue from a dict
api_vax_value_from_dict = APIVaxValue.from_dict(api_vax_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


