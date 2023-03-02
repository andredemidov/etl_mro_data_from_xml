from domain import entities
from . import neosintez_gateway
from . import serializers
from .get_operation_object_adapter import GetOperationObjectAdapter


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

    def get_current_equipment(self, operation_object: entities.OperationObject) -> list[entities.Equipment]:
        data = self._get_data(root_id=operation_object.self_id, class_id=self.equipment_class_id)
        items = [serializers.EquipmentSerializer.init_from_neosintez(item) for item in data]
        return items

    def get_current_tech_position(self, operation_object: entities.OperationObject) -> list[entities.TechPosition]:
        data = self._get_data(root_id=operation_object.self_id, class_id=self.tech_position_class_id)
        items = [serializers.TechPositionSerializer.init_from_neosintez(item) for item in data]
        return items

    def get_current_object_repair_group(self, operation_object: entities.OperationObject) -> list[entities.ObjectRepairGroup]:
        data = self._get_data(root_id=operation_object.self_id, class_id=self.object_repair_group_class_id)
        items = [serializers.ObjectRepairGroupSerializer.init_from_neosintez(item) for item in data]
        return items

    def get_operation_objects(self) -> list[entities.OperationObject]:
        return GetOperationObjectAdapter(self._url, self._session).execute()
