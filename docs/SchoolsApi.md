# schooldigger.SchoolsApi

All URIs are relative to *https://api.schooldigger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_school**](SchoolsApi.md#get_school) | **GET** /v2.3/schools/{id} | Returns a detailed record for one school
[**search_schools**](SchoolsApi.md#search_schools) | **GET** /v2.3/schools | Returns a list of schools


# **get_school**
> APISchoolFull22 get_school(id)

Returns a detailed record for one school

Retrieve a school record from the SchoolDigger database

### Example

* Api Key Authentication (appID):
* Api Key Authentication (appKey):

```python
import schooldigger
from schooldigger.models.api_school_full22 import APISchoolFull22
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
    api_instance = schooldigger.SchoolsApi(api_client)
    id = 'id_example' # str | The 12 digit School ID (e.g. 064215006903)

    try:
        # Returns a detailed record for one school
        api_response = api_instance.get_school(id)
        print("The response of SchoolsApi->get_school:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchoolsApi->get_school: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The 12 digit School ID (e.g. 064215006903) | 

### Return type

[**APISchoolFull22**](APISchoolFull22.md)

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

# **search_schools**
> APISchoolList22 search_schools(st, q=q, q_search_school_name_only=q_search_school_name_only, district_id=district_id, level=level, city=city, zip=zip, is_magnet=is_magnet, is_charter=is_charter, is_virtual=is_virtual, is_title_i=is_title_i, is_title_i_schoolwide=is_title_i_schoolwide, near_latitude=near_latitude, near_longitude=near_longitude, near_address=near_address, distance_miles=distance_miles, box_latitude_nw=box_latitude_nw, box_longitude_nw=box_longitude_nw, box_latitude_se=box_latitude_se, box_longitude_se=box_longitude_se, page=page, per_page=per_page, sort_by=sort_by, include_unranked_schools_in_rank_sort=include_unranked_schools_in_rank_sort)

Returns a list of schools

Search the SchoolDigger database for schools. You may use any combination of criteria as query parameters.

### Example

* Api Key Authentication (appID):
* Api Key Authentication (appKey):

```python
import schooldigger
from schooldigger.models.api_school_list22 import APISchoolList22
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
    api_instance = schooldigger.SchoolsApi(api_client)
    st = 'st_example' # str | Two character state (e.g. 'CA') - required
    q = 'q_example' # str | Search term - note: will match school name or city (optional) (optional)
    q_search_school_name_only = True # bool | For parameter 'q', only search school names instead of school and city (optional) (optional)
    district_id = 'district_id_example' # str | Search for schools within this district (7 digit district id) (optional) (optional)
    level = 'level_example' # str | Search for schools at this level. Valid values: 'Elementary', 'Middle', 'High', 'Alt', 'Public', 'Private' (optional). 'Public' returns all Elementary, Middle, High and Alternative schools (optional)
    city = 'city_example' # str | Search for schools in this city (optional) (optional)
    zip = 'zip_example' # str | Search for schools in this 5-digit zip code (optional) (optional)
    is_magnet = True # bool | True = return only magnet schools, False = return only non-magnet schools (optional) (Pro, Enterprise API levels only) (optional)
    is_charter = True # bool | True = return only charter schools, False = return only non-charter schools (optional) (Pro, Enterprise API levels only) (optional)
    is_virtual = True # bool | True = return only virtual schools, False = return only non-virtual schools (optional) (Pro, Enterprise API levels only) (optional)
    is_title_i = True # bool | True = return only Title I schools, False = return only non-Title I schools (optional) (Pro, Enterprise API levels only) (optional)
    is_title_i_schoolwide = True # bool | True = return only Title I school-wide schools, False = return only non-Title I school-wide schools (optional) (Pro, Enterprise API levels only) (optional)
    near_latitude = 3.4 # float | Search for schools within (distanceMiles) of (nearLatitude)/(nearLongitude) (e.g. 44.982560) (optional) (Pro, Enterprise API levels only.) (optional)
    near_longitude = 3.4 # float | Search for schools within (distanceMiles) of (nearLatitude)/(nearLongitude) (e.g. -124.289185) (optional) (Pro, Enterprise API levels only.) (optional)
    near_address = 'near_address_example' # str | Search for schools within (distanceMiles) of this address. Example: '123 Main St. AnyTown CA 90001' (optional) (Pro, Enterprise API level only) IMPORTANT NOTE: If you have the lat/long of the address, use nearLatitude and nearLongitude instead for much faster response times (optional)
    distance_miles = 56 # int | Search for schools within (distanceMiles) of (nearLatitude)/(nearLongitude) (Default 5 miles) (optional) (Pro, Enterprise API levels only) (optional)
    box_latitude_nw = 3.4 # float | Search for schools within a 'box' defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional) (optional)
    box_longitude_nw = 3.4 # float | Search for schools within a 'box' defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional) (optional)
    box_latitude_se = 3.4 # float | Search for schools within a 'box' defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional) (optional)
    box_longitude_se = 3.4 # float | Search for schools within a 'box' defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional) (optional)
    page = 56 # int | Page number to retrieve (optional, default: 1) (optional)
    per_page = 56 # int | Number of schools to retrieve on a page (50 max) (optional, default: 10) (optional)
    sort_by = 'sort_by_example' # str | Sort list. Values are: schoolname, distance, rank. For descending order, precede with '-' i.e. -schoolname (optional, default: schoolname) (optional)
    include_unranked_schools_in_rank_sort = True # bool | If sortBy is 'rank', this boolean determines if schools with no rank are included in the result (optional, default: false) (optional)

    try:
        # Returns a list of schools
        api_response = api_instance.search_schools(st, q=q, q_search_school_name_only=q_search_school_name_only, district_id=district_id, level=level, city=city, zip=zip, is_magnet=is_magnet, is_charter=is_charter, is_virtual=is_virtual, is_title_i=is_title_i, is_title_i_schoolwide=is_title_i_schoolwide, near_latitude=near_latitude, near_longitude=near_longitude, near_address=near_address, distance_miles=distance_miles, box_latitude_nw=box_latitude_nw, box_longitude_nw=box_longitude_nw, box_latitude_se=box_latitude_se, box_longitude_se=box_longitude_se, page=page, per_page=per_page, sort_by=sort_by, include_unranked_schools_in_rank_sort=include_unranked_schools_in_rank_sort)
        print("The response of SchoolsApi->search_schools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchoolsApi->search_schools: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **st** | **str**| Two character state (e.g. &#39;CA&#39;) - required | 
 **q** | **str**| Search term - note: will match school name or city (optional) | [optional] 
 **q_search_school_name_only** | **bool**| For parameter &#39;q&#39;, only search school names instead of school and city (optional) | [optional] 
 **district_id** | **str**| Search for schools within this district (7 digit district id) (optional) | [optional] 
 **level** | **str**| Search for schools at this level. Valid values: &#39;Elementary&#39;, &#39;Middle&#39;, &#39;High&#39;, &#39;Alt&#39;, &#39;Public&#39;, &#39;Private&#39; (optional). &#39;Public&#39; returns all Elementary, Middle, High and Alternative schools | [optional] 
 **city** | **str**| Search for schools in this city (optional) | [optional] 
 **zip** | **str**| Search for schools in this 5-digit zip code (optional) | [optional] 
 **is_magnet** | **bool**| True &#x3D; return only magnet schools, False &#x3D; return only non-magnet schools (optional) (Pro, Enterprise API levels only) | [optional] 
 **is_charter** | **bool**| True &#x3D; return only charter schools, False &#x3D; return only non-charter schools (optional) (Pro, Enterprise API levels only) | [optional] 
 **is_virtual** | **bool**| True &#x3D; return only virtual schools, False &#x3D; return only non-virtual schools (optional) (Pro, Enterprise API levels only) | [optional] 
 **is_title_i** | **bool**| True &#x3D; return only Title I schools, False &#x3D; return only non-Title I schools (optional) (Pro, Enterprise API levels only) | [optional] 
 **is_title_i_schoolwide** | **bool**| True &#x3D; return only Title I school-wide schools, False &#x3D; return only non-Title I school-wide schools (optional) (Pro, Enterprise API levels only) | [optional] 
 **near_latitude** | **float**| Search for schools within (distanceMiles) of (nearLatitude)/(nearLongitude) (e.g. 44.982560) (optional) (Pro, Enterprise API levels only.) | [optional] 
 **near_longitude** | **float**| Search for schools within (distanceMiles) of (nearLatitude)/(nearLongitude) (e.g. -124.289185) (optional) (Pro, Enterprise API levels only.) | [optional] 
 **near_address** | **str**| Search for schools within (distanceMiles) of this address. Example: &#39;123 Main St. AnyTown CA 90001&#39; (optional) (Pro, Enterprise API level only) IMPORTANT NOTE: If you have the lat/long of the address, use nearLatitude and nearLongitude instead for much faster response times | [optional] 
 **distance_miles** | **int**| Search for schools within (distanceMiles) of (nearLatitude)/(nearLongitude) (Default 5 miles) (optional) (Pro, Enterprise API levels only) | [optional] 
 **box_latitude_nw** | **float**| Search for schools within a &#39;box&#39; defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional) | [optional] 
 **box_longitude_nw** | **float**| Search for schools within a &#39;box&#39; defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional) | [optional] 
 **box_latitude_se** | **float**| Search for schools within a &#39;box&#39; defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional) | [optional] 
 **box_longitude_se** | **float**| Search for schools within a &#39;box&#39; defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional) | [optional] 
 **page** | **int**| Page number to retrieve (optional, default: 1) | [optional] 
 **per_page** | **int**| Number of schools to retrieve on a page (50 max) (optional, default: 10) | [optional] 
 **sort_by** | **str**| Sort list. Values are: schoolname, distance, rank. For descending order, precede with &#39;-&#39; i.e. -schoolname (optional, default: schoolname) | [optional] 
 **include_unranked_schools_in_rank_sort** | **bool**| If sortBy is &#39;rank&#39;, this boolean determines if schools with no rank are included in the result (optional, default: false) | [optional] 

### Return type

[**APISchoolList22**](APISchoolList22.md)

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

