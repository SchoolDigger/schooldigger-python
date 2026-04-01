# APIBoundary12


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**polyline_collection** | [**List[APIPolyline]**](APIPolyline.md) | Collection of one or more Google Maps encoded polylines representing the attendance boundary. IMPORTANT: Polyline strings are JSON-encoded with escaped backslashes (double backslashes). You must unescape before passing to Google Maps decoding functions. Multiple polylines represent districts/schools with non-contiguous boundary areas. | [optional] 
**polylines** | **str** | Boundary as a WKT (Well-Known Text) MULTIPOLYGON string with explicit latitude/longitude vertices. Can be used directly with GIS software, PostGIS, or any system that accepts WKT geometry. Format: MULTIPOLYGON (((-122.27 47.77, ...))) | [optional] 
**has_boundary** | **bool** | States whether there is a boundary available | [optional] 

## Example

```python
from schooldigger.models.api_boundary12 import APIBoundary12

# TODO update the JSON string below
json = "{}"
# create an instance of APIBoundary12 from a JSON string
api_boundary12_instance = APIBoundary12.from_json(json)
# print the JSON string representation of the object
print(APIBoundary12.to_json())

# convert the object into a dict
api_boundary12_dict = api_boundary12_instance.to_dict()
# create an instance of APIBoundary12 from a dict
api_boundary12_from_dict = APIBoundary12.from_dict(api_boundary12_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


