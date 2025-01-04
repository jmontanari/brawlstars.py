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

class MatchTeamPlayer(object):
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
        'caused_termination': 'bool',
        'tag': 'str',
        'is_leader': 'bool',
        'brawler': 'BrawlerInfo'
    }

    attribute_map = {
        'caused_termination': 'causedTermination',
        'tag': 'tag',
        'is_leader': 'isLeader',
        'brawler': 'brawler'
    }

    def __init__(self, caused_termination=None, tag=None, is_leader=None, brawler=None):  # noqa: E501
        """MatchTeamPlayer - a model defined in Swagger"""  # noqa: E501
        self._caused_termination = None
        self._tag = None
        self._is_leader = None
        self._brawler = None
        self.discriminator = None
        if caused_termination is not None:
            self.caused_termination = caused_termination
        if tag is not None:
            self.tag = tag
        if is_leader is not None:
            self.is_leader = is_leader
        if brawler is not None:
            self.brawler = brawler

    @property
    def caused_termination(self):
        """Gets the caused_termination of this MatchTeamPlayer.  # noqa: E501


        :return: The caused_termination of this MatchTeamPlayer.  # noqa: E501
        :rtype: bool
        """
        return self._caused_termination

    @caused_termination.setter
    def caused_termination(self, caused_termination):
        """Sets the caused_termination of this MatchTeamPlayer.


        :param caused_termination: The caused_termination of this MatchTeamPlayer.  # noqa: E501
        :type: bool
        """

        self._caused_termination = caused_termination

    @property
    def tag(self):
        """Gets the tag of this MatchTeamPlayer.  # noqa: E501


        :return: The tag of this MatchTeamPlayer.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this MatchTeamPlayer.


        :param tag: The tag of this MatchTeamPlayer.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def is_leader(self):
        """Gets the is_leader of this MatchTeamPlayer.  # noqa: E501


        :return: The is_leader of this MatchTeamPlayer.  # noqa: E501
        :rtype: bool
        """
        return self._is_leader

    @is_leader.setter
    def is_leader(self, is_leader):
        """Sets the is_leader of this MatchTeamPlayer.


        :param is_leader: The is_leader of this MatchTeamPlayer.  # noqa: E501
        :type: bool
        """

        self._is_leader = is_leader

    @property
    def brawler(self):
        """Gets the brawler of this MatchTeamPlayer.  # noqa: E501


        :return: The brawler of this MatchTeamPlayer.  # noqa: E501
        :rtype: BrawlerInfo
        """
        return self._brawler

    @brawler.setter
    def brawler(self, brawler):
        """Sets the brawler of this MatchTeamPlayer.


        :param brawler: The brawler of this MatchTeamPlayer.  # noqa: E501
        :type: BrawlerInfo
        """

        self._brawler = brawler

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
        if issubclass(MatchTeamPlayer, dict):
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
        if not isinstance(other, MatchTeamPlayer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
