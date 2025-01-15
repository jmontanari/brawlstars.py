# CompletedGame


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**teams** | [**List[CompletedGameTeam]**](CompletedGameTeam.md) |  | [optional] 
**duration** | **int** |  | [optional] 
**location** | [**MatchLocation**](MatchLocation.md) |  | [optional] 
**replay_id** | **str** |  | [optional] 

## Example

```python
from brawlstars.models.completed_game import CompletedGame

# TODO update the JSON string below
json = "{}"
# create an instance of CompletedGame from a JSON string
completed_game_instance = CompletedGame.from_json(json)
# print the JSON string representation of the object
print(CompletedGame.to_json())

# convert the object into a dict
completed_game_dict = completed_game_instance.to_dict()
# create an instance of CompletedGame from a dict
completed_game_from_dict = CompletedGame.from_dict(completed_game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


