# PlayerClub


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from brawlstars.models.player_club import PlayerClub

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerClub from a JSON string
player_club_instance = PlayerClub.from_json(json)
# print the JSON string representation of the object
print(PlayerClub.to_json())

# convert the object into a dict
player_club_dict = player_club_instance.to_dict()
# create an instance of PlayerClub from a dict
player_club_from_dict = PlayerClub.from_dict(player_club_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


