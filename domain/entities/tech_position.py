from dataclasses import dataclass
from typing import Literal

STATUS = Literal['updated', 'replaced', 'new', 'empty', 'delete', 'not updated']


@dataclass
class TechPosition:

    toir_id: str
    level: int
    parent_toir_id: str
    name: str
    departament_id: str
    toir_url: str
    parent_object: object = None
    tech_number: str = None
    replaced: bool = False

    self_id: str = None
    update_status: STATUS = 'empty'

    def to_compare_dict(self) -> dict:
        return {
            'toir_id': self.toir_id,
            'name': self.name,
            'toir_url': self.toir_url,
            'tech_number': self.tech_number,
        }

    def to_dict(self) -> dict:
        return {
            'toir_id': self.toir_id,
            'level': self.level,
            'parent_toir_id': self.parent_toir_id,
            'name': self.name,
            'departament_id': self.departament_id,
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
            departament_id=data.get('departament_id'),
            toir_url=data.get('toir_url'),
            tech_number=data.get('tech_number'),
            self_id=data.get('self_id'),
            replaced=data.get('replaced'),
        )
