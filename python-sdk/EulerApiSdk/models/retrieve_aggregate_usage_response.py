from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_string_record_string_any import RecordStringRecordStringAny


T = TypeVar("T", bound="RetrieveAggregateUsageResponse")


@_attrs_define
class RetrieveAggregateUsageResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        usage (RecordStringRecordStringAny | Unset): Construct a type with a set of properties K of type T
    """

    code: float
    message: str | Unset = UNSET
    usage: RecordStringRecordStringAny | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        usage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.record_string_record_string_any import RecordStringRecordStringAny

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _usage = d.pop("usage", UNSET)
        usage: RecordStringRecordStringAny | Unset
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = RecordStringRecordStringAny.from_dict(_usage)

        retrieve_aggregate_usage_response = cls(
            code=code,
            message=message,
            usage=usage,
        )

        return retrieve_aggregate_usage_response
