# GearInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**level** | **int** |  | [optional] 

## Example

```python
from brawlstars.models.gear_info import GearInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GearInfo from a JSON string
gear_info_instance = GearInfo.from_json(json)
# print the JSON string representation of the object
print(GearInfo.to_json())

# convert the object into a dict
gear_info_dict = gear_info_instance.to_dict()
# create an instance of GearInfo from a dict
gear_info_from_dict = GearInfo.from_dict(gear_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


