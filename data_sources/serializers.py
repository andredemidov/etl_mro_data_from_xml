from datetime import datetime
from domain import entities


class Serializer:

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
    failure_collection_class_id = 'e483b423-1131-e811-810f-edf0bf5e0091'
    part_collection_class_id = '96d11c5b-8e80-eb11-9113-005056b6948b'
    property_collection_class_id = 'f9ed1ca9-5349-e811-810f-edf0bf5e0091'
    fact_repair_collection_class_id = '4427f4a0-af5d-e811-810f-edf0bf5e0091'
    plan_repair_collection_class_id = '053cdbdb-3c33-e811-810f-edf0bf5e0091'

    # collection attributes
    failure_collection_attribute_id = '909f260f-6333-e811-810f-edf0bf5e0091'
    part_collection_attribute_id = '86faae6e-5747-ec11-9117-005056b6948b'
    property_collection_attribute_id = '=170c062a-5c49-e811-810f-edf0bf5e0091'
    fact_repair_collection_attribute_id = '3b42cbc3-bd5d-e811-810f-edf0bf5e0091'
    plan_repair_collection_attribute_id = 'e56f151e-7641-e811-810f-edf0bf5e0091'

    # collection objects attributes
    failure_description_attribute_id = 'a22c722a-6233-e811-810f-edf0bf5e0091'  # - 2
    failure_date_attribute_id = 'b4b819ba-6133-e811-810f-edf0bf5e0091'  # - 3
    type_reason_failure_attribute_id = 'a882a0e6-6133-e811-810f-edf0bf5e0091'
    type_failure_attribute_id = '6c83117f-1131-e811-810f-edf0bf5e0091'
    act_investigation_attribute_id = '4b2812fe-ce64-e811-810f-edf0bf5e0091'

    unit_attribute_id = '21e9cd03-5207-e811-810c-9ec54093bb77'  # - 2
    amount_attribute_id = '1aa7531e-9080-eb11-9113-005056b6948b'
    code_attribute_id = '8182cfff-8f80-eb11-9113-005056b6948b'
    name_repair_attribute_id = ''
    type_repair_attribute_id = '2c93c947-3d33-e811-810f-edf0bf5e0091'
    part_name_attribute_id = '0830a7cd-8f80-eb11-9113-005056b6948b'

    property_value_attribute_id = 'c70cdba4-5c49-e811-810f-edf0bf5e0091'  # - 2
    property_attribute_id = '9c6a07e3-5b49-e811-810f-edf0bf5e0091'

    repair_id_attribute_id = '90b90a17-b4e3-ea11-9110-005056b6948b'
    repair_start_date_attribute_id = '9ba8c224-3d33-e811-810f-edf0bf5e0091'  # - 3
    repair_finish_date_attribute_id = '79b54cb4-3f33-e811-810f-edf0bf5e0091'
    plan_url_attribute_id = '3e004f4b-f264-e811-810f-edf0bf5e0091'
    act_url_attribute_id = '48d84614-f264-e811-810f-edf0bf5e0091'  # 6
    operating_value_attribute_id = '5dfd213a-4133-e811-810f-edf0bf5e0091'  # 2

    reference_attributes = {
        departament_id_attribute_id: {
            'folder_id': 'f558614f-e430-e811-810f-edf0bf5e0091',
            'class_id': '5f50ea6b-5627-e811-810c-9ec54093bb77',
            'key_attribute_id': '73e3c201-5527-e811-810c-9ec54093bb77'
        },
        category_attribute_id: {
            'folder_id': 'e0f6bda7-0829-e811-810d-c4afdb1aea70',
            'class_id': '6285225b-5727-e811-810c-9ec54093bb77',
            'key_attribute_id': '73e3c201-5527-e811-810c-9ec54093bb77'
        },
        type_failure_attribute_id: {
            'folder_id': '512847aa-f730-e811-810f-edf0bf5e0091',
            'class_id': '5f50ea6b-5627-e811-810c-9ec54093bb77',
            'key_attribute_id': '73e3c201-5527-e811-810c-9ec54093bb77'
        },
        unit_attribute_id: {
            'folder_id': '',
            'class_id': '',
            'key_attribute_id': ''
        },
        type_repair_attribute_id: {
            'folder_id': '0d84ecc4-f730-e811-810f-edf0bf5e0091',
            'class_id': '5f50ea6b-5627-e811-810c-9ec54093bb77',
            'key_attribute_id': '73e3c201-5527-e811-810c-9ec54093bb77'
        },
        property_attribute_id: {
            'folder_id': '69c6f051-2633-e811-810f-edf0bf5e0091',
            'class_id': '70806174-2633-e811-810f-edf0bf5e0091',
            'key_attribute_id': '73e3c201-5527-e811-810c-9ec54093bb77'
        },
        typical_object_attribute_id: {
            'folder_id': '6c0e01c4-d025-e811-810c-9ec54093bb77',
            'class_id': 'b4b245dc-34e1-ea11-9110-005056b6948b',
            'key_attribute_id': '73e3c201-5527-e811-810c-9ec54093bb77'
        },
        type_reason_failure_attribute_id: {
            'folder_id': 'ebb409d7-f730-e811-810f-edf0bf5e0091',
            'class_id': '5f50ea6b-5627-e811-810c-9ec54093bb77',
            'key_attribute_id': '73e3c201-5527-e811-810c-9ec54093bb77'
        }
    }
    dimension_files = {
        'ВидРемонта': {'file': 'ТаблицаВидыРемонтов', 'toir_id': 'ВидРемонта', 'value': 'ВидРемонта_Наименование'},
        # '':'ТаблицаПараметровНаработки',
        'ВидОтказа': {'file': 'ТаблицаВидыОтказа', 'toir_id': 'ВидОтказа', 'value': 'ВидОтказа_Наименование'},
        'ПодразделениеВладелец': {'file': 'ТаблицаПодразделений', 'toir_id': 'МВЗ', 'value': 'МВЗ_Наименование'},
        'ПричинаОтказа': {'file': 'ТаблицаПричиныОтказа',
                          'toir_id': 'ПричинаОтказа',
                          'value': 'ПричинаОтказа_Наименование'},
        'ТиповойОР': {'file': 'ТаблицаТОР', 'toir_id': 'ТиповойОР', 'value': 'ТиповойОР_Наименование'},
        'Характеристика': {'file': 'ТаблицаХарактеристики',
                           'toir_id': 'Характеристика',
                           'value': 'Характеристика_Наименование'},
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
            # elif item_type == 3:
            #     value = attributes[attribute_id]['Value']
            #     return datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')
            elif item_type == 1:
                return round(attributes[attribute_id]['Value'], 4)
            else:
                return attributes[attribute_id]['Value']
        else:
            if attribute_type == 'int':
                return 0
            else:
                return None

    @staticmethod
    def _get_value_from_xml(element, tag):
        return element.find(tag).text if element.find(tag) is not None else None


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

    @classmethod
    def init_from_xml(cls, element) -> entities.ObjectRepairGroup:
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
            departament=entities.ReferenceAttribute(toir_id=departament_id, name='ПодразделениеВладелец',
                                                    attribute_id=cls.departament_id_attribute_id),
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

    @classmethod
    def init_from_xml(cls, element) -> entities.TechPosition:
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
            departament=entities.ReferenceAttribute(toir_id=departament_id, name='ПодразделениеВладелец',
                                                    attribute_id=cls.departament_id_attribute_id),
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

    @classmethod
    def init_from_xml(cls, element) -> entities.Equipment:
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
            departament=entities.ReferenceAttribute(toir_id=departament_id, name='ПодразделениеВладелец',
                                                    attribute_id=cls.departament_id_attribute_id),
            typical_object=entities.ReferenceAttribute(toir_id=typical_object, name='ТиповойОР',
                                                       attribute_id=cls.typical_object_attribute_id),
            category=entities.ReferenceAttribute(value=category, name='КатегорияОборудования',
                                                 attribute_id=cls.category_attribute_id),
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

    @classmethod
    def init_from_xml(cls, element) -> entities.Failure:
        toir_id = cls._get_value_from_xml(element, 'ОР')
        type_failure_id = cls._get_value_from_xml(element, 'ВидОтказа')
        type_reason_failure_id = cls._get_value_from_xml(element, 'ПричинаОтказа')
        toir_url = cls._get_value_from_xml(element, 'СсылкаРеестрОтказов')
        # TODO: string date like 2020-01-14T23:10:00 to datetime
        failure_date = cls._get_value_from_xml(element, 'ДатаОтказа')
        failure_description = cls._get_value_from_xml(element, 'Симптомы')

        entity = entities.Failure(
            toir_id=toir_id,
            type_failure=entities.ReferenceAttribute(toir_id=type_failure_id, name='ВидОтказа',
                                                     attribute_id=cls.type_failure_attribute_id),
            type_reason_failure=entities.ReferenceAttribute(toir_id=type_reason_failure_id, name='ПричинаОтказа',
                                                            attribute_id=cls.type_reason_failure_attribute_id),
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
        toir_url = cls._get_value(attributes, cls.act_investigation_attribute_id)
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
                'Value': item.failure_description if item.failure_description else None,
                'Type': 2,
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
                'Id': cls.act_investigation_attribute_id
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

    @classmethod
    def init_from_xml(cls, element) -> entities.Part:
        toir_id = cls._get_value_from_xml(element, 'ОР')
        name = cls._get_value_from_xml(element, 'НоменклатураНаименование')
        unit = cls._get_value_from_xml(element, 'ЕдиницаИзмеренияНаименование')
        amount = cls._get_value_from_xml(element, 'Количество')
        code = cls._get_value_from_xml(element, 'Код1СБухгалтерия')
        if code:
            # In file there are two options:
            # 1) values starting with 1 and consisting of 11 chars,
            # 2) values starting with 0, but ending with space and consisting of 11 chars.
            # The correct code must consists of 10 chars without spaces
            code = code.strip()
            code = code[1:] if len(code) == 11 else code
        type_repair_id = cls._get_value_from_xml(element, 'ВидРемонта')

        entity = entities.Part(
            toir_id=toir_id,
            name=name,
            unit=unit,
            amount=amount,
            code=code,
            type_repair=entities.ReferenceAttribute(toir_id=type_repair_id, name='ВидРемонта',
                                                    attribute_id=cls.type_repair_attribute_id),
        )
        return entity

    @classmethod
    def init_from_neosintez(cls, item: dict) -> entities.Part:
        attributes = item['Object']['Attributes']
        self_id = item['Object']['Id']
        host_id = item['Object']['HostObjectId']

        toir_id = cls._get_value(attributes, cls.toir_id_attribute_id)
        name = cls._get_value(attributes, cls.part_name_attribute_id)
        unit = cls._get_value(attributes, cls.unit_attribute_id)
        amount = cls._get_value(attributes, cls.amount_attribute_id)
        code = cls._get_value(attributes, cls.code_attribute_id)
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
                'Value': item.name if item.name else None,
                'Type': 2,
                'Id': cls.part_name_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.unit if item.unit else None,
                'Type': 2,
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
                'Value': item.type_repair.request_value,
                'Type': 8,
                'Id': cls.type_repair_attribute_id
            },
        ]
        return put_request_body


