class GetEntitiesForDelete:

    def __init__(self, current_entities_repository, delete_entities_repository):
        self._current_entities_repository = current_entities_repository
        self._delete_entities_repository = delete_entities_repository

    def execute(self):
        current_entities = self._current_entities_repository.list()
        entities_for_delete = list(filter(lambda x: x.update_status == 'empty', current_entities))
        self._delete_entities_repository.add(entities_for_delete)
