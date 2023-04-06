from datetime import datetime
from domain import entities


class Serializer:
    # TODO: specify id
    equipment_class_id = '98a4bfa3-0929-e811-810d-c4afdb1aea70'
    tech_position_class_id = '379086c1-575b-ed11-914d-005056b6948b'
    object_repair_group_class_id = '9e8f1a26-778d-e811-810f-edf0bf5e0091'
    operation_object_class_id = 'ac65f34b-5623-ed11-9141-005056b6948b'

    object_attribute_id = '1f99882d-e232-ea11-9100-005056b6e70e'
    toir_id_attribute_id = '73e3c201-5527-e811-810c-9ec54093bb77'
    config_attribute_id = '723bba30-4175-ed11-9152-005056b6948b'
    level_attribute_id = 'ef7b693e-46c0-ea11-9110-005056b6948b'
    parent_attribute_id = 'a607d6ef-575b-ed11-914d-005056b6948b'
    name_attribute_id = '3b1ed651-5527-e811-810c-9ec54093bb77'
    tech_number_attribute_id = 'ca97a0b1-0a29-e811-810d-c4afdb1aea70'
    toir_url_attribute_id = 'a5072ee5-f164-e811-810f-edf0bf5e0091'
    operation_date_attribute_id = '02964d6c-0b29-e811-810d-c4afdb1aea70'
    departament_id_attribute_id = '057708a1-0b29-e811-810d-c4afdb1aea70'
    object_type_attribute_id = '456b1f0f-0b29-e811-810d-c4afdb1aea70'
    operating_attribute_id = ''
    registration_number_attribute_id = 'f535c056-0b29-e811-810d-c4afdb1aea70'
    commodity_producer_attribute_id = '626cd129-e330-e811-810f-edf0bf5e0091'
    commodity_number_attribute_id = '706297c6-0a29-e811-810d-c4afdb1aea70'
    category_attribute_id = '2daf9add-0a29-e811-810d-c4afdb1aea70'

    # collection classes
    failure_collection_class_id = ''
    part_collection_class_id = ''
    property_collection_class_id = ''
    fact_repair_collection_class_id = ''
    plan_repair_collection_class_id = ''

    # collection attributes
    failure_collection_attribute_id = ''
    part_collection_attribute_id = ''
    property_collection_attribute_id = ''
    fact_repair_collection_attribute_id = ''
    plan_repair_collection_attribute_id = ''

    # collection objects attributes
    failure_description_attribute_id = ''
    failure_date_attribute_id = ''
    type_reason_failure_id_attribute_id = ''
    type_failure_id_attribute_id = ''

    unit_attribute_id = ''
    amount_attribute_id = ''
    code_attribute_id = ''
    name_repair_attribute_id = ''
    type_repair_id_attribute_id = ''

    property_value_attribute_id = ''
    property_id_attribute_id = ''

    repair_id_attribute_id = ''
    repair_start_date_attribute_id = ''
    repair_finish_date_attribute_id = ''

    reference_attributes = {
        departament_id_attribute_id: {'folder_id': '', 'class_id': ''},
        category_attribute_id: {'folder_id': '', 'class_id': ''},
        type_failure_id_attribute_id: {'folder_id': '', 'class_id': ''},
        unit_attribute_id: {'folder_id': '', 'class_id': ''},
        type_repair_id_attribute_id: {'folder_id': '', 'class_id': ''},
        property_id_attribute_id: {'folder_id': '', 'class_id': ''},
    }

    @staticmethod
    def _get_value(attributes: dict, attribute_id: str, attribute_type='str', get_only_id=False):
        result = attributes.get(attribute_id, None)
        if result:
            item_type = result['Type']
            if item_type == 8 and get_only_id:
                return attributes[attribute_id]['Value']['Id']
            elif item_type == 8:
                return attributes[attribute_id]['Value']['Name']
            elif item_type == 3:
                value = attributes[attribute_id]['Value']
                return datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')
            elif item_type == 1:
                return round(attributes[attribute_id]['Value'], 4)
            else:
                return attributes[attribute_id]['Value']
        else:
            if attribute_type == 'int':
                return 0
            else:
                return None


