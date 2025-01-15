# BannedBrawlerEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**side** | **int** |  | [optional] 

## Example

```python
from brawlstars.models.banned_brawler_entry import BannedBrawlerEntry

# TODO update the JSON string below
json = "{}"
# create an instance of BannedBrawlerEntry from a JSON string
banned_brawler_entry_instance = BannedBrawlerEntry.from_json(json)
# print the JSON string representation of the object
print(BannedBrawlerEntry.to_json())

# convert the object into a dict
banned_brawler_entry_dict = banned_brawler_entry_instance.to_dict()
# create an instance of BannedBrawlerEntry from a dict
banned_brawler_entry_from_dict = BannedBrawlerEntry.from_dict(banned_brawler_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


