# PlayerRanking


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club** | [**PlayerRankingClub**](PlayerRankingClub.md) |  | [optional] 
**icon** | [**PlayerIcon**](PlayerIcon.md) |  | [optional] 
**trophies** | **int** |  | [optional] 
**tag** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**rank** | **int** |  | [optional] 
**name_color** | **str** |  | [optional] 

## Example

```python
from brawlstars.models.player_ranking import PlayerRanking

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerRanking from a JSON string
player_ranking_instance = PlayerRanking.from_json(json)
# print the JSON string representation of the object
print(PlayerRanking.to_json())

# convert the object into a dict
player_ranking_dict = player_ranking_instance.to_dict()
# create an instance of PlayerRanking from a dict
player_ranking_from_dict = PlayerRanking.from_dict(player_ranking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


