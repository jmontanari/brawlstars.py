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
    def __init__(self, key: str):
        configuration = Configuration()
        configuration.api_key['authorization'] = key
        self.client = ApiClient(configuration)

    def get_brawlers(self) -> List[Brawler]:
        return BrawlersApi(self.client).get_brawlers()

    def get_brawler(self, brawler_id: str) -> Brawler:
        return BrawlersApi(self.client).get_brawler(brawler_id=brawler_id)

    def get_club_members(self, club_tag: str) -> List[ClubMember]:
        return ClubsApi(self.client).get_club_members(club_tag=club_tag)

    def get_club(self, club_tag: str) -> Club:
        return ClubsApi(self.client).get_club(club_tag=club_tag)

    def get_scheduled_events(self) -> List[ScheduledEvent]:
        return EventsApi(self.client).get_scheduled_events()

    def get_battle_log(self, player_tag: str) -> List[Battle]:
        return PlayersApi(self.client).get_battle_log(player_tag=player_tag)

    def get_player(self, player_tag: str) -> Player:
        return PlayersApi(self.client).get_player(player_tag=player_tag)

    def get_brawler_rankings(self, brawler_id: str, country_code: str = "global") -> List[PlayerRanking]:
        return RankingsApi(self.client).get_brawler_rankings(brawler_id=brawler_id, country_code=country_code)

    def get_club_rankings(self, country_code: str = "global") -> List[ClubRanking]:
        return RankingsApi(self.client).get_club_rankings(client=self.client, country_code=country_code)

    def get_player_rankings(self, country_code: str = "global") -> List[PlayerRanking]:
        return RankingsApi(self.client).get_player_rankings(client=self.client, country_code=country_code)
