# APITestScoreWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test** | **str** | The name of the state-administered test | [optional] 
**subject** | **str** | Test subject | [optional] 
**year** | **int** | Year test was administered (2018 &#x3D; 2017-18) | [optional] 
**grade** | **str** | Grade level for which this test score applies (e.g. &#39;3&#39;, &#39;5&#39;, &#39;8&#39;, &#39;10&#39;, &#39;HS&#39;) | [optional] 
**school_test_score** | [**APITestScore**](APITestScore.md) |  | [optional] 
**district_test_score** | [**APITestScore**](APITestScore.md) |  | [optional] 
**state_test_score** | [**APITestScore**](APITestScore.md) |  | [optional] 
**tier1** | **str** | Label for the lowest performance tier on this test (e.g. &#39;Below Basic&#39;, &#39;Level 1&#39;). Tier labels are state-specific. Enterprise API level only. | [optional] 
**tier2** | **str** | Label for the second performance tier (e.g. &#39;Basic&#39;, &#39;Level 2&#39;). Enterprise API level only. | [optional] 
**tier3** | **str** | Label for the third performance tier (e.g. &#39;Proficient&#39;, &#39;Level 3&#39;). Enterprise API level only. | [optional] 
**tier4** | **str** | Label for the fourth performance tier (e.g. &#39;Advanced&#39;, &#39;Level 4&#39;). Enterprise API level only. | [optional] 
**tier5** | **str** | Label for the fifth performance tier, if applicable (e.g. &#39;No Score&#39;). Not all states use 5 tiers. Enterprise API level only. | [optional] 

## Example

```python
from schooldigger.models.api_test_score_wrapper import APITestScoreWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of APITestScoreWrapper from a JSON string
api_test_score_wrapper_instance = APITestScoreWrapper.from_json(json)
# print the JSON string representation of the object
print(APITestScoreWrapper.to_json())

# convert the object into a dict
api_test_score_wrapper_dict = api_test_score_wrapper_instance.to_dict()
# create an instance of APITestScoreWrapper from a dict
api_test_score_wrapper_from_dict = APITestScoreWrapper.from_dict(api_test_score_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


