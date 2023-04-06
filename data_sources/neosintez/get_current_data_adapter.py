from typing import Literal
from domain import entities
from . import neosintez_gateway
from .. import serializers


class GetCurrentDataAdapter(neosintez_gateway.NeosintezGateway):

    OBJECTS = Literal[
        'operation_object',
        'equipment',
        'tech_position',
        'object_repair_group',
        'property',
        'plan_repair',
        'fact_repair',
        'failure',
        'part',
    ]

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

    def retrieve(self, operation_object: entities.OperationObject, retrievable_object: OBJECTS) -> list:
        if retrievable_object not in self.OBJECTS:
            raise TypeError(f'{retrievable_object} is not available')
        retrievable_objects = {
            'operation_object': {
                'class_id': serializers.Serializer.operation_object_class_id,
                'serializer': serializers.OperationObjectSerializer
            },
            'equipment': {
                'class_id': serializers.Serializer.equipment_class_id,
                'serializer': serializers.EquipmentSerializer
            },
            'tech_position': {
                'class_id': serializers.Serializer.tech_position_class_id,
                'serializer': serializers.TechPositionSerializer
            },
            'object_repair_group': {
                'class_id': serializers.Serializer.object_repair_group_class_id,
                'serializer': serializers.ObjectRepairGroupSerializer
            },
            'property': {
                'class_id': serializers.Serializer.property_collection_class_id,
                'serializer': serializers.PropertySerializer
            },
            'plan_repair': {
                'class_id': serializers.Serializer.plan_repair_collection_class_id,
                'serializer': serializers.PlanRepairSerializer
            },
            'fact_repair': {
                'class_id': serializers.Serializer.fact_repair_collection_class_id,
                'serializer': serializers.FactRepairSerializer
            },
            'failure': {
                'class_id': serializers.Serializer.failure_collection_class_id,
                'serializer': serializers.FailureSerializer
            },
            'part': {
                'class_id': serializers.Serializer.part_collection_class_id,
                'serializer': serializers.PartSerializer
            },
        }
        class_id = retrievable_objects[retrievable_object]['class_id']
        serializer = retrievable_objects[retrievable_object]['serializer']
        if retrievable_object == 'operation_object':
            data = self._get_operation_objects_data(class_id=class_id)
        else:
            data = self._get_data(root_id=operation_object.self_id, class_id=class_id)
        items = [serializer.init_from_neosintez(item) for item in data]
        return items
