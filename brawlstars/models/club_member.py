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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from brawlstars.models.player_icon import PlayerIcon
from typing import Optional, Set
from typing_extensions import Self

class ClubMember(BaseModel):
    """
    ClubMember
    """ # noqa: E501
    icon: Optional[PlayerIcon] = None
    tag: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    trophies: Optional[StrictInt] = None
    role: Optional[StrictStr] = None
    name_color: Optional[StrictStr] = Field(default=None, alias="nameColor")
    __properties: ClassVar[List[str]] = ["icon", "tag", "name", "trophies", "role", "nameColor"]

    @field_validator('role')
    def role_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['notMember', 'member', 'president', 'senior', 'vicePresident', 'unknown']):
            raise ValueError("must be one of enum values ('notMember', 'member', 'president', 'senior', 'vicePresident', 'unknown')")
        return value

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
        """Create an instance of ClubMember from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of icon
        if self.icon:
            _dict['icon'] = self.icon.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClubMember from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "icon": PlayerIcon.from_dict(obj["icon"]) if obj.get("icon") is not None else None,
            "tag": obj.get("tag"),
            "name": obj.get("name"),
            "trophies": obj.get("trophies"),
            "role": obj.get("role"),
            "nameColor": obj.get("nameColor")
        })
        return _obj

