from domain.entities import OperationObject


class GetCurrentTechPosition:

    def __init__(self, adapter, repository):
        self._adapter = adapter
        self._repository = repository

    def execute(self, operation_object: OperationObject):
        tech_position = self._adapter.get_current_tech_position(operation_object)
        self._repository.add(tech_position)
