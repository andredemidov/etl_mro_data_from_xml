from domain.entities import Equipment, TechPosition, ObjectRepairGroup


class SaveEntities:

    def __init__(self, adapter, repository):
        self._adapter = adapter
        self._repository = repository

    @staticmethod
    def _pass_action(entity):
        pass

    def _operate_entity(self, entity: (Equipment, TechPosition, ObjectRepairGroup)):
        actions = {
            'updated': self._adapter.update,
            'new': self._adapter.create,
            'replaced': self._adapter.replace,
        }
        actions.get(entity.update_status, self._pass_action)(entity)
        if entity.replaced:
            self._adapter.replace(entity)

    def execute(self):
        entities = self._repository.list()
        for entity in entities:
            self._operate_entity(entity)
