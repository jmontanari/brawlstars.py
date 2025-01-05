# Stats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**healing_done** | **int** |  | [optional] 
**deaths** | **int** |  | [optional] 
**damage_dealt** | **int** |  | [optional] 
**kills** | **int** |  | [optional] 
**average_latency** | **int** |  | [optional] 
**damage_received** | **int** |  | [optional] 
**total_damage_to_safe** | **int** |  | [optional] 
**total_damage_to_pets** | **int** |  | [optional] 
**siege_damage_to_robot** | **int** |  | [optional] 
**siege_bolts_collected** | **int** |  | [optional] 
**brawl_ball_goals_scored** | **int** |  | [optional] 
**gem_grab_gems_collected** | **int** |  | [optional] 
**gem_grab_gems_lost** | **int** |  | [optional] 
**bounty_stars_gained** | **int** |  | [optional] 
**bounty_stars_lost** | **int** |  | [optional] 
**super_used_count** | **int** |  | [optional] 
**gadget_used_count** | **int** |  | [optional] 
**bounty_picked_middle_star** | **bool** |  | [optional] 
**match_end_kill_streak** | **int** |  | [optional] 
**max_kill_streak** | **int** |  | [optional] 
**hot_zone_inside_zone_percentage** | **int** |  | [optional] 
**healing_done_to_self** | **int** |  | [optional] 
**healing_done_to_team_mates** | **int** |  | [optional] 
**objectives_recovered** | **int** |  | [optional] 
**objectives_stolen** | **int** |  | [optional] 
**brawl_ball_shots_on_goal** | **int** |  | [optional] 
**brawl_ball_shots_saved** | **int** |  | [optional] 

## Example

```python
from brawlstars.generated.models.stats import Stats

# TODO update the JSON string below
json = "{}"
# create an instance of Stats from a JSON string
stats_instance = Stats.from_json(json)
# print the JSON string representation of the object
print Stats.to_json()

# convert the object into a dict
stats_dict = stats_instance.to_dict()
# create an instance of Stats from a dict
stats_from_dict = Stats.from_dict(stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


