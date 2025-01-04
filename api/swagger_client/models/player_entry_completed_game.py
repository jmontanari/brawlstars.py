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

class PlayerEntryCompletedGame(object):
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
        'brawler': 'BrawlerInfo',
        'statistics': 'Stats',
        'tag': 'str',
        'account_id': 'str'
    }

    attribute_map = {
        'brawler': 'brawler',
        'statistics': 'statistics',
        'tag': 'tag',
        'account_id': 'accountId'
    }

    def __init__(self, brawler=None, statistics=None, tag=None, account_id=None):  # noqa: E501
        """PlayerEntryCompletedGame - a model defined in Swagger"""  # noqa: E501
        self._brawler = None
        self._statistics = None
        self._tag = None
        self._account_id = None
        self.discriminator = None
        if brawler is not None:
            self.brawler = brawler
        if statistics is not None:
            self.statistics = statistics
        if tag is not None:
            self.tag = tag
        if account_id is not None:
            self.account_id = account_id

    @property
    def brawler(self):
        """Gets the brawler of this PlayerEntryCompletedGame.  # noqa: E501


        :return: The brawler of this PlayerEntryCompletedGame.  # noqa: E501
        :rtype: BrawlerInfo
        """
        return self._brawler

    @brawler.setter
    def brawler(self, brawler):
        """Sets the brawler of this PlayerEntryCompletedGame.


        :param brawler: The brawler of this PlayerEntryCompletedGame.  # noqa: E501
        :type: BrawlerInfo
        """

        self._brawler = brawler

    @property
    def statistics(self):
        """Gets the statistics of this PlayerEntryCompletedGame.  # noqa: E501


        :return: The statistics of this PlayerEntryCompletedGame.  # noqa: E501
        :rtype: Stats
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """Sets the statistics of this PlayerEntryCompletedGame.


        :param statistics: The statistics of this PlayerEntryCompletedGame.  # noqa: E501
        :type: Stats
        """

        self._statistics = statistics

    @property
    def tag(self):
        """Gets the tag of this PlayerEntryCompletedGame.  # noqa: E501


        :return: The tag of this PlayerEntryCompletedGame.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this PlayerEntryCompletedGame.


        :param tag: The tag of this PlayerEntryCompletedGame.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def account_id(self):
        """Gets the account_id of this PlayerEntryCompletedGame.  # noqa: E501


        :return: The account_id of this PlayerEntryCompletedGame.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this PlayerEntryCompletedGame.


        :param account_id: The account_id of this PlayerEntryCompletedGame.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

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
        if issubclass(PlayerEntryCompletedGame, dict):
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
        if not isinstance(other, PlayerEntryCompletedGame):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
