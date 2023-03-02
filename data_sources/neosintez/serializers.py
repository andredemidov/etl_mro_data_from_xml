from .neosintez_gateway import NeosintezGateway
from domain import entities


class ObjectRepairGroupSerializer:

    @staticmethod
    def init_from_neosintez(item: dict) -> entities.ObjectRepairGroup:
        attributes = item['Object']['Attributes']
        self_id = item['Object']['Id']

        toir_id = NeosintezGateway.get_value(attributes, NeosintezGateway.toir_id_attribute_id)
        level = int(NeosintezGateway.get_value(attributes, NeosintezGateway.level_attribute_id, attribute_type='int'))
        parent = NeosintezGateway.get_value(attributes, NeosintezGateway.parent_attribute_id)
        name = NeosintezGateway.get_value(attributes, NeosintezGateway.name_attribute_id)
        toir_url = NeosintezGateway.get_value(attributes, NeosintezGateway.toir_url_attribute_id)
        departament_id = NeosintezGateway.get_value(attributes, NeosintezGateway.departament_id_attribute_id)
        object_id = NeosintezGateway.get_value(attributes, NeosintezGateway.object_attribute_id, get_only_id=True)

        repair_object = entities.ObjectRepairGroup(
            toir_id=toir_id,
            level=level,
            parent_toir_id=parent,
            name=name,
            toir_url=toir_url,
            departament_id=departament_id,
            self_id=self_id,
            object_id=object_id,
        )
        return repair_object

    @staticmethod
    def get_create_request_body(item: entities.ObjectRepairGroup) -> dict:
        create_request_body = {
            "Id": "00000000-0000-0000-0000-000000000000",
            "Name": item.name,
            "Entity": {
                "Id": NeosintezGateway.object_repair_group_class_id,
                "Name": "forvalidation"
            },
        }
        return create_request_body

    @staticmethod
    def get_update_request_body(item: entities.ObjectRepairGroup) -> list:
        put_request_body = [
            {
                'Name': 'forvalidation',
                'Value': {'Name': 'forvalidation', 'Id': item.object_id} if item.object_id else None,
                'Type': 8,
                'Id': NeosintezGateway.object_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.toir_id if item.toir_id else None,
                'Type': 2,
                'Id': NeosintezGateway.toir_id_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.level if item.level else None,
                'Type': 2,
                'Id': NeosintezGateway.level_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.name if item.name else None,
                'Type': 2,
                'Id': NeosintezGateway.name_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.parent_toir_id if item.parent_toir_id else None,
                'Type': 2,
                'Id': NeosintezGateway.parent_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.toir_url if item.toir_url else None,
                'Type': 6,
                'Id': NeosintezGateway.toir_url_attribute_id
            },
            # TODO: get department id based on neosintez data, because item.department_id is 1C system value
            # {
            #     'Name': 'forvalidation',
            #     'Value': {'Id': item.departament_id, 'Name': 'forvalidation'} if item.departament_id else None,
            #     'Type': 6,
            #     'Id': self.departament_id_attribute_id
            # },
        ]
        return put_request_body


class TechPositionSerializer:

    @staticmethod
    def init_from_neosintez(item: dict) -> entities.TechPosition:
        attributes = item['Object']['Attributes']
        self_id = item['Object']['Id']

        toir_id = NeosintezGateway.get_value(attributes, NeosintezGateway.toir_id_attribute_id)
        level = int(NeosintezGateway.get_value(attributes, NeosintezGateway.level_attribute_id, attribute_type='int'))
        parent = NeosintezGateway.get_value(attributes, NeosintezGateway.parent_attribute_id)
        name = NeosintezGateway.get_value(attributes, NeosintezGateway.name_attribute_id)
        tech_number = NeosintezGateway.get_value(attributes, NeosintezGateway.tech_number_attribute_id)
        toir_url = NeosintezGateway.get_value(attributes, NeosintezGateway.toir_url_attribute_id)
        departament_id = NeosintezGateway.get_value(attributes, NeosintezGateway.departament_id_attribute_id)
        object_id = NeosintezGateway.get_value(attributes, NeosintezGateway.object_attribute_id, get_only_id=True)

        repair_object = entities.TechPosition(
            toir_id=toir_id,
            level=level,
            parent_toir_id=parent,
            name=name,
            tech_number=tech_number,
            toir_url=toir_url,
            departament_id=departament_id,
            self_id=self_id,
            object_id=object_id,
        )
        return repair_object

    @staticmethod
    def get_create_request_body(item: entities.TechPosition) -> dict:
        create_request_body = {
            "Id": "00000000-0000-0000-0000-000000000000",
            "Name": item.name,
            "Entity": {
                "Id": NeosintezGateway.tech_position_class_id,
                "Name": "forvalidation"
            },
        }
        return create_request_body

    @staticmethod
    def get_update_request_body(item: entities.TechPosition) -> list:

        put_request_body = [
            {
                'Name': 'forvalidation',
                'Value': {'Name': 'forvalidation', 'Id': item.object_id} if item.object_id else None,
                'Type': 8,
                'Id': NeosintezGateway.object_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.toir_id if item.toir_id else None,
                'Type': 2,
                'Id': NeosintezGateway.toir_id_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.level if item.level else None,
                'Type': 2,
                'Id': NeosintezGateway.level_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.parent_toir_id if item.parent_toir_id else None,
                'Type': 2,
                'Id': NeosintezGateway.parent_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.name if item.name else None,
                'Type': 2,
                'Id': NeosintezGateway.name_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.toir_url if item.toir_url else None,
                'Type': 6,
                'Id': NeosintezGateway.toir_url_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.tech_number if item.tech_number else None,
                'Type': 2,
                'Id': NeosintezGateway.tech_number_attribute_id
            },
            # TODO: get department id based on neosintez data, because item.department_id is 1C system value
            # {
            #     'Name': 'forvalidation',
            #     'Value': {'Id': item.departament_id, 'Name': 'forvalidation'} if item.departament_id else None,
            #     'Type': 6,
            #     'Id': self.departament_id_attribute_id
            # },
        ]
        return put_request_body


