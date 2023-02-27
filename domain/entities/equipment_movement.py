from dataclasses import dataclass
from datetime import datetime


@dataclass
class EquipmentMovement:
    toir_id: str
    previous_toir_id: str
    previous_name: str
    movement_reason: str
    movement_date: datetime

    def to_dict(self) -> dict:
        return dict()

    @classmethod
    def from_dict(cls, data: dict):
        return EquipmentMovement()
