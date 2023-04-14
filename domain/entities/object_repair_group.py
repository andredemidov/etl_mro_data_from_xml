from dataclasses import dataclass
from typing import Literal
from . import reference_attribute

STATUS = Literal['updated', 'new', 'empty', 'not updated']


@dataclass
class ObjectRepairGroup:
    toir_id: str
    level: int
    parent_toir_id: str
    name: str
    toir_url: str
    departament: reference_attribute.ReferenceAttribute
    parent_object = None
    self_id: str = None
    replaced: bool = False
    update_status: STATUS = 'empty'
    object_id: str = None

    def get_nested_objects(self):
        return []

    def to_compare_dict(self) -> dict:
        return {
            'toir_id': self.toir_id,
            'name': self.name,
            'toir_url': self.toir_url,
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
            'self_id': self.self_id,
            'update_status': self.update_status,
            'replaced': self.replaced,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return ObjectRepairGroup(
            toir_id=data.get('toir_id'),
            level=data.get('level'),
            parent_toir_id=data.get('parent_toir_id'),
            name=data.get('name'),
            departament=data.get('departament_id'),
            toir_url=data.get('toir_url'),
            self_id=data.get('self_id'),
            replaced=data.get('replaced'),
        )
