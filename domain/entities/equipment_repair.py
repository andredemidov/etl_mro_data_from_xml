from dataclasses import dataclass
from datetime import datetime


@dataclass
class EquipmentRepair:
    toir_id: str
    repair_id: str
    type_repair_id: str
    toir_url: str
    self_id: str
    fact_start_date: datetime
    fact_finish_date: datetime

    def to_dict(self) -> dict:
        return dict()

    @classmethod
    def from_dict(cls, data: dict):
        return EquipmentRepair()
