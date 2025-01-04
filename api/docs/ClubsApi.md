# swagger_client.ClubsApi

All URIs are relative to *https://api.brawlstars.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_club**](ClubsApi.md#get_club) | **GET** /clubs/{clubTag} | Get club information.
[**get_club_members**](ClubsApi.md#get_club_members) | **GET** /clubs/{clubTag}/members | List club members.

# **get_club**
> Club get_club(club_tag)

Get club information.

Get information about a single clan by club tag. Club tags can be found in game. Note that clan tags start with hash character '#' and that needs to be URL-encoded properly to work in URL, so for example clan tag '#2ABC' would become '%232ABC' in the URL. 

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
api_instance = swagger_client.ClubsApi(swagger_client.ApiClient(configuration))
club_tag = 'club_tag_example' # str | Tag of the club.

try:
    # Get club information.
    api_response = api_instance.get_club(club_tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubsApi->get_club: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **club_tag** | **str**| Tag of the club. | 

### Return type

[**Club**](Club.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_club_members**
> ClubMemberList get_club_members(club_tag, before=before, after=after, limit=limit)

List club members.

List club members.

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
api_instance = swagger_client.ClubsApi(swagger_client.ApiClient(configuration))
club_tag = 'club_tag_example' # str | Tag of the club.
before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
limit = 56 # int | Limit the number of items returned in the response. (optional)

try:
    # List club members.
    api_response = api_instance.get_club_members(club_tag, before=before, after=after, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubsApi->get_club_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **club_tag** | **str**| Tag of the club. | 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#x27;paging&#x27; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 

### Return type

[**ClubMemberList**](ClubMemberList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

