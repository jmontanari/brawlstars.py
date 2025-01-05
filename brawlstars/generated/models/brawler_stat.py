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


class BrawlerStat(object):
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
        'gadgets': 'AccessoryList',
        'star_powers': 'StarPowerList',
        'id': 'int',
        'rank': 'int',
        'trophies': 'int',
        'highest_trophies': 'int',
        'power': 'int',
        'gears': 'GearStatList',
        'name': 'JsonLocalizedName'
    }

    attribute_map = {
        'gadgets': 'gadgets',
        'star_powers': 'starPowers',
        'id': 'id',
        'rank': 'rank',
        'trophies': 'trophies',
        'highest_trophies': 'highestTrophies',
        'power': 'power',
        'gears': 'gears',
        'name': 'name'
    }

    def __init__(self, gadgets=None, star_powers=None, id=None, rank=None, trophies=None, highest_trophies=None, power=None, gears=None, name=None, _configuration=None):  # noqa: E501
        """BrawlerStat - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._gadgets = None
        self._star_powers = None
        self._id = None
        self._rank = None
        self._trophies = None
        self._highest_trophies = None
        self._power = None
        self._gears = None
        self._name = None
        self.discriminator = None

        if gadgets is not None:
            self.gadgets = gadgets
        if star_powers is not None:
            self.star_powers = star_powers
        if id is not None:
            self.id = id
        if rank is not None:
            self.rank = rank
        if trophies is not None:
            self.trophies = trophies
        if highest_trophies is not None:
            self.highest_trophies = highest_trophies
        if power is not None:
            self.power = power
        if gears is not None:
            self.gears = gears
        if name is not None:
            self.name = name

    @property
    def gadgets(self):
        """Gets the gadgets of this BrawlerStat.  # noqa: E501


        :return: The gadgets of this BrawlerStat.  # noqa: E501
        :rtype: AccessoryList
        """
        return self._gadgets

    @gadgets.setter
    def gadgets(self, gadgets):
        """Sets the gadgets of this BrawlerStat.


        :param gadgets: The gadgets of this BrawlerStat.  # noqa: E501
        :type: AccessoryList
        """

        self._gadgets = gadgets

    @property
    def star_powers(self):
        """Gets the star_powers of this BrawlerStat.  # noqa: E501


        :return: The star_powers of this BrawlerStat.  # noqa: E501
        :rtype: StarPowerList
        """
        return self._star_powers

    @star_powers.setter
    def star_powers(self, star_powers):
        """Sets the star_powers of this BrawlerStat.


        :param star_powers: The star_powers of this BrawlerStat.  # noqa: E501
        :type: StarPowerList
        """

        self._star_powers = star_powers

    @property
    def id(self):
        """Gets the id of this BrawlerStat.  # noqa: E501


        :return: The id of this BrawlerStat.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BrawlerStat.


        :param id: The id of this BrawlerStat.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def rank(self):
        """Gets the rank of this BrawlerStat.  # noqa: E501


        :return: The rank of this BrawlerStat.  # noqa: E501
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this BrawlerStat.


        :param rank: The rank of this BrawlerStat.  # noqa: E501
        :type: int
        """

        self._rank = rank

    @property
    def trophies(self):
        """Gets the trophies of this BrawlerStat.  # noqa: E501


        :return: The trophies of this BrawlerStat.  # noqa: E501
        :rtype: int
        """
        return self._trophies

    @trophies.setter
    def trophies(self, trophies):
        """Sets the trophies of this BrawlerStat.


        :param trophies: The trophies of this BrawlerStat.  # noqa: E501
        :type: int
        """

        self._trophies = trophies

    @property
    def highest_trophies(self):
        """Gets the highest_trophies of this BrawlerStat.  # noqa: E501


        :return: The highest_trophies of this BrawlerStat.  # noqa: E501
        :rtype: int
        """
        return self._highest_trophies

    @highest_trophies.setter
    def highest_trophies(self, highest_trophies):
        """Sets the highest_trophies of this BrawlerStat.


        :param highest_trophies: The highest_trophies of this BrawlerStat.  # noqa: E501
        :type: int
        """

        self._highest_trophies = highest_trophies

    @property
    def power(self):
        """Gets the power of this BrawlerStat.  # noqa: E501


        :return: The power of this BrawlerStat.  # noqa: E501
        :rtype: int
        """
        return self._power

    @power.setter
    def power(self, power):
        """Sets the power of this BrawlerStat.


        :param power: The power of this BrawlerStat.  # noqa: E501
        :type: int
        """

        self._power = power

    @property
    def gears(self):
        """Gets the gears of this BrawlerStat.  # noqa: E501


        :return: The gears of this BrawlerStat.  # noqa: E501
        :rtype: GearStatList
        """
        return self._gears

    @gears.setter
    def gears(self, gears):
        """Sets the gears of this BrawlerStat.


        :param gears: The gears of this BrawlerStat.  # noqa: E501
        :type: GearStatList
        """

        self._gears = gears

    @property
    def name(self):
        """Gets the name of this BrawlerStat.  # noqa: E501


        :return: The name of this BrawlerStat.  # noqa: E501
        :rtype: JsonLocalizedName
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BrawlerStat.


        :param name: The name of this BrawlerStat.  # noqa: E501
        :type: JsonLocalizedName
        """

        self._name = name

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
        if issubclass(BrawlerStat, dict):
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
        if not isinstance(other, BrawlerStat):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BrawlerStat):
            return True

        return self.to_dict() != other.to_dict()
