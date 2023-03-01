from typing import Sequence
from datetime import datetime
import xml.etree.ElementTree as ElementTree
from domain import entities
from data_sources import xml_file


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

    def get_new_equipment(self, operation_object: entities.OperationObject) -> Sequence:
        xml_elements = xml_file.GetElementsByParent(self._elements).execute(operation_object.toir_id, 'equipment')
        result = list()
        for element in xml_elements:
            result.append(self._init_equipment(element))

        return result

    def get_new_tech_position(self, operation_object: entities.OperationObject) -> Sequence:
        xml_elements = xml_file.GetElementsByParent(self._elements).execute(operation_object.toir_id, 'tech_position')
        result = list()
        for element in xml_elements:
            result.append(self._init_tech_position(element))

        return result

    def get_new_object_repair_group(self, operation_object: entities.OperationObject) -> Sequence:
        xml_elements = xml_file.GetElementsByParent(self._elements).execute(operation_object.toir_id, 'object_repair_group')
        result = list()
        for element in xml_elements:
            result.append(self._init_object_repair_group(element))

        return result

    @staticmethod
    def _init_equipment(element):

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
            object_type_id=object_type_id,
            category=category,
        )
        return repair_object

    @staticmethod
    def _init_object_repair_group(element):
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

    @staticmethod
    def _init_tech_position(element):

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
