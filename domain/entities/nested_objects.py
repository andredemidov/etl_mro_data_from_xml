from dataclasses import dataclass
from typing import Literal
from datetime import datetime
from . import reference_attribute

STATUS = Literal['updated', 'new', 'empty', 'not updated']


@dataclass
class Failure:
    toir_id: str
    toir_url: str
    type_failure: reference_attribute.ReferenceAttribute
    type_reason_failure: reference_attribute.ReferenceAttribute
    failure_date: datetime
    failure_description: str
    self_id: str = None
    host_id: str = None
    update_status: STATUS = 'empty'

    def to_compare_dict(self) -> dict:
        return {
            'toir_url': self.toir_url,
            'type_failure_id': self.type_failure.comparison_value,
            'type_reason_failure_id': self.type_reason_failure.comparison_value,
            'failure_date': self.failure_date[:10] if self.failure_date else self.failure_date,
            'failure_description': self.failure_description,
        }

    @property
    def unique_id(self):
        return self.toir_url


@dataclass
class Part:
    toir_id: str
    name: str
    unit: str
    amount: float
    code: str
    type_repair: reference_attribute.ReferenceAttribute
    name_repair: str = None
    self_id: str = None
    host_id: str = None
    update_status: STATUS = 'empty'

    def to_compare_dict(self) -> dict:
        return {
            'name': self.name,
            'unit': self.unit,
            'amount': round(self.amount, 4),
            'code': self.code,
            'type_repair_id': self.type_repair.comparison_value,
        }

    @property
    def unique_id(self):
        cons = [self.code, self.type_repair.comparison_value]
        result = [one for one in cons if one]
        return ' '.join(result)


@dataclass
class Property:
    toir_id: str
    toir_property: reference_attribute.ReferenceAttribute
    value: str
    self_id: str = None
    host_id: str = None
    update_status: STATUS = 'empty'

    def to_compare_dict(self) -> dict:
        return {
            'property_toir_id': self.toir_id,
            'property': self.toir_property.comparison_value,
            'value': self.value,
        }

    @property
    def unique_id(self):
        # toir_id here is property's toir id
        return self.toir_id


@dataclass
class PlanRepair:
    toir_id: str
    repair_id: str
    type_repair: reference_attribute.ReferenceAttribute
    toir_url: str
    start_date: str
    finish_date: str
    self_id: str = None
    host_id: str = None
    update_status: STATUS = 'empty'

    def to_compare_dict(self) -> dict:
        return {
            'repair_id': self.repair_id,
            'type_repair_id': self.type_repair.comparison_value,
            'toir_url': self.toir_url,
            'start_date': self.start_date[:10] if self.start_date else self.start_date,
            'finish_date': self.finish_date[:10] if self.finish_date else self.finish_date,
        }

    @property
    def unique_id(self):
        cons = [self.repair_id, self.toir_url]
        result = [one for one in cons if one]
        return ' '.join(result)


@dataclass
class FactRepair:
    toir_id: str
    repair_id: str
    type_repair: reference_attribute.ReferenceAttribute
    toir_url: str
    fact_start_date: str
    fact_finish_date: str
    operating: float
    self_id: str = None
    host_id: str = None
    update_status: STATUS = 'empty'

    def to_compare_dict(self) -> dict:
        return {
            'repair_id': self.repair_id,
            'type_repair_id': self.type_repair.comparison_value,
            'toir_url': self.toir_url,
            'fact_start_date': self.fact_start_date[:10] if self.fact_start_date else self.fact_start_date,
            'fact_finish_date': self.fact_finish_date[:10] if self.fact_finish_date else self.fact_finish_date,
            'operating': self.operating,
        }

    @property
    def unique_id(self):
        cons = [self.repair_id, self.toir_url]
        result = [one for one in cons if one]
        return ' '.join(result)


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
            'previous_toir_id': self.previous_toir_id,
            'previous_name': self.previous_name,
            'movement_reason': self.movement_reason,
            'movement_date': self.movement_date,
        }

    @property
    def unique_id(self):
        return self.previous_toir_id
