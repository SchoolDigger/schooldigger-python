# APIVaxNote

A footnote the state's data carries (API 3.1), e.g. a change of definition between years. Figures list the ids of the notes that apply to them.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Note id, as listed in a figure&#39;s notes | [optional] 
**text** | **str** | Note text | [optional] 

## Example

```python
from schooldigger.models.api_vax_note import APIVaxNote

# TODO update the JSON string below
json = "{}"
# create an instance of APIVaxNote from a JSON string
api_vax_note_instance = APIVaxNote.from_json(json)
# print the JSON string representation of the object
print(APIVaxNote.to_json())

# convert the object into a dict
api_vax_note_dict = api_vax_note_instance.to_dict()
# create an instance of APIVaxNote from a dict
api_vax_note_from_dict = APIVaxNote.from_dict(api_vax_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


