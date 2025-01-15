# ClubRanking


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**trophies** | **int** |  | [optional] 
**rank** | **int** |  | [optional] 
**member_count** | **int** |  | [optional] 
**badge_id** | **int** |  | [optional] 

## Example

```python
from brawlstars.models.club_ranking import ClubRanking

# TODO update the JSON string below
json = "{}"
# create an instance of ClubRanking from a JSON string
club_ranking_instance = ClubRanking.from_json(json)
# print the JSON string representation of the object
print(ClubRanking.to_json())

# convert the object into a dict
club_ranking_dict = club_ranking_instance.to_dict()
# create an instance of ClubRanking from a dict
club_ranking_from_dict = ClubRanking.from_dict(club_ranking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


