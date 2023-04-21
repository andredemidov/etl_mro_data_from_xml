import json
from domain import entities
from . import neosintez_gateway
from .. import serializers


class PostDataAdapter(neosintez_gateway.NeosintezGateway):

    # dict like {attribute_id: {value: reference_id}}
    REFERENCE_ATTRIBUTES_VALUES = {}
    # dict like {host_id: {collection_attribute_id: {self_id: delete_self_id}}}
    HOST_COLLECTIONS_DATA = {}

    def update(self, item) -> str:
        serializer = serializers.get_serializer(item.object_type)
        put_request_body = serializer.get_update_request_body(item)

        # self._get_reference_attribute_value(item)
        status = 'error'
        response = self.put_attributes(item.self_id, put_request_body)
        if response.status_code == 200:
            status = 'success'
        if hasattr(item, 'name'):
            status = 'error'
            response_put = self.change_name(item.self_id, item.name)
            if response_put.status_code == 200:
                status = 'success'
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
        serializer = serializers.get_serializer(item.object_type)
        collection_attribute_id = serializer.collection_attribute_id

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

    def create(self, item: (entities.Equipment, entities.TechPosition, entities.ObjectRepairGroup, entities.Dimension)) -> str:
        serializer = serializers.get_serializer(item.object_type)
        create_request_body = serializer.get_create_request_body(item)
        put_request_body = serializer.get_update_request_body(item)

        # self._get_reference_attribute_value(item)

        parent_id = item.parent_id if item.parent_id else serializer.folder_id
        response = self.create_item(parent_id, create_request_body)
        status = 'error'
        if response.status_code == 200:
            item.self_id = json.loads(response.text)['Id']
            response = self.put_attributes(item.self_id, put_request_body)
            if response.status_code == 200:
                status = 'success'
        return status

    def create_nested_object(self, item) -> str:
        serializer = serializers.get_serializer(item.object_type)
        create_request_body = serializer.get_create_request_body(item)
        collection_attribute_id = serializer.collection_attribute_id

        # self._get_reference_attribute_value(item)

        host_id = item.host_id
        response = self.create_item(host_id, create_request_body, collection_attribute_id)
        if response.status_code == 200:
            status = 'success'
        else:
            status = 'error'
        return status
