from domain import entities
from . import neosintez_gateway
from .. import serializers


class GetCurrentDataAdapter(neosintez_gateway.NeosintezGateway):

    def _get_data(self, root_id, class_id) -> list:
        print(f'called getting objects with class {class_id} from {root_id}')
        payload = {
            "Filters": [
                {
                    "Type": 4,
                    "Value": root_id
                },
                {
                    "Type": 5,
                    "Value": class_id
                }
            ]
        }
        result = self.make_smart_search_request(payload)
        print('response is got', len(result))
        return result

    def _get_operation_objects_data(self, class_id):
        print('get operation objects is called')
        payload = {
            "Filters": [
                {
                    "Type": 5,
                    "Value": class_id
                }
            ],
            "Conditions": [
                {
                    "Type": 1,
                    "Attribute": serializers.Serializer.config_attribute_id,
                    "Operator": 7,
                },
            ]
        }
        result = self.make_smart_search_request(payload)
        print('response is got', len(result))
        return result

    def retrieve(self, operation_object: entities.OperationObject, retrievable_object: str) -> list:
        serializer = serializers.get_serializer(retrievable_object)
        class_id = serializer.class_id
        root_id = serializer.folder_id if serializer.folder_id else operation_object.self_id

        if retrievable_object == 'operation_object':
            data = self._get_operation_objects_data(class_id=class_id)
            items = [serializer.init_from_neosintez(item) for item in data]
        else:
            data = self._get_data(root_id=root_id, class_id=class_id)
            items = [serializer.init_from_neosintez(item) for item in data]
            self._get_nested_objects(operation_object, items)

        return items

    def _get_nested_objects(self, operation_object: entities.OperationObject, items: list):
        nested_objects = [
            {'nested_object': 'property', 'attribute_name': 'properties'},
            {'nested_object': 'plan_repair', 'attribute_name': 'plan_repairs'},
            {'nested_object': 'fact_repair', 'attribute_name': 'fact_repairs'},
            {'nested_object': 'failure', 'attribute_name': 'failures'},
            {'nested_object': 'part', 'attribute_name': 'parts'},
        ]
        for nested_object in nested_objects:
            retrievable_nested_object = nested_object['nested_object']
            attribute_name = nested_object['attribute_name']
            items = list(filter(lambda x: hasattr(x, attribute_name), items))
            if items:
                nested_objects = self.retrieve(operation_object, retrievable_nested_object)
                nested_objects_dict = {}
                nested_objects_hosts = set(map(lambda x: x.host_id, nested_objects))
                for host in nested_objects_hosts:
                    nested_objects_dict[host] = list(filter(lambda x: x.host_id == host, nested_objects))

                for item in items:
                    item_nested_objects = nested_objects_dict.get(item.self_id)
                    if item_nested_objects:
                        setattr(item, attribute_name, item_nested_objects)
