from typing import List

from brawlstars.generated.api.brawlers_api import BrawlersApi
from brawlstars.generated.api.clubs_api import ClubsApi
from brawlstars.generated.api.events_api import EventsApi
from brawlstars.generated.api.players_api import PlayersApi
from brawlstars.generated.api.rankings_api import RankingsApi
from brawlstars.generated.api_client import ApiClient
from brawlstars.generated.configuration import Configuration
from brawlstars.generated.models.battle import Battle
from brawlstars.generated.models.brawler import Brawler
from brawlstars.generated.models.club import Club
from brawlstars.generated.models.club_member import ClubMember
from brawlstars.generated.models.club_ranking import ClubRanking
from brawlstars.generated.models.player import Player
from brawlstars.generated.models.player_ranking import PlayerRanking
from brawlstars.generated.models.scheduled_event import ScheduledEvent


class BrawlClient:
    def __init__(self):
        self.configuration = Configuration()
        self.configuration.api_key_prefix['authorization'] = 'Bearer'
        self.client = None

    async def login(self, email: str, password: str):
        """Retrieves all keys and creates an HTTP connection ready for use.

        Parameters
        ----------
        email : str
            Your password email from https://developer.clashofclans.com
            This is used when updating keys automatically if your IP changes

        password : str
            Your password login from https://developer.clashofclans.com
            This is used when updating keys automatically if your IP changes
        """
        self.configuration.email = email
        self.configuration.password = password
        self.configuration.api_key_prefix['authorization'] = 'Bearer'

        self.client = ApiClient(self.configuration)
        await self.client.init_keys()

    async def login_with_token(self, token: str) -> None:
        """Creates an HTTP connection ready for use with the tokens you provide.

        Parameters
        ----------
        key: str
            Token as found from https://developer.brawlstars.com under "My account" -> <your key> -> "token".
        """
        self.configuration.api_key['authorization'] = token

        self.client = ApiClient(self.configuration)

    def get_brawlers(self) -> List[Brawler]:
        response = BrawlersApi(self.client).get_brawlers()
        return response

    def get_brawler(self, brawler_id: str) -> Brawler:
        response = BrawlersApi(self.client).get_brawler(brawler_id=brawler_id)
        return response

    def get_club_members(self, club_tag: str) -> List[ClubMember]:
        response = ClubsApi(self.client).get_club_members(club_tag=club_tag)
        return response

    def get_club(self, club_tag: str) -> Club:
        response = ClubsApi(self.client).get_club(club_tag=club_tag)
        return response

    def get_scheduled_events(self) -> List[ScheduledEvent]:
        response = EventsApi(self.client).get_scheduled_events()
        return response

    def get_battle_log(self, player_tag: str) -> List[Battle]:
        response = PlayersApi(self.client).get_battle_log(player_tag=player_tag)
        return response

    def get_player(self, player_tag: str) -> Player:
        response = PlayersApi(self.client).get_player(player_tag=player_tag)
        return response

    def get_brawler_rankings(self, brawler_id: str, country_code: str = "global") -> List[PlayerRanking]:
        response = RankingsApi(self.client).get_brawler_rankings(brawler_id=brawler_id, country_code=country_code)
        return response

    def get_club_rankings(self, country_code: str = "global") -> List[ClubRanking]:
        response = RankingsApi(self.client).get_club_rankings(client=self.client, country_code=country_code)
        return response

    def get_player_rankings(self, country_code: str = "global") -> List[PlayerRanking]:
        response = RankingsApi(self.client).get_player_rankings(client=self.client, country_code=country_code)
        return response
