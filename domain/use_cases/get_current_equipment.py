from domain.entities import OperationObject


class GetCurrentEquipment:

    def __init__(self, adapter, repository):
        self._adapter = adapter
        self._repository = repository

    def execute(self, operation_object: OperationObject):
        equipments = self._adapter.get_current_equipment(operation_object)
        self._repository.add(equipments)
