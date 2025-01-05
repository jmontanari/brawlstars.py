# coding: utf-8

"""
    Brawl Stars API

    Brawl Stars API

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from brawlstars.generated.models.player_icon import PlayerIcon
from brawlstars.generated.models.player_ranking_club import PlayerRankingClub

class PlayerRanking(BaseModel):
    """
    PlayerRanking
    """
    club: Optional[PlayerRankingClub] = None
    icon: Optional[PlayerIcon] = None
    trophies: Optional[StrictInt] = None
    tag: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    rank: Optional[StrictInt] = None
    name_color: Optional[StrictStr] = Field(default=None, alias="nameColor")
    __properties = ["club", "icon", "trophies", "tag", "name", "rank", "nameColor"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> PlayerRanking:
        """Create an instance of PlayerRanking from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of club
        if self.club:
            _dict['club'] = self.club.to_dict()
        # override the default output from pydantic by calling `to_dict()` of icon
        if self.icon:
            _dict['icon'] = self.icon.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlayerRanking:
        """Create an instance of PlayerRanking from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlayerRanking.parse_obj(obj)

        _obj = PlayerRanking.parse_obj({
            "club": PlayerRankingClub.from_dict(obj.get("club")) if obj.get("club") is not None else None,
            "icon": PlayerIcon.from_dict(obj.get("icon")) if obj.get("icon") is not None else None,
            "trophies": obj.get("trophies"),
            "tag": obj.get("tag"),
            "name": obj.get("name"),
            "rank": obj.get("rank"),
            "name_color": obj.get("nameColor")
        })
        return _obj


