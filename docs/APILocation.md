# APILocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat_long** | [**APILatLong**](APILatLong.md) |  | [optional] 
**street** | **str** | Street address of the school or district (e.g. &#39;18500 37th Avenue N.E.&#39;) | [optional] 
**city** | **str** | City where the school or district is located | [optional] 
**state** | **str** | Two-letter state abbreviation (e.g. &#39;WA&#39;) | [optional] 
**state_full** | **str** | Full state name (WA &#x3D; Washington) | [optional] 
**zip** | **str** | 5-digit ZIP code | [optional] 
**zip4** | **str** | ZIP+4 suffix (4 digits, may be empty) | [optional] 
**city_url** | **str** | SchoolDigger URL for schools in this city | [optional] 
**zip_url** | **str** | SchoolDigger URL for schools in this zip code | [optional] 
**html** | **str** | HTML formatted address | [optional] 

## Example

```python
from schooldigger.models.api_location import APILocation

# TODO update the JSON string below
json = "{}"
# create an instance of APILocation from a JSON string
api_location_instance = APILocation.from_json(json)
# print the JSON string representation of the object
print(APILocation.to_json())

# convert the object into a dict
api_location_dict = api_location_instance.to_dict()
# create an instance of APILocation from a dict
api_location_from_dict = APILocation.from_dict(api_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


