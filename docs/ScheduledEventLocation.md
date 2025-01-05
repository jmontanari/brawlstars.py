# ScheduledEventLocation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | [optional] 
**modifiers** | **List[str]** |  | [optional] 
**id** | **int** |  | [optional] 
**map** | **object** |  | [optional] 

## Example

```python
from brawlstars.generated.models.scheduled_event_location import ScheduledEventLocation

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledEventLocation from a JSON string
scheduled_event_location_instance = ScheduledEventLocation.from_json(json)
# print the JSON string representation of the object
print ScheduledEventLocation.to_json()

# convert the object into a dict
scheduled_event_location_dict = scheduled_event_location_instance.to_dict()
# create an instance of ScheduledEventLocation from a dict
scheduled_event_location_from_dict = ScheduledEventLocation.from_dict(scheduled_event_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


