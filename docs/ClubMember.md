# ClubMember


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icon** | [**PlayerIcon**](PlayerIcon.md) |  | [optional] 
**tag** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**trophies** | **int** |  | [optional] 
**role** | **str** |  | [optional] 
**name_color** | **str** |  | [optional] 

## Example

```python
from brawlstars.generated.models.club_member import ClubMember

# TODO update the JSON string below
json = "{}"
# create an instance of ClubMember from a JSON string
club_member_instance = ClubMember.from_json(json)
# print the JSON string representation of the object
print ClubMember.to_json()

# convert the object into a dict
club_member_dict = club_member_instance.to_dict()
# create an instance of ClubMember from a dict
club_member_from_dict = ClubMember.from_dict(club_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


