from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.point import Point


T = TypeVar("T", bound="IconsResult")


@_attrs_define
class IconsResult:
    """
    Attributes:
        time_ms (float):
        points (list[Point]):
    """

    time_ms: float
    points: list[Point]

    def to_dict(self) -> dict[str, Any]:
        time_ms = self.time_ms

        points = []
        for points_item_data in self.points:
            points_item = points_item_data.to_dict()
            points.append(points_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "time_ms": time_ms,
                "points": points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.point import Point

        d = dict(src_dict)
        time_ms = d.pop("time_ms")

        points = []
        _points = d.pop("points")
        for points_item_data in _points:
            points_item = Point.from_dict(points_item_data)

            points.append(points_item)

        icons_result = cls(
            time_ms=time_ms,
            points=points,
        )

        return icons_result
