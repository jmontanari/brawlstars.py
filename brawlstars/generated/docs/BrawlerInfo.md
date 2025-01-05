# BrawlerInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trophy_change** | **int** |  | [optional] 
**gears** | [**List[GearInfo]**](GearInfo.md) |  | [optional] 
**star_power** | [**StarPower**](StarPower.md) |  | [optional] 
**gadget** | [**Accessory**](Accessory.md) |  | [optional] 
**power** | **int** |  | [optional] 
**trophies** | **int** |  | [optional] 
**name** | **object** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from brawlstars.generated.models.brawler_info import BrawlerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BrawlerInfo from a JSON string
brawler_info_instance = BrawlerInfo.from_json(json)
# print the JSON string representation of the object
print(BrawlerInfo.to_json())

# convert the object into a dict
brawler_info_dict = brawler_info_instance.to_dict()
# create an instance of BrawlerInfo from a dict
brawler_info_from_dict = BrawlerInfo.from_dict(brawler_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


