class DeleteEntities:

    def __init__(self, adapter, repository):
        self._adapter = adapter
        self._repository = repository

    def execute(self):
        entities = self._repository.list()
        for entity in entities:
            self._adapter.delete(entity)
