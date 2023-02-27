from typing import Sequence
import xml.etree.ElementTree as ElementTree
from domain.entities import OperationObject

from data_sources.xml_file.get_new_equipment_adapter import GetNewEquipmentAdapter
from data_sources.xml_file.get_new_tech_position_adapter import GetNewTechPositionAdapter
from data_sources.xml_file.get_new_object_repair_group_adapter import GetNewObjectRepairGroupAdapter


class GetNewDataAdapter:

    def __init__(self, file_path):
        self._file_path = file_path
        self._elements = self._get_all_elements(file_path)

    @staticmethod
    def _get_all_elements(file_path):
        xml_iterator = ElementTree.iterparse(file_path)
        result = list()
        for _, element in xml_iterator:
            if 'ДанныеОР_' in element.tag:
                result.append(element)
        return result

    def get_new_equipment(self, operation_object: OperationObject) -> Sequence:
        return GetNewEquipmentAdapter(self._elements).execute(
            operation_object.toir_id,
            'equipment'
        )

    def get_new_tech_position(self, operation_object: OperationObject) -> Sequence:
        return GetNewTechPositionAdapter(self._elements).execute(
            operation_object.toir_id,
            'tech_position'
        )

    def get_new_object_repair_group(self, operation_object: OperationObject) -> Sequence:
        return GetNewObjectRepairGroupAdapter(self._elements).execute(
            operation_object.toir_id,
            'object_repair_group'
        )
