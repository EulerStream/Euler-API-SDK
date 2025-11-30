from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.record_string_any import RecordStringAny


T = TypeVar("T", bound="RecordStringRecordStringAny")


@_attrs_define
class RecordStringRecordStringAny:
    """Construct a type with a set of properties K of type T"""

    additional_properties: dict[str, RecordStringAny] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.record_string_any import RecordStringAny

        d = dict(src_dict)
        record_string_record_string_any = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = RecordStringAny.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        record_string_record_string_any.additional_properties = additional_properties
        return record_string_record_string_any

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> RecordStringAny:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: RecordStringAny) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
