from dataclasses import dataclass
from typing import Literal
from datetime import datetime

STATUS = Literal['updated', 'new', 'empty', 'not updated']


@dataclass
class Failure:
    toir_id: str
    toir_url: str
    type_failure_id: str
    type_reason_failure_id: str
    failure_date: datetime
    failure_description: str
    self_id: str = None
    host_id: str = None
    update_status: STATUS = 'empty'

    def to_compare_dict(self) -> dict:
        return {
            'toir_id': self.toir_id,
            'toir_url': self.toir_url,
            'type_failure_id': self.type_failure_id,
            'type_reason_failure_id': self.type_reason_failure_id,
            'failure_date': self.failure_date,
            'failure_description': self.failure_description,
        }


@dataclass
class Part:
    toir_id: str
    name: str
    unit: str
    amount: float
    code: str
    type_repair_id: str
    name_repair: str
    self_id: str = None
    host_id: str = None
    update_status: STATUS = 'empty'

    def to_compare_dict(self) -> dict:
        return {
            'toir_id': self.toir_id,
            'name': self.name,
            'unit': self.unit,
            'amount': round(self.amount, 4),
            'code': self.code,
            'type_repair_id': self.type_repair_id,
            'name_repair': self.name_repair,
        }


@dataclass
class Property:
    toir_id: str
    property_id: str
    value: str
    self_id: str = None
    host_id: str = None
    update_status: STATUS = 'empty'

    def to_compare_dict(self) -> dict:
        return {
            'toir_id': self.toir_id,
            'property_id': self.property_id,
            'value': self.value,
        }


@dataclass
class PlanRepair:
    toir_id: str
    repair_id: str
    type_repair_id: str
    toir_url: str
    start_date: datetime
    finish_date: datetime
    self_id: str = None
    host_id: str = None
    update_status: STATUS = 'empty'

    def to_compare_dict(self) -> dict:
        return {
            'toir_id': self.toir_id,
            'repair_id': self.repair_id,
            'type_repair_id': self.type_repair_id,
            'toir_url': self.toir_url,
            'start_date': self.start_date,
            'finish_date': self.finish_date,
        }


@dataclass
class FactRepair:
    toir_id: str
    repair_id: str
    type_repair_id: str
    toir_url: str
    fact_start_date: datetime
    fact_finish_date: datetime
    operating: float
    self_id: str = None
    host_id: str = None
    update_status: STATUS = 'empty'

    def to_compare_dict(self) -> dict:
        return {
            'toir_id': self.toir_id,
            'repair_id': self.repair_id,
            'type_repair_id': self.type_repair_id,
            'toir_url': self.toir_url,
            'fact_start_date': self.fact_start_date,
            'fact_finish_date': self.fact_finish_date,
            'operating': self.operating,
        }


@dataclass
class Movement:
    toir_id: str
    previous_toir_id: str
    previous_name: str
    movement_reason: str
    movement_date: datetime
    self_id: str = None
    host_id: str = None
    update_status: STATUS = 'empty'

    def to_compare_dict(self) -> dict:
        return {
            'toir_id': self.toir_id,
            'previous_toir_id': self.previous_toir_id,
            'previous_name': self.previous_name,
            'movement_reason': self.movement_reason,
            'movement_date': self.movement_date,
        }
