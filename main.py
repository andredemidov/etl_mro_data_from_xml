from domain.use_cases import GetOperationObjects, GetUpdatedEntities, GetNewEquipment, GetCurrentEquipment, \
    SaveEntities, GetCurrentTechPosition, GetCurrentObjectRepairGroup, GetNewObjectRepairGroup, GetNewTechPosition,\
    GetEntitiesForDelete, DeleteEntities, SetParentReference
from data_sources import GetNewDataAdapter, GetCurrentDataAdapter, PostDataAdapter, GetToken
from repositories import Repository

URL = 'https://operation.irkutskoil.ru/'
XML_FILE = 'test_data/test_toir_data.xml'


def start():
    get_new_data_adapter = GetNewDataAdapter(file_path=XML_FILE)

    with open('auth_data.txt') as f:
        aut_string = f.read()
    token = GetToken(URL).execute(aut_string)
    operation_object_repository = Repository()
    get_current_data_adapter = GetCurrentDataAdapter(url=URL, token=token)
    post_data_adapter = PostDataAdapter(url=URL, token=token)

    GetOperationObjects(get_current_data_adapter, operation_object_repository).execute()

    for operation_object in operation_object_repository.list():

        # new data
        new_object_repair_group_repository = Repository()
        GetNewObjectRepairGroup(get_new_data_adapter, new_object_repair_group_repository, operation_object).execute()

        new_tech_position_repository = Repository()
        GetNewTechPosition(get_new_data_adapter, new_tech_position_repository, operation_object).execute()

        new_equipment_repository = Repository()
        GetNewEquipment(get_new_data_adapter, new_equipment_repository, operation_object).execute()

        SetParentReference(
            operation_object=operation_object,
            object_repair_group_repository=new_object_repair_group_repository,
            tech_position_repository=new_tech_position_repository,
            equipment_repository=new_equipment_repository,
        )
        # object_repair_group
        current_object_repair_group_repository = Repository()
        GetCurrentObjectRepairGroup(
            adapter=get_current_data_adapter,
            repository=current_object_repair_group_repository,
        ).execute(operation_object)
        updated_object_repair_group_repository = Repository()
        GetUpdatedEntities(
            new_entities_repository=new_object_repair_group_repository,
            current_entities_repository=current_object_repair_group_repository,
            updated_entities_repository=updated_object_repair_group_repository,
        ).execute()
        delete_object_repair_group_repository = Repository()
        GetEntitiesForDelete(
            current_entities_repository=current_object_repair_group_repository,
            delete_entities_repository=delete_object_repair_group_repository,
        ).execute()

        SaveEntities(post_data_adapter, updated_object_repair_group_repository).execute()

        # tech_position
        current_tech_position_repository = Repository()
        GetCurrentTechPosition(
            adapter=get_current_data_adapter,
            repository=current_tech_position_repository,
        ).execute(operation_object)
        updated_tech_position_repository = Repository()
        GetUpdatedEntities(
            new_entities_repository=new_tech_position_repository,
            current_entities_repository=current_tech_position_repository,
            updated_entities_repository=updated_tech_position_repository,
        ).execute()
        delete_tech_position_repository = Repository()
        GetEntitiesForDelete(
            current_entities_repository=current_tech_position_repository,
            delete_entities_repository=delete_tech_position_repository,
        ).execute()

        SaveEntities(post_data_adapter, updated_tech_position_repository).execute()

        # equipment
        current_equipment_repository = Repository()
        GetCurrentEquipment(
            adapter=get_current_data_adapter,
            repository=current_equipment_repository,
        ).execute(operation_object)
        updated_equipment_repository = Repository()
        GetUpdatedEntities(
            new_entities_repository=new_equipment_repository,
            current_entities_repository=current_equipment_repository,
            updated_entities_repository=updated_equipment_repository,
        ).execute()
        delete_equipment_repository = Repository()
        GetEntitiesForDelete(
            current_entities_repository=current_equipment_repository,
            delete_entities_repository=delete_equipment_repository,
        ).execute()

        SaveEntities(post_data_adapter, updated_equipment_repository).execute()

        # delete

        DeleteEntities(post_data_adapter, delete_object_repair_group_repository).execute()
        DeleteEntities(post_data_adapter, delete_tech_position_repository).execute()
        DeleteEntities(post_data_adapter, delete_equipment_repository).execute()


if __name__ == '__main__':
    start()
