from domain.entities import OperationObject


class GetCurrentObjectRepairGroup:

    def __init__(self, adapter, repository):
        self._adapter = adapter
        self._repository = repository

    def execute(self, operation_object: OperationObject):
        object_repair_groups = self._adapter.get_current_object_repair_group(operation_object)
        self._repository.add(object_repair_groups)
