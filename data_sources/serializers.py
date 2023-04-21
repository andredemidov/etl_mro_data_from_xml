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
    category_attribute_id = '8b64419b-f3df-ed11-916a-005056b6948b'

    # collection classes
    failure_collection_class_id = 'e483b423-1131-e811-810f-edf0bf5e0091'
    part_collection_class_id = '96d11c5b-8e80-eb11-9113-005056b6948b'
    property_collection_class_id = 'f9ed1ca9-5349-e811-810f-edf0bf5e0091'
    fact_repair_collection_class_id = '4427f4a0-af5d-e811-810f-edf0bf5e0091'
    plan_repair_collection_class_id = '053cdbdb-3c33-e811-810f-edf0bf5e0091'

    # collection attributes
    failure_collection_attribute_id = '909f260f-6333-e811-810f-edf0bf5e0091'
    part_collection_attribute_id = '86faae6e-5747-ec11-9117-005056b6948b'
    property_collection_attribute_id = '170c062a-5c49-e811-810f-edf0bf5e0091'
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

    dim_departament_class_id = '5f50ea6b-5627-e811-810c-9ec54093bb77'
    dim_category_class_id = '6285225b-5727-e811-810c-9ec54093bb77'
    dim_type_failure_class_id = '5f50ea6b-5627-e811-810c-9ec54093bb77'
    dim_type_repair_class_id = '5f50ea6b-5627-e811-810c-9ec54093bb77'
    dim_property_class_id = '70806174-2633-e811-810f-edf0bf5e0091'
    dim_typical_object_class_id = 'b4b245dc-34e1-ea11-9110-005056b6948b'
    dim_type_reason_failure_class_id = '5f50ea6b-5627-e811-810c-9ec54093bb77'

    dimensions = {
        'dim_departament': {
            'tag': 'ПодразделениеВладелец',
            'file': 'ТаблицаПодразделений',
            'toir_id_header': 'МВЗ',
            'name_header': 'МВЗ_Наименование',
            'parent_toir_id_header': 'МВЗ_Родитель',
            'attribute_id': departament_id_attribute_id,
            'class_id': dim_departament_class_id,
            'folder_id': 'f558614f-e430-e811-810f-edf0bf5e0091',
        },
        'dim_type_failure': {
            'tag': 'ВидОтказа',
            'file': 'ТаблицаВидыОтказа',
            'toir_id_header': 'ВидОтказа',
            'name_header': 'ВидОтказа_Наименование',
            'parent_toir_id_header': 'ВидОтказа_Родитель',
            'attribute_id': type_failure_attribute_id,
            'class_id': dim_type_failure_class_id,
            'folder_id': '512847aa-f730-e811-810f-edf0bf5e0091',
        },
        'dim_type_repair': {
            'tag': 'ВидРемонта',
            'file': 'ТаблицаВидыРемонтов',
            'toir_id_header': 'ВидРемонта',
            'name_header': 'ВидРемонта_Наименование',
            'parent_toir_id_header': 'ВидРемонта_Родитель',
            'attribute_id': type_repair_attribute_id,
            'class_id': dim_type_repair_class_id,
            'folder_id': '0d84ecc4-f730-e811-810f-edf0bf5e0091',
        },
        'dim_property': {
            'tag': 'Характеристика',
            'file': 'ТаблицаХарактеристики',
            'toir_id_header': 'Характеристика',
            'name_header': 'Характеристика_Наименование',
            'parent_toir_id_header': '',
            'attribute_id': property_attribute_id,
            'class_id': dim_property_class_id,
            'folder_id': '69c6f051-2633-e811-810f-edf0bf5e0091',
        },
        'dim_typical_object': {
            'tag': 'ТиповойОР',
            'file': 'ТаблицаТОР',
            'toir_id_header': 'ТиповойОР',
            'name_header': 'ТиповойОР_Наименование',
            'parent_toir_id_header': 'ТиповойОР_Родитель',
            'attribute_id': typical_object_attribute_id,
            'class_id': dim_typical_object_class_id,
            'folder_id': '6c0e01c4-d025-e811-810c-9ec54093bb77',
        },
        'dim_type_reason_failure': {
            'tag': 'ПричинаОтказа',
            'file': 'ТаблицаПричиныОтказа',
            'toir_id_header': 'ПричинаОтказа',
            'name_header': 'ПричинаОтказа_Наименование',
            'parent_toir_id_header': 'ПричинаОтказа_Родитель',
            'attribute_id': type_reason_failure_attribute_id,
            'class_id': dim_type_reason_failure_class_id,
            'folder_id': 'ebb409d7-f730-e811-810f-edf0bf5e0091',
        },
    }

    @staticmethod
    def _get_value(attributes: dict, attribute_id: str, attribute_type='str', get_only_id=False):
        result = attributes.get(attribute_id, None)
        if result:
            item_type = result['Type']
            if item_type == 8 and get_only_id:
                return attributes[attribute_id]['Value']['Id']
            elif item_type == 8:
                value = attributes[attribute_id]['Value']['Name']
                return value.strip() if value else value
            # elif item_type == 3:
            #     value = attributes[attribute_id]['Value']
            #     return datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')
            elif item_type == 1:
                return round(attributes[attribute_id]['Value'], 4)
            else:
                value = attributes[attribute_id]['Value']
                return value.strip() if value else value
        else:
            if attribute_type == 'num':
                return 0
            else:
                return None

    @staticmethod
    def _get_value_from_xml(element, tag):
        value = element.find(tag).text if element.find(tag) is not None else None
        if value and value.strip() and value.strip() != '00000000-0000-0000-0000-000000000000':
            return value.strip()
        else:
            return None


