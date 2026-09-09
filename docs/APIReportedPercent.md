# APIReportedPercent

A percent metric (percentMetStandard, percentTier1..5) that the state did not publish as a single exact number.  In API 3.0 a percent metric is EITHER a plain number (the state reported an exact value) OR this object, and is  absent when nothing was reported. status is one of: 'range' (the state published only a range: low / high are  the state's bounds), 'suppressed' (withheld by the state to protect student privacy; no value), 'legacyImputed'  (a pre-2018 SchoolDigger stand-in: value is the 4 / 96 number older API versions return, low / high are the  state's bounds), 'derived' (computed by SchoolDigger from the other reported levels: value when exact, otherwise  low / high). Rendering rule: exact 82.3 -&gt; '82.3%'; low 0 -&gt; '&lt; 10%'; high 100 -&gt; '&gt;= 95%'; otherwise  '10-15%'; suppressed -&gt; a dash. See https://developer.schooldigger.com/data-quality

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Why there is no exact number: &#39;range&#39;, &#39;suppressed&#39;, &#39;legacyImputed&#39; or &#39;derived&#39; | [optional] 
**value** | **float** | The percent value, when one exists (status &#39;derived&#39; with an exact result, or the &#39;legacyImputed&#39; stand-in). Absent otherwise. | [optional] 
**low** | **float** | Lower bound of the range in percent (0 means &#39;less than high&#39;). Absent for &#39;suppressed&#39;. | [optional] 
**high** | **float** | Upper bound of the range in percent (100 means &#39;at least low&#39;). Absent for &#39;suppressed&#39;. | [optional] 

## Example

```python
from schooldigger.models.api_reported_percent import APIReportedPercent

# TODO update the JSON string below
json = "{}"
# create an instance of APIReportedPercent from a JSON string
api_reported_percent_instance = APIReportedPercent.from_json(json)
# print the JSON string representation of the object
print(APIReportedPercent.to_json())

# convert the object into a dict
api_reported_percent_dict = api_reported_percent_instance.to_dict()
# create an instance of APIReportedPercent from a dict
api_reported_percent_from_dict = APIReportedPercent.from_dict(api_reported_percent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


