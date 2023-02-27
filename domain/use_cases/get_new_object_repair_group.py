from domain.entities import OperationObject


class GetNewObjectRepairGroup:

    def __init__(self, adapter, repository, operation_object: OperationObject):
        self._adapter = adapter
        self._repository = repository
        self._operation_object = operation_object

    def execute(self):
        object_repair_groups = self._adapter.get_new_object_repair_group(self._operation_object)
        self._repository.add(object_repair_groups)