class OperationObjectSerializer(Serializer):

    class_id = Serializer.operation_object_class_id
    object_type = ''

    def init_from_neosintez(self, item) -> entities.OperationObject:
        attributes = item['Object']['Attributes']
        name = item['Object']['Name']
        operation_object_id = item['Object']['Id']
        operation_object_toir_id = self._get_value(attributes, self.config_attribute_id)
        object_id = self._get_value(attributes, self.object_attribute_id, get_only_id=True)

        repair_object = entities.OperationObject(
            name=name,
            self_id=operation_object_id,
            toir_id=operation_object_toir_id,
            object_id=object_id,
            object_type=self.object_type,
        )
        return repair_object


class DimensionSerializer(Serializer):

    class_id = ''
    folder_id = ''
    file = ''
    toir_id_header = ''
    parent_toir_id_header = ''
    name_header = ''
    object_type = ''

    def init_from_neosintez(self, item: dict) -> entities.Dimension:
        attributes = item['Object']['Attributes']
        self_id = item['Object']['Id']
        name = item['Object']['Name']
        toir_id = self._get_value(attributes, self.toir_id_attribute_id)
        entity = entities.Dimension(
            toir_id=toir_id,
            name=name,
            self_id=self_id,
            object_type=self.object_type,
        )
        return entity

    def init_from_dict(self, data: dict) -> entities.Dimension:
        entity = entities.Dimension(
            toir_id=data.get(self.toir_id_header),
            parent_toir_id=data.get(self.parent_toir_id_header),
            name=data.get(self.name_header),
            self_id=data.get('self_id'),
            object_type=self.object_type,
        )
        return entity

    def get_create_request_body(self, item: entities.Dimension) -> dict:
        create_request_body = {
            "Id": "00000000-0000-0000-0000-000000000000",
            "Name": item.name,
            "Entity": {
                "Id": self.class_id,
                "Name": "forvalidation"
            },
        }
        return create_request_body

    @classmethod
    def get_update_request_body(cls, item: entities.Dimension) -> list:
        put_request_body = [
            {
                'Name': 'forvalidation',
                'Value': item.toir_id,
                'Type': 2,
                'Id': cls.toir_id_attribute_id
            }
        ]
        return put_request_body


