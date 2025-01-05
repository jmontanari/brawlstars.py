# Player


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club** | [**PlayerClub**](PlayerClub.md) |  | [optional] 
**is_qualified_from_championship_challenge** | **bool** |  | [optional] 
**var_3vs3_victories** | **int** |  | [optional] 
**icon** | [**PlayerIcon**](PlayerIcon.md) |  | [optional] 
**tag** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**trophies** | **int** |  | [optional] 
**exp_level** | **int** |  | [optional] 
**exp_points** | **int** |  | [optional] 
**highest_trophies** | **int** |  | [optional] 
**solo_victories** | **int** |  | [optional] 
**duo_victories** | **int** |  | [optional] 
**best_robo_rumble_time** | **int** |  | [optional] 
**best_time_as_big_brawler** | **int** |  | [optional] 
**brawlers** | [**List[BrawlerStat]**](BrawlerStat.md) |  | [optional] 
**name_color** | **str** |  | [optional] 

## Example

```python
from brawlstars.generated.models.player import Player

# TODO update the JSON string below
json = "{}"
# create an instance of Player from a JSON string
player_instance = Player.from_json(json)
# print the JSON string representation of the object
print(Player.to_json())

# convert the object into a dict
player_dict = player_instance.to_dict()
# create an instance of Player from a dict
player_from_dict = Player.from_dict(player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


