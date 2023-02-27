from domain.entities import OperationObject


class GetNewEquipment:

    def __init__(self, adapter, repository, operation_object: OperationObject):
        self._adapter = adapter
        self._repository = repository
        self._operation_object = operation_object

    def execute(self):
        equipment = self._adapter.get_new_equipment(self._operation_object)
        self._repository.add(equipment)
