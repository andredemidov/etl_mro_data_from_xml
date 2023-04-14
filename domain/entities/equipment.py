from dataclasses import dataclass, field
from typing import List, Literal
from datetime import datetime
from . import nested_objects, reference_attribute

STATUS = Literal['updated', 'new', 'empty', 'not updated']


@dataclass
class Equipment:

    toir_id: str
    level: int
    parent_toir_id: str
    name: str
    operating: float
    departament: reference_attribute.ReferenceAttribute
    typical_object: reference_attribute.ReferenceAttribute
    toir_url: str
    parent_object: object = None
    tech_number: str = None
    registration_number: str = None
    commodity_producer: str = None
    commodity_number: str = None
    operation_date: datetime = None
    category: reference_attribute.ReferenceAttribute = None
    replaced: bool = False
    object_id: str = None

    properties: List[nested_objects.Property] = field(default_factory=list)
    fact_repairs: List[nested_objects.FactRepair] = field(default_factory=list)
    plan_repairs: List[nested_objects.PlanRepair] = field(default_factory=list)
    failures: List[nested_objects.Failure] = field(default_factory=list)
    parts: List[nested_objects.Part] = field(default_factory=list)
    movements: List[nested_objects.Movement] = field(default_factory=list)

    self_id: str = None
    update_status: STATUS = 'empty'

    def __str__(self):
        return f'{self.name}, {self.toir_id}'

    def get_nested_objects(self):
        return [
            self.properties,
            self.fact_repairs,
            self.plan_repairs,
            self.failures,
            self.parts,
        ]

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
            'departament': self.departament.comparison_value,
            'typical_object': self.typical_object.comparison_value,
            'category': self.category.comparison_value,
        }

    def to_dict(self) -> dict:
        return {
            'toir_id': self.toir_id,
            'level': self.level,
            'parent_toir_id': self.parent_toir_id,
            'name': self.name,
            'operating': self.operating,
            'departament_id': self.departament.toir_id,
            'object_type_id': self.typical_object.toir_id,
            'toir_url': self.toir_url,
            'tech_number': self.tech_number,
            'registration_number': self.registration_number,
            'commodity_producer': self.commodity_producer,
            'commodity_number': self.commodity_number,
            'operation_date': self.operation_date,
            'category': self.category.value,
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
            departament=data.get('departament_id'),
            typical_object=data.get('object_type_id'),
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
