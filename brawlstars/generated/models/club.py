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
from brawlstars.generated.models.club_member import ClubMember
from typing import Optional, Set
from typing_extensions import Self

class Club(BaseModel):
    """
    Club
    """ # noqa: E501
    tag: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    trophies: Optional[StrictInt] = None
    required_trophies: Optional[StrictInt] = Field(default=None, alias="requiredTrophies")
    members: Optional[List[ClubMember]] = None
    type: Optional[StrictStr] = None
    badge_id: Optional[StrictInt] = Field(default=None, alias="badgeId")
    __properties: ClassVar[List[str]] = ["tag", "name", "description", "trophies", "requiredTrophies", "members", "type", "badgeId"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['open', 'inviteOnly', 'closed', 'unknown']):
            raise ValueError("must be one of enum values ('open', 'inviteOnly', 'closed', 'unknown')")
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
        """Create an instance of Club from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in members (list)
        _items = []
        if self.members:
            for _item_members in self.members:
                if _item_members:
                    _items.append(_item_members.to_dict())
            _dict['members'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Club from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tag": obj.get("tag"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "trophies": obj.get("trophies"),
            "requiredTrophies": obj.get("requiredTrophies"),
            "members": [ClubMember.from_dict(_item) for _item in obj["members"]] if obj.get("members") is not None else None,
            "type": obj.get("type"),
            "badgeId": obj.get("badgeId")
        })
        return _obj


