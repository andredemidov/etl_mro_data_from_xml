from domain import entities


class MatchNewAndCurrentEntities:

    def __init__(
            self,
            new_entities_repository,
            current_entities_repository,
    ):
        self._new_entities_repository = new_entities_repository
        self._current_entities_repository = current_entities_repository

    def execute(self):
        new_entities = self._new_entities_repository.get()
        current_entities_dict = {entity.toir_id: entity for entity in self._current_entities_repository.get()}

        for new_entity in new_entities:
            self._check_update_replace_status(new_entity, current_entities_dict)

        # if the current one still has status 'empty' it means that there is no match with
        # any new one, and it has to be deleted
        # add such an entities to the new entities repository
        entities_for_delete = list(filter(lambda x: x.update_status == 'empty', self._current_entities_repository.get()))
        self._new_entities_repository.add(entities_for_delete)

    @classmethod
    def _check_update_replace_status(
            cls,
            new_entity: (entities.Equipment, entities.TechPosition, entities.ObjectRepairGroup),
            current_entities_dict: dict[str, (entities.Equipment, entities.TechPosition, entities.ObjectRepairGroup)],
    ):
        current_entity = current_entities_dict.get(new_entity.toir_id)
        # check if the current one and the new one have the same class
        # if the class is not the same skip the current one and set status 'new' for the new one
        if current_entity and isinstance(current_entity, type(new_entity)):
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

        # nested objects
        cls._check_update_status_for_nested_objects(new_entity, current_entity)

    @staticmethod
    def _check_update_status_for_nested_objects(new_entity, current_entity):
        if current_entity:
            for i in range(len(new_entity.get_nested_objects())):
                current = current_entity.get_nested_objects()[i]
                current_dict = {nested_object.unique_id: nested_object for nested_object in current}
                nested_objects_in_new = new_entity.get_nested_objects()[i]
                for new_object in nested_objects_in_new:
                    current_object = current_dict.get(new_object.unique_id)
                    if current_object:
                        new_object.self_id = current_object.self_id
                        new_object.host_id = current_object.host_id
                        # update status
                        if new_object.to_compare_dict() != current_object.to_compare_dict():
                            new_object.update_status = 'updated'
                            current_object.update_status = 'updated'
                        else:
                            new_object.update_status = 'not updated'
                            current_object.update_status = 'not updated'
                    else:
                        new_object.update_status = 'new'

                # if the current one still has status 'empty' it means that there is no match with
                # any new one, and it has to be deleted
                # add such an entities to the nested objects list with status 'empty'
                nested_for_delete = list(filter(lambda x: x.update_status == 'empty', current))
                nested_objects_in_new.extend(nested_for_delete)
        else:
            for i in range(len(new_entity.get_nested_objects())):
                for new_object in new_entity.get_nested_objects()[i]:
                    new_object.update_status = 'new'
