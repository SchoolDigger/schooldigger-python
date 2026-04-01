# APILatLong


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | Latitude coordinate of the school or district address (WGS84 decimal degrees) | [optional] 
**longitude** | **float** | Longitude coordinate of the school or district address (WGS84 decimal degrees, negative for Western Hemisphere) | [optional] 

## Example

```python
from schooldigger.models.api_lat_long import APILatLong

# TODO update the JSON string below
json = "{}"
# create an instance of APILatLong from a JSON string
api_lat_long_instance = APILatLong.from_json(json)
# print the JSON string representation of the object
print(APILatLong.to_json())

# convert the object into a dict
api_lat_long_dict = api_lat_long_instance.to_dict()
# create an instance of APILatLong from a dict
api_lat_long_from_dict = APILatLong.from_dict(api_lat_long_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


