# generated.EventsApi

All URIs are relative to *https://api.brawlstars.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_scheduled_events**](EventsApi.md#get_scheduled_events) | **GET** /events/rotation | Get event rotation

# **get_scheduled_events**
> ScheduledEvents get_scheduled_events()

Get event rotation

Get event rotation for ongoing events.

### Example
```python
from __future__ import print_function
import time
import generated
from generated.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT
configuration = generated.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = generated.EventsApi(generated.ApiClient(configuration))

try:
    # Get event rotation
    api_response = api_instance.get_scheduled_events()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_scheduled_events: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ScheduledEvents**](ScheduledEvents.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