class EquipmentSerializer:

    @staticmethod
    def init_from_neosintez(item: dict) -> entities.Equipment:
        attributes = item['Object']['Attributes']
        self_id = item['Object']['Id']

        toir_id = NeosintezGateway.get_value(attributes, NeosintezGateway.toir_id_attribute_id)
        level = int(NeosintezGateway.get_value(attributes, NeosintezGateway.level_attribute_id, attribute_type='int'))
        parent = NeosintezGateway.get_value(attributes, NeosintezGateway.parent_attribute_id)
        name = NeosintezGateway.get_value(attributes, NeosintezGateway.name_attribute_id)
        tech_number = NeosintezGateway.get_value(attributes, NeosintezGateway.tech_number_attribute_id)
        toir_url = NeosintezGateway.get_value(attributes, NeosintezGateway.toir_url_attribute_id)
        operation_date = NeosintezGateway.get_value(attributes, NeosintezGateway.operation_date_attribute_id)
        registration_number = NeosintezGateway.get_value(attributes, NeosintezGateway.registration_number_attribute_id)
        commodity_producer = NeosintezGateway.get_value(attributes, NeosintezGateway.commodity_producer_attribute_id)
        commodity_number = NeosintezGateway.get_value(attributes, NeosintezGateway.commodity_number_attribute_id)
        departament_id = NeosintezGateway.get_value(attributes, NeosintezGateway.departament_id_attribute_id)
        object_type_id = NeosintezGateway.get_value(attributes, NeosintezGateway.object_type_attribute_id)
        operating = NeosintezGateway.get_value(attributes, NeosintezGateway.operating_attribute_id)
        category = NeosintezGateway.get_value(attributes, NeosintezGateway.category_attribute_id)
        object_id = NeosintezGateway.get_value(attributes, NeosintezGateway.object_attribute_id, get_only_id=True)

        repair_object = entities.Equipment(
            toir_id=toir_id,
            level=level,
            parent_toir_id=parent,
            name=name,
            operating=operating,
            tech_number=tech_number,
            toir_url=toir_url,
            registration_number=registration_number,
            commodity_producer=commodity_producer,
            commodity_number=commodity_number,
            operation_date=operation_date,
            departament_id=departament_id,
            object_type_id=object_type_id,
            self_id=self_id,
            category=category,
            object_id=object_id,
        )
        return repair_object

    @staticmethod
    def get_create_request_body(item: entities.Equipment) -> dict:
        create_request_body = {
            "Id": "00000000-0000-0000-0000-000000000000",
            "Name": item.name,
            "Entity": {
                "Id": NeosintezGateway.equipment_class_id,
                "Name": "forvalidation"
            },
        }
        return create_request_body

    @staticmethod
    def get_update_request_body(item: entities.Equipment) -> list:

        put_request_body = [
            {
                'Name': 'forvalidation',
                'Value': {'Name': 'forvalidation', 'Id': item.object_id} if item.object_id else None,
                'Type': 8,
                'Id': NeosintezGateway.object_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.toir_id if item.toir_id else None,
                'Type': 2,
                'Id': NeosintezGateway.toir_id_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.level if item.level else None,
                'Type': 2,
                'Id': NeosintezGateway.level_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.parent_toir_id if item.parent_toir_id else None,
                'Type': 2,
                'Id': NeosintezGateway.parent_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.name if item.name else None,
                'Type': 2,
                'Id': NeosintezGateway.name_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.toir_url if item.toir_url else None,
                'Type': 6,
                'Id': NeosintezGateway.toir_url_attribute_id
            },
            # {
            #     'Name': 'forvalidation',
            #     'Value': item.operating if item.operating else None,
            #     'Type': 1,
            #     'Id': self.operating_attribute_id
            # },
            {
                'Name': 'forvalidation',
                'Value': item.tech_number if item.tech_number else None,
                'Type': 2,
                'Id': NeosintezGateway.tech_number_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.registration_number if item.registration_number else None,
                'Type': 2,
                'Id': NeosintezGateway.registration_number_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.commodity_producer if item.commodity_producer else None,
                'Type': 2,
                'Id': NeosintezGateway.commodity_producer_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.commodity_number if item.commodity_number else None,
                'Type': 2,
                'Id': NeosintezGateway.commodity_number_attribute_id
            },
            # TODO: get category id based on neosintez data, because item.department_id is 1C system value
            # TODO: get object type id based on neosintez data, because item.department_id is 1C system value
            # TODO: get department id based on neosintez data, because item.department_id is 1C system value
            # {
            #     'Name': 'forvalidation',
            #     'Value': {'Id': item.departament_id, 'Name': 'forvalidation'} if item.departament_id else None,
            #     'Type': 6,
            #     'Id': self.departament_id_attribute_id
            # },
        ]
        return put_request_body
