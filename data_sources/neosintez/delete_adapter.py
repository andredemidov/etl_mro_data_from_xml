from .neosintez_gateway import NeosintezGateway
from domain import entities


class DeleteAdapter(NeosintezGateway):

    def execute(self, item: (entities.Equipment, entities.TechPosition, entities.ObjectRepairGroup)) -> str:

        response = self.delete_item(item.self_id)
        if response.status_code == 200:
            status = 'success'
        else:
            status = 'error'
        return status
