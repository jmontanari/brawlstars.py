# MatchTeamPlayer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caused_termination** | **bool** |  | [optional] 
**tag** | **str** |  | [optional] 
**is_leader** | **bool** |  | [optional] 
**brawler** | [**BrawlerInfo**](BrawlerInfo.md) |  | [optional] 

## Example

```python
from brawlstars.models.match_team_player import MatchTeamPlayer

# TODO update the JSON string below
json = "{}"
# create an instance of MatchTeamPlayer from a JSON string
match_team_player_instance = MatchTeamPlayer.from_json(json)
# print the JSON string representation of the object
print(MatchTeamPlayer.to_json())

# convert the object into a dict
match_team_player_dict = match_team_player_instance.to_dict()
# create an instance of MatchTeamPlayer from a dict
match_team_player_from_dict = MatchTeamPlayer.from_dict(match_team_player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


