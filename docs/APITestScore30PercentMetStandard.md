# APITestScore30PercentMetStandard

Percent of students meeting state standard: a number when the state reported an exact value, otherwise an APIReportedPercent object (range, suppressed, legacyImputed or derived). Absent when not reported.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Why there is no exact number: &#39;range&#39;, &#39;suppressed&#39;, &#39;legacyImputed&#39; or &#39;derived&#39; | [optional] 
**value** | **float** | The percent value, when one exists (status &#39;derived&#39; with an exact result, or the &#39;legacyImputed&#39; stand-in). Absent otherwise. | [optional] 
**low** | **float** | Lower bound of the range in percent (0 means &#39;less than high&#39;). Absent for &#39;suppressed&#39;. | [optional] 
**high** | **float** | Upper bound of the range in percent (100 means &#39;at least low&#39;). Absent for &#39;suppressed&#39;. | [optional] 

## Example

```python
from schooldigger.models.api_test_score30_percent_met_standard import APITestScore30PercentMetStandard

# TODO update the JSON string below
json = "{}"
# create an instance of APITestScore30PercentMetStandard from a JSON string
api_test_score30_percent_met_standard_instance = APITestScore30PercentMetStandard.from_json(json)
# print the JSON string representation of the object
print(APITestScore30PercentMetStandard.to_json())

# convert the object into a dict
api_test_score30_percent_met_standard_dict = api_test_score30_percent_met_standard_instance.to_dict()
# create an instance of APITestScore30PercentMetStandard from a dict
api_test_score30_percent_met_standard_from_dict = APITestScore30PercentMetStandard.from_dict(api_test_score30_percent_met_standard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


