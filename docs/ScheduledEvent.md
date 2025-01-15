# ScheduledEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**ScheduledEventLocation**](ScheduledEventLocation.md) |  | [optional] 
**slot_id** | **int** |  | [optional] 
**start_time** | **str** |  | [optional] 
**end_time** | **str** |  | [optional] 

## Example

```python
from brawlstars.models.scheduled_event import ScheduledEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledEvent from a JSON string
scheduled_event_instance = ScheduledEvent.from_json(json)
# print the JSON string representation of the object
print(ScheduledEvent.to_json())

# convert the object into a dict
scheduled_event_dict = scheduled_event_instance.to_dict()
# create an instance of ScheduledEvent from a dict
scheduled_event_from_dict = ScheduledEvent.from_dict(scheduled_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


