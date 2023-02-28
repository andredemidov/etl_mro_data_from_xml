class SetParentReference:

    def __init__(self, operation_object, object_repair_group_repository, tech_position_repository, equipment_repository):
        self._object_repair_group_repository = object_repair_group_repository
        self._tech_position_repository = tech_position_repository
        self._equipment_repository = equipment_repository
        self._operation_object = operation_object

    @staticmethod
    def _set_parent_for_entity(data_dict, repository):
        for entity in repository.list():
            entity.parent_object = data_dict.get(entity.parent_toir_id)

    def execute(self):
        data_dict = dict(map(lambda x: (x.toir_id, x), self._object_repair_group_repository.list()))
        data_dict.update(dict(map(lambda x: (x.toir_id, x), self._tech_position_repository.list())))
        data_dict.update(dict(map(lambda x: (x.toir_id, x), self._equipment_repository.list())))
        data_dict.update({self._operation_object.toir_id: self._operation_object})

        self._set_parent_for_entity(data_dict, self._object_repair_group_repository)
        self._set_parent_for_entity(data_dict, self._tech_position_repository)
        self._set_parent_for_entity(data_dict, self._equipment_repository)
