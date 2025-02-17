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

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from brawlstars.models.brawler_info import BrawlerInfo
from brawlstars.models.match_team_player import MatchTeamPlayer
from typing import Optional, Set
from typing_extensions import Self

class MatchTeam(BaseModel):
    """
    MatchTeam
    """ # noqa: E501
    players: Optional[List[MatchTeamPlayer]] = None
    bans: Optional[List[BrawlerInfo]] = None
    side: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["players", "bans", "side"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of MatchTeam from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in players (list)
        _items = []
        if self.players:
            for _item_players in self.players:
                if _item_players:
                    _items.append(_item_players.to_dict())
            _dict['players'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in bans (list)
        _items = []
        if self.bans:
            for _item_bans in self.bans:
                if _item_bans:
                    _items.append(_item_bans.to_dict())
            _dict['bans'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MatchTeam from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "players": [MatchTeamPlayer.from_dict(_item) for _item in obj["players"]] if obj.get("players") is not None else None,
            "bans": [BrawlerInfo.from_dict(_item) for _item in obj["bans"]] if obj.get("bans") is not None else None,
            "side": obj.get("side")
        })
        return _obj


