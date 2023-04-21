from domain import entities


class Repository:
    """
    Абстрактный класс для всех репозиториев. Реализовано ленивое получение данных - в момент инициации репозитория
    данные не запрашиваются, а запрашиваются только при первом вызове метода get
    """
    def __init__(self, entries: list = None):
        self._entries = []
        if entries:
            self._entries.extend(entries)

    def _get_data_from_source(self):
        pass

    def get(self) -> list:
        """
        Метод для получения данных из репозитория. При первом вызове извлекает данные из источника. Возвращает копию
        списка объектов в репозитории. Это сделано для того, чтобы исключить случайную фильтрацию, удаление, сортировку
        объектов оригинально списка объектов в репозитории. При этом остается возможность редактирования
         самих объектов (удобство ООП)
        :return: копию списка объектов в репозитории
        """
        if not self._entries:
            self._get_data_from_source()
        return self._entries.copy()

    def add(self, entries: list):
        """
        Метод для добавления новых объектов в репозиторий. Проверка, что в переданном списке именно объекты нужного
        класса не проводится.
        :param entries: список объектов
        """
        self._entries.extend(entries)


class OperationObjectsRepository(Repository):

    def __init__(self, get_current_data_adapter):
        self._get_current_data_adapter = get_current_data_adapter
        super().__init__()

    def _get_data_from_source(self):
        # Здесь репозиторий взаимодействует с адаптером для получения соответствующих данных
        # метод реализует интерфейс, в соответствии с которым адаптер должен иметь метод retrieve, принимающий два
        # аргумента: объект OperationObject (в данном случае None) и строку с типом объекта.
        items = self._get_current_data_adapter.retrieve(None, 'operation_object')
        self.add(items)


class DimensionsRepository(Repository):

    def __init__(self, get_data_adapter, post_data_adapter=None):
        self._get_data_adapter = get_data_adapter
        self._post_data_adapter = post_data_adapter
        super().__init__()

    def _get_data_from_source(self):
        # Здесь репозиторий взаимодействует с адаптером для получения соответствующих данных

        objects = ['dim_departament', 'dim_type_failure', 'dim_type_repair', 'dim_property', 'dim_typical_object', 'dim_type_reason_failure']
        for object_type in objects:
            items = self._get_data_adapter.retrieve(None, object_type)
            self.add(items)

    def save(self):
        if not self._post_data_adapter:
            raise NotImplementedError('There is no post adapter')
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
        return statistic


class RepairObjectsRepository(Repository):

    def __init__(self, operation_object: entities.OperationObject, get_data_adapter, post_data_adapter=None):
        self._operation_object = operation_object
        self._get_data_adapter = get_data_adapter
        self._post_data_adapter = post_data_adapter
        super().__init__()

    def _get_data_from_source(self):
        objects = ['object_repair_group', 'tech_position', 'equipment']
        for object_type in objects:
            items = self._get_data_adapter.retrieve(self._operation_object, object_type)
            self.add(items)

    def save(self) -> dict:
        """
        Метод для сохранения (записи) данных. Включает в себя операции по созданию и обновлению. Соответствующее
        действие для конкретной сущности выбирается исходя из статуса - update_status.
        :return: возвращает dict со статистикой ошибок и успешных сохранений типа: {'success': 0, 'error': 0}
        """
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
            if hasattr(item, 'replaced') and item.replaced:
                self._post_data_adapter.replace(item)
        return statistic

    def save_nested_objects(self) -> dict:
        """
        Метод для сохранения (записи) данных по вложенным объектам. Включает в себя операции по созданию и обновлению.
        Соответствующее действие для конкретной сущности выбирается исходя из статуса - update_status.
        :return: возвращает dict со статистикой ошибок и успешных сохранений типа: {'success': 0, 'error': 0}
        """
        statistic = {'success': 0, 'error': 0}
        actions = {
            'updated': self._post_data_adapter.update,
            'new': self._post_data_adapter.create_nested_object,
        }
        # get only relevant (not for delete) host items
        host_items = list(filter(lambda x: x.update_status != 'empty', self.get()))
        for host_item in host_items:
            for nested_items in host_item.get_nested_objects():
                for item in nested_items:
                    # before any action set host_id from host_item
                    item.host_id = host_item.self_id
                    action = actions.get(item.update_status)
                    if action:
                        status = action(item)
                        statistic[status] += 1
        return statistic

    def delete(self):
        """
        Метод для удаления объекта.
        :return: возвращает dict со статистикой ошибок и успешных сохранений типа: {'success': 0, 'error': 0}
        """
        statistic = {'success': 0, 'error': 0}
        # статус обновления empty означает, что сущность подлежит удалению
        entities_for_delete = list(filter(lambda x: x.update_status == 'empty', self.get()))
        for entity in entities_for_delete:
            status = self._post_data_adapter.delete(entity)
            statistic[status] += 1
        return statistic

    def delete_nested_objects(self):
        """
        Метод для удаления вложенного объекта.
        :return: возвращает dict со статистикой ошибок и успешных сохранений типа: {'success': 0, 'error': 0}
        """
        statistic = {'success': 0, 'error': 0}
        # статус обновления empty означает, что сущность подлежит удалению
        host_items = list(filter(lambda x: x.update_status != 'empty', self.get()))
        for host_item in host_items:
            for nested_items in host_item.get_nested_objects():
                nested_items_for_delete = list(filter(lambda x: x.update_status == 'empty', nested_items))
                for item in nested_items_for_delete:
                    # before any action set host_id from host_item
                    item.host_id = host_item.self_id
                    status = self._post_data_adapter.delete_nested_object(item)
                    statistic[status] += 1
        return statistic
