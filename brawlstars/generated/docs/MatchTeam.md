# MatchTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**players** | [**List[MatchTeamPlayer]**](MatchTeamPlayer.md) |  | [optional] 
**bans** | [**List[BrawlerInfo]**](BrawlerInfo.md) |  | [optional] 
**side** | **int** |  | [optional] 

## Example

```python
from brawlstars.generated.models.match_team import MatchTeam

# TODO update the JSON string below
json = "{}"
# create an instance of MatchTeam from a JSON string
match_team_instance = MatchTeam.from_json(json)
# print the JSON string representation of the object
print(MatchTeam.to_json())

# convert the object into a dict
match_team_dict = match_team_instance.to_dict()
# create an instance of MatchTeam from a dict
match_team_from_dict = MatchTeam.from_dict(match_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