class OperationObjectSerializer(Serializer):

    @classmethod
    def init_from_neosintez(cls, item) -> entities.OperationObject:
        attributes = item['Object']['Attributes']
        name = item['Object']['Name']
        operation_object_id = item['Object']['Id']
        operation_object_toir_id = cls._get_value(attributes, cls.config_attribute_id)
        object_id = cls._get_value(attributes, cls.object_attribute_id, get_only_id=True)

        repair_object = entities.OperationObject(
            name=name,
            self_id=operation_object_id,
            toir_id=operation_object_toir_id,
            object_id=object_id,
        )
        return repair_object


class ObjectRepairGroupSerializer(Serializer):

    @staticmethod
    def init_from_xml(element) -> entities.ObjectRepairGroup:
        toir_id = element.find('РеквизитыОР/ОбъектРемонта').text
        level = int(element.find('РеквизитыОР/УровеньГруппы').text)
        parent = element.find('РеквизитыОР/ОбъектРемонта_Родитель').text
        name = element.find('РеквизитыОР/ОбъектРемонтаНаименование').text
        toir_url = element.find('РеквизитыОР/СсылкаОР').text
        departament_id = element.find('РеквизитыОР/ПодразделениеВладелец').text

        repair_object = entities.ObjectRepairGroup(
            toir_id=toir_id,
            level=level,
            parent_toir_id=parent,
            name=name,
            toir_url=toir_url,
            departament_id=departament_id,
        )
        return repair_object

    @classmethod
    def init_from_neosintez(cls, item: dict) -> entities.ObjectRepairGroup:
        attributes = item['Object']['Attributes']
        self_id = item['Object']['Id']

        toir_id = cls._get_value(attributes, cls.toir_id_attribute_id)
        level = int(cls._get_value(attributes, cls.level_attribute_id, attribute_type='int'))
        parent = cls._get_value(attributes, cls.parent_attribute_id)
        name = cls._get_value(attributes, cls.name_attribute_id)
        toir_url = cls._get_value(attributes, cls.toir_url_attribute_id)
        departament_name = cls._get_value(attributes, cls.departament_id_attribute_id)
        object_id = cls._get_value(attributes, cls.object_attribute_id, get_only_id=True)

        repair_object = entities.ObjectRepairGroup(
            toir_id=toir_id,
            level=level,
            parent_toir_id=parent,
            name=name,
            toir_url=toir_url,
            departament_name=departament_name,
            self_id=self_id,
            object_id=object_id,
        )
        return repair_object

    @classmethod
    def get_create_request_body(cls, item: entities.ObjectRepairGroup) -> dict:
        create_request_body = {
            "Id": "00000000-0000-0000-0000-000000000000",
            "Name": item.name,
            "Entity": {
                "Id": cls.object_repair_group_class_id,
                "Name": "forvalidation"
            },
        }
        return create_request_body

    @classmethod
    def get_update_request_body(cls, item: entities.ObjectRepairGroup) -> list:
        put_request_body = [
            {
                'Name': 'forvalidation',
                'Value': {'Name': 'forvalidation', 'Id': item.object_id} if item.object_id else None,
                'Type': 8,
                'Id': cls.object_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.toir_id if item.toir_id else None,
                'Type': 2,
                'Id': cls.toir_id_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.level if item.level else None,
                'Type': 2,
                'Id': cls.level_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.name if item.name else None,
                'Type': 2,
                'Id': cls.name_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.parent_toir_id if item.parent_toir_id else None,
                'Type': 2,
                'Id': cls.parent_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.toir_url if item.toir_url else None,
                'Type': 6,
                'Id': cls.toir_url_attribute_id
            },
            # TODO: get department id based on neosintez data, because item.department_id is 1C system value
            # {
            #     'Name': 'forvalidation',
            #     'Value': {'Id': item.departament_id, 'Name': 'forvalidation'} if item.departament_id else None,
            #     'Type': 8,
            #     'Id': self.departament_id_attribute_id
            # },
        ]
        return put_request_body


