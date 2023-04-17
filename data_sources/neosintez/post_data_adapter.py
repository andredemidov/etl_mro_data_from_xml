import json
from domain import entities
from . import neosintez_gateway
from .. import serializers


class PostDataAdapter(neosintez_gateway.NeosintezGateway):

    # dict like {attribute_id: {value: reference_id}}
    REFERENCE_ATTRIBUTES_VALUES = {}
    # dict like {host_id: {collection_attribute_id: {self_id: delete_self_id}}}
    HOST_COLLECTIONS_DATA = {}

    def update(self, item: (entities.Equipment, entities.TechPosition, entities.ObjectRepairGroup)) -> str:
        self._get_reference_attribute_value(item)

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
        self._get_reference_attribute_value(item)

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
        if isinstance(item, entities.nested_objects.Property):
            _, collection_attribute_id = serializers.PropertySerializer.get_create_request_body(item)
        elif isinstance(item, entities.nested_objects.PlanRepair):
            _, collection_attribute_id = serializers.PlanRepairSerializer.get_create_request_body(item)
        elif isinstance(item, entities.nested_objects.FactRepair):
            _, collection_attribute_id = serializers.FactRepairSerializer.get_create_request_body(item)
        elif isinstance(item, entities.nested_objects.Failure):
            _, collection_attribute_id = serializers.FailureSerializer.get_create_request_body(item)
        elif isinstance(item, entities.nested_objects.Part):
            _, collection_attribute_id = serializers.PartSerializer.get_create_request_body(item)
        else:
            raise TypeError()
        # check if data already retrieved
        if not (item.host_id in self.HOST_COLLECTIONS_DATA
                and collection_attribute_id in self.HOST_COLLECTIONS_DATA.get(item.host_id)):
            response = self.get_host_collections(item.host_id, collection_attribute_id)
            self.HOST_COLLECTIONS_DATA.setdefault(item.host_id, {})
            self.HOST_COLLECTIONS_DATA[item.host_id].setdefault(collection_attribute_id, {})
            if response.status_code == 200:
                response_text = json.loads(response.text)
                # get dict like {self_id: delete_self_id}
                collections_data = dict(map(lambda x: (x['Object']['Id'], x['Id']), response_text['Result']))
                self.HOST_COLLECTIONS_DATA[item.host_id][collection_attribute_id] = collections_data

        delete_self_id = self.HOST_COLLECTIONS_DATA[item.host_id][collection_attribute_id].get(item.self_id)
        status = 'error'
        if delete_self_id:
            response = self.delete_item(delete_self_id, item.host_id)
            if response.status_code == 200:
                status = 'success'
        return status

    def create(self, item: (entities.Equipment, entities.TechPosition, entities.ObjectRepairGroup)) -> str:
        self._get_reference_attribute_value(item)

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
        self._get_reference_attribute_value(item)
        
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

    def _get_reference_attribute_value(self, item):
        reference_attributes: list[entities.ReferenceAttribute] = list(
            filter(lambda x: isinstance(x, entities.ReferenceAttribute), item.__dict__.values()))

        # filter attributes where reference_id already exists
        reference_attributes = list(filter(lambda x: not x.reference_id, reference_attributes))
        # filter attributes where value exist
        reference_attributes = list(filter(lambda x: x.value, reference_attributes))

        for attribute in reference_attributes:
            attribute_id = attribute.attribute_id
            value = attribute.value
            # check whether reference_id already exists
            values = self.REFERENCE_ATTRIBUTES_VALUES.get(attribute_id)
            attribute.reference_id = values.get(value) if values else None
            # if there is no reference_id for that value get it from neosintez
            if not attribute.reference_id:
                class_id = serializers.Serializer.reference_attributes[attribute_id]['class_id']
                folder_id = serializers.Serializer.reference_attributes[attribute_id]['folder_id']
                if attribute.toir_id:
                    key_attribute_id = serializers.Serializer.reference_attributes[attribute_id]['key_attribute_id']
                    reference_id = self._get_id_by_key(folder_id, class_id, attribute.toir_id, key_attribute_id)
                else:
                    reference_id = self._get_id_by_name(folder_id, class_id, value)
                # check whether reference_id is got and save it to reduce requests
                if reference_id:
                    self.REFERENCE_ATTRIBUTES_VALUES.setdefault(attribute_id, {})
                    self.REFERENCE_ATTRIBUTES_VALUES[attribute_id][value] = reference_id
                    attribute.reference_id = reference_id
