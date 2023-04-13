from domain import entities


class Repository:

    def __init__(self, entries: list = None):
        self._entries = []
        if entries:
            self._entries.extend(entries)

    def _get_data_from_source(self):
        pass

    def get(self) -> list:
        if not self._entries:
            self._get_data_from_source()
        return self._entries.copy()

    def add(self, entries: list):
        self._entries.extend(entries)


class CurrentObjectsRepository(Repository):

    def __init__(self, operation_object: entities.OperationObject, get_current_data_adapter):
        self._operation_object = operation_object
        self._get_current_data_adapter = get_current_data_adapter
        super().__init__()

    def _get_data_from_source(self):
        objects = ['object_repair_group', 'tech_position', 'equipment']
        for object_type in objects:
            items = self._get_current_data_adapter.retrieve(self._operation_object, object_type)
            self.add(items)

        # nested objects
        nested_objects = ['property', 'plan_repair', 'fact_repair', 'failure', 'part']
        for nested_object in nested_objects:
            self._get_current_data_adapter.join_nested_objects_to_entities(self._operation_object, self._entries,
                                                                           nested_object)


class OperationObjectsRepository(Repository):

    def __init__(self, get_current_data_adapter):
        self._get_current_data_adapter = get_current_data_adapter
        super().__init__()

    def _get_data_from_source(self):
        items = self._get_current_data_adapter.retireve(None, 'operation_object')
        self.add(items)


class NewObjectsRepository(Repository):

    def __init__(self, operation_object: entities.OperationObject, get_new_data_adapter, post_data_adapter):
        self._operation_object = operation_object
        self._get_new_data_adapter = get_new_data_adapter
        self._post_data_adapter = post_data_adapter
        super().__init__()

    def _get_data_from_source(self):
        object_repair_groups = self._get_new_data_adapter.get_new_object_repair_group(self._operation_object)
        self.add(object_repair_groups)
        equipment = self._get_new_data_adapter.get_new_equipment(self._operation_object)
        self.add(equipment)
        tech_position = self._get_new_data_adapter.get_new_tech_position(self._operation_object)
        self.add(tech_position)

    def save(self):
        statistic = {'success': 0, 'error': 0}
        actions = {
            'updated': self._post_data_adapter.update,
            'new': self._post_data_adapter.create,
        }
        items = self.get()
        items.sort(key=lambda x: x.level)
        for item in items:
            action = actions.get(item.update_status)
            if action:
                status = action(item)
                statistic[status] += 1
            if item.replaced:
                self._post_data_adapter.replace(item)
        return statistic

    def delete(self):
        statistic = {'success': 0, 'error': 0}
        entities_for_delete = list(filter(lambda x: x.update_status == 'empty', self.get()))
        for entity in entities_for_delete:
            status = self._post_data_adapter.delete(entity)
            statistic[status] += 1
        return statistic
