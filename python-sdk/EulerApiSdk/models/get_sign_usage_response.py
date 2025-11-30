from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sign_log_public import SignLogPublic


T = TypeVar("T", bound="GetSignUsageResponse")


@_attrs_define
class GetSignUsageResponse:
    """
    Attributes:
        code (float):
        message (str | Unset):
        usage (list[SignLogPublic] | Unset):
    """

    code: float
    message: str | Unset = UNSET
    usage: list[SignLogPublic] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        usage: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.usage, Unset):
            usage = []
            for usage_item_data in self.usage:
                usage_item = usage_item_data.to_dict()
                usage.append(usage_item)

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
        from ..models.sign_log_public import SignLogPublic

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        _usage = d.pop("usage", UNSET)
        usage: list[SignLogPublic] | Unset = UNSET
        if _usage is not UNSET:
            usage = []
            for usage_item_data in _usage:
                usage_item = SignLogPublic.from_dict(usage_item_data)

                usage.append(usage_item)

        get_sign_usage_response = cls(
            code=code,
            message=message,
            usage=usage,
        )

        return get_sign_usage_response