class TechPositionSerializer(Serializer):

    @staticmethod
    def init_from_xml(element) -> entities.TechPosition:
        toir_id = element.find('РеквизитыОР/ОбъектРемонта').text
        level = int(element.find('РеквизитыОР/УровеньГруппы').text)
        parent = element.find('РеквизитыОР/ОбъектРемонта_Родитель').text
        name = element.find('РеквизитыОР/ОбъектРемонтаНаименование').text
        tech_number = element.find('РеквизитыОР/ТехНомер').text
        toir_url = element.find('РеквизитыОР/СсылкаОР').text
        departament_id = element.find('РеквизитыОР/ПодразделениеВладелец').text

        repair_object = entities.TechPosition(
            toir_id=toir_id,
            level=level,
            parent_toir_id=parent,
            name=name,
            tech_number=tech_number,
            toir_url=toir_url,
            departament_id=departament_id,
        )
        return repair_object

    @classmethod
    def init_from_neosintez(cls, item: dict) -> entities.TechPosition:
        attributes = item['Object']['Attributes']
        self_id = item['Object']['Id']

        toir_id = cls._get_value(attributes, cls.toir_id_attribute_id)
        level = int(cls._get_value(attributes, cls.level_attribute_id, attribute_type='int'))
        parent = cls._get_value(attributes, cls.parent_attribute_id)
        name = cls._get_value(attributes, cls.name_attribute_id)
        tech_number = cls._get_value(attributes, cls.tech_number_attribute_id)
        toir_url = cls._get_value(attributes, cls.toir_url_attribute_id)
        departament_id = cls._get_value(attributes, cls.departament_id_attribute_id)
        object_id = cls._get_value(attributes, cls.object_attribute_id, get_only_id=True)

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

    @classmethod
    def get_create_request_body(cls, item: entities.TechPosition) -> dict:
        create_request_body = {
            "Id": "00000000-0000-0000-0000-000000000000",
            "Name": item.name,
            "Entity": {
                "Id": cls.tech_position_class_id,
                "Name": "forvalidation"
            },
        }
        return create_request_body

    @classmethod
    def get_update_request_body(cls, item: entities.TechPosition) -> list:
        put_request_body = [
            {
                'Name': 'forvalidation',
                'Value': {'Name': 'forvalidation', 'Id': item.object_id} if item.object_id else None,
                'Type': 8,
                'Id': cls.object_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.toir_id if item.toir_id else None,
                'Type': 2,
                'Id': cls.toir_id_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.level if item.level else None,
                'Type': 2,
                'Id': cls.level_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.parent_toir_id if item.parent_toir_id else None,
                'Type': 2,
                'Id': cls.parent_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.name if item.name else None,
                'Type': 2,
                'Id': cls.name_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.toir_url if item.toir_url else None,
                'Type': 6,
                'Id': cls.toir_url_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.tech_number if item.tech_number else None,
                'Type': 2,
                'Id': cls.tech_number_attribute_id
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


class EquipmentSerializer(Serializer):

    @staticmethod
    def init_from_xml(element) -> entities.Equipment:
        toir_id = element.find('РеквизитыОР/ОбъектРемонта').text
        level = int(element.find('РеквизитыОР/УровеньГруппы').text)
        parent = element.find('РеквизитыОР/ОбъектРемонта_Родитель').text
        name = element.find('РеквизитыОР/ОбъектРемонтаНаименование').text
        tech_number = element.find('РеквизитыОР/ТехНомер').text
        toir_url = element.find('РеквизитыОР/СсылкаОР').text
        registration_number = element.find('РеквизитыОР/РегистрационныйНомер').text
        commodity_producer = element.find('РеквизитыОР/Изготовитель').text
        commodity_number = element.find('РеквизитыОР/ЗаводскойНомер').text
        category = element.find('РеквизитыОР/КатегорияОборудования').text
        operation_date = element.find('РеквизитыОР/ДатаВводаВЭксплуатацию').text
        departament_id = element.find('РеквизитыОР/ПодразделениеВладелец').text
        object_type_id = element.find('РеквизитыОР/ТиповойОР').text
        operating = element.find('Наработка/Значение').text

        if operation_date:
            operation_date = datetime.strptime(operation_date, '%Y-%m-%dT%H:%M:%S')

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
            typical_object_id=object_type_id,
            category=category,
        )
        return repair_object

    @classmethod
    def init_from_neosintez(cls, item: dict) -> entities.Equipment:
        attributes = item['Object']['Attributes']
        self_id = item['Object']['Id']

        toir_id = cls._get_value(attributes, cls.toir_id_attribute_id)
        level = int(cls._get_value(attributes, cls.level_attribute_id, attribute_type='int'))
        parent = cls._get_value(attributes, cls.parent_attribute_id)
        name = cls._get_value(attributes, cls.name_attribute_id)
        tech_number = cls._get_value(attributes, cls.tech_number_attribute_id)
        toir_url = cls._get_value(attributes, cls.toir_url_attribute_id)
        operation_date = cls._get_value(attributes, cls.operation_date_attribute_id)
        registration_number = cls._get_value(attributes, cls.registration_number_attribute_id)
        commodity_producer = cls._get_value(attributes, cls.commodity_producer_attribute_id)
        commodity_number = cls._get_value(attributes, cls.commodity_number_attribute_id)
        departament_id = cls._get_value(attributes, cls.departament_id_attribute_id)
        object_type_id = cls._get_value(attributes, cls.object_type_attribute_id)
        operating = cls._get_value(attributes, cls.operating_attribute_id)
        category = cls._get_value(attributes, cls.category_attribute_id)
        object_id = cls._get_value(attributes, cls.object_attribute_id, get_only_id=True)

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
            typical_object_id=object_type_id,
            self_id=self_id,
            category=category,
            object_id=object_id,
        )
        return repair_object

    @classmethod
    def get_create_request_body(cls, item: entities.Equipment) -> dict:
        create_request_body = {
            "Id": "00000000-0000-0000-0000-000000000000",
            "Name": item.name,
            "Entity": {
                "Id": cls.equipment_class_id,
                "Name": "forvalidation"
            },
        }
        return create_request_body

    @classmethod
    def get_update_request_body(cls, item: entities.Equipment) -> list:
        put_request_body = [
            {
                'Name': 'forvalidation',
                'Value': {'Name': 'forvalidation', 'Id': item.object_id} if item.object_id else None,
                'Type': 8,
                'Id': cls.object_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.toir_id if item.toir_id else None,
                'Type': 2,
                'Id': cls.toir_id_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.level if item.level else None,
                'Type': 2,
                'Id': cls.level_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.parent_toir_id if item.parent_toir_id else None,
                'Type': 2,
                'Id': cls.parent_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.name if item.name else None,
                'Type': 2,
                'Id': cls.name_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.toir_url if item.toir_url else None,
                'Type': 6,
                'Id': cls.toir_url_attribute_id
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
                'Id': cls.tech_number_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.registration_number if item.registration_number else None,
                'Type': 2,
                'Id': cls.registration_number_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.commodity_producer if item.commodity_producer else None,
                'Type': 2,
                'Id': cls.commodity_producer_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.commodity_number if item.commodity_number else None,
                'Type': 2,
                'Id': cls.commodity_number_attribute_id
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


class FailureSerializer(Serializer):

    @staticmethod
    def init_from_xml(element) -> entities.Failure:
        toir_id = element.find('ОР').text
        type_failure_id = element.find('ВидОтказа').text
        type_reason_failure_id = element.find('ПричинаОтказа').text
        toir_url = element.find('СсылкаРеестрОтказов').text
        failure_date = element.find('ДатаОтказа').text  # TODO: string date like 2020-01-14T23:10:00 to datetime
        failure_description = element.find('Симптомы').text

        entity = entities.Failure(
            toir_id=toir_id,
            type_failure_id=type_failure_id,
            type_reason_failure_id=type_reason_failure_id,
            toir_url=toir_url,
            failure_date=failure_date,
            failure_description=failure_description,
        )
        return entity

    @classmethod
    def init_from_neosintez(cls, item: dict) -> entities.Failure:
        attributes = item['Object']['Attributes']
        self_id = item['Object']['Id']
        host_id = item['Object']['HostObjectId']

        toir_id = cls._get_value(attributes, cls.toir_id_attribute_id)
        failure_description = cls._get_value(attributes, cls.failure_description_attribute_id)
        failure_date = cls._get_value(attributes, cls.failure_date_attribute_id)
        toir_url = cls._get_value(attributes, cls.toir_url_attribute_id)
        type_reason_failure_id = cls._get_value(attributes,
                                                cls.type_reason_failure_id_attribute_id,
                                                get_only_id=True)
        type_failure_id = cls._get_value(attributes, cls.type_failure_id_attribute_id,
                                         get_only_id=True)

        entity = entities.Failure(
            self_id=self_id,
            host_id=host_id,
            toir_id=toir_id,
            type_failure_id=type_failure_id,
            type_reason_failure_id=type_reason_failure_id,
            toir_url=toir_url,
            failure_date=failure_date,
            failure_description=failure_description,
        )
        return entity

    @classmethod
    def get_create_request_body(cls, item: entities.Failure) -> (dict, str):
        collection_attribute_id = cls.failure_collection_attribute_id
        create_request_body = {
            "Id": "00000000-0000-0000-0000-000000000000",
            "Name": "forvalidation",
            "Entity": {
                "Id": cls.failure_collection_class_id,
                "Name": "forvalidation"
            },
            "Attributes": {attribute['Id']: attribute for attribute in cls.get_update_request_body(item)}
        }
        return create_request_body, collection_attribute_id

    @classmethod
    def get_update_request_body(cls, item: entities.Failure) -> list:
        put_request_body = [
            {
                'Name': 'forvalidation',
                'Value': item.toir_id if item.toir_id else None,
                'Type': 2,
                'Id': cls.toir_id_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.failure_description if item.failure_description else None,
                'Type': 2,  # TODO: check type of attr in neosintez
                'Id': cls.failure_description_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.failure_date if item.failure_date else None,
                'Type': 5,
                'Id': cls.failure_date_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.toir_url if item.toir_url else None,
                'Type': 6,
                'Id': cls.toir_url_attribute_id
            },
            # TODO: get type_reason_failure_id based on neosintez data, because it is 1C system value
            # TODO: get type_failure_id based on neosintez data, because item.type_failure_id is 1C system value
            # {
            #     'Name': 'forvalidation',
            #     'Value': {'Id': item.departament_id, 'Name': 'forvalidation'} if item.departament_id else None,
            #     'Type': 6,
            #     'Id': self.departament_id_attribute_id
            # },
        ]
        return put_request_body


class PartSerializer(Serializer):

    @staticmethod
    def init_from_xml(element) -> entities.Part:
        toir_id = element.find('ОР').text
        name = element.find('НоменклатураНаименование').text
        unit = element.find('ЕдиницаИзмеренияНаименование').text
        amount = element.find('Количество').text
        code = element.find('Код1СБухгалтерия').text
        type_repair_id = element.find('ВидРемонта').text
        name_repair = element.find('ВидРемонтаНаименование').text

        entity = entities.Part(
            toir_id=toir_id,
            name=name,
            unit=unit,
            amount=amount,
            code=code,
            type_repair_id=type_repair_id,
            name_repair=name_repair,
        )
        return entity

    @classmethod
    def init_from_neosintez(cls, item: dict) -> entities.Part:
        attributes = item['Object']['Attributes']
        self_id = item['Object']['Id']
        host_id = item['Object']['HostObjectId']

        toir_id = cls._get_value(attributes, cls.toir_id_attribute_id)
        name = cls._get_value(attributes, cls.name_attribute_id)
        unit = cls._get_value(attributes, cls.unit_attribute_id)
        amount = cls._get_value(attributes, cls.amount_attribute_id)
        code = cls._get_value(attributes, cls.code_attribute_id)
        name_repair = cls._get_value(attributes, cls.name_repair_attribute_id)
        type_repair_id = cls._get_value(attributes, cls.type_repair_id_attribute_id,
                                        get_only_id=True)

        entity = entities.Part(
            self_id=self_id,
            host_id=host_id,
            toir_id=toir_id,
            name=name,
            unit=unit,
            amount=amount,
            code=code,
            type_repair_id=type_repair_id,
            name_repair=name_repair,
        )
        return entity

    @classmethod
    def get_create_request_body(cls, item: entities.Part) -> (dict, str):
        collection_attribute_id = cls.part_collection_attribute_id
        create_request_body = {
            "Id": "00000000-0000-0000-0000-000000000000",
            "Name": "forvalidation",
            "Entity": {
                "Id": cls.part_collection_class_id,
                "Name": "forvalidation"
            },
            "Attributes": {attribute['Id']: attribute for attribute in cls.get_update_request_body(item)}
        }
        return create_request_body, collection_attribute_id

    @classmethod
    def get_update_request_body(cls, item: entities.Part) -> list:
        put_request_body = [
            {
                'Name': 'forvalidation',
                'Value': item.toir_id if item.toir_id else None,
                'Type': 2,
                'Id': cls.toir_id_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.name if item.name else None,
                'Type': 2,  # TODO: check type of attr in neosintez
                'Id': cls.name_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.unit if item.unit else None,
                'Type': 8,
                'Id': cls.unit_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.code if item.code else None,
                'Type': 2,
                'Id': cls.code_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.code if item.code else None,
                'Type': 2,
                'Id': cls.code_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.name_repair if item.name_repair else None,
                'Type': 2,
                'Id': cls.name_repair_attribute_id
            },
            # TODO: get type_repair_id based on neosintez data, because item.type_repair_id is 1C system value
            # {
            #     'Name': 'forvalidation',
            #     'Value': {'Id': item.departament_id, 'Name': 'forvalidation'} if item.departament_id else None,
            #     'Type': 6,
            #     'Id': self.departament_id_attribute_id
            # },
        ]
        return put_request_body


class PropertySerializer(Serializer):

    @staticmethod
    def init_from_xml(element) -> entities.Property:
        toir_id = element.find('ОР').text
        property_id = element.find('Характеристика').text
        value = element.find('Значение').text

        entity = entities.Property(
            toir_id=toir_id,
            property_id=property_id,
            value=value,
        )
        return entity

    @classmethod
    def init_from_neosintez(cls, item: dict) -> entities.Property:
        attributes = item['Object']['Attributes']
        self_id = item['Object']['Id']
        host_id = item['Object']['HostObjectId']

        toir_id = cls._get_value(attributes, cls.toir_id_attribute_id)
        value = cls._get_value(attributes, cls.property_value_attribute_id)
        property_id = cls._get_value(attributes, cls.property_id_attribute_id,
                                     get_only_id=True)

        entity = entities.Property(
            self_id=self_id,
            host_id=host_id,
            toir_id=toir_id,
            property_id=property_id,
            value=value,
        )
        return entity

    @classmethod
    def get_create_request_body(cls, item: entities.Property) -> (dict, str):
        collection_attribute_id = cls.property_collection_attribute_id
        create_request_body = {
            "Id": "00000000-0000-0000-0000-000000000000",
            "Name": "forvalidation",
            "Entity": {
                "Id": cls.property_collection_class_id,
                "Name": "forvalidation"
            },
            "Attributes": {attribute['Id']: attribute for attribute in cls.get_update_request_body(item)}
        }
        return create_request_body, collection_attribute_id

    @classmethod
    def get_update_request_body(cls, item: entities.Property) -> list:
        put_request_body = [
            {
                'Name': 'forvalidation',
                'Value': item.toir_id if item.toir_id else None,
                'Type': 2,
                'Id': cls.toir_id_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.value if item.value else None,
                'Type': 2,  # TODO: check type of attr in neosintez
                'Id': cls.property_value_attribute_id
            },
            # TODO: get property_id based on neosintez data, because item.property_id is 1C system value
            # {
            #     'Name': 'forvalidation',
            #     'Value': {'Id': item.departament_id, 'Name': 'forvalidation'} if item.departament_id else None,
            #     'Type': 6,
            #     'Id': self.departament_id_attribute_id
            # },
        ]
        return put_request_body


class FactRepairSerializer(Serializer):

    @staticmethod
    def init_from_xml(element) -> entities.FactRepair:
        toir_id = element.find('ОР').text
        repair_id = element.find('ID_Ремонта').text
        toir_url = element.find('СсылкаАкт').text
        fact_start_date = element.find('ДатаНачалаФакт').text
        fact_finish_date = element.find('ДатаОкончанияФакт').text
        type_repair_id = element.find('ВидРемонта').text
        operation = element.find('Наработка').text

        entity = entities.FactRepair(
            toir_id=toir_id,
            repair_id=repair_id,
            toir_url=toir_url,
            fact_start_date=fact_start_date,
            fact_finish_date=fact_finish_date,
            type_repair_id=type_repair_id,
            operating=operation,
        )
        return entity

    @classmethod
    def init_from_neosintez(cls, item: dict) -> entities.FactRepair:
        attributes = item['Object']['Attributes']
        self_id = item['Object']['Id']
        host_id = item['Object']['HostObjectId']

        toir_id = cls._get_value(attributes, cls.toir_id_attribute_id)
        repair_id = cls._get_value(attributes, cls.repair_id_attribute_id, get_only_id=True)
        toir_url = cls._get_value(attributes, cls.toir_url_attribute_id)
        fact_start_date = cls._get_value(attributes, cls.repair_start_date_attribute_id)
        fact_finish_date = cls._get_value(attributes, cls.repair_finish_date_attribute_id)
        operating = cls._get_value(attributes, cls.operating_attribute_id)
        type_repair_id = cls._get_value(attributes, cls.type_repair_id_attribute_id,
                                        get_only_id=True)

        entity = entities.FactRepair(
            self_id=self_id,
            host_id=host_id,
            toir_id=toir_id,
            repair_id=repair_id,
            toir_url=toir_url,
            fact_start_date=fact_start_date,
            fact_finish_date=fact_finish_date,
            type_repair_id=type_repair_id,
            operating=operating,
        )
        return entity

    @classmethod
    def get_create_request_body(cls, item: entities.FactRepair) -> (dict, str):
        collection_attribute_id = cls.fact_repair_collection_attribute_id
        create_request_body = {
            "Id": "00000000-0000-0000-0000-000000000000",
            "Name": "forvalidation",
            "Entity": {
                "Id": cls.fact_repair_collection_class_id,
                "Name": "forvalidation"
            },
            "Attributes": {attribute['Id']: attribute for attribute in cls.get_update_request_body(item)}
        }
        return create_request_body, collection_attribute_id

    @classmethod
    def get_update_request_body(cls, item: entities.FactRepair) -> list:
        put_request_body = [
            {
                'Name': 'forvalidation',
                'Value': item.toir_id if item.toir_id else None,
                'Type': 2,
                'Id': cls.toir_id_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.fact_start_date if item.fact_start_date else None,
                'Type': 3,  # TODO: check type of attr in neosintez
                'Id': cls.repair_start_date_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.fact_finish_date if item.fact_finish_date else None,
                'Type': 3,  # TODO: check type of attr in neosintez
                'Id': cls.repair_finish_date_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.operating if item.operating else None,
                'Type': 1,
                'Id': cls.operating_attribute_id
            },
            # TODO: get type_repair_id based on neosintez data, because item.type_repair_id is 1C system value
            # TODO: get repair_id based on neosintez data, because item.repair_id is 1C system value
            # {
            #     'Name': 'forvalidation',
            #     'Value': {'Id': item.departament_id, 'Name': 'forvalidation'} if item.departament_id else None,
            #     'Type': 6,
            #     'Id': self.departament_id_attribute_id
            # },
        ]
        return put_request_body


class PlanRepairSerializer(Serializer):

    @staticmethod
    def init_from_xml(element) -> entities.PlanRepair:
        toir_id = element.find('ОР').text
        repair_id = element.find('ID_Ремонта').text
        toir_url = element.find('СсылкаАкт').text
        start_date = element.find('ДатаНачала').text
        finish_date = element.find('ДатаОкончания').text
        type_repair_id = element.find('ВидРемонта').text

        entity = entities.PlanRepair(
            toir_id=toir_id,
            repair_id=repair_id,
            toir_url=toir_url,
            start_date=start_date,
            finish_date=finish_date,
            type_repair_id=type_repair_id,
        )
        return entity

    @classmethod
    def init_from_neosintez(cls, item: dict) -> entities.PlanRepair:
        """
        Method to deserialize one object data from neosintez into PlanRepair instance
        :param item: one object data straight from neosintez API response as dict
        :return: PlanRepair instance
        """
        attributes = item['Object']['Attributes']
        self_id = item['Object']['Id']
        host_id = item['Object']['HostObjectId']

        toir_id = cls._get_value(attributes, cls.toir_id_attribute_id)
        repair_id = cls._get_value(attributes, cls.repair_id_attribute_id, get_only_id=True)
        toir_url = cls._get_value(attributes, cls.toir_url_attribute_id)
        start_date = cls._get_value(attributes, cls.repair_start_date_attribute_id)
        finish_date = cls._get_value(attributes, cls.repair_finish_date_attribute_id)
        type_repair_id = cls._get_value(attributes, cls.type_repair_id_attribute_id,
                                        get_only_id=True)

        entity = entities.PlanRepair(
            self_id=self_id,
            host_id=host_id,
            toir_id=toir_id,
            repair_id=repair_id,
            toir_url=toir_url,
            start_date=start_date,
            finish_date=finish_date,
            type_repair_id=type_repair_id,
        )
        return entity

    @classmethod
    def get_create_request_body(cls, item: entities.PlanRepair) -> (dict, str):
        """
        Method to serialize instance PlanRepair to POST request payload
        :param item: the instance of PlanRepair that needs to be serialized
        :return: tuple like (payload, collection attribute id), with payload as a dict with structure as neosintez needs
        """
        collection_attribute_id = cls.plan_repair_collection_attribute_id
        create_request_body = {
            "Id": "00000000-0000-0000-0000-000000000000",
            "Name": "forvalidation",
            "Entity": {
                "Id": cls.plan_repair_collection_class_id,
                "Name": "forvalidation"
            },
            "Attributes": {attribute['Id']: attribute for attribute in cls.get_update_request_body(item)}
        }
        return create_request_body, collection_attribute_id

    @classmethod
    def get_update_request_body(cls, item: entities.PlanRepair) -> list:
        """
        Method to serialize instance PlanRepair into PUT request payload
        :param item: the instance of PlanRepair that needs to be serialized
        :return: payload as a dict with structure as neosintez needs
        """
        put_request_body = [
            {
                'Name': 'forvalidation',
                'Value': item.toir_id if item.toir_id else None,
                'Type': 2,
                'Id': cls.toir_id_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.start_date if item.start_date else None,
                'Type': 3,  # TODO: check type of attr in neosintez
                'Id': cls.repair_start_date_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.finish_date if item.finish_date else None,
                'Type': 3,  # TODO: check type of attr in neosintez
                'Id': cls.repair_finish_date_attribute_id
            },
            # TODO: get type_repair_id based on neosintez data, because item.type_repair_id is 1C system value
            # TODO: get repair_id based on neosintez data, because item.repair_id is 1C system value
            # {
            #     'Name': 'forvalidation',
            #     'Value': {'Id': item.departament_id, 'Name': 'forvalidation'} if item.departament_id else None,
            #     'Type': 6,
            #     'Id': self.departament_id_attribute_id
            # },
        ]
        return put_request_body
