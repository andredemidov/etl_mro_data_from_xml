from dataclasses import dataclass, field
from typing import List, Literal
from datetime import datetime

from .equipment_part import EquipmentPart
from .equipment_repair import EquipmentRepair
from .equipment_failure import EquipmentFailure
from .equipment_attribute import EquipmentAttribute
from .equipment_movement import EquipmentMovement

STATUS = Literal['updated', 'new', 'empty', 'not updated']


@dataclass
class Equipment:

    toir_id: str
    level: int
    parent_toir_id: str
    name: str
    operating: float
    departament_id: str
    object_type_id: str
    toir_url: str
    parent_object: object = None
    tech_number: str = None
    registration_number: str = None
    commodity_producer: str = None
    commodity_number: str = None
    operation_date: datetime = None
    category: str = None
    replaced: bool = False
    object_id: str = None

    attributes: List[EquipmentAttribute] = field(default_factory=list)
    past_repairs: List[EquipmentRepair] = field(default_factory=list)
    plan_repairs: List[EquipmentRepair] = field(default_factory=list)
    failures: List[EquipmentFailure] = field(default_factory=list)
    parts: List[EquipmentPart] = field(default_factory=list)
    movements: List[EquipmentMovement] = field(default_factory=list)

    self_id: str = None
    update_status: STATUS = 'empty'

    def __str__(self):
        return f'ОР: {self.name}, guid: {self.toir_id}'

    def to_compare_dict(self) -> dict:
        return {
            'toir_id': self.toir_id,
            'name': self.name,
            'toir_url': self.toir_url,
            'tech_number': self.tech_number,
            'registration_number': self.registration_number,
            'commodity_producer': self.commodity_producer,
            'commodity_number': self.commodity_number,
            'object_id': self.object_id,
        }

    def to_dict(self) -> dict:
        return {
            'toir_id': self.toir_id,
            'level': self.level,
            'parent_toir_id': self.parent_toir_id,
            'name': self.name,
            'operating': self.operating,
            'departament_id': self.departament_id,
            'object_type_id': self.object_type_id,
            'toir_url': self.toir_url,
            'tech_number': self.tech_number,
            'registration_number': self.registration_number,
            'commodity_producer': self.commodity_producer,
            'commodity_number': self.commodity_number,
            'operation_date': self.operation_date,
            'category': self.category,
            'self_id': self.self_id,
            'update_status': self.update_status,
            'replaced': self.replaced,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return Equipment(
            toir_id=data.get('toir_id'),
            level=data.get('level'),
            parent_toir_id=data.get('parent_toir_id'),
            name=data.get('name'),
            operating=data.get('operating'),
            departament_id=data.get('departament_id'),
            object_type_id=data.get('object_type_id'),
            toir_url=data.get('toir_url'),
            tech_number=data.get('tech_number'),
            registration_number=data.get('registration_number'),
            commodity_producer=data.get('commodity_producer'),
            commodity_number=data.get('commodity_number'),
            operation_date=data.get('operation_date'),
            self_id=data.get('self_id'),
            category=data.get('category'),
            replaced=data.get('replaced'),
        )
