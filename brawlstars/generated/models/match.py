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


class Match(object):
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
        'initiative_side': 'int',
        'round': 'int',
        'teams': 'MatchTeamList',
        'termination_reason': 'str',
        'games': 'CompletedGameList',
        'phase': 'str',
        'players': 'PlayerMatchStatusList',
        'state': 'str',
        'id': 'str'
    }

    attribute_map = {
        'initiative_side': 'initiativeSide',
        'round': 'round',
        'teams': 'teams',
        'termination_reason': 'terminationReason',
        'games': 'games',
        'phase': 'phase',
        'players': 'players',
        'state': 'state',
        'id': 'id'
    }

    def __init__(self, initiative_side=None, round=None, teams=None, termination_reason=None, games=None, phase=None, players=None, state=None, id=None, _configuration=None):  # noqa: E501
        """Match - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._initiative_side = None
        self._round = None
        self._teams = None
        self._termination_reason = None
        self._games = None
        self._phase = None
        self._players = None
        self._state = None
        self._id = None
        self.discriminator = None

        if initiative_side is not None:
            self.initiative_side = initiative_side
        if round is not None:
            self.round = round
        if teams is not None:
            self.teams = teams
        if termination_reason is not None:
            self.termination_reason = termination_reason
        if games is not None:
            self.games = games
        if phase is not None:
            self.phase = phase
        if players is not None:
            self.players = players
        if state is not None:
            self.state = state
        if id is not None:
            self.id = id

    @property
    def initiative_side(self):
        """Gets the initiative_side of this Match.  # noqa: E501


        :return: The initiative_side of this Match.  # noqa: E501
        :rtype: int
        """
        return self._initiative_side

    @initiative_side.setter
    def initiative_side(self, initiative_side):
        """Sets the initiative_side of this Match.


        :param initiative_side: The initiative_side of this Match.  # noqa: E501
        :type: int
        """

        self._initiative_side = initiative_side

    @property
    def round(self):
        """Gets the round of this Match.  # noqa: E501


        :return: The round of this Match.  # noqa: E501
        :rtype: int
        """
        return self._round

    @round.setter
    def round(self, round):
        """Sets the round of this Match.


        :param round: The round of this Match.  # noqa: E501
        :type: int
        """

        self._round = round

    @property
    def teams(self):
        """Gets the teams of this Match.  # noqa: E501


        :return: The teams of this Match.  # noqa: E501
        :rtype: MatchTeamList
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this Match.


        :param teams: The teams of this Match.  # noqa: E501
        :type: MatchTeamList
        """

        self._teams = teams

    @property
    def termination_reason(self):
        """Gets the termination_reason of this Match.  # noqa: E501


        :return: The termination_reason of this Match.  # noqa: E501
        :rtype: str
        """
        return self._termination_reason

    @termination_reason.setter
    def termination_reason(self, termination_reason):
        """Sets the termination_reason of this Match.


        :param termination_reason: The termination_reason of this Match.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "playerDisconnected", "playerNotResponding", "technicalError", "matchTooLong", "other"]  # noqa: E501
        if (self._configuration.client_side_validation and
                termination_reason not in allowed_values):
            raise ValueError(
                "Invalid value for `termination_reason` ({0}), must be one of {1}"  # noqa: E501
                .format(termination_reason, allowed_values)
            )

        self._termination_reason = termination_reason

    @property
    def games(self):
        """Gets the games of this Match.  # noqa: E501


        :return: The games of this Match.  # noqa: E501
        :rtype: CompletedGameList
        """
        return self._games

    @games.setter
    def games(self, games):
        """Sets the games of this Match.


        :param games: The games of this Match.  # noqa: E501
        :type: CompletedGameList
        """

        self._games = games

    @property
    def phase(self):
        """Gets the phase of this Match.  # noqa: E501


        :return: The phase of this Match.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this Match.


        :param phase: The phase of this Match.  # noqa: E501
        :type: str
        """
        allowed_values = ["init", "banHeroes", "pickHeroes", "finalPreparation", "battle", "matchResult", "ending"]  # noqa: E501
        if (self._configuration.client_side_validation and
                phase not in allowed_values):
            raise ValueError(
                "Invalid value for `phase` ({0}), must be one of {1}"  # noqa: E501
                .format(phase, allowed_values)
            )

        self._phase = phase

    @property
    def players(self):
        """Gets the players of this Match.  # noqa: E501


        :return: The players of this Match.  # noqa: E501
        :rtype: PlayerMatchStatusList
        """
        return self._players

    @players.setter
    def players(self, players):
        """Sets the players of this Match.


        :param players: The players of this Match.  # noqa: E501
        :type: PlayerMatchStatusList
        """

        self._players = players

    @property
    def state(self):
        """Gets the state of this Match.  # noqa: E501


        :return: The state of this Match.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Match.


        :param state: The state of this Match.  # noqa: E501
        :type: str
        """
        allowed_values = ["open", "cancelled", "completed"]  # noqa: E501
        if (self._configuration.client_side_validation and
                state not in allowed_values):
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def id(self):
        """Gets the id of this Match.  # noqa: E501


        :return: The id of this Match.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Match.


        :param id: The id of this Match.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if issubclass(Match, dict):
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
        if not isinstance(other, Match):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Match):
            return True

        return self.to_dict() != other.to_dict()
