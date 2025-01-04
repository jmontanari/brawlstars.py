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

class PlayerEntry(object):
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
        'tag': 'str',
        'side': 'int'
    }

    attribute_map = {
        'tag': 'tag',
        'side': 'side'
    }

    def __init__(self, tag=None, side=None):  # noqa: E501
        """PlayerEntry - a model defined in Swagger"""  # noqa: E501
        self._tag = None
        self._side = None
        self.discriminator = None
        if tag is not None:
            self.tag = tag
        if side is not None:
            self.side = side

    @property
    def tag(self):
        """Gets the tag of this PlayerEntry.  # noqa: E501


        :return: The tag of this PlayerEntry.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this PlayerEntry.


        :param tag: The tag of this PlayerEntry.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def side(self):
        """Gets the side of this PlayerEntry.  # noqa: E501


        :return: The side of this PlayerEntry.  # noqa: E501
        :rtype: int
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this PlayerEntry.


        :param side: The side of this PlayerEntry.  # noqa: E501
        :type: int
        """

        self._side = side

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
        if issubclass(PlayerEntry, dict):
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
        if not isinstance(other, PlayerEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
