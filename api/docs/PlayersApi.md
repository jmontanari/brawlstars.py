# swagger_client.PlayersApi

All URIs are relative to *https://api.brawlstars.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_battle_log**](PlayersApi.md#get_battle_log) | **GET** /players/{playerTag}/battlelog | Get log of recent battles for a player.
[**get_player**](PlayersApi.md#get_player) | **GET** /players/{playerTag} | Get player information

# **get_battle_log**
> BattleList get_battle_log(player_tag)

Get log of recent battles for a player.

Get list of recent battle results for a player. NOTE: It may take up to 30 minutes for a new battle to appear in the battlelog. 

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
api_instance = swagger_client.PlayersApi(swagger_client.ApiClient(configuration))
player_tag = 'player_tag_example' # str | Tag of the player.

try:
    # Get log of recent battles for a player.
    api_response = api_instance.get_battle_log(player_tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->get_battle_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_tag** | **str**| Tag of the player. | 

### Return type

[**BattleList**](BattleList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player**
> Player get_player(player_tag)

Get player information

Get information about a single player by player tag. Player tags can be found either in game or by from clan member list. 

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
api_instance = swagger_client.PlayersApi(swagger_client.ApiClient(configuration))
player_tag = 'player_tag_example' # str | Tag of the player.

try:
    # Get player information
    api_response = api_instance.get_player(player_tag)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

