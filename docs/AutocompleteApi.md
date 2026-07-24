# schooldigger.AutocompleteApi

All URIs are relative to *https://api.schooldigger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autocomplete_districts**](AutocompleteApi.md#autocomplete_districts) | **GET** /v2.4/autocomplete/districts | Returns a simple and quick list of districts for use in a client-typed autocomplete
[**autocomplete_schools**](AutocompleteApi.md#autocomplete_schools) | **GET** /v2.4/autocomplete/schools | Returns a simple and quick list of schools for use in a client-typed autocomplete


# **autocomplete_districts**
> APIAutocompleteDistrictResult autocomplete_districts(q=q, st=st, box_latitude_nw=box_latitude_nw, box_longitude_nw=box_longitude_nw, box_latitude_se=box_latitude_se, box_longitude_se=box_longitude_se, return_count=return_count)

Returns a simple and quick list of districts for use in a client-typed autocomplete



### Example

* Api Key Authentication (appID):
* Api Key Authentication (appKey):

```python
import schooldigger
from schooldigger.models.api_autocomplete_district_result import APIAutocompleteDistrictResult
from schooldigger.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.schooldigger.com
# See configuration.py for a list of all supported configuration parameters.
configuration = schooldigger.Configuration(
    host = "https://api.schooldigger.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: appID
configuration.api_key['appID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['appID'] = 'Bearer'

# Configure API key authorization: appKey
configuration.api_key['appKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['appKey'] = 'Bearer'

# Enter a context with an instance of the API client
with schooldigger.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = schooldigger.AutocompleteApi(api_client)
    q = 'q_example' # str | Search term for autocomplete (e.g. 'Lincol') (required) (optional)
    st = 'st_example' # str | Two character state (e.g. 'CA') (optional -- leave blank to search entire U.S.) (optional)
    box_latitude_nw = 3.4 # float | Search within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise API levels only.) (optional)
    box_longitude_nw = 3.4 # float | Search within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise API levels only.) (optional)
    box_latitude_se = 3.4 # float | Search within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise API levels only.) (optional)
    box_longitude_se = 3.4 # float | Search within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise API levels only.) (optional)
    return_count = 56 # int | Number of districts to return. Valid values: 1-20. (default: 10) (optional)

    try:
        # Returns a simple and quick list of districts for use in a client-typed autocomplete
        api_response = api_instance.autocomplete_districts(q=q, st=st, box_latitude_nw=box_latitude_nw, box_longitude_nw=box_longitude_nw, box_latitude_se=box_latitude_se, box_longitude_se=box_longitude_se, return_count=return_count)
        print("The response of AutocompleteApi->autocomplete_districts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutocompleteApi->autocomplete_districts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Search term for autocomplete (e.g. &#39;Lincol&#39;) (required) | [optional] 
 **st** | **str**| Two character state (e.g. &#39;CA&#39;) (optional -- leave blank to search entire U.S.) | [optional] 
 **box_latitude_nw** | **float**| Search within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise API levels only.) | [optional] 
 **box_longitude_nw** | **float**| Search within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise API levels only.) | [optional] 
 **box_latitude_se** | **float**| Search within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise API levels only.) | [optional] 
 **box_longitude_se** | **float**| Search within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise API levels only.) | [optional] 
 **return_count** | **int**| Number of districts to return. Valid values: 1-20. (default: 10) | [optional] 

### Return type

[**APIAutocompleteDistrictResult**](APIAutocompleteDistrictResult.md)

### Authorization

[appID](../README.md#appID), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **autocomplete_schools**
> APIAutocompleteSchoolResult23 autocomplete_schools(q=q, q_search_city_state_name=q_search_city_state_name, st=st, level=level, district_id=district_id, box_latitude_nw=box_latitude_nw, box_longitude_nw=box_longitude_nw, box_latitude_se=box_latitude_se, box_longitude_se=box_longitude_se, return_count=return_count)

Returns a simple and quick list of schools for use in a client-typed autocomplete



### Example

* Api Key Authentication (appID):
* Api Key Authentication (appKey):

```python
import schooldigger
from schooldigger.models.api_autocomplete_school_result23 import APIAutocompleteSchoolResult23
from schooldigger.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.schooldigger.com
# See configuration.py for a list of all supported configuration parameters.
configuration = schooldigger.Configuration(
    host = "https://api.schooldigger.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: appID
configuration.api_key['appID'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['appID'] = 'Bearer'

# Configure API key authorization: appKey
configuration.api_key['appKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['appKey'] = 'Bearer'

# Enter a context with an instance of the API client
with schooldigger.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = schooldigger.AutocompleteApi(api_client)
    q = 'q_example' # str | Search term for autocomplete (e.g. 'Lincol') (required) (optional)
    q_search_city_state_name = True # bool | Extend the search term to include city and state (e.g. 'Lincoln el paso' matches Lincoln Middle School in El Paso) (optional) (optional)
    st = 'st_example' # str | Two character state (e.g. 'CA') (optional -- leave blank to search entire U.S.) (optional)
    level = 'level_example' # str | Search for schools at this level only. Valid values: 'Elementary', 'Middle', 'High', 'Alt', 'Private' (optional - leave blank to search for all schools) (optional)
    district_id = 'district_id_example' # str | Search within SchoolDigger District ID (optional. Pro, Enterprise, and Autocomplete Pro levels only.) (optional)
    box_latitude_nw = 3.4 # float | Search within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise, and Autocomplete Pro levels only.) (optional)
    box_longitude_nw = 3.4 # float | Search within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise, and Autocomplete Pro levels only.) (optional)
    box_latitude_se = 3.4 # float | Search within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise, and Autocomplete Pro levels only.) (optional)
    box_longitude_se = 3.4 # float | Search within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise, and Autocomplete Pro levels only.) (optional)
    return_count = 56 # int | Number of schools to return. Valid values: 1-20. (default: 10) (optional)

    try:
        # Returns a simple and quick list of schools for use in a client-typed autocomplete
        api_response = api_instance.autocomplete_schools(q=q, q_search_city_state_name=q_search_city_state_name, st=st, level=level, district_id=district_id, box_latitude_nw=box_latitude_nw, box_longitude_nw=box_longitude_nw, box_latitude_se=box_latitude_se, box_longitude_se=box_longitude_se, return_count=return_count)
        print("The response of AutocompleteApi->autocomplete_schools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutocompleteApi->autocomplete_schools: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Search term for autocomplete (e.g. &#39;Lincol&#39;) (required) | [optional] 
 **q_search_city_state_name** | **bool**| Extend the search term to include city and state (e.g. &#39;Lincoln el paso&#39; matches Lincoln Middle School in El Paso) (optional) | [optional] 
 **st** | **str**| Two character state (e.g. &#39;CA&#39;) (optional -- leave blank to search entire U.S.) | [optional] 
 **level** | **str**| Search for schools at this level only. Valid values: &#39;Elementary&#39;, &#39;Middle&#39;, &#39;High&#39;, &#39;Alt&#39;, &#39;Private&#39; (optional - leave blank to search for all schools) | [optional] 
 **district_id** | **str**| Search within SchoolDigger District ID (optional. Pro, Enterprise, and Autocomplete Pro levels only.) | [optional] 
 **box_latitude_nw** | **float**| Search within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise, and Autocomplete Pro levels only.) | [optional] 
 **box_longitude_nw** | **float**| Search within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise, and Autocomplete Pro levels only.) | [optional] 
 **box_latitude_se** | **float**| Search within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise, and Autocomplete Pro levels only.) | [optional] 
 **box_longitude_se** | **float**| Search within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise, and Autocomplete Pro levels only.) | [optional] 
 **return_count** | **int**| Number of schools to return. Valid values: 1-20. (default: 10) | [optional] 

### Return type

[**APIAutocompleteSchoolResult23**](APIAutocompleteSchoolResult23.md)

### Authorization

[appID](../README.md#appID), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

