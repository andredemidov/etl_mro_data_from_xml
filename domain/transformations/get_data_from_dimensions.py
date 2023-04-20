from domain import entities


class GetDataFromDimensions:

    def __init__(self, repository, dim_repository):
        self._repository = repository
        self._dim_repository = dim_repository
        self._indexed_by_toir_id = None
        self._indexed_by_reference_id = None

    def _get_reference_attribute_value(self, item):
        reference_attributes: list[entities.ReferenceAttribute] = list(
            filter(lambda x: isinstance(x, entities.ReferenceAttribute), item.__dict__.values()))
        for attribute in reference_attributes:
            if attribute.toir_id:
                dimension = self._indexed_by_toir_id.get(attribute.toir_id)
                attribute.reference_id = dimension.self_id
                attribute.reference_name = dimension.name
            elif attribute.reference_id:
                dimension = self._indexed_by_reference_id.get(attribute.reference_id)
                attribute.toir_id = dimension.toir_id
                attribute.value = dimension.name

    def execute(self):
        self._indexed_by_toir_id = {dimension.toir_id: dimension for dimension in self._dim_repository.get()}
        self._indexed_by_reference_id = {dimension.self_id: dimension for dimension in self._dim_repository.get()}
        for item in self._repository.get():
            self._get_reference_attribute_value(item)
            for nested_object_attribute in item.get_nested_objects():
                for nested_object in nested_object_attribute:
                    self._get_reference_attribute_value(nested_object)
