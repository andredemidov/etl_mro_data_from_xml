from .neosintez_gateway import NeosintezGateway
from . import serializers
from domain import entities


class UpdateAdapter(NeosintezGateway):

    def execute(self, item: (entities.Equipment, entities.TechPosition, entities.ObjectRepairGroup)) -> str:
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