class ObjectRepairGroupSerializer(Serializer):

    class_id = Serializer.object_repair_group_class_id
    object_type = ''

    def init_from_xml(self, element) -> entities.ObjectRepairGroup:
        toir_id = self._get_value_from_xml(element, 'РеквизитыОР/ОбъектРемонта')
        level = int(self._get_value_from_xml(element, 'РеквизитыОР/УровеньГруппы'))
        parent = self._get_value_from_xml(element, 'РеквизитыОР/ОбъектРемонта_Родитель')
        name = self._get_value_from_xml(element, 'РеквизитыОР/ОбъектРемонтаНаименование')
        toir_url = self._get_value_from_xml(element, 'РеквизитыОР/СсылкаОР')
        departament_id = self._get_value_from_xml(element, 'РеквизитыОР/ПодразделениеВладелец')

        repair_object = entities.ObjectRepairGroup(
            toir_id=toir_id,
            object_type=self.object_type,
            level=level,
            parent_toir_id=parent,
            name=name,
            toir_url=toir_url,
            departament=entities.ReferenceAttribute(toir_id=departament_id, name='ПодразделениеВладелец',
                                                    attribute_id=self.departament_id_attribute_id),
        )
        return repair_object

    def init_from_neosintez(self, item: dict) -> entities.ObjectRepairGroup:
        attributes = item['Object']['Attributes']
        self_id = item['Object']['Id']

        toir_id = self._get_value(attributes, self.toir_id_attribute_id)
        level = int(self._get_value(attributes, self.level_attribute_id, attribute_type='num'))
        parent = self._get_value(attributes, self.parent_attribute_id)
        name = self._get_value(attributes, self.name_attribute_id)
        toir_url = self._get_value(attributes, self.toir_url_attribute_id)
        departament_name = self._get_value(attributes, self.departament_id_attribute_id)
        departament_id = self._get_value(attributes, self.departament_id_attribute_id, get_only_id=True)
        object_id = self._get_value(attributes, self.object_attribute_id, get_only_id=True)

        repair_object = entities.ObjectRepairGroup(
            toir_id=toir_id,
            object_type=self.object_type,
            level=level,
            parent_toir_id=parent,
            name=name,
            toir_url=toir_url,
            departament=entities.ReferenceAttribute(reference_name=departament_name, reference_id=departament_id,
                                                    attribute_id=self.departament_id_attribute_id),
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

    class_id = Serializer.tech_position_class_id
    object_type = ''

    def init_from_xml(self, element) -> entities.TechPosition:
        toir_id = self._get_value_from_xml(element, 'РеквизитыОР/ОбъектРемонта')
        level = int(self._get_value_from_xml(element, 'РеквизитыОР/УровеньГруппы'))
        parent = self._get_value_from_xml(element, 'РеквизитыОР/ОбъектРемонта_Родитель')
        name = self._get_value_from_xml(element, 'РеквизитыОР/ОбъектРемонтаНаименование')
        tech_number = self._get_value_from_xml(element, 'РеквизитыОР/ТехНомер')
        toir_url = self._get_value_from_xml(element, 'РеквизитыОР/СсылкаОР')
        departament_id = self._get_value_from_xml(element, 'РеквизитыОР/ПодразделениеВладелец')

        repair_object = entities.TechPosition(
            toir_id=toir_id,
            object_type=self.object_type,
            level=level,
            parent_toir_id=parent,
            name=name,
            tech_number=tech_number,
            toir_url=toir_url,
            departament=entities.ReferenceAttribute(toir_id=departament_id, name='ПодразделениеВладелец',
                                                    attribute_id=self.departament_id_attribute_id),
        )
        return repair_object

    def init_from_neosintez(self, item: dict) -> entities.TechPosition:
        attributes = item['Object']['Attributes']
        self_id = item['Object']['Id']

        toir_id = self._get_value(attributes, self.toir_id_attribute_id)
        level = int(self._get_value(attributes, self.level_attribute_id, attribute_type='num'))
        parent = self._get_value(attributes, self.parent_attribute_id)
        name = self._get_value(attributes, self.name_attribute_id)
        tech_number = self._get_value(attributes, self.tech_number_attribute_id)
        toir_url = self._get_value(attributes, self.toir_url_attribute_id)
        departament_id = self._get_value(attributes, self.departament_id_attribute_id, get_only_id=True)
        departament_name = self._get_value(attributes, self.departament_id_attribute_id)
        object_id = self._get_value(attributes, self.object_attribute_id, get_only_id=True)

        repair_object = entities.TechPosition(
            toir_id=toir_id,
            object_type=self.object_type,
            level=level,
            parent_toir_id=parent,
            name=name,
            tech_number=tech_number,
            toir_url=toir_url,
            departament=entities.ReferenceAttribute(reference_id=departament_id, reference_name=departament_name,
                                                    attribute_id=self.departament_id_attribute_id),
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

    class_id = Serializer.equipment_class_id
    object_type = ''

    def init_from_xml(self, element) -> entities.Equipment:
        toir_id = self._get_value_from_xml(element, 'РеквизитыОР/ОбъектРемонта')
        level = int(self._get_value_from_xml(element, 'РеквизитыОР/УровеньГруппы'))
        parent = self._get_value_from_xml(element, 'РеквизитыОР/ОбъектРемонта_Родитель')
        name = self._get_value_from_xml(element, 'РеквизитыОР/ОбъектРемонтаНаименование')
        tech_number = self._get_value_from_xml(element, 'РеквизитыОР/ТехНомер')
        toir_url = self._get_value_from_xml(element, 'РеквизитыОР/СсылкаОР')
        registration_number = self._get_value_from_xml(element, 'РеквизитыОР/РегистрационныйНомер')
        commodity_producer = self._get_value_from_xml(element, 'РеквизитыОР/Изготовитель')
        commodity_number = self._get_value_from_xml(element, 'РеквизитыОР/ЗаводскойНомер')
        category = self._get_value_from_xml(element, 'РеквизитыОР/КатегорияОборудования')
        operation_date = self._get_value_from_xml(element, 'РеквизитыОР/ДатаВводаВЭксплуатацию')
        departament_id = self._get_value_from_xml(element, 'РеквизитыОР/ПодразделениеВладелец')
        typical_object = self._get_value_from_xml(element, 'РеквизитыОР/ТиповойОР')
        operating = self._get_value_from_xml(element, 'Наработка/Значение')

        if operation_date:
            operation_date = datetime.strptime(operation_date, '%Y-%m-%dT%H:%M:%S')

        repair_object = entities.Equipment(
            toir_id=toir_id,
            object_type=self.object_type,
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
                                                    attribute_id=self.departament_id_attribute_id),
            typical_object=entities.ReferenceAttribute(toir_id=typical_object, name='ТиповойОР',
                                                       attribute_id=self.typical_object_attribute_id),
            category=category,
        )
        return repair_object

    def init_from_neosintez(self, item: dict) -> entities.Equipment:
        attributes = item['Object']['Attributes']
        self_id = item['Object']['Id']

        toir_id = self._get_value(attributes, self.toir_id_attribute_id)
        level = int(self._get_value(attributes, self.level_attribute_id, attribute_type='num'))
        parent = self._get_value(attributes, self.parent_attribute_id)
        name = self._get_value(attributes, self.name_attribute_id)
        tech_number = self._get_value(attributes, self.tech_number_attribute_id)
        toir_url = self._get_value(attributes, self.toir_url_attribute_id)
        operation_date = self._get_value(attributes, self.operation_date_attribute_id)
        registration_number = self._get_value(attributes, self.registration_number_attribute_id)
        commodity_producer = self._get_value(attributes, self.commodity_producer_attribute_id)
        commodity_number = self._get_value(attributes, self.commodity_number_attribute_id)
        departament_id = self._get_value(attributes, self.departament_id_attribute_id, get_only_id=True)
        departament_name = self._get_value(attributes, self.departament_id_attribute_id)
        object_type_id = self._get_value(attributes, self.typical_object_attribute_id, get_only_id=True)
        object_type_name = self._get_value(attributes, self.typical_object_attribute_id)
        operating = self._get_value(attributes, self.operating_attribute_id)
        category = self._get_value(attributes, self.category_attribute_id)
        object_id = self._get_value(attributes, self.object_attribute_id, get_only_id=True)

        repair_object = entities.Equipment(
            toir_id=toir_id,
            object_type=self.object_type,
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
                                                    attribute_id=self.departament_id_attribute_id),
            typical_object=entities.ReferenceAttribute(reference_name=object_type_name, reference_id=object_type_id,
                                                       attribute_id=self.typical_object_attribute_id),
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
                'Value': item.category,
                'Type': 2,
                'Id': cls.category_attribute_id
            },
        ]
        return put_request_body


