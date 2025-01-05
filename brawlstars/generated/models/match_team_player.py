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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from brawlstars.generated.models.brawler_info import BrawlerInfo
from typing import Optional, Set
from typing_extensions import Self

class MatchTeamPlayer(BaseModel):
    """
    MatchTeamPlayer
    """ # noqa: E501
    caused_termination: Optional[StrictBool] = Field(default=None, alias="causedTermination")
    tag: Optional[StrictStr] = None
    is_leader: Optional[StrictBool] = Field(default=None, alias="isLeader")
    brawler: Optional[BrawlerInfo] = None
    __properties: ClassVar[List[str]] = ["causedTermination", "tag", "isLeader", "brawler"]

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
        """Create an instance of MatchTeamPlayer from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MatchTeamPlayer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "causedTermination": obj.get("causedTermination"),
            "tag": obj.get("tag"),
            "isLeader": obj.get("isLeader"),
            "brawler": BrawlerInfo.from_dict(obj["brawler"]) if obj.get("brawler") is not None else None
        })
        return _obj


