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


from typing import Any, Dict, Optional
from pydantic import BaseModel, StrictInt, StrictStr, validator

class Event(BaseModel):
    """
    Event
    """
    mode: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    map: Optional[Dict[str, Any]] = None
    __properties = ["mode", "id", "map"]

    @validator('mode')
    def mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('soloShowdown', 'duoShowdown', 'heist', 'bounty', 'siege', 'gemGrab', 'brawlBall', 'bigGame', 'bossFight', 'roboRumble', 'takedown', 'loneStar', 'presentPlunder', 'hotZone', 'superCityRampage', 'knockout', 'volleyBrawl', 'basketBrawl', 'holdTheTrophy', 'trophyThieves', 'duels', 'wipeout', 'payload', 'botDrop', 'hunters', 'lastStand', 'snowtelThieves', 'pumpkinPlunder', 'trophyEscape', 'wipeout5V5', 'knockout5V5', 'gemGrab5V5', 'brawlBall5V5', 'godzillaCitySmash', 'paintBrawl', 'trioShowdown', 'zombiePlunder', 'jellyfishing', 'unknown',):
            raise ValueError("must be one of enum values ('soloShowdown', 'duoShowdown', 'heist', 'bounty', 'siege', 'gemGrab', 'brawlBall', 'bigGame', 'bossFight', 'roboRumble', 'takedown', 'loneStar', 'presentPlunder', 'hotZone', 'superCityRampage', 'knockout', 'volleyBrawl', 'basketBrawl', 'holdTheTrophy', 'trophyThieves', 'duels', 'wipeout', 'payload', 'botDrop', 'hunters', 'lastStand', 'snowtelThieves', 'pumpkinPlunder', 'trophyEscape', 'wipeout5V5', 'knockout5V5', 'gemGrab5V5', 'brawlBall5V5', 'godzillaCitySmash', 'paintBrawl', 'trioShowdown', 'zombiePlunder', 'jellyfishing', 'unknown')")
        return value

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
    def from_json(cls, json_str: str) -> Event:
        """Create an instance of Event from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Event:
        """Create an instance of Event from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Event.parse_obj(obj)

        _obj = Event.parse_obj({
            "mode": obj.get("mode"),
            "id": obj.get("id"),
            "map": obj.get("map")
        })
        return _obj


