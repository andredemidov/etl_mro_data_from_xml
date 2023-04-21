class SetParentReference:

    def __init__(self, repository, operation_object=None):
        self._repository = repository
        self._operation_object = operation_object

    @staticmethod
    def _set_parent_for_entity(data_dict, repository):
        for entity in repository.get():
            entity.parent_object = data_dict.get(entity.parent_toir_id)

    def execute(self):
        data_dict = dict(map(lambda x: (x.toir_id, x), self._repository.get()))
        if self._operation_object:
            data_dict.update({self._operation_object.toir_id: self._operation_object})

        self._set_parent_for_entity(data_dict, self._repository)
