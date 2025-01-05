# Battle


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**battle** | **object** |  | [optional] 
**battle_time** | **str** |  | [optional] 
**event** | [**Event**](Event.md) |  | [optional] 

## Example

```python
from brawlstars.generated.models.battle import Battle

# TODO update the JSON string below
json = "{}"
# create an instance of Battle from a JSON string
battle_instance = Battle.from_json(json)
# print the JSON string representation of the object
print Battle.to_json()

# convert the object into a dict
battle_dict = battle_instance.to_dict()
# create an instance of Battle from a dict
battle_from_dict = Battle.from_dict(battle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


