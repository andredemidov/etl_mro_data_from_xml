import json
from .neosintez_gateway import NeosintezGateway
from . import serializers
from domain import entities


class CreateAdapter(NeosintezGateway):

    def execute(self, item: (entities.Equipment, entities.TechPosition, entities.ObjectRepairGroup)) -> str:
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
        response = self.create(parent_id, create_request_body)
        status = 'error'
        if response.status_code == 200:
            item.self_id = json.loads(response.text)['Id']
            response = self.put_attributes(item.self_id, put_request_body)
            if response.status_code == 200:
                status = 'success'
        return status
