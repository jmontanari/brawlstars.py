# Brawler


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gadgets** | [**List[Accessory]**](Accessory.md) |  | [optional] 
**name** | **object** |  | [optional] 
**id** | **int** |  | [optional] 
**star_powers** | [**List[StarPower]**](StarPower.md) |  | [optional] 

## Example

```python
from brawlstars.generated.models.brawler import Brawler

# TODO update the JSON string below
json = "{}"
# create an instance of Brawler from a JSON string
brawler_instance = Brawler.from_json(json)
# print the JSON string representation of the object
print Brawler.to_json()

# convert the object into a dict
brawler_dict = brawler_instance.to_dict()
# create an instance of Brawler from a dict
brawler_from_dict = Brawler.from_dict(brawler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


