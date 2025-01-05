# RegisterMatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | [optional] 
**players** | [**List[PlayerEntry]**](PlayerEntry.md) |  | [optional] 
**location_id** | **int** |  | [optional] 
**wins_required** | **int** |  | [optional] 
**gadgets_allowed** | **bool** |  | [optional] 
**banned_brawlers** | [**List[BannedBrawlerEntry]**](BannedBrawlerEntry.md) |  | [optional] 
**timer_preset** | **str** |  | [optional] 

## Example

```python
from brawlstars.generated.models.register_match_request import RegisterMatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterMatchRequest from a JSON string
register_match_request_instance = RegisterMatchRequest.from_json(json)
# print the JSON string representation of the object
print(RegisterMatchRequest.to_json())

# convert the object into a dict
register_match_request_dict = register_match_request_instance.to_dict()
# create an instance of RegisterMatchRequest from a dict
register_match_request_from_dict = RegisterMatchRequest.from_dict(register_match_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


