from typing import Sequence

from .get_elements_by_parent import GetElementsByParent


class GetNewDataAdapterAbstract:

    def __init__(self, elements: list):
        self._elements = elements
        self._result_entities = list()

    def _init_entities(self, element):
        pass

    def execute(self, root_toir_id: str, class_name: str) -> Sequence:
        xml_elements = GetElementsByParent(self._elements).execute(root_toir_id, class_name)

        for element in xml_elements:
            self._init_entities(element)

        return self._result_entities
