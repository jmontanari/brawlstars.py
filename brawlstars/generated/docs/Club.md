# Club


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**trophies** | **int** |  | [optional] 
**required_trophies** | **int** |  | [optional] 
**members** | [**List[ClubMember]**](ClubMember.md) |  | [optional] 
**type** | **str** |  | [optional] 
**badge_id** | **int** |  | [optional] 

## Example

```python
from brawlstars.generated.models.club import Club

# TODO update the JSON string below
json = "{}"
# create an instance of Club from a JSON string
club_instance = Club.from_json(json)
# print the JSON string representation of the object
print(Club.to_json())

# convert the object into a dict
club_dict = club_instance.to_dict()
# create an instance of Club from a dict
club_from_dict = Club.from_dict(club_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


