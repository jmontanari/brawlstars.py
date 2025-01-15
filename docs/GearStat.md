# GearStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**level** | **int** |  | [optional] 

## Example

```python
from brawlstars.models.gear_stat import GearStat

# TODO update the JSON string below
json = "{}"
# create an instance of GearStat from a JSON string
gear_stat_instance = GearStat.from_json(json)
# print the JSON string representation of the object
print(GearStat.to_json())

# convert the object into a dict
gear_stat_dict = gear_stat_instance.to_dict()
# create an instance of GearStat from a dict
gear_stat_from_dict = GearStat.from_dict(gear_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


