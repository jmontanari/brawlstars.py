# BrawlerStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gadgets** | [**List[Accessory]**](Accessory.md) |  | [optional] 
**star_powers** | [**List[StarPower]**](StarPower.md) |  | [optional] 
**id** | **int** |  | [optional] 
**rank** | **int** |  | [optional] 
**trophies** | **int** |  | [optional] 
**highest_trophies** | **int** |  | [optional] 
**power** | **int** |  | [optional] 
**gears** | [**List[GearStat]**](GearStat.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from brawlstars.models.brawler_stat import BrawlerStat

# TODO update the JSON string below
json = "{}"
# create an instance of BrawlerStat from a JSON string
brawler_stat_instance = BrawlerStat.from_json(json)
# print the JSON string representation of the object
print(BrawlerStat.to_json())

# convert the object into a dict
brawler_stat_dict = brawler_stat_instance.to_dict()
# create an instance of BrawlerStat from a dict
brawler_stat_from_dict = BrawlerStat.from_dict(brawler_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


