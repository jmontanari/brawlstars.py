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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from brawlstars.models.brawler_info import BrawlerInfo
from brawlstars.models.stats import Stats
from typing import Optional, Set
from typing_extensions import Self

class PlayerEntryCompletedGame(BaseModel):
    """
    PlayerEntryCompletedGame
    """ # noqa: E501
    brawler: Optional[BrawlerInfo] = None
    statistics: Optional[Stats] = None
    tag: Optional[StrictStr] = None
    account_id: Optional[StrictStr] = Field(default=None, alias="accountId")
    __properties: ClassVar[List[str]] = ["brawler", "statistics", "tag", "accountId"]

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
        """Create an instance of PlayerEntryCompletedGame from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of brawler
        if self.brawler:
            _dict['brawler'] = self.brawler.to_dict()
        # override the default output from pydantic by calling `to_dict()` of statistics
        if self.statistics:
            _dict['statistics'] = self.statistics.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PlayerEntryCompletedGame from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "brawler": BrawlerInfo.from_dict(obj["brawler"]) if obj.get("brawler") is not None else None,
            "statistics": Stats.from_dict(obj["statistics"]) if obj.get("statistics") is not None else None,
            "tag": obj.get("tag"),
            "accountId": obj.get("accountId")
        })
        return _obj

