# APIVaxSource

The state agency and publication the vaccination figures come from (API 3.1).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | SchoolDigger source id; figures from another source carry it as sourceId | [optional] 
**agency** | **str** | Publishing agency, e.g. \&quot;Washington State Department of Health\&quot; | [optional] 
**url** | **str** | The agency&#39;s page for the data | [optional] 
**headline_label** | **str** | What the state&#39;s headline figure measures, e.g. \&quot;Kindergartners complete for all required immunizations\&quot;. Absent when the state publishes no headline (e.g. HI: exemptions only) | [optional] 
**suppression_note** | **str** | How the state suppresses small groups, when it says so | [optional] 
**suppressed_count_text** | **str** | The meaning of a redacted count, e.g. \&quot;fewer than 10\&quot; (figures with value.status \&quot;redactedCount\&quot;) | [optional] 
**district_scope** | **str** | What the state&#39;s district figures cover: \&quot;public\&quot; (public schools only) or \&quot;publicAndPrivate\&quot; (public and private schools in the district&#39;s area); absent when the state does not say or publishes no district figures | [optional] 
**state_figure_label** | **str** | What the state figure covers when it is not statewide, e.g. \&quot;reporting schools\&quot; (NC); absent &#x3D; statewide | [optional] 
**is_legacy** | **bool** | True for figures migrated from an older SchoolDigger source the state no longer publishes in that form | [optional] 

## Example

```python
from schooldigger.models.api_vax_source import APIVaxSource

# TODO update the JSON string below
json = "{}"
# create an instance of APIVaxSource from a JSON string
api_vax_source_instance = APIVaxSource.from_json(json)
# print the JSON string representation of the object
print(APIVaxSource.to_json())

# convert the object into a dict
api_vax_source_dict = api_vax_source_instance.to_dict()
# create an instance of APIVaxSource from a dict
api_vax_source_from_dict = APIVaxSource.from_dict(api_vax_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