class FailureSerializer(Serializer):

    class_id = Serializer.failure_collection_class_id
    collection_attribute_id = Serializer.failure_collection_attribute_id
    tag = 'Отказы'
    object_type = ''

    def init_from_xml(self, element) -> entities.Failure:
        toir_id = self._get_value_from_xml(element, 'ОР')
        type_failure_id = self._get_value_from_xml(element, 'ВидОтказа')
        type_reason_failure_id = self._get_value_from_xml(element, 'ПричинаОтказа')
        toir_url = self._get_value_from_xml(element, 'СсылкаРеестрОтказов')
        failure_date = self._get_value_from_xml(element, 'ДатаОтказа')
        failure_description = self._get_value_from_xml(element, 'Симптомы')

        entity = entities.Failure(
            toir_id=toir_id,
            object_type=self.object_type,
            type_failure=entities.ReferenceAttribute(toir_id=type_failure_id, name='ВидОтказа',
                                                     attribute_id=self.type_failure_attribute_id),
            type_reason_failure=entities.ReferenceAttribute(toir_id=type_reason_failure_id, name='ПричинаОтказа',
                                                            attribute_id=self.type_reason_failure_attribute_id),
            toir_url=toir_url,
            failure_date=failure_date,
            failure_description=failure_description,
        )
        return entity

    def init_from_neosintez(self, item: dict) -> entities.Failure:
        attributes = item['Object']['Attributes']
        self_id = item['Object']['Id']
        host_id = item['Object']['HostObjectId']

        toir_id = self._get_value(attributes, self.toir_id_attribute_id)
        failure_description = self._get_value(attributes, self.failure_description_attribute_id)
        failure_date = self._get_value(attributes, self.failure_date_attribute_id)
        toir_url = self._get_value(attributes, self.act_investigation_attribute_id)
        type_reason_failure_id = self._get_value(attributes,
                                                 self.type_reason_failure_attribute_id,
                                                 get_only_id=True)
        type_reason_failure_name = self._get_value(attributes, self.type_reason_failure_attribute_id)
        type_failure_id = self._get_value(attributes, self.type_failure_attribute_id, get_only_id=True)
        type_failure_name = self._get_value(attributes, self.type_failure_attribute_id)

        entity = entities.Failure(
            self_id=self_id,
            host_id=host_id,
            toir_id=toir_id,
            object_type=self.object_type,
            type_failure=entities.ReferenceAttribute(reference_name=type_failure_name, reference_id=type_failure_id,
                                                     attribute_id=self.type_failure_attribute_id),
            type_reason_failure=entities.ReferenceAttribute(reference_name=type_reason_failure_name,
                                                            reference_id=type_reason_failure_id,
                                                            attribute_id=self.type_reason_failure_attribute_id),
            toir_url=toir_url,
            failure_date=failure_date,
            failure_description=failure_description,
        )
        return entity

    @classmethod
    def get_create_request_body(cls, item: entities.Failure) -> dict:

        create_request_body = {
            "Id": "00000000-0000-0000-0000-000000000000",
            "Name": "forvalidation",
            "Entity": {
                "Id": cls.failure_collection_class_id,
                "Name": "forvalidation"
            },
            "Attributes": {attribute['Id']: attribute for attribute in cls.get_update_request_body(item)}
        }
        return create_request_body

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
                'Type': 3,
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

    class_id = Serializer.part_collection_class_id
    collection_attribute_id = Serializer.part_collection_attribute_id
    tag = 'Запчасти'
    object_type = ''

    def init_from_xml(self, element) -> entities.Part:
        toir_id = self._get_value_from_xml(element, 'ОР')
        name = self._get_value_from_xml(element, 'НоменклатураНаименование')
        unit = self._get_value_from_xml(element, 'ЕдиницаИзмеренияНаименование')
        amount = self._get_value_from_xml(element, 'Количество')
        if amount:
            amount = float(amount)
        else:
            amount = 0
        code = self._get_value_from_xml(element, 'Код1СБухгалтерия')
        if code:
            # In file there are two options:
            # 1) values starting with 1 and consisting of 11 chars,
            # 2) values starting with 0, but ending with space and consisting of 11 chars.
            # The correct code must consists of 10 chars without spaces
            code = code.strip()
            code = code[1:] if len(code) == 11 else code
        type_repair_id = self._get_value_from_xml(element, 'ВидРемонта')

        entity = entities.Part(
            toir_id=toir_id,
            object_type=self.object_type,
            name=name,
            unit=unit,
            amount=amount,
            code=code,
            type_repair=entities.ReferenceAttribute(toir_id=type_repair_id, name='ВидРемонта',
                                                    attribute_id=self.type_repair_attribute_id),
        )
        return entity

    def init_from_neosintez(self, item: dict) -> entities.Part:
        attributes = item['Object']['Attributes']
        self_id = item['Object']['Id']
        host_id = item['Object']['HostObjectId']

        toir_id = self._get_value(attributes, self.toir_id_attribute_id)
        name = self._get_value(attributes, self.part_name_attribute_id)
        unit = self._get_value(attributes, self.unit_attribute_id)
        amount = self._get_value(attributes, self.amount_attribute_id, attribute_type='num')
        code = self._get_value(attributes, self.code_attribute_id)
        type_repair_id = self._get_value(attributes, self.type_repair_attribute_id, get_only_id=True)
        type_repair_name = self._get_value(attributes, self.type_repair_attribute_id)

        entity = entities.Part(
            self_id=self_id,
            host_id=host_id,
            toir_id=toir_id,
            object_type=self.object_type,
            name=name,
            unit=unit,
            amount=amount,
            code=code,
            type_repair=entities.ReferenceAttribute(reference_name=type_repair_name, reference_id=type_repair_id,
                                                    attribute_id=self.type_repair_attribute_id),
        )
        return entity

    @classmethod
    def get_create_request_body(cls, item: entities.Part) -> dict:
        create_request_body = {
            "Id": "00000000-0000-0000-0000-000000000000",
            "Name": "forvalidation",
            "Entity": {
                "Id": cls.part_collection_class_id,
                "Name": "forvalidation"
            },
            "Attributes": {attribute['Id']: attribute for attribute in cls.get_update_request_body(item)}
        }
        return create_request_body

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
                'Value': item.amount if item.amount else None,
                'Type': 1,
                'Id': cls.amount_attribute_id
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

    class_id = Serializer.property_collection_class_id
    collection_attribute_id = Serializer.property_collection_attribute_id
    tag = 'Характеристики'
    object_type = ''

    def init_from_xml(self, element) -> entities.Property:
        # within Property toir id is property's toir id
        toir_id = self._get_value_from_xml(element, 'Характеристика')
        property_id = self._get_value_from_xml(element, 'Характеристика')
        value = self._get_value_from_xml(element, 'Значение')

        entity = entities.Property(
            toir_id=toir_id,
            object_type=self.object_type,
            toir_property=entities.ReferenceAttribute(toir_id=property_id, name='Характеристика',
                                                      attribute_id=self.property_attribute_id),
            value=value,
        )
        return entity

    def init_from_neosintez(self, item: dict) -> entities.Property:
        attributes = item['Object']['Attributes']
        self_id = item['Object']['Id']
        host_id = item['Object']['HostObjectId']

        toir_id = self._get_value(attributes, self.toir_id_attribute_id)
        value = self._get_value(attributes, self.property_value_attribute_id)
        property_id = self._get_value(attributes, self.property_attribute_id, get_only_id=True)
        property_name = self._get_value(attributes, self.property_attribute_id)

        entity = entities.Property(
            self_id=self_id,
            host_id=host_id,
            toir_id=toir_id,
            object_type=self.object_type,
            toir_property=entities.ReferenceAttribute(reference_name=property_name, reference_id=property_id,
                                                      attribute_id=self.property_attribute_id),
            value=value,
        )
        return entity

    @classmethod
    def get_create_request_body(cls, item: entities.Property) -> dict:

        create_request_body = {
            "Id": "00000000-0000-0000-0000-000000000000",
            "Name": "forvalidation",
            "Entity": {
                "Id": cls.property_collection_class_id,
                "Name": "forvalidation"
            },
            "Attributes": {attribute['Id']: attribute for attribute in cls.get_update_request_body(item)}
        }
        return create_request_body

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

    class_id = Serializer.fact_repair_collection_class_id
    collection_attribute_id = Serializer.fact_repair_collection_attribute_id
    tag = 'ИсторияРемонтов'
    object_type = ''

    def init_from_xml(self, element) -> entities.FactRepair:
        toir_id = self._get_value_from_xml(element, 'ОР')
        repair_id = self._get_value_from_xml(element, 'ID_Ремонта')
        toir_url = self._get_value_from_xml(element, 'СсылкаАкт')
        fact_start_date = self._get_value_from_xml(element, 'ДатаНачалаФакт')
        fact_finish_date = self._get_value_from_xml(element, 'ДатаОкончанияФакт')
        type_repair_id = self._get_value_from_xml(element, 'ВидРемонта')
        operation = self._get_value_from_xml(element, 'Наработка')

        entity = entities.FactRepair(
            toir_id=toir_id,
            object_type=self.object_type,
            repair_id=repair_id,
            toir_url=toir_url,
            fact_start_date=fact_start_date,
            fact_finish_date=fact_finish_date,
            type_repair=entities.ReferenceAttribute(toir_id=type_repair_id, name='ВидРемонта',
                                                    attribute_id=self.type_repair_attribute_id),
            operating=operation,
        )
        return entity

    def init_from_neosintez(self, item: dict) -> entities.FactRepair:
        attributes = item['Object']['Attributes']
        self_id = item['Object']['Id']
        host_id = item['Object']['HostObjectId']

        toir_id = self._get_value(attributes, self.toir_id_attribute_id)
        repair_id = self._get_value(attributes, self.repair_id_attribute_id)
        toir_url = self._get_value(attributes, self.act_url_attribute_id)
        fact_start_date = self._get_value(attributes, self.repair_start_date_attribute_id)
        fact_finish_date = self._get_value(attributes, self.repair_finish_date_attribute_id)
        operating = self._get_value(attributes, self.operating_value_attribute_id)
        type_repair_id = self._get_value(attributes, self.type_repair_attribute_id, get_only_id=True)
        type_repair_name = self._get_value(attributes, self.type_repair_attribute_id)

        entity = entities.FactRepair(
            self_id=self_id,
            host_id=host_id,
            toir_id=toir_id,
            object_type=self.object_type,
            repair_id=repair_id,
            toir_url=toir_url,
            fact_start_date=fact_start_date,
            fact_finish_date=fact_finish_date,
            type_repair=entities.ReferenceAttribute(reference_id=type_repair_id, reference_name=type_repair_name,
                                                    attribute_id=self.type_repair_attribute_id),
            operating=operating,
        )
        return entity

    @classmethod
    def get_create_request_body(cls, item: entities.FactRepair) -> dict:
        create_request_body = {
            "Id": "00000000-0000-0000-0000-000000000000",
            "Name": "forvalidation",
            "Entity": {
                "Id": cls.fact_repair_collection_class_id,
                "Name": "forvalidation"
            },
            "Attributes": {attribute['Id']: attribute for attribute in cls.get_update_request_body(item)}
        }
        return create_request_body

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

    class_id = Serializer.plan_repair_collection_class_id
    collection_attribute_id = Serializer.plan_repair_collection_attribute_id
    tag = 'ПредстоящиеРемонты'
    object_type = ''

    def init_from_xml(self, element) -> entities.PlanRepair:
        toir_id = self._get_value_from_xml(element, 'ОР')
        repair_id = self._get_value_from_xml(element, 'ID_Ремонта')
        toir_url = self._get_value_from_xml(element, 'СсылкаППР')
        start_date = self._get_value_from_xml(element, 'ДатаНачала')
        finish_date = self._get_value_from_xml(element, 'ДатаОкончания')
        type_repair_id = self._get_value_from_xml(element, 'ВидРемонта')

        entity = entities.PlanRepair(
            toir_id=toir_id,
            object_type=self.object_type,
            repair_id=repair_id,
            toir_url=toir_url,
            start_date=start_date,
            finish_date=finish_date,
            type_repair=entities.ReferenceAttribute(toir_id=type_repair_id, name='ВидРемонта',
                                                    attribute_id=self.type_repair_attribute_id),
        )
        return entity

    def init_from_neosintez(self, item: dict) -> entities.PlanRepair:
        """
        Method to deserialize one object data from neosintez into PlanRepair instance
        :param item: one object data straight from neosintez API response as dict
        :return: PlanRepair instance
        """
        attributes = item['Object']['Attributes']
        self_id = item['Object']['Id']
        host_id = item['Object']['HostObjectId']

        toir_id = self._get_value(attributes, self.toir_id_attribute_id)
        repair_id = self._get_value(attributes, self.repair_id_attribute_id)
        toir_url = self._get_value(attributes, self.plan_url_attribute_id)
        start_date = self._get_value(attributes, self.repair_start_date_attribute_id)
        finish_date = self._get_value(attributes, self.repair_finish_date_attribute_id)
        type_repair_id = self._get_value(attributes, self.type_repair_attribute_id, get_only_id=True)
        type_repair_name = self._get_value(attributes, self.type_repair_attribute_id)

        entity = entities.PlanRepair(
            self_id=self_id,
            host_id=host_id,
            toir_id=toir_id,
            object_type=self.object_type,
            repair_id=repair_id,
            toir_url=toir_url,
            start_date=start_date,
            finish_date=finish_date,
            type_repair=entities.ReferenceAttribute(reference_name=type_repair_name, reference_id=type_repair_id,
                                                    attribute_id=self.type_repair_attribute_id),
        )
        return entity

    @classmethod
    def get_create_request_body(cls, item: entities.PlanRepair) -> dict:
        """
        Method to serialize instance PlanRepair to POST request payload
        :param item: the instance of PlanRepair that needs to be serialized
        :return: tuple like (payload, collection attribute id), with payload as a dict with structure as neosintez needs
        """

        create_request_body = {
            "Id": "00000000-0000-0000-0000-000000000000",
            "Name": "forvalidation",
            "Entity": {
                "Id": cls.plan_repair_collection_class_id,
                "Name": "forvalidation"
            },
            "Attributes": {attribute['Id']: attribute for attribute in cls.get_update_request_body(item)}
        }
        return create_request_body

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
            {
                'Name': 'forvalidation',
                'Value': item.repair_id,
                'Type': 2,
                'Id': cls.repair_id_attribute_id
            },
        ]
        return put_request_body


