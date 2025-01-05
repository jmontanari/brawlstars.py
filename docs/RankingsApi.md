# brawlstars.generated.RankingsApi

All URIs are relative to *https://api.brawlstars.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_brawler_rankings**](RankingsApi.md#get_brawler_rankings) | **GET** /rankings/{countryCode}/brawlers/{brawlerId} | Get brawler rankings for a country or global rankings.
[**get_club_rankings**](RankingsApi.md#get_club_rankings) | **GET** /rankings/{countryCode}/clubs | Get club rankings for a country or global rankings.
[**get_player_rankings**](RankingsApi.md#get_player_rankings) | **GET** /rankings/{countryCode}/players | Get player rankings for a country or global rankings.


# **get_brawler_rankings**
> List[PlayerRanking] get_brawler_rankings(country_code, brawler_id, before=before, after=after, limit=limit)

Get brawler rankings for a country or global rankings.

Get brawler rankings for a country or global rankings. Brawler identifiers can be found by using the /v1/brawlers API endpoint. 

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import brawlstars.generated
from brawlstars.generated.models.player_ranking import PlayerRanking
from brawlstars.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.brawlstars.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = brawlstars.generated.Configuration(
    host = "https://api.brawlstars.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with brawlstars.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = brawlstars.generated.RankingsApi(api_client)
    country_code = 'country_code_example' # str | Two letter country code, or 'global' for global rankings.
    brawler_id = 'brawler_id_example' # str | Identifier of the brawler.
    before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
    after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
    limit = 56 # int | Limit the number of items returned in the response. (optional)

    try:
        # Get brawler rankings for a country or global rankings.
        api_response = api_instance.get_brawler_rankings(country_code, brawler_id, before=before, after=after, limit=limit)
        print("The response of RankingsApi->get_brawler_rankings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RankingsApi->get_brawler_rankings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| Two letter country code, or &#39;global&#39; for global rankings. | 
 **brawler_id** | **str**| Identifier of the brawler. | 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 

### Return type

[**List[PlayerRanking]**](PlayerRanking.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Client provided incorrect parameters for the request. |  -  |
**403** | Access denied, either because of missing/incorrect credentials or used API token does not grant access to the requested resource.  |  -  |
**404** | Resource was not found. |  -  |
**429** | Request was throttled, because amount of requests was above the threshold defined for the used API token.  |  -  |
**500** | Unknown error happened when handling the request. |  -  |
**503** | Service is temprorarily unavailable because of maintenance. |  -  |
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_club_rankings**
> List[ClubRanking] get_club_rankings(country_code, before=before, after=after, limit=limit)

Get club rankings for a country or global rankings.

Get club rankings for a country or global rankings.

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import brawlstars.generated
from brawlstars.generated.models.club_ranking import ClubRanking
from brawlstars.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.brawlstars.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = brawlstars.generated.Configuration(
    host = "https://api.brawlstars.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with brawlstars.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = brawlstars.generated.RankingsApi(api_client)
    country_code = 'country_code_example' # str | Two letter country code, or 'global' for global rankings.
    before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
    after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
    limit = 56 # int | Limit the number of items returned in the response. (optional)

    try:
        # Get club rankings for a country or global rankings.
        api_response = api_instance.get_club_rankings(country_code, before=before, after=after, limit=limit)
        print("The response of RankingsApi->get_club_rankings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RankingsApi->get_club_rankings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| Two letter country code, or &#39;global&#39; for global rankings. | 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 

### Return type

[**List[ClubRanking]**](ClubRanking.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Client provided incorrect parameters for the request. |  -  |
**403** | Access denied, either because of missing/incorrect credentials or used API token does not grant access to the requested resource.  |  -  |
**404** | Resource was not found. |  -  |
**429** | Request was throttled, because amount of requests was above the threshold defined for the used API token.  |  -  |
**500** | Unknown error happened when handling the request. |  -  |
**503** | Service is temprorarily unavailable because of maintenance. |  -  |
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_rankings**
> List[PlayerRanking] get_player_rankings(country_code, before=before, after=after, limit=limit)

Get player rankings for a country or global rankings.

Get player rankings for a country or global rankings.

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import brawlstars.generated
from brawlstars.generated.models.player_ranking import PlayerRanking
from brawlstars.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.brawlstars.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = brawlstars.generated.Configuration(
    host = "https://api.brawlstars.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with brawlstars.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = brawlstars.generated.RankingsApi(api_client)
    country_code = 'country_code_example' # str | Two letter country code, or 'global' for global rankings.
    before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
    after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
    limit = 56 # int | Limit the number of items returned in the response. (optional)

    try:
        # Get player rankings for a country or global rankings.
        api_response = api_instance.get_player_rankings(country_code, before=before, after=after, limit=limit)
        print("The response of RankingsApi->get_player_rankings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RankingsApi->get_player_rankings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| Two letter country code, or &#39;global&#39; for global rankings. | 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 

### Return type

[**List[PlayerRanking]**](PlayerRanking.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Client provided incorrect parameters for the request. |  -  |
**403** | Access denied, either because of missing/incorrect credentials or used API token does not grant access to the requested resource.  |  -  |
**404** | Resource was not found. |  -  |
**429** | Request was throttled, because amount of requests was above the threshold defined for the used API token.  |  -  |
**500** | Unknown error happened when handling the request. |  -  |
**503** | Service is temprorarily unavailable because of maintenance. |  -  |
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

