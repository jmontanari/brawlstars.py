# brawlstars.ClubsApi

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

* Api Key Authentication (JWT):

```python
import brawlstars
from brawlstars.models.club import Club
from brawlstars.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.brawlstars.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = brawlstars.Configuration(
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
with brawlstars.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = brawlstars.ClubsApi(api_client)
    club_tag = 'club_tag_example' # str | Tag of the club.

    try:
        # Get club information.
        api_response = api_instance.get_club(club_tag)
        print("The response of ClubsApi->get_club:\n")
        pprint(api_response)
    except Exception as e:
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

# **get_club_members**
> List[ClubMember] get_club_members(club_tag, before=before, after=after, limit=limit)

List club members.

List club members.

### Example

* Api Key Authentication (JWT):

```python
import brawlstars
from brawlstars.models.club_member import ClubMember
from brawlstars.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.brawlstars.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = brawlstars.Configuration(
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
with brawlstars.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = brawlstars.ClubsApi(api_client)
    club_tag = 'club_tag_example' # str | Tag of the club.
    before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
    after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
    limit = 56 # int | Limit the number of items returned in the response. (optional)

    try:
        # List club members.
        api_response = api_instance.get_club_members(club_tag, before=before, after=after, limit=limit)
        print("The response of ClubsApi->get_club_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubsApi->get_club_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **club_tag** | **str**| Tag of the club. | 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 

### Return type

[**List[ClubMember]**](ClubMember.md)

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

