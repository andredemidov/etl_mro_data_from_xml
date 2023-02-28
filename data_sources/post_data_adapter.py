from domain import entities
from . import neosintez


class PostDataAdapter:

    def __init__(self, url, token):
        self._url = url
        self._token = token

    def update(self, item: (entities.Equipment, entities.TechPosition, entities.ObjectRepairGroup)) -> str:
        return neosintez.UpdateAdapter(self._url, self._token).execute(item)

    def replace(self, item: (entities.Equipment, entities.TechPosition, entities.ObjectRepairGroup)) -> str:
        return ReplaceRelatedMaterialAdapter(self._url, self._token).execute(item)

    def delete(self, item: (entities.Equipment, entities.TechPosition, entities.ObjectRepairGroup)) -> str:
        return neosintez.DeleteAdapter(self._url, self._token).execute(item)

    def create(self, item: (entities.Equipment, entities.TechPosition, entities.ObjectRepairGroup)) -> str:
        return neosintez.CreateAdapter(self._url, self._token).execute(item)
