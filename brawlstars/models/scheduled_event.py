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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from brawlstars.models.scheduled_event_location import ScheduledEventLocation
from typing import Optional, Set
from typing_extensions import Self

class ScheduledEvent(BaseModel):
    """
    ScheduledEvent
    """ # noqa: E501
    event: Optional[ScheduledEventLocation] = None
    slot_id: Optional[StrictInt] = Field(default=None, alias="slotId")
    start_time: Optional[StrictStr] = Field(default=None, alias="startTime")
    end_time: Optional[StrictStr] = Field(default=None, alias="endTime")
    __properties: ClassVar[List[str]] = ["event", "slotId", "startTime", "endTime"]

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
        """Create an instance of ScheduledEvent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of event
        if self.event:
            _dict['event'] = self.event.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScheduledEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "event": ScheduledEventLocation.from_dict(obj["event"]) if obj.get("event") is not None else None,
            "slotId": obj.get("slotId"),
            "startTime": obj.get("startTime"),
            "endTime": obj.get("endTime")
        })
        return _obj


