from typing import List

from brawlstars.generated import StarPower, Accessory
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
        configuration.api_key_prefix['authorization'] = 'Bearer'
        configuration.api_key['authorization'] = key
        self.client = ApiClient(configuration)

    def __cast_response(self, response, response_type):
        if isinstance(response, dict):
            response_list = [self.client.deserialize(brawler_dict, response_type) for brawler_dict in
                             response["items"]]
            return response_list
        if isinstance(response, list):
            response_list = [self.client.deserialize(item, response_type) for item in
                             response]
            return response_list
        else:
            response = self.client.deserialize(response, response_type)
            return response

    def get_brawlers(self) -> List[Brawler]:
        response = BrawlersApi(self.client).get_brawlers()
        brawlers: List[Brawler] = self.__cast_response(response, Brawler)
        for brawler in brawlers:
            brawler.star_powers = self.__cast_response(brawler.star_powers, StarPower)
            brawler.gadgets = self.__cast_response(brawler.gadgets, Accessory)

        return brawlers

    def get_brawler(self, brawler_id: str) -> Brawler:
        response = BrawlersApi(self.client).get_brawler(brawler_id=brawler_id)
        return self.__cast_response(response, Brawler)

    def get_club_members(self, club_tag: str) -> List[ClubMember]:
        response = ClubsApi(self.client).get_club_members(club_tag=club_tag)
        return self.__cast_response(response, ClubMember)

    def get_club(self, club_tag: str) -> Club:
        response = ClubsApi(self.client).get_club(club_tag=club_tag)
        return self.__cast_response(response, Club)

    def get_scheduled_events(self) -> List[ScheduledEvent]:
        response = EventsApi(self.client).get_scheduled_events()
        return self.__cast_response(response, ScheduledEvent)

    def get_battle_log(self, player_tag: str) -> List[Battle]:
        response = PlayersApi(self.client).get_battle_log(player_tag=player_tag)
        return self.__cast_response(response, Battle)

    def get_player(self, player_tag: str) -> Player:
        response = PlayersApi(self.client).get_player(player_tag=player_tag)
        return self.__cast_response(response, Player)

    def get_brawler_rankings(self, brawler_id: str, country_code: str = "global") -> List[PlayerRanking]:
        response = RankingsApi(self.client).get_brawler_rankings(brawler_id=brawler_id, country_code=country_code)
        return self.__cast_response(response, PlayerRanking)

    def get_club_rankings(self, country_code: str = "global") -> List[ClubRanking]:
        response = RankingsApi(self.client).get_club_rankings(client=self.client, country_code=country_code)
        return self.__cast_response(response, ClubRanking)

    def get_player_rankings(self, country_code: str = "global") -> List[PlayerRanking]:
        response = RankingsApi(self.client).get_player_rankings(client=self.client, country_code=country_code)
        return self.__cast_response(response, response)
