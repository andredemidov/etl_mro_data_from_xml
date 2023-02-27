from typing import List
from domain.entities import OperationObject, Equipment, TechPosition, ObjectRepairGroup
from .neosintez.get_current_object_repair_group_adapter import GetCurrentObjectRepairGroupAdapter
from .neosintez.get_current_equipment_adapter import GetCurrentEquipmentAdapter
from .neosintez.get_current_tech_position_adapter import GetCurrentTechPositionAdapter
from .neosintez.get_operation_object_adapter import GetOperationObjectAdapter


class GetCurrentDataAdapter:

    def __init__(self, url, token):
        self._url = url
        self._token = token

    def get_current_equipment(self, operation_object: OperationObject) -> List[Equipment]:
        return GetCurrentEquipmentAdapter(self._url, self._token).execute(operation_object)

    def get_current_tech_position(self, operation_object: OperationObject) -> List[TechPosition]:
        return GetCurrentTechPositionAdapter(self._url, self._token).execute(operation_object)

    def get_current_object_repair_group(self, operation_object: OperationObject) -> List[ObjectRepairGroup]:
        return GetCurrentObjectRepairGroupAdapter(self._url, self._token).execute(operation_object)

    def get_operation_objects(self) -> List[OperationObject]:
        return GetOperationObjectAdapter(self._url, self._token).execute()
