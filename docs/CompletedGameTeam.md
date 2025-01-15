# CompletedGameTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **int** |  | [optional] 
**is_winner** | **bool** |  | [optional] 
**siege** | [**SiegeStats**](SiegeStats.md) |  | [optional] 
**players** | [**List[PlayerEntryCompletedGame]**](PlayerEntryCompletedGame.md) |  | [optional] 

## Example

```python
from brawlstars.models.completed_game_team import CompletedGameTeam

# TODO update the JSON string below
json = "{}"
# create an instance of CompletedGameTeam from a JSON string
completed_game_team_instance = CompletedGameTeam.from_json(json)
# print the JSON string representation of the object
print(CompletedGameTeam.to_json())

# convert the object into a dict
completed_game_team_dict = completed_game_team_instance.to_dict()
# create an instance of CompletedGameTeam from a dict
completed_game_team_from_dict = CompletedGameTeam.from_dict(completed_game_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


