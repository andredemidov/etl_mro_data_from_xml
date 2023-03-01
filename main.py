import logging
from datetime import datetime
from domain import use_cases
import data_sources
from repositories import Repository

URL = 'https://operation.irkutskoil.ru/'
XML_FILE = 'test_data/test_toir_data.xml'


def log_statistic(statistic: dict):
    message = ', '.join([f'{c[0]} - {c[1]}' for c in statistic.items()])
    if statistic.get('error'):
        logging.warning(message)
    else:
        logging.info(message)


def start():
    logs_path = 'c://python/logs/'
    logging.basicConfig(
        format='%(asctime)s : %(levelname)s : %(message)s',
        level=logging.INFO,
        handlers=[
            logging.FileHandler(logs_path + datetime.now().strftime("%Y-%m-%d") + f'_toir.log'),
            logging.StreamHandler()
        ]
    )

    get_new_data_adapter = data_sources.GetNewDataAdapter(file_path=XML_FILE)

    with open('auth_data.txt') as f:
        aut_string = f.read()
    token = data_sources.GetToken(URL).execute(aut_string)
    operation_object_repository = Repository()
    get_current_data_adapter = data_sources.GetCurrentDataAdapter(url=URL, token=token)
    post_data_adapter = data_sources.PostDataAdapter(url=URL, token=token)

    use_cases.GetOperationObjects(get_current_data_adapter, operation_object_repository).execute()
    logging.info(f'Total objects {len(operation_object_repository.list())}')

    for operation_object in operation_object_repository.list():

        # new data
        new_object_repair_group_repository = Repository()
        use_cases.GetNewObjectRepairGroup(
            adapter=get_new_data_adapter,
            repository=new_object_repair_group_repository,
            operation_object=operation_object,
        ).execute()

        new_tech_position_repository = Repository()
        use_cases.GetNewTechPosition(get_new_data_adapter, new_tech_position_repository, operation_object).execute()

        new_equipment_repository = Repository()
        use_cases.GetNewEquipment(get_new_data_adapter, new_equipment_repository, operation_object).execute()

        logging.info(
            f'groups: {len(new_object_repair_group_repository.list())}',
            f'tech_positions: {len(new_tech_position_repository.list())}',
            f'equipments: {len(new_equipment_repository.list())}',
        )

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
        use_cases.MapNewAndCurrentEntities(
            new_entities_repository=new_object_repair_group_repository,
            current_entities_repository=current_object_repair_group_repository,
        ).execute()

        logging.info('creating and updating of groups')
        statistic = use_cases.SaveEntities(post_data_adapter, new_object_repair_group_repository).execute()
        log_statistic(statistic)

        # tech_position
        current_tech_position_repository = Repository()
        use_cases.GetCurrentTechPosition(
            adapter=get_current_data_adapter,
            repository=current_tech_position_repository,
        ).execute(operation_object)
        use_cases.MapNewAndCurrentEntities(
            new_entities_repository=new_tech_position_repository,
            current_entities_repository=current_tech_position_repository,
        ).execute()

        logging.info('creating and updating of tech_positions')
        statistic = use_cases.SaveEntities(post_data_adapter, new_tech_position_repository).execute()
        log_statistic(statistic)

        # equipment
        current_equipment_repository = Repository()
        use_cases.GetCurrentEquipment(
            adapter=get_current_data_adapter,
            repository=current_equipment_repository,
        ).execute(operation_object)
        use_cases.MapNewAndCurrentEntities(
            new_entities_repository=new_equipment_repository,
            current_entities_repository=current_equipment_repository,
        ).execute()

        logging.info('creating and updating of equipments')
        statistic = use_cases.SaveEntities(post_data_adapter, new_equipment_repository).execute()
        log_statistic(statistic)

        # delete
        logging.info('deleting of groups')
        statistic = use_cases.DeleteEntities(post_data_adapter, new_object_repair_group_repository).execute()
        log_statistic(statistic)

        logging.info('deleting of tech_positions')
        statistic = use_cases.DeleteEntities(post_data_adapter, new_tech_position_repository).execute()
        log_statistic(statistic)

        logging.info('deleting of equipments')
        statistic = use_cases.DeleteEntities(post_data_adapter, new_equipment_repository).execute()
        log_statistic(statistic)


if __name__ == '__main__':
    start()
