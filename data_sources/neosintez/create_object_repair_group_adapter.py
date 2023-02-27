from .neosintez_gateway import NeosintezGateway
from domain.entities import ObjectRepairGroup


class CreateObjectRepairGroupAdapter(NeosintezGateway):

    def _get_request_body(self, item: ObjectRepairGroup):
        request_body = []
        request_body.extend([
            {
                'Name': 'forvalidation',
                'Value': item.level if item.level else None,
                'Type': 2,
                'Id': self.level_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.parent_toir_id if item.parent_toir_id else None,
                'Type': 2,
                'Id': self.parent_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.name if item.name else None,
                'Type': 2,
                'Id': self.name_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': item.toir_url if item.toir_url else None,
                'Type': 6,
                'Id': self.toir_url_attribute_id
            },
            {
                'Name': 'forvalidation',
                'Value': {'Id': item.departament_id, 'Name': 'forvalidation'} if item.departament_id else None,
                'Type': 6,
                'Id': self.departament_id_attribute_id
            },
        ])
        return request_body

    def execute(self, object_repair_group: ObjectRepairGroup):
        if not object_repair_group.parent_object:
            return 500
        request_body = self._get_request_body(object_repair_group)
        parent_id = object_repair_group.parent_object.self_id
        response = self.create(parent_id, request_body)
        return response.status_code
