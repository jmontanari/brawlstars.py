# swagger_client.RankingsApi

All URIs are relative to *https://api.brawlstars.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_brawler_rankings**](RankingsApi.md#get_brawler_rankings) | **GET** /rankings/{countryCode}/brawlers/{brawlerId} | Get brawler rankings for a country or global rankings.
[**get_club_rankings**](RankingsApi.md#get_club_rankings) | **GET** /rankings/{countryCode}/clubs | Get club rankings for a country or global rankings.
[**get_player_rankings**](RankingsApi.md#get_player_rankings) | **GET** /rankings/{countryCode}/players | Get player rankings for a country or global rankings.

# **get_brawler_rankings**
> PlayerRankingList get_brawler_rankings(country_code, brawler_id, before=before, after=after, limit=limit)

Get brawler rankings for a country or global rankings.

Get brawler rankings for a country or global rankings. Brawler identifiers can be found by using the /v1/brawlers API endpoint. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT
configuration = swagger_client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RankingsApi(swagger_client.ApiClient(configuration))
country_code = 'country_code_example' # str | Two letter country code, or 'global' for global rankings.
brawler_id = 'brawler_id_example' # str | Identifier of the brawler.
before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
limit = 56 # int | Limit the number of items returned in the response. (optional)

try:
    # Get brawler rankings for a country or global rankings.
    api_response = api_instance.get_brawler_rankings(country_code, brawler_id, before=before, after=after, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankingsApi->get_brawler_rankings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| Two letter country code, or &#x27;global&#x27; for global rankings. | 
 **brawler_id** | **str**| Identifier of the brawler. | 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 

### Return type

[**PlayerRankingList**](PlayerRankingList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_club_rankings**
> ClubRankingList get_club_rankings(country_code, before=before, after=after, limit=limit)

Get club rankings for a country or global rankings.

Get club rankings for a country or global rankings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT
configuration = swagger_client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RankingsApi(swagger_client.ApiClient(configuration))
country_code = 'country_code_example' # str | Two letter country code, or 'global' for global rankings.
before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
limit = 56 # int | Limit the number of items returned in the response. (optional)

try:
    # Get club rankings for a country or global rankings.
    api_response = api_instance.get_club_rankings(country_code, before=before, after=after, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankingsApi->get_club_rankings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| Two letter country code, or &#x27;global&#x27; for global rankings. | 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 

### Return type

[**ClubRankingList**](ClubRankingList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_rankings**
> PlayerRankingList get_player_rankings(country_code, before=before, after=after, limit=limit)

Get player rankings for a country or global rankings.

Get player rankings for a country or global rankings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT
configuration = swagger_client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RankingsApi(swagger_client.ApiClient(configuration))
country_code = 'country_code_example' # str | Two letter country code, or 'global' for global rankings.
before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
limit = 56 # int | Limit the number of items returned in the response. (optional)

try:
    # Get player rankings for a country or global rankings.
    api_response = api_instance.get_player_rankings(country_code, before=before, after=after, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankingsApi->get_player_rankings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| Two letter country code, or &#x27;global&#x27; for global rankings. | 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 

### Return type

[**PlayerRankingList**](PlayerRankingList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

