from typing import List, Annotated

from pydantic import StrictStr, Field

from brawlstars.api.brawlers_api import BrawlersApi
from brawlstars.api.clubs_api import ClubsApi
from brawlstars.api.events_api import EventsApi
from brawlstars.api.players_api import PlayersApi
from brawlstars.api.rankings_api import RankingsApi
from brawlstars.api_client import ApiClient
from brawlstars.configuration import Configuration
from brawlstars.models.battle import Battle
from brawlstars.models.brawler import Brawler
from brawlstars.models.club import Club
from brawlstars.models.club_member import ClubMember
from brawlstars.models.club_ranking import ClubRanking
from brawlstars.models.player import Player
from brawlstars.models.player_ranking import PlayerRanking
from brawlstars.models.scheduled_event import ScheduledEvent


class BrawlClient:
    def __init__(self):
        self.configuration = Configuration()
        self.configuration.api_key_prefix['JWT'] = 'Bearer'
        self.client = None

    async def login(self, username: str, password: str):
        """Retrieves all keys and creates an HTTP connection ready for use.

        Parameters
        ----------
        username : str
            Your password email from https://developer.brawlstars.com
            This is used when updating keys automatically if your IP changes

        password : str
            Your password login from https://developer.brawlstars.com
            This is used when updating keys automatically if your IP changes
        """
        self.configuration.username = username
        self.configuration.password = password

        self.client = ApiClient(self.configuration)
        await self.client.init_keys()

    async def login_with_token(self, token: str) -> None:
        """Creates an HTTP connection ready for use with the tokens you provide.

        Parameters
        ----------
        token: str
            Token as found from https://developer.brawlstars.com under "My account" -> <your key> -> "token".
        """
        self.configuration.api_key['JWT'] = token
        self.client = ApiClient(self.configuration)

    async def get_brawlers(self) -> List[Brawler]:
        response = await BrawlersApi(self.client).get_brawlers()
        return response

    async def get_brawler(self, brawler_id: str) -> Brawler:
        response = await BrawlersApi(self.client).get_brawler(self.__to_annotated_str(brawler_id))
        return response

    async def get_club_members(self, club_tag: str) -> List[ClubMember]:
        response = await ClubsApi(self.client).get_club_members(club_tag=self.__to_annotated_str(club_tag))
        return response

    async def get_club(self, club_tag: str) -> Club:
        response = await ClubsApi(self.client).get_club(club_tag=self.__to_annotated_str(club_tag))
        return response

    async def get_scheduled_events(self) -> List[ScheduledEvent]:
        response = await EventsApi(self.client).get_scheduled_events()
        return response

    async def get_battle_log(self, player_tag: str) -> List[Battle]:
        response = await PlayersApi(self.client).get_battle_log(player_tag=self.__to_annotated_str(player_tag))
        return response

    async def get_player(self, player_tag: str) -> Player:
        response = await PlayersApi(self.client).get_player(player_tag=self.__to_annotated_str(player_tag))
        return response

    async def get_brawler_rankings(self, brawler_id: str, country_code: str = "global") -> List[PlayerRanking]:
        response = await RankingsApi(self.client).get_brawler_rankings(brawler_id=self.__to_annotated_str(brawler_id),
                                                                       country_code=self.__to_annotated_str(
                                                                           country_code))
        return response

    async def get_club_rankings(self, country_code: str = "global") -> List[ClubRanking]:
        response = await RankingsApi(self.client).get_club_rankings(client=self.client, country_code=country_code)
        return response

    async def get_player_rankings(self, country_code: str = "global") -> List[PlayerRanking]:
        response = await RankingsApi(self.client).get_player_rankings(client=self.client, country_code=country_code)
        return response

    def __to_annotated_str(self, value: str) -> Annotated[StrictStr, Field(description="Identifier")]:
        return Annotated[StrictStr, Field(description="Identifier of the brawler.")](value)