def get_serializer(type_object: str):
    """
    Фабрика для сериалайзера.
    :param type_object: тип объекта.
    :return: объект сериалайзера с соответствующим классом и атрибутами
    """
    retrievable_objects = {
        'operation_object': OperationObjectSerializer,
        'equipment': EquipmentSerializer,
        'tech_position': TechPositionSerializer,
        'object_repair_group': ObjectRepairGroupSerializer,
        'property': PropertySerializer,
        'plan_repair': PlanRepairSerializer,
        'fact_repair': FactRepairSerializer,
        'failure': FailureSerializer,
        'part': PartSerializer,
        'dim_departament': DimensionSerializer,
        'dim_type_failure': DimensionSerializer,
        'dim_type_repair': DimensionSerializer,
        'dim_property': DimensionSerializer,
        'dim_typical_object': DimensionSerializer,
        'dim_type_reason_failure': DimensionSerializer,
    }
    if type_object not in retrievable_objects:
        raise TypeError(f'{type_object} is not available')
    serializer = retrievable_objects.get(type_object)
    serializer = serializer()
    serializer.folder_id = None
    serializer.object_type = type_object
    if isinstance(serializer, DimensionSerializer):
        serializer.folder_id = serializer.dimensions.get(type_object)['folder_id']
        serializer.class_id = serializer.dimensions.get(type_object)['class_id']
        serializer.file = serializer.dimensions.get(type_object)['file']
        serializer.toir_id_header = serializer.dimensions.get(type_object)['toir_id_header']
        serializer.parent_toir_id_header = serializer.dimensions.get(type_object)['parent_toir_id_header']
        serializer.name_header = serializer.dimensions.get(type_object)['name_header']
        serializer.tag = serializer.dimensions.get(type_object)['tag']
    return serializer
