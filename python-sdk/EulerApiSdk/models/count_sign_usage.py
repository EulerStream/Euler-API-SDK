from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CountSignUsage")


@_attrs_define
class CountSignUsage:
    """
    Attributes:
        code (float):
        message (str | Unset):
        pages (float | Unset):
    """

    code: float
    message: str | Unset = UNSET
    pages: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        pages = self.pages

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if pages is not UNSET:
            field_dict["pages"] = pages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message", UNSET)

        pages = d.pop("pages", UNSET)

        count_sign_usage = cls(
            code=code,
            message=message,
            pages=pages,
        )

        return count_sign_usage
