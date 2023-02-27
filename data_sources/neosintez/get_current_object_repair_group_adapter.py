from typing import List

from domain.entities import OperationObject, ObjectRepairGroup
from .neosintez_gateway import NeosintezGateway


class GetCurrentObjectRepairGroupAdapter(NeosintezGateway):

    def __init__(self, url, token):
        super().__init__(url, token)
        self._object_group_data = []
        self._object_groups = []

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
                    "Value": self.object_repair_group_class_id
                }
            ]
        }
        result = self.make_smart_search_request(payload)
        self._object_group_data.extend(result)

    def _init_object_groups(self, item):
        attributes = item['Object']['Attributes']
        self_id = item['Object']['Id']

        toir_id = self.get_value(attributes, self.toir_id_attribute_id)
        level = self.get_value(attributes, self.level_attribute_id, attribute_type='int')
        parent = self.get_value(attributes, self.parent_attribute_id)
        name = self.get_value(attributes, self.name_attribute_id)
        toir_url = self.get_value(attributes, self.toir_url_attribute_id)
        departament_id = self.get_value(attributes, self.departament_id_attribute_id)

        repair_object = ObjectRepairGroup(
            toir_id=toir_id,
            level=level,
            parent_toir_id=parent,
            name=name,
            toir_url=toir_url,
            departament_id=departament_id,
            self_id=self_id,
        )
        self._object_groups.append(repair_object)

    def execute(self, operating_object: OperationObject) -> List[ObjectRepairGroup]:
        self._get_data(root_id=operating_object.self_id)
        print('response of repair objects is got', len(self._object_group_data))
        for item in self._object_group_data:
            self._init_object_groups(item)
        return self._object_groups
