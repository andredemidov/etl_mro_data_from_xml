import logging
import sys
from collections import Counter
from datetime import datetime
from domain import transformations, repositories
import data_sources

URL = 'https://operation.irkutskoil.ru/'
XML_FILE_DIRECTORY = '//irkoil/dfs/WorkDATA/1C_OBMEN/ТОиР_Неосинтез/'
MODES = ['dim', 'toir']

def log_statistic(statistic: dict):
    message = ', '.join([f'{c[0]} - {c[1]}' for c in statistic.items()])
    if statistic.get('error'):
        logging.warning(message)
    else:
        logging.info(message)


def integrate_operation_object(operation_object, get_new_data_adapter, get_current_data_adapter, post_data_adapter):

    # создние репозитория для новых данных из файла

    # new data
    new_repository = repositories.RepairObjectsRepository(
        operation_object=operation_object,
        get_data_adapter=get_new_data_adapter,
        post_data_adapter=post_data_adapter
    )
    logging.info(f'new entities: {len(new_repository.get())}')

    transformations.SetParentReference(operation_object=operation_object, repository=new_repository).execute()

    # current data
    current_repository = repositories.RepairObjectsRepository(operation_object, get_current_data_adapter)
    current_dim_repository = repositories.DimensionsRepository(get_data_adapter=get_current_data_adapter)

    transformations.GetDataFromDimensions(current_repository, current_dim_repository).execute()
    transformations.GetDataFromDimensions(new_repository, current_dim_repository).execute()

    transformations.MatchNewAndCurrentEntities(
        new_entities_repository=new_repository,
        current_entities_repository=current_repository,
    ).execute()
    statuses = list(map(lambda x: x.update_status, new_repository.get()))
    counter = Counter(statuses)
    logging.info(f'statuses:')
    log_statistic(counter)

    logging.info('creating and updating')
    statistic = new_repository.save()
    log_statistic(statistic)

    # statistic for nested objects
    nested_object_statuses = []
    host_items = list(filter(lambda x: x.update_status != 'empty', new_repository.get()))
    for host_item in host_items:
        for nested_items in host_item.get_nested_objects():
            for item in nested_items:
                nested_object_statuses.append(item.update_status)
    counter = Counter(statuses)
    logging.info(f'nested objects statuses:')
    log_statistic(counter)

    logging.info('creating and updating nested objects')
    statistic = new_repository.save_nested_objects()
    log_statistic(statistic)

    # delete
    logging.info('deleting')
    statistic = new_repository.delete()
    log_statistic(statistic)

    logging.info('deleting nested objects')
    statistic = new_repository.delete_nested_objects()
    log_statistic(statistic)


def update_dimension_tables(get_new_data_adapter, get_current_data_adapter, post_data_adapter):
    current_repository = repositories.DimensionsRepository(get_data_adapter=get_current_data_adapter)
    new_repository = repositories.DimensionsRepository(get_data_adapter=get_new_data_adapter, post_data_adapter=post_data_adapter)

    transformations.SetParentReference(repository=new_repository).execute()
    # compare data
    transformations.MatchNewAndCurrentEntities(
        new_entities_repository=new_repository,
        current_entities_repository=current_repository
    ).execute()
    statuses = list(map(lambda x: x.update_status, new_repository.get()))
    counter = Counter(statuses)
    logging.info(f'statuses:')
    log_statistic(counter)
    # update and create data in neosintez
    logging.info('creating and updating dimensions')
    statistic = new_repository.save()
    log_statistic(statistic)


def init_log(logs_path: str = None):
    if not logs_path:
        logs_path = 'c://python/logs/'
    logging.basicConfig(
        format='%(asctime)s : %(levelname)s : %(message)s',
        level=logging.INFO,
        handlers=[
            logging.FileHandler(logs_path + datetime.now().strftime("%Y-%m-%d") + f'_toir.log'),
            logging.StreamHandler()
        ]
    )


def init_neosintez_session(url, auth_data_file_path: str = None):
    if not auth_data_file_path:
        auth_data_file_path = 'auth_data.txt'
    with open(auth_data_file_path) as f:
        aut_string = f.read()
    return data_sources.GetSession.execute(url, aut_string)


if __name__ == '__main__':
    session = None

    if len(sys.argv) != 2:
        raise EnvironmentError('Mode expected')
    mode = sys.argv[1]
    if mode not in MODES:
        raise EnvironmentError(f'Invalid mode {mode}. Only {",".join(MODES)} are available')

    try:
        init_log()
        session = init_neosintez_session(URL)
        get_new_data_adapter = data_sources.GetNewDataAdapter(file_directory=XML_FILE_DIRECTORY)
        get_current_data_adapter = data_sources.GetCurrentDataAdapter(url=URL, session=session)
        post_data_adapter = data_sources.PostDataAdapter(url=URL, session=session)

        if mode == 'toir':
            operation_object_repository = repositories.OperationObjectsRepository(get_current_data_adapter)
            logging.info(f'Total objects {len(operation_object_repository.get())}')
            for operation_object in operation_object_repository.get():
                logging.info(operation_object.name)
                try:
                    integrate_operation_object(
                        operation_object=operation_object,
                        get_new_data_adapter=get_new_data_adapter,
                        get_current_data_adapter=get_current_data_adapter,
                        post_data_adapter=post_data_adapter
                    )

                except Exception as e:
                    print(e)
                    logging.exception('Exception occurred')
        elif mode == 'dim':
            update_dimension_tables(
                get_new_data_adapter=get_new_data_adapter,
                get_current_data_adapter=get_current_data_adapter,
                post_data_adapter=post_data_adapter
            )
    finally:
        session.close()
        logging.info('Session is closed')
