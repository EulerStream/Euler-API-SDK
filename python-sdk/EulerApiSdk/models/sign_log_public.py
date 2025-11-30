from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from dateutil.parser import isoparse

T = TypeVar("T", bound="SignLogPublic")


@_attrs_define
class SignLogPublic:
    """
    Attributes:
        id (str):
        ts (datetime.datetime):
        code (float):
        client (str):
        ip (str):
        api_key_id (float):
        user_agent (str):
        agent_id (str):
    """

    id: str
    ts: datetime.datetime
    code: float
    client: str
    ip: str
    api_key_id: float
    user_agent: str
    agent_id: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ts = self.ts.isoformat()

        code = self.code

        client = self.client

        ip = self.ip

        api_key_id = self.api_key_id

        user_agent = self.user_agent

        agent_id = self.agent_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "ts": ts,
                "code": code,
                "client": client,
                "ip": ip,
                "api_key_id": api_key_id,
                "user_agent": user_agent,
                "agent_id": agent_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        ts = isoparse(d.pop("ts"))

        code = d.pop("code")

        client = d.pop("client")

        ip = d.pop("ip")

        api_key_id = d.pop("api_key_id")

        user_agent = d.pop("user_agent")

        agent_id = d.pop("agent_id")

        sign_log_public = cls(
            id=id,
            ts=ts,
            code=code,
            client=client,
            ip=ip,
            api_key_id=api_key_id,
            user_agent=user_agent,
            agent_id=agent_id,
        )

        return sign_log_public
