# brawlstars.generated.BrawlersApi

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

* Api Key Authentication (JWT):
```python
import time
import os
import brawlstars.generated
from brawlstars.generated.models.brawler import Brawler
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
    api_instance = brawlstars.generated.BrawlersApi(api_client)
    brawler_id = 'brawler_id_example' # str | Identifier of the brawler.

    try:
        # Get information about a brawler.
        api_response = api_instance.get_brawler(brawler_id)
        print("The response of BrawlersApi->get_brawler:\n")
        pprint(api_response)
    except Exception as e:
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

# **get_brawlers**
> List[Brawler] get_brawlers(before=before, after=after, limit=limit)

Get list of available brawlers.

Get list of available brawlers.

### Example

* Api Key Authentication (JWT):
```python
import time
import os
import brawlstars.generated
from brawlstars.generated.models.brawler import Brawler
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
    api_instance = brawlstars.generated.BrawlersApi(api_client)
    before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
    after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
    limit = 56 # int | Limit the number of items returned in the response. (optional)

    try:
        # Get list of available brawlers.
        api_response = api_instance.get_brawlers(before=before, after=after, limit=limit)
        print("The response of BrawlersApi->get_brawlers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrawlersApi->get_brawlers: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 

### Return type

[**List[Brawler]**](Brawler.md)

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