class PropertySerializer(Serializer):

    @classmethod
    def init_from_xml(cls, element) -> entities.Property:
        toir_id = cls._get_value_from_xml(element, 'ОР')
        property_id = cls._get_value_from_xml(element, 'Характеристика')
        value = cls._get_value_from_xml(element, 'Значение')

        entity = entities.Property(
            toir_id=toir_id,
            toir_property=entities.ReferenceAttribute(toir_id=property_id, name='Характеристика',
                                                      attribute_id=cls.property_attribute_id),
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
                'Type': 2,
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

    @classmethod
    def init_from_xml(cls, element) -> entities.FactRepair:
        toir_id = cls._get_value_from_xml(element, 'ОР')
        repair_id = cls._get_value_from_xml(element, 'ID_Ремонта')
        toir_url = cls._get_value_from_xml(element, 'СсылкаАкт')
        fact_start_date = cls._get_value_from_xml(element, 'ДатаНачалаФакт')
        fact_finish_date = cls._get_value_from_xml(element, 'ДатаОкончанияФакт')
        type_repair_id = cls._get_value_from_xml(element, 'ВидРемонта')
        operation = cls._get_value_from_xml(element, 'Наработка')

        entity = entities.FactRepair(
            toir_id=toir_id,
            repair_id=repair_id,
            toir_url=toir_url,
            fact_start_date=fact_start_date,
            fact_finish_date=fact_finish_date,
            type_repair=entities.ReferenceAttribute(toir_id=type_repair_id, name='ВидРемонта',
                                                    attribute_id=cls.type_repair_attribute_id),
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
        toir_url = cls._get_value(attributes, cls.act_url_attribute_id)
        fact_start_date = cls._get_value(attributes, cls.repair_start_date_attribute_id)
        fact_finish_date = cls._get_value(attributes, cls.repair_finish_date_attribute_id)
        operating = cls._get_value(attributes, cls.operating_value_attribute_id)
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
                'Value': item.fact_start_date if item.fact_start_date else None,
                'Type': 3,
                'Id': cls.repair_start_date_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.fact_finish_date if item.fact_finish_date else None,
                'Type': 3,
                'Id': cls.repair_finish_date_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.operating if item.operating else None,
                'Type': 2,
                'Id': cls.operating_value_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.repair_id if item.repair_id else None,
                'Type': 2,
                'Id': cls.repair_id_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.type_repair.request_value,
                'Type': 8,
                'Id': cls.type_repair_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.toir_url,
                'Type': 6,
                'Id': cls.act_url_attribute_id
            },
        ]
        return put_request_body


