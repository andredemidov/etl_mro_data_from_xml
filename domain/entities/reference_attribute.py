from dataclasses import dataclass


@dataclass
class ReferenceAttribute:
    toir_id: str = ''
    value: str = ''
    reference_id: str = ''
    reference_name: str = ''
    attribute_id: str = ''
    name: str = ''

    @property
    def request_value(self):
        if not self.reference_id:
            return None
        return {'Id': self.reference_id, 'Name': 'forvalidation'}

    @property
    def comparison_value(self):
        return self.value if self.value else self.reference_name
