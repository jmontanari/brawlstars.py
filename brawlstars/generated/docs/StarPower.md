# StarPower


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from brawlstars.generated.models.star_power import StarPower

# TODO update the JSON string below
json = "{}"
# create an instance of StarPower from a JSON string
star_power_instance = StarPower.from_json(json)
# print the JSON string representation of the object
print(StarPower.to_json())

# convert the object into a dict
star_power_dict = star_power_instance.to_dict()
# create an instance of StarPower from a dict
star_power_from_dict = StarPower.from_dict(star_power_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


