# SetEsportsNotificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**players** | **List[object]** |  | [optional] 
**ttl** | **int** |  | [optional] 

## Example

```python
from brawlstars.models.set_esports_notification_request import SetEsportsNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetEsportsNotificationRequest from a JSON string
set_esports_notification_request_instance = SetEsportsNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(SetEsportsNotificationRequest.to_json())

# convert the object into a dict
set_esports_notification_request_dict = set_esports_notification_request_instance.to_dict()
# create an instance of SetEsportsNotificationRequest from a dict
set_esports_notification_request_from_dict = SetEsportsNotificationRequest.from_dict(set_esports_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


