from typing import List

from .neosintez_gateway import NeosintezGateway

from domain.entities import OperationObject


class GetOperationObjectAdapter(NeosintezGateway):

    def __init__(self, url, token):
        super().__init__(url, token)
        self._data = []
        self._operation_objects = []

    def _get_data(self):
        print('get operation objects is called')
        payload = {
            "Filters": [
                {
                    "Type": 5,
                    "Value": self.operation_object_class_id
                }
            ],
            "Conditions": [
                {
                    "Type": 1,
                    "Attribute": self.config_attribute_id,
                    "Operator": 7,
                },
            ]
        }
        result = self.make_smart_search_request(payload)
        self._data.extend(result)

    def _init_operation_object(self, item):
        attributes = item['Object']['Attributes']
        name = item['Object']['Name']
        operation_object_id = item['Object']['Id']
        operation_object_toir_id = self.get_value(attributes, self.config_attribute_id)

        repair_object = OperationObject(
            name=name,
            self_id=operation_object_id,
            toir_id=operation_object_toir_id,
        )
        self._operation_objects.append(repair_object)

    def execute(self) -> List[OperationObject]:
        self._get_data()
        print('response of operation object is got', len(self._data))
        for item in self._data:
            self._init_operation_object(item)
        return self._operation_objects
