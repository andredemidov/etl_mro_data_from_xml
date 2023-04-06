from typing import Sequence
import xml.etree.ElementTree as ElementTree
from domain import entities
from .. import xml_file, serializers


class GetNewDataAdapter:

    def __init__(self, file_path):
        self._file_path = file_path
        self._elements = self._get_all_elements(file_path)

    @staticmethod
    def _get_all_elements(file_path) -> dict[str, list]:
        """
        :param file_path: path to xml file
        :return: dict like {'parent toir id': [elements]}
        """
        xml_iterator = ElementTree.iterparse(file_path)
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

        return result

    @staticmethod
    def _get_extra_elements(host_element, tag: str) -> list:
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
            if element:
                element.append(child)
        items = [serializers_objects.get(tag)(one) for one in xml_elements]
        return items
