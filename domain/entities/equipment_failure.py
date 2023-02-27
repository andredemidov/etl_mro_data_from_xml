from dataclasses import dataclass
from datetime import datetime


@dataclass
class EquipmentFailure:
    toir_id: str
    toir_url: str
    type_failure_id: str
    type_reason_failure_id: str
    value: str
    failure_date: datetime
    failure_description: str
    self_id: str

    def to_dict(self) -> dict:
        return dict()

    @classmethod
    def from_dict(cls, data: dict):
        return EquipmentFailure()
