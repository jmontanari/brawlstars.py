# SiegeStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bot_damage_to_base** | **int** |  | [optional] 
**bot_level_by_round** | **List[object]** |  | [optional] 

## Example

```python
from brawlstars.generated.models.siege_stats import SiegeStats

# TODO update the JSON string below
json = "{}"
# create an instance of SiegeStats from a JSON string
siege_stats_instance = SiegeStats.from_json(json)
# print the JSON string representation of the object
print SiegeStats.to_json()

# convert the object into a dict
siege_stats_dict = siege_stats_instance.to_dict()
# create an instance of SiegeStats from a dict
siege_stats_from_dict = SiegeStats.from_dict(siege_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


