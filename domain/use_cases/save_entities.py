
class SaveEntities:

    def __init__(self, adapter, repository):
        self._adapter = adapter
        self._repository = repository

    def execute(self) -> dict:
        statistic = {'success': 0, 'error': 0}
        actions = {
            'updated': self._adapter.update,
            'new': self._adapter.create,
        }
        entities = self._repository.list()
        for entity in entities:
            action = actions.get(entity.update_status)
            if action:
                status = action(entity)
                statistic[status] += 1
            if entity.replaced:
                self._adapter.replace(entity)
        return statistic
