# brawlstars.py
Brawl Stars API

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 1.1.0
- Generator version: 7.10.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import brawlstars
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import brawlstars
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import brawlstars
from brawlstars.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.brawlstars.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = brawlstars.Configuration(
    host = "https://api.brawlstars.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'


# Enter a context with an instance of the API client
async with brawlstars.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = brawlstars.BrawlersApi(api_client)
    brawler_id = 'brawler_id_example' # str | Identifier of the brawler.

    try:
        # Get information about a brawler.
        api_response = await api_instance.get_brawler(brawler_id)
        print("The response of BrawlersApi->get_brawler:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BrawlersApi->get_brawler: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.brawlstars.com/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BrawlersApi* | [**get_brawler**](docs/BrawlersApi.md#get_brawler) | **GET** /brawlers/{brawlerId} | Get information about a brawler.
*BrawlersApi* | [**get_brawlers**](docs/BrawlersApi.md#get_brawlers) | **GET** /brawlers | Get list of available brawlers.
*ClubsApi* | [**get_club**](docs/ClubsApi.md#get_club) | **GET** /clubs/{clubTag} | Get club information.
*ClubsApi* | [**get_club_members**](docs/ClubsApi.md#get_club_members) | **GET** /clubs/{clubTag}/members | List club members.
*EventsApi* | [**get_scheduled_events**](docs/EventsApi.md#get_scheduled_events) | **GET** /events/rotation | Get event rotation
*PlayersApi* | [**get_battle_log**](docs/PlayersApi.md#get_battle_log) | **GET** /players/{playerTag}/battlelog | Get log of recent battles for a player.
*PlayersApi* | [**get_player**](docs/PlayersApi.md#get_player) | **GET** /players/{playerTag} | Get player information
*RankingsApi* | [**get_brawler_rankings**](docs/RankingsApi.md#get_brawler_rankings) | **GET** /rankings/{countryCode}/brawlers/{brawlerId} | Get brawler rankings for a country or global rankings.
*RankingsApi* | [**get_club_rankings**](docs/RankingsApi.md#get_club_rankings) | **GET** /rankings/{countryCode}/clubs | Get club rankings for a country or global rankings.
*RankingsApi* | [**get_player_rankings**](docs/RankingsApi.md#get_player_rankings) | **GET** /rankings/{countryCode}/players | Get player rankings for a country or global rankings.


## Documentation For Models

 - [Accessory](docs/Accessory.md)
 - [BannedBrawlerEntry](docs/BannedBrawlerEntry.md)
 - [Battle](docs/Battle.md)
 - [BattleRegion](docs/BattleRegion.md)
 - [Brawler](docs/Brawler.md)
 - [BrawlerInfo](docs/BrawlerInfo.md)
 - [BrawlerStat](docs/BrawlerStat.md)
 - [CancelMatchResponse](docs/CancelMatchResponse.md)
 - [ClientError](docs/ClientError.md)
 - [Club](docs/Club.md)
 - [ClubMember](docs/ClubMember.md)
 - [ClubRanking](docs/ClubRanking.md)
 - [CompletedGame](docs/CompletedGame.md)
 - [CompletedGameTeam](docs/CompletedGameTeam.md)
 - [Event](docs/Event.md)
 - [GearInfo](docs/GearInfo.md)
 - [GearStat](docs/GearStat.md)
 - [Match](docs/Match.md)
 - [MatchLocation](docs/MatchLocation.md)
 - [MatchTeam](docs/MatchTeam.md)
 - [MatchTeamPlayer](docs/MatchTeamPlayer.md)
 - [Player](docs/Player.md)
 - [PlayerClub](docs/PlayerClub.md)
 - [PlayerEntry](docs/PlayerEntry.md)
 - [PlayerEntryCompletedGame](docs/PlayerEntryCompletedGame.md)
 - [PlayerIcon](docs/PlayerIcon.md)
 - [PlayerMatchStatus](docs/PlayerMatchStatus.md)
 - [PlayerRanking](docs/PlayerRanking.md)
 - [PlayerRankingClub](docs/PlayerRankingClub.md)
 - [RegisterMatchRequest](docs/RegisterMatchRequest.md)
 - [RegisterMatchResponse](docs/RegisterMatchResponse.md)
 - [ScheduledEvent](docs/ScheduledEvent.md)
 - [ScheduledEventLocation](docs/ScheduledEventLocation.md)
 - [ServiceVersion](docs/ServiceVersion.md)
 - [SetEsportsNotificationRequest](docs/SetEsportsNotificationRequest.md)
 - [SetEsportsNotificationResponse](docs/SetEsportsNotificationResponse.md)
 - [SiegeStats](docs/SiegeStats.md)
 - [StarPower](docs/StarPower.md)
 - [Stats](docs/Stats.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="JWT"></a>
### JWT

- **Type**: API key
- **API key parameter name**: authorization
- **Location**: HTTP header


## Author



