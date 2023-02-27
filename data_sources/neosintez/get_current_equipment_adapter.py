from typing import List

from domain.entities import OperationObject, Equipment
from .neosintez_gateway import NeosintezGateway


class GetCurrentEquipmentAdapter(NeosintezGateway):

    def __init__(self, url, token):
        super().__init__(url, token)
        self._equipment_data = []
        self._equipments = []

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
                    "Value": self.equipment_class_id
                }
            ]
        }
        result = self.make_smart_search_request(payload)
        self._equipment_data.extend(result)

    def _init_equipment(self, item):
        attributes = item['Object']['Attributes']
        self_id = item['Object']['Id']

        toir_id = self.get_value(attributes, self.toir_id_attribute_id)
        level = self.get_value(attributes, self.level_attribute_id, attribute_type='int')
        parent = self.get_value(attributes, self.parent_attribute_id)
        name = self.get_value(attributes, self.name_attribute_id)
        tech_number = self.get_value(attributes, self.tech_number_attribute_id)
        toir_url = self.get_value(attributes, self.toir_url_attribute_id)
        operation_date = self.get_value(attributes, self.operation_date_attribute_id)
        registration_number = self.get_value(attributes, self.registration_number_attribute_id)
        commodity_producer = self.get_value(attributes, self.commodity_producer_attribute_id)
        commodity_number = self.get_value(attributes, self.commodity_number_attribute_id)
        departament_id = self.get_value(attributes, self.departament_id_attribute_id)
        object_type_id = self.get_value(attributes, self.object_type_attribute_id)
        operating = self.get_value(attributes, self.operating_attribute_id)
        category = self.get_value(attributes, self.category_attribute_id)

        repair_object = Equipment(
            toir_id=toir_id,
            level=level,
            parent_toir_id=parent,
            name=name,
            operating=operating,
            tech_number=tech_number,
            toir_url=toir_url,
            registration_number=registration_number,
            commodity_producer=commodity_producer,
            commodity_number=commodity_number,
            operation_date=operation_date,
            departament_id=departament_id,
            object_type_id=object_type_id,
            self_id=self_id,
            category=category,
        )
        self._equipments.append(repair_object)

    def execute(self, operating_object: OperationObject) -> List[Equipment]:
        self._get_data(root_id=operating_object.self_id)
        print('response of repair objects is got', len(self._equipment_data))
        for item in self._equipment_data:
            self._init_equipment(item)
        return self._equipments
