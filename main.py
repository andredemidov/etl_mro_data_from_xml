from domain import use_cases
import data_sources
from repositories import Repository

URL = 'https://operation.irkutskoil.ru/'
XML_FILE = 'test_data/test_toir_data.xml'


def start():
    get_new_data_adapter = data_sources.GetNewDataAdapter(file_path=XML_FILE)

    with open('auth_data.txt') as f:
        aut_string = f.read()
    token = data_sources.GetToken(URL).execute(aut_string)
    operation_object_repository = Repository()
    get_current_data_adapter = data_sources.GetCurrentDataAdapter(url=URL, token=token)
    post_data_adapter = data_sources.PostDataAdapter(url=URL, token=token)

    use_cases.GetOperationObjects(get_current_data_adapter, operation_object_repository).execute()

    for operation_object in operation_object_repository.list():

        # new data
        new_object_repair_group_repository = Repository()
        use_cases.GetNewObjectRepairGroup(get_new_data_adapter, new_object_repair_group_repository, operation_object).execute()

        new_tech_position_repository = Repository()
        use_cases.GetNewTechPosition(get_new_data_adapter, new_tech_position_repository, operation_object).execute()

        new_equipment_repository = Repository()
        use_cases.GetNewEquipment(get_new_data_adapter, new_equipment_repository, operation_object).execute()

        use_cases.SetParentReference(
            operation_object=operation_object,
            object_repair_group_repository=new_object_repair_group_repository,
            tech_position_repository=new_tech_position_repository,
            equipment_repository=new_equipment_repository,
        ).execute()
        # object_repair_group
        current_object_repair_group_repository = Repository()
        use_cases.GetCurrentObjectRepairGroup(
            adapter=get_current_data_adapter,
            repository=current_object_repair_group_repository,
        ).execute(operation_object)
        updated_object_repair_group_repository = Repository()
        use_cases.GetUpdatedReplacedEntities(
            new_entities_repository=new_object_repair_group_repository,
            current_entities_repository=current_object_repair_group_repository,
            updated_entities_repository=updated_object_repair_group_repository,
        ).execute()
        delete_object_repair_group_repository = Repository()
        use_cases.GetEntitiesForDelete(
            current_entities_repository=current_object_repair_group_repository,
            delete_entities_repository=delete_object_repair_group_repository,
        ).execute()

        statistic = use_cases.SaveEntities(post_data_adapter, updated_object_repair_group_repository).execute()
        print(statistic)

        # tech_position
        current_tech_position_repository = Repository()
        use_cases.GetCurrentTechPosition(
            adapter=get_current_data_adapter,
            repository=current_tech_position_repository,
        ).execute(operation_object)
        updated_tech_position_repository = Repository()
        use_cases.GetUpdatedReplacedEntities(
            new_entities_repository=new_tech_position_repository,
            current_entities_repository=current_tech_position_repository,
            updated_entities_repository=updated_tech_position_repository,
        ).execute()
        delete_tech_position_repository = Repository()
        use_cases.GetEntitiesForDelete(
            current_entities_repository=current_tech_position_repository,
            delete_entities_repository=delete_tech_position_repository,
        ).execute()

        statistic = use_cases.SaveEntities(post_data_adapter, updated_tech_position_repository).execute()
        print(statistic)

        # equipment
        current_equipment_repository = Repository()
        use_cases.GetCurrentEquipment(
            adapter=get_current_data_adapter,
            repository=current_equipment_repository,
        ).execute(operation_object)
        updated_equipment_repository = Repository()
        use_cases.GetUpdatedReplacedEntities(
            new_entities_repository=new_equipment_repository,
            current_entities_repository=current_equipment_repository,
            updated_entities_repository=updated_equipment_repository,
        ).execute()
        delete_equipment_repository = Repository()
        use_cases.GetEntitiesForDelete(
            current_entities_repository=current_equipment_repository,
            delete_entities_repository=delete_equipment_repository,
        ).execute()

        statistic = use_cases.SaveEntities(post_data_adapter, updated_equipment_repository).execute()
        print(statistic)

        # delete

        statistic = use_cases.DeleteEntities(post_data_adapter, delete_object_repair_group_repository).execute()
        print('object_repair_group', statistic)
        statistic = use_cases.DeleteEntities(post_data_adapter, delete_tech_position_repository).execute()
        print('tech_position', statistic)
        statistic = use_cases.DeleteEntities(post_data_adapter, delete_equipment_repository).execute()
        print('equipment', statistic)


if __name__ == '__main__':
    start()
