# coding: utf-8

"""
    Brawl Stars API

    Brawl Stars API  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from brawlstars.generated.configuration import Configuration


class Player(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'club': 'PlayerClub',
        'is_qualified_from_championship_challenge': 'bool',
        '_3vs3_victories': 'int',
        'icon': 'PlayerIcon',
        'tag': 'str',
        'name': 'str',
        'trophies': 'int',
        'exp_level': 'int',
        'exp_points': 'int',
        'highest_trophies': 'int',
        'solo_victories': 'int',
        'duo_victories': 'int',
        'best_robo_rumble_time': 'int',
        'best_time_as_big_brawler': 'int',
        'brawlers': 'BrawlerStatList',
        'name_color': 'str'
    }

    attribute_map = {
        'club': 'club',
        'is_qualified_from_championship_challenge': 'isQualifiedFromChampionshipChallenge',
        '_3vs3_victories': '3vs3Victories',
        'icon': 'icon',
        'tag': 'tag',
        'name': 'name',
        'trophies': 'trophies',
        'exp_level': 'expLevel',
        'exp_points': 'expPoints',
        'highest_trophies': 'highestTrophies',
        'solo_victories': 'soloVictories',
        'duo_victories': 'duoVictories',
        'best_robo_rumble_time': 'bestRoboRumbleTime',
        'best_time_as_big_brawler': 'bestTimeAsBigBrawler',
        'brawlers': 'brawlers',
        'name_color': 'nameColor'
    }

    def __init__(self, club=None, is_qualified_from_championship_challenge=None, _3vs3_victories=None, icon=None, tag=None, name=None, trophies=None, exp_level=None, exp_points=None, highest_trophies=None, solo_victories=None, duo_victories=None, best_robo_rumble_time=None, best_time_as_big_brawler=None, brawlers=None, name_color=None, _configuration=None):  # noqa: E501
        """Player - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._club = None
        self._is_qualified_from_championship_challenge = None
        self.__3vs3_victories = None
        self._icon = None
        self._tag = None
        self._name = None
        self._trophies = None
        self._exp_level = None
        self._exp_points = None
        self._highest_trophies = None
        self._solo_victories = None
        self._duo_victories = None
        self._best_robo_rumble_time = None
        self._best_time_as_big_brawler = None
        self._brawlers = None
        self._name_color = None
        self.discriminator = None

        if club is not None:
            self.club = club
        if is_qualified_from_championship_challenge is not None:
            self.is_qualified_from_championship_challenge = is_qualified_from_championship_challenge
        if _3vs3_victories is not None:
            self._3vs3_victories = _3vs3_victories
        if icon is not None:
            self.icon = icon
        if tag is not None:
            self.tag = tag
        if name is not None:
            self.name = name
        if trophies is not None:
            self.trophies = trophies
        if exp_level is not None:
            self.exp_level = exp_level
        if exp_points is not None:
            self.exp_points = exp_points
        if highest_trophies is not None:
            self.highest_trophies = highest_trophies
        if solo_victories is not None:
            self.solo_victories = solo_victories
        if duo_victories is not None:
            self.duo_victories = duo_victories
        if best_robo_rumble_time is not None:
            self.best_robo_rumble_time = best_robo_rumble_time
        if best_time_as_big_brawler is not None:
            self.best_time_as_big_brawler = best_time_as_big_brawler
        if brawlers is not None:
            self.brawlers = brawlers
        if name_color is not None:
            self.name_color = name_color

    @property
    def club(self):
        """Gets the club of this Player.  # noqa: E501


        :return: The club of this Player.  # noqa: E501
        :rtype: PlayerClub
        """
        return self._club

    @club.setter
    def club(self, club):
        """Sets the club of this Player.


        :param club: The club of this Player.  # noqa: E501
        :type: PlayerClub
        """

        self._club = club

    @property
    def is_qualified_from_championship_challenge(self):
        """Gets the is_qualified_from_championship_challenge of this Player.  # noqa: E501


        :return: The is_qualified_from_championship_challenge of this Player.  # noqa: E501
        :rtype: bool
        """
        return self._is_qualified_from_championship_challenge

    @is_qualified_from_championship_challenge.setter
    def is_qualified_from_championship_challenge(self, is_qualified_from_championship_challenge):
        """Sets the is_qualified_from_championship_challenge of this Player.


        :param is_qualified_from_championship_challenge: The is_qualified_from_championship_challenge of this Player.  # noqa: E501
        :type: bool
        """

        self._is_qualified_from_championship_challenge = is_qualified_from_championship_challenge

    @property
    def _3vs3_victories(self):
        """Gets the _3vs3_victories of this Player.  # noqa: E501


        :return: The _3vs3_victories of this Player.  # noqa: E501
        :rtype: int
        """
        return self.__3vs3_victories

    @_3vs3_victories.setter
    def _3vs3_victories(self, _3vs3_victories):
        """Sets the _3vs3_victories of this Player.


        :param _3vs3_victories: The _3vs3_victories of this Player.  # noqa: E501
        :type: int
        """

        self.__3vs3_victories = _3vs3_victories

    @property
    def icon(self):
        """Gets the icon of this Player.  # noqa: E501


        :return: The icon of this Player.  # noqa: E501
        :rtype: PlayerIcon
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this Player.


        :param icon: The icon of this Player.  # noqa: E501
        :type: PlayerIcon
        """

        self._icon = icon

    @property
    def tag(self):
        """Gets the tag of this Player.  # noqa: E501


        :return: The tag of this Player.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this Player.


        :param tag: The tag of this Player.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def name(self):
        """Gets the name of this Player.  # noqa: E501


        :return: The name of this Player.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Player.


        :param name: The name of this Player.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def trophies(self):
        """Gets the trophies of this Player.  # noqa: E501


        :return: The trophies of this Player.  # noqa: E501
        :rtype: int
        """
        return self._trophies

    @trophies.setter
    def trophies(self, trophies):
        """Sets the trophies of this Player.


        :param trophies: The trophies of this Player.  # noqa: E501
        :type: int
        """

        self._trophies = trophies

    @property
    def exp_level(self):
        """Gets the exp_level of this Player.  # noqa: E501


        :return: The exp_level of this Player.  # noqa: E501
        :rtype: int
        """
        return self._exp_level

    @exp_level.setter
    def exp_level(self, exp_level):
        """Sets the exp_level of this Player.


        :param exp_level: The exp_level of this Player.  # noqa: E501
        :type: int
        """

        self._exp_level = exp_level

    @property
    def exp_points(self):
        """Gets the exp_points of this Player.  # noqa: E501


        :return: The exp_points of this Player.  # noqa: E501
        :rtype: int
        """
        return self._exp_points

    @exp_points.setter
    def exp_points(self, exp_points):
        """Sets the exp_points of this Player.


        :param exp_points: The exp_points of this Player.  # noqa: E501
        :type: int
        """

        self._exp_points = exp_points

    @property
    def highest_trophies(self):
        """Gets the highest_trophies of this Player.  # noqa: E501


        :return: The highest_trophies of this Player.  # noqa: E501
        :rtype: int
        """
        return self._highest_trophies

    @highest_trophies.setter
    def highest_trophies(self, highest_trophies):
        """Sets the highest_trophies of this Player.


        :param highest_trophies: The highest_trophies of this Player.  # noqa: E501
        :type: int
        """

        self._highest_trophies = highest_trophies

    @property
    def solo_victories(self):
        """Gets the solo_victories of this Player.  # noqa: E501


        :return: The solo_victories of this Player.  # noqa: E501
        :rtype: int
        """
        return self._solo_victories

    @solo_victories.setter
    def solo_victories(self, solo_victories):
        """Sets the solo_victories of this Player.


        :param solo_victories: The solo_victories of this Player.  # noqa: E501
        :type: int
        """

        self._solo_victories = solo_victories

    @property
    def duo_victories(self):
        """Gets the duo_victories of this Player.  # noqa: E501


        :return: The duo_victories of this Player.  # noqa: E501
        :rtype: int
        """
        return self._duo_victories

    @duo_victories.setter
    def duo_victories(self, duo_victories):
        """Sets the duo_victories of this Player.


        :param duo_victories: The duo_victories of this Player.  # noqa: E501
        :type: int
        """

        self._duo_victories = duo_victories

    @property
    def best_robo_rumble_time(self):
        """Gets the best_robo_rumble_time of this Player.  # noqa: E501


        :return: The best_robo_rumble_time of this Player.  # noqa: E501
        :rtype: int
        """
        return self._best_robo_rumble_time

    @best_robo_rumble_time.setter
    def best_robo_rumble_time(self, best_robo_rumble_time):
        """Sets the best_robo_rumble_time of this Player.


        :param best_robo_rumble_time: The best_robo_rumble_time of this Player.  # noqa: E501
        :type: int
        """

        self._best_robo_rumble_time = best_robo_rumble_time

    @property
    def best_time_as_big_brawler(self):
        """Gets the best_time_as_big_brawler of this Player.  # noqa: E501


        :return: The best_time_as_big_brawler of this Player.  # noqa: E501
        :rtype: int
        """
        return self._best_time_as_big_brawler

    @best_time_as_big_brawler.setter
    def best_time_as_big_brawler(self, best_time_as_big_brawler):
        """Sets the best_time_as_big_brawler of this Player.


        :param best_time_as_big_brawler: The best_time_as_big_brawler of this Player.  # noqa: E501
        :type: int
        """

        self._best_time_as_big_brawler = best_time_as_big_brawler

    @property
    def brawlers(self):
        """Gets the brawlers of this Player.  # noqa: E501


        :return: The brawlers of this Player.  # noqa: E501
        :rtype: BrawlerStatList
        """
        return self._brawlers

    @brawlers.setter
    def brawlers(self, brawlers):
        """Sets the brawlers of this Player.


        :param brawlers: The brawlers of this Player.  # noqa: E501
        :type: BrawlerStatList
        """

        self._brawlers = brawlers

    @property
    def name_color(self):
        """Gets the name_color of this Player.  # noqa: E501


        :return: The name_color of this Player.  # noqa: E501
        :rtype: str
        """
        return self._name_color

    @name_color.setter
    def name_color(self, name_color):
        """Sets the name_color of this Player.


        :param name_color: The name_color of this Player.  # noqa: E501
        :type: str
        """

        self._name_color = name_color

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Player, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Player):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Player):
            return True

        return self.to_dict() != other.to_dict()
