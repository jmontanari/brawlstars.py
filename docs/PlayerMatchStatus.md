# PlayerMatchStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brawler** | [**BrawlerInfo**](BrawlerInfo.md) |  | [optional] 
**is_in_battle** | **bool** |  | [optional] 
**is_ready** | **bool** |  | [optional] 
**is_online** | **bool** |  | [optional] 
**has_joined** | **bool** |  | [optional] 
**tag** | **str** |  | [optional] 

## Example

```python
from brawlstars.models.player_match_status import PlayerMatchStatus

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerMatchStatus from a JSON string
player_match_status_instance = PlayerMatchStatus.from_json(json)
# print the JSON string representation of the object
print(PlayerMatchStatus.to_json())

# convert the object into a dict
player_match_status_dict = player_match_status_instance.to_dict()
# create an instance of PlayerMatchStatus from a dict
player_match_status_from_dict = PlayerMatchStatus.from_dict(player_match_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


