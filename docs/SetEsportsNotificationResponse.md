# SetEsportsNotificationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification** | [**SetEsportsNotificationRequest**](SetEsportsNotificationRequest.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from brawlstars.models.set_esports_notification_response import SetEsportsNotificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetEsportsNotificationResponse from a JSON string
set_esports_notification_response_instance = SetEsportsNotificationResponse.from_json(json)
# print the JSON string representation of the object
print(SetEsportsNotificationResponse.to_json())

# convert the object into a dict
set_esports_notification_response_dict = set_esports_notification_response_instance.to_dict()
# create an instance of SetEsportsNotificationResponse from a dict
set_esports_notification_response_from_dict = SetEsportsNotificationResponse.from_dict(set_esports_notification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


