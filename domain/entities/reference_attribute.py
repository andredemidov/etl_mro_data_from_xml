from dataclasses import dataclass


@dataclass
class ReferenceAttribute:
    toir_id: str = ''
    value: str = ''
    reference_item_id: str = ''
    attribute_id: str = ''

    @property
    def request_value(self):
        return {'Id': self.reference_item_id, 'Name': 'forvalidation'}