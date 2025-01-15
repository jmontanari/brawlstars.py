# PlayerIcon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 

## Example

```python
from brawlstars.models.player_icon import PlayerIcon

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerIcon from a JSON string
player_icon_instance = PlayerIcon.from_json(json)
# print the JSON string representation of the object
print(PlayerIcon.to_json())

# convert the object into a dict
player_icon_dict = player_icon_instance.to_dict()
# create an instance of PlayerIcon from a dict
player_icon_from_dict = PlayerIcon.from_dict(player_icon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


