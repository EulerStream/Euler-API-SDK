from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CaptchaCreditsResponse")


@_attrs_define
class CaptchaCreditsResponse:
    """
    Attributes:
        code (float):
        plan_credits (float):
        purchased_credits (float):
        message (str | Unset):
    """

    code: float
    plan_credits: float
    purchased_credits: float
    message: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        plan_credits = self.plan_credits

        purchased_credits = self.purchased_credits

        message = self.message

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "plan_credits": plan_credits,
                "purchased_credits": purchased_credits,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        plan_credits = d.pop("plan_credits")

        purchased_credits = d.pop("purchased_credits")

        message = d.pop("message", UNSET)

        captcha_credits_response = cls(
            code=code,
            plan_credits=plan_credits,
            purchased_credits=purchased_credits,
            message=message,
        )

        return captcha_credits_response
