class SetParentReference:

    def __init__(self, operation_object, repository):
        self._repository = repository
        self._operation_object = operation_object

    @staticmethod
    def _set_parent_for_entity(data_dict, repository):
        for entity in repository.list():
            entity.parent_object = data_dict.get(entity.parent_toir_id)

    def execute(self):
        data_dict = dict(map(lambda x: (x.toir_id, x), self._repository.list()))
        data_dict.update({self._operation_object.toir_id: self._operation_object})

        self._set_parent_for_entity(data_dict, self._repository)