class PlanRepairSerializer(Serializer):

    @classmethod
    def init_from_xml(cls, element) -> entities.PlanRepair:
        toir_id = cls._get_value_from_xml(element, 'ОР')
        repair_id = cls._get_value_from_xml(element, 'ID_Ремонта')
        toir_url = cls._get_value_from_xml(element, 'СсылкаППР')
        start_date = cls._get_value_from_xml(element, 'ДатаНачала')
        finish_date = cls._get_value_from_xml(element, 'ДатаОкончания')
        type_repair_id = cls._get_value_from_xml(element, 'ВидРемонта')

        entity = entities.PlanRepair(
            toir_id=toir_id,
            repair_id=repair_id,
            toir_url=toir_url,
            start_date=start_date,
            finish_date=finish_date,
            type_repair=entities.ReferenceAttribute(toir_id=type_repair_id, name='ВидРемонта',
                                                    attribute_id=cls.type_repair_attribute_id),
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
        toir_url = cls._get_value(attributes, cls.plan_url_attribute_id)
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
                'Value': item.start_date if item.start_date else None,
                'Type': 3,
                'Id': cls.repair_start_date_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.finish_date if item.finish_date else None,
                'Type': 3,
                'Id': cls.repair_finish_date_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.type_repair.request_value,
                'Type': 8,
                'Id': cls.type_repair_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.toir_url,
                'Type': 6,
                'Id': cls.plan_url_attribute_id
            },
        ]
        return put_request_body
