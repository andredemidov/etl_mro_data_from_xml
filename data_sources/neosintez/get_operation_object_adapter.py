from typing import List

from .neosintez_gateway import NeosintezGateway

from domain.entities import OperationObject


class GetOperationObjectAdapter(NeosintezGateway):

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
        return result

    def _init_operation_object(self, item) -> OperationObject:
        attributes = item['Object']['Attributes']
        name = item['Object']['Name']
        operation_object_id = item['Object']['Id']
        operation_object_toir_id = self.get_value(attributes, self.config_attribute_id)
        object_id = self.get_value(attributes, self.object_attribute_id, get_only_id=True)

        repair_object = OperationObject(
            name=name,
            self_id=operation_object_id,
            toir_id=operation_object_toir_id,
            object_id=object_id,
        )
        return repair_object

    def execute(self) -> List[OperationObject]:
        result = []
        data = self._get_data()
        print('response of operation object is got', len(data))
        for item in data:
            operation_object = self._init_operation_object(item)
            result.append(operation_object)
        return result
