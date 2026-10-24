# APIVaxLevelValue

One level's published value for a measure (API 3.1): the school's own figure, or the state's own published district, county or state figure for the same year, grade, vaccine and status. SchoolDigger never calculates district, county or state figures; they appear only where the state publishes them.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | \&quot;exact\&quot; (pct), \&quot;range\&quot; (rangeLow / rangeHigh; e.g. 95-100 for a published \&quot;95% or more\&quot;), \&quot;suppressed\&quot; (percent withheld by the state, usually for small groups; see source.suppressionNote), \&quot;redactedCount\&quot; (a student count withheld by the state, e.g. \&quot;fewer than 10\&quot;: see source.suppressedCountText), \&quot;countOnly\&quot; (a count of students, no percent: see students / studentsTotal) or \&quot;invalid\&quot; (not given: the published value is outside 0-100, qualityFlag 1, or the state&#39;s own figures contradict it, e.g. a non-report printed as zeros, qualityFlag 2) | [optional] 
**pct** | **float** | Percent of students (0-100), as published; status \&quot;exact\&quot; only | [optional] 
**range_low** | **float** | Lower bound of a published range (0-100); status \&quot;range\&quot; only | [optional] 
**range_high** | **float** | Upper bound of a published range (0-100); status \&quot;range\&quot; only | [optional] 
**students** | **int** | Students with this status, when published | [optional] 
**students_total** | **int** | Students the state counted for this figure (enrolled, or with a record on file, or required to have this vaccine, as the state defines it), when published | [optional] 
**sector** | **str** | County and state figures: \&quot;public\&quot; or \&quot;private\&quot; when the state published the figure for one sector only (the school&#39;s own); absent &#x3D; all schools | [optional] 
**quality_flag** | **int** | 1 &#x3D; the published value is outside 0-100; 2 &#x3D; the state&#39;s own figures contradict it, e.g. a non-report printed as zeros (status \&quot;invalid\&quot; either way) | [optional] 
**notes** | **List[int]** | Ids of the notes (vaccination.notes) that apply to this figure | [optional] 
**source_id** | **int** | Source id when the figure comes from one of vaccination.otherSources; absent &#x3D; vaccination.source | [optional] 

## Example

```python
from schooldigger.models.api_vax_level_value import APIVaxLevelValue

# TODO update the JSON string below
json = "{}"
# create an instance of APIVaxLevelValue from a JSON string
api_vax_level_value_instance = APIVaxLevelValue.from_json(json)
# print the JSON string representation of the object
print(APIVaxLevelValue.to_json())

# convert the object into a dict
api_vax_level_value_dict = api_vax_level_value_instance.to_dict()
# create an instance of APIVaxLevelValue from a dict
api_vax_level_value_from_dict = APIVaxLevelValue.from_dict(api_vax_level_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


