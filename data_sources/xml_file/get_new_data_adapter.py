import os
from typing import Sequence
import xml.etree.ElementTree as ElementTree
import xmltodict
from domain import entities
from .. import xml_file, serializers


class GetNewDataAdapter:
    XML_FILE = 'ВыгрузкаДанныхОР'
    # dict like {attribute_name: {toir_id: value}}
    REFERENCE_ATTRIBUTES_VALUES = {}

    def __init__(self, file_directory):
        self._file_directory = file_directory
        self._elements_all = None

    def _get_file_path(self, name):
        f_list = [f for f in os.listdir(path=self._file_directory) if name in f and '~' not in f]
        if f_list:
            f_date = [os.path.getctime(self._file_directory + f) for f in f_list]
            file_path = self._file_directory + f_list[f_date.index(max(f_date))]
        else:
            raise FileNotFoundError()
        return file_path

    @property
    def _elements(self) -> dict[str, list]:
        """
        :return: dict like {'parent toir id': [elements]}
        """
        if self._elements_all:
            return self._elements_all
        xml_iterator = ElementTree.iterparse(self._get_file_path(self.XML_FILE))
        elements_hash_table = {}
        for _, element in xml_iterator:
            if 'ДанныеОР_' in element.tag:
                parent = element.find('РеквизитыОР/ОбъектРемонта_Родитель').text
                if parent in elements_hash_table:
                    elements_hash_table[parent].append(element)
                else:
                    elements_hash_table[parent] = [element]

        return elements_hash_table

    def get_new_equipment(self, operation_object: entities.OperationObject) -> Sequence[entities.Equipment]:
        xml_elements = xml_file.GetElementsByParent(self._elements).execute(operation_object.toir_id, 'equipment')
        result = list()
        for element in xml_elements:
            item = serializers.EquipmentSerializer.init_from_xml(element)
            item.object_id = operation_object.object_id
            result.append(item)

            item.properties = self._get_extra_elements(element, 'Характеристики')
            item.fact_repairs = self._get_extra_elements(element, 'ИсторияРемонтов')
            item.plan_repairs = self._get_extra_elements(element, 'ПредстоящиеРемонты')
            item.failures = self._get_extra_elements(element, 'Отказы')
            item.parts = self._get_extra_elements(element, 'Запчасти')

            self._get_reference_attribute_value(item)
        return result

    def get_new_tech_position(self, operation_object: entities.OperationObject) -> Sequence[entities.TechPosition]:
        xml_elements = xml_file.GetElementsByParent(self._elements).execute(operation_object.toir_id, 'tech_position')
        result = list()
        for element in xml_elements:
            item = serializers.TechPositionSerializer.init_from_xml(element)
            item.object_id = operation_object.object_id
            result.append(item)

            item.properties = self._get_extra_elements(element, 'Характеристики')
            item.fact_repairs = self._get_extra_elements(element, 'ИсторияРемонтов')
            item.plan_repairs = self._get_extra_elements(element, 'ПредстоящиеРемонты')
            item.failures = self._get_extra_elements(element, 'Отказы')
            item.parts = self._get_extra_elements(element, 'Запчасти')

            self._get_reference_attribute_value(item)
        return result

    def get_new_object_repair_group(
            self,
            operation_object: entities.OperationObject) -> Sequence[entities.ObjectRepairGroup]:
        xml_elements = xml_file.GetElementsByParent(self._elements).execute(operation_object.toir_id,
                                                                            'object_repair_group')
        result = list()
        for element in xml_elements:
            item = serializers.ObjectRepairGroupSerializer.init_from_xml(element)
            item.object_id = operation_object.object_id
            result.append(item)

            self._get_reference_attribute_value(item)

        return result

    def _get_extra_elements(self, host_element, tag: str) -> list:
        serializers_objects = {
            'Характеристики': serializers.PropertySerializer.init_from_xml,
            'ИсторияРемонтов': serializers.FactRepairSerializer.init_from_xml,
            'ПредстоящиеРемонты': serializers.PlanRepairSerializer.init_from_xml,
            'Отказы': serializers.FailureSerializer.init_from_xml,
            'Запчасти': serializers.PartSerializer.init_from_xml,
        }
        data = host_element.find(tag)
        xml_elements = []
        element = None
        for child in data:
            if child.tag == 'ОР':
                element = ElementTree.Element(tag)
                xml_elements.append(element)
            # add child only if it has value
            if element is not None and child.text is not None:
                element.append(child)
        # do not serialize empty objects
        xml_elements = list(filter(lambda x: len(x) > 1, xml_elements))
        items = [serializers_objects.get(tag)(one) for one in xml_elements]
        for item in items:
            self._get_reference_attribute_value(item)
        return items

    def _get_reference_attribute_value(self, item):
        reference_attributes: list[entities.ReferenceAttribute] = list(
            filter(lambda x: isinstance(x, entities.ReferenceAttribute), item.__dict__.values()))

        # filter attributes where toir id is equal '00000000-0000-0000-0000-000000000000'
        reference_attributes = list(
            filter(lambda x: x.toir_id != '00000000-0000-0000-0000-000000000000', reference_attributes))
        for attribute in reference_attributes:
            attribute_name = attribute.name
            toir_id = attribute.toir_id
            # check whether value already exists
            ids = self.dimensions.get(attribute_name)
            value = ids.get(toir_id) if ids else None
            if value:
                attribute.value = value

    @property
    def dimensions(self):
        if self.REFERENCE_ATTRIBUTES_VALUES:
            return self.REFERENCE_ATTRIBUTES_VALUES

        for table, config in serializers.Serializer.dimension_files.items():
            data = self._get_raw_data(config['file'])
            data_dict = dict(map(lambda x: (x[config['toir_id']], x[config['value']]), data))
            self.REFERENCE_ATTRIBUTES_VALUES[table] = data_dict
        return self.REFERENCE_ATTRIBUTES_VALUES

    def _get_raw_data(self, table_name) -> list[dict]:
        with open(self._get_file_path(table_name), encoding='UTF-8') as fd:
            doc = xmltodict.parse(fd.read())

        headers = []
        for column in doc['ValueTable']['column']:
            headers.append(column['Title'])

        rows = []
        for row in doc['ValueTable']['row']:
            values = []
            for value in row['Value']:
                value_text = value['#text'] if value['@xsi:type'] != 'Null' else None
                values.append(value_text)
            rows.append(values)

        return list(map(lambda x: dict(zip(headers, x)), rows))
