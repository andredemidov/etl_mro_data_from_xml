from domain.entities import Equipment, TechPosition, ObjectRepairGroup
from .neosintez import CreateObjectRepairGroupAdapter


class PostDataAdapter:

    def __init__(self, url, token):
        self._url = url
        self._token = token

    def update(self, item: (Equipment, TechPosition, ObjectRepairGroup)):
        return UpdateRelatedMaterialAdapter(self._url, self._token).execute(item)

    def replace(self, item: (Equipment, TechPosition, ObjectRepairGroup)):
        return ReplaceRelatedMaterialAdapter(self._url, self._token).execute(item)

    def delete(self, item: (Equipment, TechPosition, ObjectRepairGroup)):
        return DeleteRelatedMaterialAdapter(self._url, self._token).execute(item)

    def create(self, item: (Equipment, TechPosition, ObjectRepairGroup)):
        return CreateObjectRepairGroupAdapter(self._url, self._token).execute(item)
