from domain.entities import Equipment, TechPosition, ObjectRepairGroup


class MapNewAndCurrentEntities:

    def __init__(
            self,
            new_entities_repository,
            current_entities_repository,
    ):
        self._new_entities_repository = new_entities_repository
        self._current_entities_repository = current_entities_repository

    def execute(self):
        new_entities = self._new_entities_repository.list()
        current_entities_dict = {entity.toir_id: entity for entity in self._current_entities_repository.list()}

        for new_entity in new_entities:
            self._set_update_replace_status(new_entity, current_entities_dict)

        entities_for_delete = list(filter(lambda x: x.update_status == 'empty', self._current_entities_repository.list()))
        self._new_entities_repository.add(entities_for_delete)

    @staticmethod
    def _set_update_replace_status(
            new_entity: (Equipment, TechPosition, ObjectRepairGroup),
            current_entities_dict: dict[str, (Equipment, TechPosition, ObjectRepairGroup)],
    ):
        current_entity = current_entities_dict.get(new_entity.toir_id)
        if current_entity:
            new_entity.self_id = current_entity.self_id
            # replaced
            if new_entity.parent_toir_id != current_entity.parent_toir_id:
                new_entity.replaced = True
            # update status
            if new_entity.to_compare_dict() != current_entity.to_compare_dict():
                new_entity.update_status = 'updated'
                current_entity.update_status = 'updated'
            else:
                new_entity.update_status = 'not updated'
                current_entity.update_status = 'not updated'
        else:
            new_entity.update_status = 'new'
