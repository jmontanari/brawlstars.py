# swagger_client.BrawlersApi

All URIs are relative to *https://api.brawlstars.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_brawler**](BrawlersApi.md#get_brawler) | **GET** /brawlers/{brawlerId} | Get information about a brawler.
[**get_brawlers**](BrawlersApi.md#get_brawlers) | **GET** /brawlers | Get list of available brawlers.

# **get_brawler**
> Brawler get_brawler(brawler_id)

Get information about a brawler.

Get information about a brawler.

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
api_instance = swagger_client.BrawlersApi(swagger_client.ApiClient(configuration))
brawler_id = 'brawler_id_example' # str | Identifier of the brawler.

try:
    # Get information about a brawler.
    api_response = api_instance.get_brawler(brawler_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BrawlersApi->get_brawler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brawler_id** | **str**| Identifier of the brawler. | 

### Return type

[**Brawler**](Brawler.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_brawlers**
> BrawlerList get_brawlers(before=before, after=after, limit=limit)

Get list of available brawlers.

Get list of available brawlers.

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
api_instance = swagger_client.BrawlersApi(swagger_client.ApiClient(configuration))
before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
limit = 56 # int | Limit the number of items returned in the response. (optional)

try:
    # Get list of available brawlers.
    api_response = api_instance.get_brawlers(before=before, after=after, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BrawlersApi->get_brawlers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 

### Return type

[**BrawlerList**](BrawlerList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

