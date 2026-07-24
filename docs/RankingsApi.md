# schooldigger.RankingsApi

All URIs are relative to *https://api.schooldigger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_district_rankings**](RankingsApi.md#get_district_rankings) | **GET** /v2.4/rankings/districts/{st} | Returns a SchoolDigger district ranking list
[**get_school_rankings**](RankingsApi.md#get_school_rankings) | **GET** /v2.4/rankings/schools/{st} | Returns a SchoolDigger school ranking list


# **get_district_rankings**
> APIDistrictListRank21 get_district_rankings(st, year=year, page=page, per_page=per_page)

Returns a SchoolDigger district ranking list

### Example

* Api Key Authentication (appID):
* Api Key Authentication (appKey):

```python
import schooldigger
from schooldigger.models.api_district_list_rank21 import APIDistrictListRank21
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
    api_instance = schooldigger.RankingsApi(api_client)
    st = 'st_example' # str | Two character state (e.g. 'CA')
    year = 56 # int | The ranking year (leave blank for most recent year) (optional)
    page = 56 # int | Page number to retrieve (optional, default: 1) (optional)
    per_page = 56 # int | Number of districts to retrieve on a page (50 max) (optional, default: 10) (optional)

    try:
        # Returns a SchoolDigger district ranking list
        api_response = api_instance.get_district_rankings(st, year=year, page=page, per_page=per_page)
        print("The response of RankingsApi->get_district_rankings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RankingsApi->get_district_rankings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **st** | **str**| Two character state (e.g. &#39;CA&#39;) | 
 **year** | **int**| The ranking year (leave blank for most recent year) | [optional] 
 **page** | **int**| Page number to retrieve (optional, default: 1) | [optional] 
 **per_page** | **int**| Number of districts to retrieve on a page (50 max) (optional, default: 10) | [optional] 

### Return type

[**APIDistrictListRank21**](APIDistrictListRank21.md)

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

# **get_school_rankings**
> APISchoolListRank21 get_school_rankings(st, year=year, level=level, page=page, per_page=per_page)

Returns a SchoolDigger school ranking list

### Example

* Api Key Authentication (appID):
* Api Key Authentication (appKey):

```python
import schooldigger
from schooldigger.models.api_school_list_rank21 import APISchoolListRank21
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
    api_instance = schooldigger.RankingsApi(api_client)
    st = 'st_example' # str | Two character state (e.g. 'CA')
    year = 56 # int | The ranking year (leave blank for most recent year) (optional)
    level = 'level_example' # str | Level of ranking: 'Elementary', 'Middle', or 'High' (optional)
    page = 56 # int | Page number to retrieve (optional, default: 1) (optional)
    per_page = 56 # int | Number of schools to retrieve on a page (50 max) (optional, default: 10) (optional)

    try:
        # Returns a SchoolDigger school ranking list
        api_response = api_instance.get_school_rankings(st, year=year, level=level, page=page, per_page=per_page)
        print("The response of RankingsApi->get_school_rankings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RankingsApi->get_school_rankings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **st** | **str**| Two character state (e.g. &#39;CA&#39;) | 
 **year** | **int**| The ranking year (leave blank for most recent year) | [optional] 
 **level** | **str**| Level of ranking: &#39;Elementary&#39;, &#39;Middle&#39;, or &#39;High&#39; | [optional] 
 **page** | **int**| Page number to retrieve (optional, default: 1) | [optional] 
 **per_page** | **int**| Number of schools to retrieve on a page (50 max) (optional, default: 10) | [optional] 

### Return type

[**APISchoolListRank21**](APISchoolListRank21.md)

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

