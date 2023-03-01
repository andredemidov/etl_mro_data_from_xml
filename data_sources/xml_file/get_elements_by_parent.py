from typing import Sequence


class GetElementsByParent:

    def __init__(self, elements: dict[str, list]):
        self._result = list()
        self._elements = elements

    @staticmethod
    def _check_equipment(element) -> bool:
        group_flag = element.find('РеквизитыОР/ЭтоГруппа').text == 'true'
        tech_position_flag = element.find('РеквизитыОР/Группа').text == 'Технологическая позиция'
        return not group_flag and not tech_position_flag

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
        childs = self._elements.get(parent_id)
        if childs:
            for child in childs:
                toir_id = child.find('РеквизитыОР/ОбъектРемонта').text
                if function(child):
                    self._result.append(child)
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
        self._result = []
        self.get_elements_by_parent(parent_toir_id, function)
        return self._result
