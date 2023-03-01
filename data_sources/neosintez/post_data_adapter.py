import json
from domain import entities
from . import neosintez_gateway
from . import serializers


class PostDataAdapter(neosintez_gateway.NeosintezGateway):

    def update(self, item: (entities.Equipment, entities.TechPosition, entities.ObjectRepairGroup)) -> str:
        if isinstance(item, entities.ObjectRepairGroup):
            put_request_body = serializers.ObjectRepairGroupSerializer.get_update_request_body(item)
        elif isinstance(item, entities.TechPosition):
            put_request_body = serializers.TechPositionSerializer.get_update_request_body(item)
        elif isinstance(item, entities.Equipment):
            put_request_body = serializers.EquipmentSerializer.get_update_request_body(item)
        else:
            raise TypeError()

        response = self.put_attributes(item.self_id, put_request_body)
        if response.status_code == 200:
            status = 'success'
        else:
            status = 'error'
        return status

    def replace(self, item: (entities.Equipment, entities.TechPosition, entities.ObjectRepairGroup)) -> str:
        # TODO: replace
        pass

    def delete(self, item: (entities.Equipment, entities.TechPosition, entities.ObjectRepairGroup)) -> str:
        response = self.delete_item(item.self_id)
        if response.status_code == 200:
            status = 'success'
        else:
            status = 'error'
        return status

    def create(self, item: (entities.Equipment, entities.TechPosition, entities.ObjectRepairGroup)) -> str:
        if isinstance(item, entities.ObjectRepairGroup):
            create_request_body = serializers.ObjectRepairGroupSerializer.get_create_request_body(item)
            put_request_body = serializers.ObjectRepairGroupSerializer.get_update_request_body(item)
        elif isinstance(item, entities.TechPosition):
            create_request_body = serializers.TechPositionSerializer.get_create_request_body(item)
            put_request_body = serializers.TechPositionSerializer.get_update_request_body(item)
        elif isinstance(item, entities.Equipment):
            create_request_body = serializers.EquipmentSerializer.get_create_request_body(item)
            put_request_body = serializers.EquipmentSerializer.get_update_request_body(item)
        else:
            raise TypeError()

        parent_id = item.parent_object.self_id
        response = self.create_item(parent_id, create_request_body)
        status = 'error'
        if response.status_code == 200:
            item.self_id = json.loads(response.text)['Id']
            response = self.put_attributes(item.self_id, put_request_body)
            if response.status_code == 200:
                status = 'success'
        return status
