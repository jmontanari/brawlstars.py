# PlayerEntryCompletedGame


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brawler** | [**BrawlerInfo**](BrawlerInfo.md) |  | [optional] 
**statistics** | [**Stats**](Stats.md) |  | [optional] 
**tag** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 

## Example

```python
from brawlstars.generated.models.player_entry_completed_game import PlayerEntryCompletedGame

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerEntryCompletedGame from a JSON string
player_entry_completed_game_instance = PlayerEntryCompletedGame.from_json(json)
# print the JSON string representation of the object
print(PlayerEntryCompletedGame.to_json())

# convert the object into a dict
player_entry_completed_game_dict = player_entry_completed_game_instance.to_dict()
# create an instance of PlayerEntryCompletedGame from a dict
player_entry_completed_game_from_dict = PlayerEntryCompletedGame.from_dict(player_entry_completed_game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


