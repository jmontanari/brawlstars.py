# MatchLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**game_mode** | **str** |  | [optional] 

## Example

```python
from brawlstars.models.match_location import MatchLocation

# TODO update the JSON string below
json = "{}"
# create an instance of MatchLocation from a JSON string
match_location_instance = MatchLocation.from_json(json)
# print the JSON string representation of the object
print(MatchLocation.to_json())

# convert the object into a dict
match_location_dict = match_location_instance.to_dict()
# create an instance of MatchLocation from a dict
match_location_from_dict = MatchLocation.from_dict(match_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


