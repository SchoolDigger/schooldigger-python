# APITestScore30

One test result (school, district or state level) as returned by API 3.0. Same members as the 2.4 object except  that the six percent metrics are either a plain number or an APIReportedPercent object (see that class), and a  score object is returned whenever the state reported anything - including a result that consists only of  suppressed or ranged values. Hand-written (not inherited from clsSD2testScore) because the number-or-object  union cannot come from the reflection copy the 2.4 models use.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**students_eligible** | **int** | Count of students eligible to take test | [optional] 
**students_tested** | **int** | Count of students tested | [optional] 
**mean_scaled_score** | **float** | Mean scale score | [optional] 
**percent_met_standard** | [**APITestScore30PercentMetStandard**](APITestScore30PercentMetStandard.md) |  | [optional] 
**number_met_standard** | **float** | Count of students meeting state standard | [optional] 
**num_tier1** | **int** | Count of students performing at tier 1 (Enterprise API level only) | [optional] 
**num_tier2** | **int** | Count of students performing at tier 2 (Enterprise API level only) | [optional] 
**num_tier3** | **int** | Count of students performing at tier 3 (Enterprise API level only) | [optional] 
**num_tier4** | **int** | Count of students performing at tier 4 (Enterprise API level only) | [optional] 
**num_tier5** | **int** | Count of students performing at tier 5 (Enterprise API level only) | [optional] 
**percent_tier1** | [**APITestScore30PercentTier1**](APITestScore30PercentTier1.md) |  | [optional] 
**percent_tier2** | [**APITestScore30PercentTier2**](APITestScore30PercentTier2.md) |  | [optional] 
**percent_tier3** | [**APITestScore30PercentTier3**](APITestScore30PercentTier3.md) |  | [optional] 
**percent_tier4** | [**APITestScore30PercentTier4**](APITestScore30PercentTier4.md) |  | [optional] 
**percent_tier5** | [**APITestScore30PercentTier5**](APITestScore30PercentTier5.md) |  | [optional] 

## Example

```python
from schooldigger.models.api_test_score30 import APITestScore30

# TODO update the JSON string below
json = "{}"
# create an instance of APITestScore30 from a JSON string
api_test_score30_instance = APITestScore30.from_json(json)
# print the JSON string representation of the object
print(APITestScore30.to_json())

# convert the object into a dict
api_test_score30_dict = api_test_score30_instance.to_dict()
# create an instance of APITestScore30 from a dict
api_test_score30_from_dict = APITestScore30.from_dict(api_test_score30_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


