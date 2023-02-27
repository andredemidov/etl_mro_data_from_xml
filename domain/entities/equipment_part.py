from dataclasses import dataclass


@dataclass
class EquipmentPart:
    toir_id: str
    self_id: str
    name: str
    unit: str
    amount: float
    code: str
    type_repair_id: str
    name_repair: str

    def to_dict(self) -> dict:
        return dict()

    @classmethod
    def from_dict(cls, data: dict):
        return EquipmentPart()
