from typing import List

from domain.entities import OperationObject, TechPosition
from .neosintez_gateway import NeosintezGateway


class GetCurrentTechPositionAdapter(NeosintezGateway):

    def __init__(self, url, token):
        super().__init__(url, token)
        self._tech_positions_data = []
        self._tech_positions = []

    def _get_data(self, root_id):
        print('get repair objects is called')
        payload = {
            "Filters": [
                {
                    "Type": 4,
                    "Value": root_id
                },
                {
                    "Type": 5,
                    "Value": self.tech_position_class_id
                }
            ]
        }
        result = self.make_smart_search_request(payload)
        self._tech_positions_data.extend(result)

    def _init_tech_positions(self, item):
        attributes = item['Object']['Attributes']
        self_id = item['Object']['Id']

        toir_id = self.get_value(attributes, self.toir_id_attribute_id)
        level = self.get_value(attributes, self.level_attribute_id, attribute_type='int')
        parent = self.get_value(attributes, self.parent_attribute_id)
        name = self.get_value(attributes, self.name_attribute_id)
        tech_number = self.get_value(attributes, self.tech_number_attribute_id)
        toir_url = self.get_value(attributes, self.toir_url_attribute_id)
        departament_id = self.get_value(attributes, self.departament_id_attribute_id)

        repair_object = TechPosition(
            toir_id=toir_id,
            level=level,
            parent_toir_id=parent,
            name=name,
            tech_number=tech_number,
            toir_url=toir_url,
            departament_id=departament_id,
            self_id=self_id,
        )
        self._tech_positions.append(repair_object)

    def execute(self, operating_object: OperationObject) -> List[TechPosition]:
        self._get_data(root_id=operating_object.self_id)
        print('response of repair objects is got', len(self._tech_positions_data))
        for item in self._tech_positions_data:
            self._init_tech_positions(item)
        return self._tech_positions
