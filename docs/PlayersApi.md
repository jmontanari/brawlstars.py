# brawlstars.PlayersApi

All URIs are relative to *https://api.brawlstars.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_battle_log**](PlayersApi.md#get_battle_log) | **GET** /players/{playerTag}/battlelog | Get log of recent battles for a player.
[**get_player**](PlayersApi.md#get_player) | **GET** /players/{playerTag} | Get player information


# **get_battle_log**
> List[Battle] get_battle_log(player_tag)

Get log of recent battles for a player.

Get list of recent battle results for a player. NOTE: It may take up to 30 minutes for a new battle to appear in the battlelog. 

### Example

* Api Key Authentication (JWT):

```python
import brawlstars
from brawlstars.models.battle import Battle
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
async with brawlstars.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = brawlstars.PlayersApi(api_client)
    player_tag = 'player_tag_example' # str | Tag of the player.

    try:
        # Get log of recent battles for a player.
        api_response = await api_instance.get_battle_log(player_tag)
        print("The response of PlayersApi->get_battle_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->get_battle_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_tag** | **str**| Tag of the player. | 

### Return type

[**List[Battle]**](Battle.md)

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

# **get_player**
> Player get_player(player_tag)

Get player information

Get information about a single player by player tag. Player tags can be found either in game or by from clan member list. 

### Example

* Api Key Authentication (JWT):

```python
import brawlstars
from brawlstars.models.player import Player
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
async with brawlstars.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = brawlstars.PlayersApi(api_client)
    player_tag = 'player_tag_example' # str | Tag of the player.

    try:
        # Get player information
        api_response = await api_instance.get_player(player_tag)
        print("The response of PlayersApi->get_player:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->get_player: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_tag** | **str**| Tag of the player. | 

### Return type

[**Player**](Player.md)

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

