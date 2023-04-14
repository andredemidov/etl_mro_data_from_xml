from dataclasses import dataclass, field
from typing import Literal, List
from . import reference_attribute, nested_objects

STATUS = Literal['updated', 'replaced', 'new', 'empty', 'delete', 'not updated']


@dataclass
class TechPosition:

    toir_id: str
    level: int
    parent_toir_id: str
    name: str
    departament: reference_attribute.ReferenceAttribute
    toir_url: str
    parent_object: object = None
    tech_number: str = None
    replaced: bool = False

    self_id: str = None
    update_status: STATUS = 'empty'
    object_id: str = None

    properties: List[nested_objects.Property] = field(default_factory=list)
    fact_repairs: List[nested_objects.FactRepair] = field(default_factory=list)
    plan_repairs: List[nested_objects.PlanRepair] = field(default_factory=list)
    failures: List[nested_objects.Failure] = field(default_factory=list)
    parts: List[nested_objects.Part] = field(default_factory=list)
    movements: List[nested_objects.Movement] = field(default_factory=list)

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
            'object_id': self.object_id,
            'departament': self.departament.comparison_value,
        }

    def to_dict(self) -> dict:
        return {
            'toir_id': self.toir_id,
            'level': self.level,
            'parent_toir_id': self.parent_toir_id,
            'name': self.name,
            'departament_id': self.departament.toir_id,
            'toir_url': self.toir_url,
            'tech_number': self.tech_number,
            'self_id': self.self_id,
            'update_status': self.update_status,
            'replaced': self.replaced,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return TechPosition(
            toir_id=data.get('toir_id'),
            level=data.get('level'),
            parent_toir_id=data.get('parent_toir_id'),
            name=data.get('name'),
            departament=reference_attribute.ReferenceAttribute(toir_id=data.get('departament_id')),
            toir_url=data.get('toir_url'),
            tech_number=data.get('tech_number'),
            self_id=data.get('self_id'),
            replaced=data.get('replaced'),
        )
