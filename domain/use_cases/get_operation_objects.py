class GetOperationObjects:

    def __init__(self, adapter, repository):
        self._adapter = adapter
        self._repository = repository

    def execute(self):
        operation_objects = self._adapter.get_operation_objects()
        self._repository.add(operation_objects)
