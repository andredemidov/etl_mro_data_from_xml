from dataclasses import dataclass


@dataclass
class EquipmentAttribute:
    toir_id: str
    self_id: str
    attribute_id: str
    value: str

    def to_dict(self) -> dict:
        return dict()

    @classmethod
    def from_dict(cls, data: dict):
        return EquipmentAttribute()
