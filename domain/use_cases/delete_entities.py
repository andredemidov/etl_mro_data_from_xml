class DeleteEntities:

    def __init__(self, adapter, repository):
        self._adapter = adapter
        self._repository = repository

    def execute(self) -> dict:
        statistic = {'success': 0, 'error': 0}
        entities_for_delete = list(filter(lambda x: x.update_status == 'empty', self._repository.list()))
        for entity in entities_for_delete:
            status = self._adapter.delete(entity)
            statistic[status] += 1
        return statistic
