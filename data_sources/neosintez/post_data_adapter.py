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

    # def _get_reference_attribute_value(self, item):
    #     reference_attributes: list[entities.ReferenceAttribute] = list(
    #         filter(lambda x: isinstance(x, entities.ReferenceAttribute), item.__dict__.values()))
    #
    #     # filter attributes where reference_id already exists
    #     reference_attributes = list(filter(lambda x: not x.reference_id, reference_attributes))
    #     # filter attributes where value exist
    #     reference_attributes = list(filter(lambda x: x.value, reference_attributes))
    #
    #     for attribute in reference_attributes:
    #         attribute_id = attribute.attribute_id
    #         value = attribute.value
    #         # check whether reference_id already exists
    #         values = self.REFERENCE_ATTRIBUTES_VALUES.get(attribute_id)
    #         attribute.reference_id = values.get(value) if values else None
    #         # if there is no reference_id for that value get it from neosintez
    #         if not attribute.reference_id:
    #             class_id = serializers.Serializer.reference_attributes[attribute_id]['class_id']
    #             folder_id = serializers.Serializer.reference_attributes[attribute_id]['folder_id']
    #             if attribute.toir_id:
    #                 key_attribute_id = serializers.Serializer.reference_attributes[attribute_id]['key_attribute_id']
    #                 reference_id = self._get_id_by_key(folder_id, class_id, attribute.toir_id, key_attribute_id)
    #             else:
    #                 reference_id = self._get_id_by_name(folder_id, class_id, value)
    #             # check whether reference_id is got and save it to reduce requests
    #             if reference_id:
    #                 self.REFERENCE_ATTRIBUTES_VALUES.setdefault(attribute_id, {})
    #                 self.REFERENCE_ATTRIBUTES_VALUES[attribute_id][value] = reference_id
    #                 attribute.reference_id = reference_id

    # def _create_reference_item(self, folder_id, class_id, value, key_attribute_value=None, key_attribute_id=None, parent_key_attribute_value=None):
    #     create_request_body = {
    #         "Id": "00000000-0000-0000-0000-000000000000",
    #         "Name": value,
    #         "Entity": {
    #             "Id": class_id,
    #             "Name": "forvalidation"
    #         },
    #     }
    #     if parent_key_attribute_value and key_attribute_id and key_attribute_value:
    #         parent_id = self._get_id_by_key(folder_id, class_id, parent_key_attribute_value, key_attribute_id)
    #         if not parent_id:
    #             self._create_reference_item()
    #
    #     response = self.create_item(folder_id, create_request_body)
    #     status = 'success'
    #     if response.status_code == 200:
    #         if key_attribute_value and key_attribute_id:
    #             self_id = json.loads(response.text)['Id']
    #             put_request_body = [
    #                 {
    #                     'Name': 'forvalidation',
    #                     'Value': key_attribute_value,
    #                     'Type': 2,
    #                     'Id': key_attribute_id
    #                 },
    #             ]
    #             response = self.put_attributes(self_id, put_request_body)
    #             if response.status_code == 200:
    #                 status = 'success'
    #         else:
    #             status = 'success'
    #     return status
