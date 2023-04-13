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
    typical_object_attribute_id = '456b1f0f-0b29-e811-810d-c4afdb1aea70'
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
    type_reason_failure_attribute_id = ''
    type_failure_attribute_id = ''

    unit_attribute_id = ''
    amount_attribute_id = ''
    code_attribute_id = ''
    name_repair_attribute_id = ''
    type_repair_attribute_id = ''

    property_value_attribute_id = ''
    property_attribute_id = ''

    repair_id_attribute_id = ''
    repair_start_date_attribute_id = ''
    repair_finish_date_attribute_id = ''

    reference_attributes = {
        departament_id_attribute_id: {
            'folder_id': '',
            'class_id': '',
            # 'key_attribute_id': '73e3c201-5527-e811-810c-9ec54093bb77'
        },
        category_attribute_id: {
            'folder_id': '',
            'class_id': '',
            # 'key_attribute_id': '73e3c201-5527-e811-810c-9ec54093bb77'
        },
        type_failure_attribute_id: {
            'folder_id': '',
            'class_id': '',
            # 'key_attribute_id': '73e3c201-5527-e811-810c-9ec54093bb77'
        },
        unit_attribute_id: {
            'folder_id': '',
            'class_id': '',
            # 'key_attribute_id': '73e3c201-5527-e811-810c-9ec54093bb77'
        },
        type_repair_attribute_id: {
            'folder_id': '',
            'class_id': '',
            # 'key_attribute_id': '73e3c201-5527-e811-810c-9ec54093bb77'
        },
        property_attribute_id: {
            'folder_id': '',
            'class_id': '',
            # 'key_attribute_id': '73e3c201-5527-e811-810c-9ec54093bb77'
        },
    }
    dimension_files = {
        'ВидРемонта': {'file': 'ТаблицаВидыРемонтов', 'toir_id': 'ВидРемонта', 'value': 'ВидРемонта_Наименование'},
        # '':'ТаблицаПараметровНаработки',
        'ВидОтказа': {'file': 'ТаблицаВидыОтказа', 'toir_id': 'ВидОтказа', 'value': 'ВидОтказа_Наименование'},
        'ПодразделениеВладелец': {'file': 'ТаблицаПодразделений', 'toir_id': 'МВЗ', 'value': 'МВЗ_Наименование'},
        'ПричинаОтказа': {'file': 'ТаблицаПричиныОтказа', 'toir_id': 'ПричинаОтказа', 'value': 'ПричинаОтказа_Наименование'},
        'ТиповойОР': {'file': 'ТаблицаТОР', 'toir_id': 'ТиповойОР', 'value': 'ТиповойОР_Наименование'},
        'Характеристика': {'file': 'ТаблицаХарактеристики', 'toir_id': 'Характеристика', 'value': 'Характеристика_Наименование'},
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
            departament=entities.ReferenceAttribute(toir_id=departament_id, name='ПодразделениеВладелец'),
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
        departament_id = cls._get_value(attributes, cls.departament_id_attribute_id, get_only_id=True)
        object_id = cls._get_value(attributes, cls.object_attribute_id, get_only_id=True)

        repair_object = entities.ObjectRepairGroup(
            toir_id=toir_id,
            level=level,
            parent_toir_id=parent,
            name=name,
            toir_url=toir_url,
            departament=entities.ReferenceAttribute(reference_name=departament_name, reference_id=departament_id,
                                                    attribute_id=cls.departament_id_attribute_id),
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
            {
                'Name': 'forvalidation',
                'Value': item.departament.request_value,
                'Type': 8,
                'Id': cls.departament_id_attribute_id
            },
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
            departament=entities.ReferenceAttribute(toir_id=departament_id, name='ПодразделениеВладелец'),
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
        departament_id = cls._get_value(attributes, cls.departament_id_attribute_id, get_only_id=True)
        departament_name = cls._get_value(attributes, cls.departament_id_attribute_id)
        object_id = cls._get_value(attributes, cls.object_attribute_id, get_only_id=True)

        repair_object = entities.TechPosition(
            toir_id=toir_id,
            level=level,
            parent_toir_id=parent,
            name=name,
            tech_number=tech_number,
            toir_url=toir_url,
            departament=entities.ReferenceAttribute(reference_id=departament_id, reference_name=departament_name,
                                                    attribute_id=cls.departament_id_attribute_id),
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
            {
                'Name': 'forvalidation',
                'Value': item.departament.request_value,
                'Type': 8,
                'Id': cls.departament_id_attribute_id
            },
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
        typical_object = element.find('РеквизитыОР/ТиповойОР').text
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
            departament=entities.ReferenceAttribute(toir_id=departament_id, name='ПодразделениеВладелец'),
            typical_object=entities.ReferenceAttribute(toir_id=typical_object, name='ТиповойОР'),
            category=entities.ReferenceAttribute(value=category, name='КатегорияОборудования'),
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
        departament_id = cls._get_value(attributes, cls.departament_id_attribute_id, get_only_id=True)
        departament_name = cls._get_value(attributes, cls.departament_id_attribute_id)
        object_type_id = cls._get_value(attributes, cls.typical_object_attribute_id, get_only_id=True)
        object_type_name = cls._get_value(attributes, cls.typical_object_attribute_id)
        operating = cls._get_value(attributes, cls.operating_attribute_id)
        category_id = cls._get_value(attributes, cls.category_attribute_id, get_only_id=True)
        category_name = cls._get_value(attributes, cls.category_attribute_id)
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
            departament=entities.ReferenceAttribute(reference_name=departament_name, reference_id=departament_id,
                                                    attribute_id=cls.departament_id_attribute_id),
            typical_object=entities.ReferenceAttribute(reference_name=object_type_name, reference_id=object_type_id,
                                                       attribute_id=cls.typical_object_attribute_id),
            self_id=self_id,
            category=entities.ReferenceAttribute(reference_name=category_name, reference_id=category_id,
                                                 attribute_id=cls.category_attribute_id),
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
            {
                'Name': 'forvalidation',
                'Value': item.departament.request_value,
                'Type': 8,
                'Id': cls.departament_id_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.typical_object.request_value,
                'Type': 8,
                'Id': cls.typical_object_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.category.request_value,
                'Type': 8,
                'Id': cls.category_attribute_id
            },
        ]
        return put_request_body


class FailureSerializer(Serializer):

    @staticmethod
    def init_from_xml(element) -> entities.Failure:
        toir_id = element.find('ОР').text if element.find('ОР') else None
        type_failure_id = element.find('ВидОтказа').text if element.find('ВидОтказа') else None
        type_reason_failure_id = element.find('ПричинаОтказа').text if element.find('ПричинаОтказа') else None
        toir_url = element.find('СсылкаРеестрОтказов').text if element.find('СсылкаРеестрОтказов') else None
        # TODO: string date like 2020-01-14T23:10:00 to datetime
        failure_date = element.find('ДатаОтказа').text if element.find('ДатаОтказа') else None
        failure_description = element.find('Симптомы').text if element.find('Симптомы') else None

        entity = entities.Failure(
            toir_id=toir_id,
            type_failure=entities.ReferenceAttribute(toir_id=type_failure_id, name='ВидОтказа'),
            type_reason_failure=entities.ReferenceAttribute(toir_id=type_reason_failure_id, name='ПричинаОтказа'),
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
                                                cls.type_reason_failure_attribute_id,
                                                get_only_id=True)
        type_reason_failure_name = cls._get_value(attributes, cls.type_reason_failure_attribute_id)
        type_failure_id = cls._get_value(attributes, cls.type_failure_attribute_id, get_only_id=True)
        type_failure_name = cls._get_value(attributes, cls.type_failure_attribute_id)

        entity = entities.Failure(
            self_id=self_id,
            host_id=host_id,
            toir_id=toir_id,
            type_failure=entities.ReferenceAttribute(reference_name=type_failure_name, reference_id=type_failure_id,
                                                     attribute_id=cls.type_failure_attribute_id),
            type_reason_failure=entities.ReferenceAttribute(reference_name=type_reason_failure_name,
                                                            reference_id=type_reason_failure_id,
                                                            attribute_id=cls.type_reason_failure_attribute_id),
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
            {
                'Name': 'forvalidation',
                'Value': item.type_failure.request_value,
                'Type': 8,
                'Id': cls.type_failure_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.type_reason_failure.request_value,
                'Type': 8,
                'Id': cls.type_reason_failure_attribute_id
            },
        ]
        return put_request_body


class PartSerializer(Serializer):

    @staticmethod
    def init_from_xml(element) -> entities.Part:
        toir_id = element.find('ОР').text if element.find('ОР') else None
        name = element.find('НоменклатураНаименование').text if element.find('НоменклатураНаименование') else None
        unit = element.find('ЕдиницаИзмеренияНаименование').text if element.find('ЕдиницаИзмеренияНаименование') else None
        amount = element.find('Количество').text if element.find('Количество') else None
        code = element.find('Код1СБухгалтерия')
        if code:
            # In file there are two options:
            # 1) values starting with 1 and consisting of 11 chars,
            # 2) values starting with 0, but ending with space and consisting of 11 chars.
            # The correct code must consists of 10 chars without spaces
            code = code.text.strip()
            code = code[1:] if len(code) == 11 else code
        type_repair_id = element.find('ВидРемонта').text if element.find('ВидРемонта') else None
        name_repair = element.find('ВидРемонтаНаименование').text if element.find('ВидРемонтаНаименование') else None

        entity = entities.Part(
            toir_id=toir_id,
            name=name,
            unit=unit,
            amount=amount,
            code=code,
            type_repair=entities.ReferenceAttribute(toir_id=type_repair_id, name='ВидРемонта'),
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
        type_repair_id = cls._get_value(attributes, cls.type_repair_attribute_id, get_only_id=True)
        type_repair_name = cls._get_value(attributes, cls.type_repair_attribute_id)

        entity = entities.Part(
            self_id=self_id,
            host_id=host_id,
            toir_id=toir_id,
            name=name,
            unit=unit,
            amount=amount,
            code=code,
            type_repair=entities.ReferenceAttribute(reference_name=type_repair_name, reference_id=type_repair_id,
                                                    attribute_id=cls.type_repair_attribute_id),
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
            {
                'Name': 'forvalidation',
                'Value': item.type_repair.request_value,
                'Type': 8,
                'Id': cls.type_repair_attribute_id
            },
        ]
        return put_request_body


class PropertySerializer(Serializer):

    @staticmethod
    def init_from_xml(element) -> entities.Property:
        toir_id = element.find('ОР').text if element.find('ОР') else None
        property_id = element.find('Характеристика').text if element.find('Характеристика') else None
        value = element.find('Значение').text if element.find('Значение') else None

        entity = entities.Property(
            toir_id=toir_id,
            toir_property=entities.ReferenceAttribute(toir_id=property_id, name='Характеристика'),
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
        property_id = cls._get_value(attributes, cls.property_attribute_id, get_only_id=True)
        property_name = cls._get_value(attributes, cls.property_attribute_id)

        entity = entities.Property(
            self_id=self_id,
            host_id=host_id,
            toir_id=toir_id,
            toir_property=entities.ReferenceAttribute(reference_name=property_name, reference_id=property_id,
                                                      attribute_id=cls.property_attribute_id),
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
            {
                'Name': 'forvalidation',
                'Value': item.toir_property.request_value,
                'Type': 8,
                'Id': cls.property_attribute_id
            },
        ]
        return put_request_body


class FactRepairSerializer(Serializer):

    @staticmethod
    def init_from_xml(element) -> entities.FactRepair:
        toir_id = element.find('ОР').text if element.find('ОР') else None
        repair_id = element.find('ID_Ремонта').text if element.find('ID_Ремонта') else None
        toir_url = element.find('СсылкаАкт').text if element.find('СсылкаАкт') else None
        fact_start_date = element.find('ДатаНачалаФакт').text if element.find('ДатаНачалаФакт') else None
        fact_finish_date = element.find('ДатаОкончанияФакт').text if element.find('ДатаОкончанияФакт') else None
        type_repair_id = element.find('ВидРемонта').text if element.find('ВидРемонта') else None
        operation = element.find('Наработка').text if element.find('Наработка') else None

        entity = entities.FactRepair(
            toir_id=toir_id,
            repair_id=repair_id,
            toir_url=toir_url,
            fact_start_date=fact_start_date,
            fact_finish_date=fact_finish_date,
            type_repair=entities.ReferenceAttribute(toir_id=type_repair_id, name='ВидРемонта'),
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
        type_repair_id = cls._get_value(attributes, cls.type_repair_attribute_id, get_only_id=True)
        type_repair_name = cls._get_value(attributes, cls.type_repair_attribute_id)

        entity = entities.FactRepair(
            self_id=self_id,
            host_id=host_id,
            toir_id=toir_id,
            repair_id=repair_id,
            toir_url=toir_url,
            fact_start_date=fact_start_date,
            fact_finish_date=fact_finish_date,
            type_repair=entities.ReferenceAttribute(reference_id=type_repair_id, reference_name=type_repair_name,
                                                    attribute_id=cls.type_repair_attribute_id),
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
            {
                'Name': 'forvalidation',
                'Value': item.repair_id if item.repair_id else None,
                'Type': 2,
                'Id': cls.operating_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.type_repair.request_value,
                'Type': 8,
                'Id': cls.type_repair_attribute_id
            },
        ]
        return put_request_body


class PlanRepairSerializer(Serializer):

    @staticmethod
    def init_from_xml(element) -> entities.PlanRepair:
        toir_id = element.find('ОР').text if element.find('ОР') else None
        repair_id = element.find('ID_Ремонта').text if element.find('ID_Ремонта') else None
        toir_url = element.find('СсылкаППР').text if element.find('СсылкаППР') else None
        start_date = element.find('ДатаНачала').text if element.find('ДатаНачала') else None
        finish_date = element.find('ДатаОкончания').text if element.find('ДатаОкончания') else None
        type_repair_id = element.find('ВидРемонта').text if element.find('ВидРемонта') else None

        entity = entities.PlanRepair(
            toir_id=toir_id,
            repair_id=repair_id,
            toir_url=toir_url,
            start_date=start_date,
            finish_date=finish_date,
            type_repair=entities.ReferenceAttribute(toir_id=type_repair_id, name='ВидРемонта'),
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
        type_repair_id = cls._get_value(attributes, cls.type_repair_attribute_id, get_only_id=True)
        type_repair_name = cls._get_value(attributes, cls.type_repair_attribute_id)

        entity = entities.PlanRepair(
            self_id=self_id,
            host_id=host_id,
            toir_id=toir_id,
            repair_id=repair_id,
            toir_url=toir_url,
            start_date=start_date,
            finish_date=finish_date,
            type_repair=entities.ReferenceAttribute(reference_name=type_repair_name, reference_id=type_repair_id,
                                                    attribute_id=cls.type_repair_attribute_id),
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
            {
                'Name': 'forvalidation',
                'Value': item.type_repair.request_value,
                'Type': 8,
                'Id': cls.departament_id_attribute_id
            },
        ]
        return put_request_body
