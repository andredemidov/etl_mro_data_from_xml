import json
from domain import entities
from . import neosintez_gateway
from .. import serializers


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

    def update_nested_object(self, item) -> str:
        if isinstance(item, entities.nested_objects.Property):
            put_request_body = serializers.PropertySerializer.get_update_request_body(item)
        elif isinstance(item, entities.nested_objects.PlanRepair):
            put_request_body = serializers.PlanRepairSerializer.get_update_request_body(item)
        elif isinstance(item, entities.nested_objects.FactRepair):
            put_request_body = serializers.FactRepairSerializer.get_update_request_body(item)
        elif isinstance(item, entities.nested_objects.Failure):
            put_request_body = serializers.FailureSerializer.get_update_request_body(item)
        elif isinstance(item, entities.nested_objects.Part):
            put_request_body = serializers.PartSerializer.get_update_request_body(item)
        else:
            raise TypeError()

        response = self.put_attributes(item.self_id, put_request_body)
        if response.status_code == 200:
            status = 'success'
        else:
            status = 'error'
        return status

    def replace(self, item: (entities.Equipment, entities.TechPosition, entities.ObjectRepairGroup)) -> str:
        response = self.change_parent(item.self_id, item.parent_object.self_id)
        if response.status_code == 200:
            status = 'success'
        else:
            status = 'error'
        return status

    def delete(self, item: (entities.Equipment, entities.TechPosition, entities.ObjectRepairGroup)) -> str:
        response = self.delete_item(item.self_id)
        if response.status_code == 200:
            status = 'success'
        else:
            status = 'error'
        return status

    def delete_nested_object(self, item) -> str:
        response = self.delete_item(item.self_id, item.host_id)
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

    def create_nested_object(self, item) -> str:
        if isinstance(item, entities.nested_objects.Property):
            create_request_body, collection_attribute_id = serializers.PropertySerializer.get_create_request_body(item)
        elif isinstance(item, entities.nested_objects.PlanRepair):
            create_request_body, collection_attribute_id = serializers.PlanRepairSerializer.get_create_request_body(item)
        elif isinstance(item, entities.nested_objects.FactRepair):
            create_request_body, collection_attribute_id = serializers.FactRepairSerializer.get_create_request_body(item)
        elif isinstance(item, entities.nested_objects.Failure):
            create_request_body, collection_attribute_id = serializers.FailureSerializer.get_create_request_body(item)
        elif isinstance(item, entities.nested_objects.Part):
            create_request_body, collection_attribute_id = serializers.PartSerializer.get_create_request_body(item)
        else:
            raise TypeError()

        host_id = item.host_id
        response = self.create_item(host_id, create_request_body, collection_attribute_id)
        if response.status_code == 200:
            status = 'success'
        else:
            status = 'error'
        return status

    def _get_reference_attribute_value(self, request_body: (dict, list[dict])):
        if isinstance(request_body, dict):
            reference_attributes = list(filter(lambda x: x['Type'] == 8, request_body['Attributes'].values()))
        else:
            reference_attributes = list(filter(lambda x: x['Type'] == 8, request_body))

        for attribute in reference_attributes:
            attribute_id = attribute['Id']
            value = attribute['Value']
            class_id = serializers.Serializer.reference_attributes['class_id']
            folder_id = serializers.Serializer.reference_attributes['folder_id']
            reference_id = self._get_id_by_key(folder_id, class_id, value, attribute_id)
            if reference_id:
                attribute['Value'] = {'Id': reference_id, 'Name': 'forvalidation'}
