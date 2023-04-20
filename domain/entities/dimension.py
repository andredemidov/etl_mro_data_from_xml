from dataclasses import dataclass


@dataclass
class Dimension:
    toir_id: str
    object_type: str
    update_status: str = 'empty'
    name: str = None
    parent_object: object = None
    parent_toir_id: str = None
    self_id: str = None
    class_id: str = None
    replaced: bool = False

    def to_compare_dict(self) -> dict:
        return {
            'toir_id': self.toir_id,
            'name': self.name,
        }

    @property
    def unique_id(self):
        return self.toir_id

    @property
    def parent_id(self):
        return self.parent_object.self_id if self.parent_object else None
