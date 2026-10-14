# APIFreeReducedLunch

Students eligible for free or reduced-price school meals in one school year (API 3.1). Either count and percent, or a status when the reported count is not usable as a percent: \"communityEligibility\" (count is 98% or more of enrollment; the school likely serves free meals to all students), \"repeated\" (the state repeated the prior year's counts for most schools; not shown), \"aboveEnrollment\" (count exceeds enrollment; not shown).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Absent when count and percent are usable; otherwise \&quot;communityEligibility\&quot;, \&quot;repeated\&quot; or \&quot;aboveEnrollment\&quot; | [optional] 
**count** | **int** | Number of students eligible for free or reduced-price meals (absent for \&quot;repeated\&quot; and \&quot;aboveEnrollment\&quot;) | [optional] 
**percent** | **float** | Percent of enrolled students excluding pre-kindergarten (0-100, two decimals); absent when status is present | [optional] 

## Example

```python
from schooldigger.models.api_free_reduced_lunch import APIFreeReducedLunch

# TODO update the JSON string below
json = "{}"
# create an instance of APIFreeReducedLunch from a JSON string
api_free_reduced_lunch_instance = APIFreeReducedLunch.from_json(json)
# print the JSON string representation of the object
print(APIFreeReducedLunch.to_json())

# convert the object into a dict
api_free_reduced_lunch_dict = api_free_reduced_lunch_instance.to_dict()
# create an instance of APIFreeReducedLunch from a dict
api_free_reduced_lunch_from_dict = APIFreeReducedLunch.from_dict(api_free_reduced_lunch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


