# Accessory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from brawlstars.generated.models.accessory import Accessory

# TODO update the JSON string below
json = "{}"
# create an instance of Accessory from a JSON string
accessory_instance = Accessory.from_json(json)
# print the JSON string representation of the object
print Accessory.to_json()

# convert the object into a dict
accessory_dict = accessory_instance.to_dict()
# create an instance of Accessory from a dict
accessory_from_dict = Accessory.from_dict(accessory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


