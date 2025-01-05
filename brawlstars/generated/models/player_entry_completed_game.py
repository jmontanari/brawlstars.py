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
from pydantic import BaseModel, Field, StrictStr
from brawlstars.generated.models.brawler_info import BrawlerInfo
from brawlstars.generated.models.stats import Stats

class PlayerEntryCompletedGame(BaseModel):
    """
    PlayerEntryCompletedGame
    """
    brawler: Optional[BrawlerInfo] = None
    statistics: Optional[Stats] = None
    tag: Optional[StrictStr] = None
    account_id: Optional[StrictStr] = Field(default=None, alias="accountId")
    __properties = ["brawler", "statistics", "tag", "accountId"]

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
    def from_json(cls, json_str: str) -> PlayerEntryCompletedGame:
        """Create an instance of PlayerEntryCompletedGame from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of brawler
        if self.brawler:
            _dict['brawler'] = self.brawler.to_dict()
        # override the default output from pydantic by calling `to_dict()` of statistics
        if self.statistics:
            _dict['statistics'] = self.statistics.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlayerEntryCompletedGame:
        """Create an instance of PlayerEntryCompletedGame from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlayerEntryCompletedGame.parse_obj(obj)

        _obj = PlayerEntryCompletedGame.parse_obj({
            "brawler": BrawlerInfo.from_dict(obj.get("brawler")) if obj.get("brawler") is not None else None,
            "statistics": Stats.from_dict(obj.get("statistics")) if obj.get("statistics") is not None else None,
            "tag": obj.get("tag"),
            "account_id": obj.get("accountId")
        })
        return _obj


