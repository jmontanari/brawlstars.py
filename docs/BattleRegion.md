# BattleRegion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from brawlstars.models.battle_region import BattleRegion

# TODO update the JSON string below
json = "{}"
# create an instance of BattleRegion from a JSON string
battle_region_instance = BattleRegion.from_json(json)
# print the JSON string representation of the object
print(BattleRegion.to_json())

# convert the object into a dict
battle_region_dict = battle_region_instance.to_dict()
# create an instance of BattleRegion from a dict
battle_region_from_dict = BattleRegion.from_dict(battle_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


