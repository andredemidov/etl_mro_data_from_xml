from domain.entities import OperationObject


class GetNewTechPosition:

    def __init__(self, adapter, repository, operation_object: OperationObject):
        self._adapter = adapter
        self._repository = repository
        self._operation_object = operation_object

    def execute(self):
        tech_position = self._adapter.get_new_tech_position(self._operation_object)
        self._repository.add(tech_position)
