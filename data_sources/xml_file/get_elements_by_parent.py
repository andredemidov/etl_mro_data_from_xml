from typing import Sequence


class GetElementsByParent:

    def __init__(self, elements: list):
        self._result = list()
        self._elements = elements

    @staticmethod
    def _check_equipment(element) -> bool:
        group_flag = element.find('РеквизитыОР/ЭтоГруппа').text == 'true'
        tech_position_flag = element.find('РеквизитыОР/Группа').text == 'Технологическая позиция'
        return group_flag or tech_position_flag

    @staticmethod
    def _check_tech_position(element) -> bool:
        group_flag = element.find('РеквизитыОР/ЭтоГруппа').text == 'true'
        tech_position_flag = element.find('РеквизитыОР/Группа').text == 'Технологическая позиция'
        return not group_flag and tech_position_flag

    @staticmethod
    def _check_object_repair_group(element) -> bool:
        group_flag = element.find('РеквизитыОР/ЭтоГруппа').text == 'true'
        return group_flag

    def get_elements_by_parent(self, parent_id, function):
        for element in self._elements:
            if 'ДанныеОР_' in element.tag:
                parent = element.find('РеквизитыОР/ОбъектРемонта_Родитель').text

                if parent == parent_id and function(element):
                    self._result.append(element)
                    toir_id = element.find('РеквизитыОР/ОбъектРемонта').text
                    self.get_elements_by_parent(toir_id, function)

    def execute(self, parent_toir_id: str, class_name: str) -> Sequence:
        check_functions = {
            'equipment': self._check_equipment,
            'tech_position': self._check_tech_position,
            'object_repair_group': self._check_object_repair_group,
        }
        function = check_functions.get(class_name)
        if function is None:
            message = f'There is no function for class name {class_name}'
            raise KeyError(message)
        self.get_elements_by_parent(parent_toir_id, function)
        return self._result
