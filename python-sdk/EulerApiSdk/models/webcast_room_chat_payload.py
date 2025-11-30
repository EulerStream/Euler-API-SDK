from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebcastRoomChatPayload")


@_attrs_define
class WebcastRoomChatPayload:
    """
    Attributes:
        content (str):
        session_id (str):
        tt_target_idc (str):
        room_id (str):
    """

    content: str
    session_id: str
    tt_target_idc: str
    room_id: str

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        session_id = self.session_id

        tt_target_idc = self.tt_target_idc

        room_id = self.room_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "content": content,
                "sessionId": session_id,
                "ttTargetIdc": tt_target_idc,
                "roomId": room_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        session_id = d.pop("sessionId")

        tt_target_idc = d.pop("ttTargetIdc")

        room_id = d.pop("roomId")

        webcast_room_chat_payload = cls(
            content=content,
            session_id=session_id,
            tt_target_idc=tt_target_idc,
            room_id=room_id,
        )

        return webcast_room_chat_payload
