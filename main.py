import logging
from datetime import datetime
from domain import transformations, repositories
import data_sources

URL = 'https://operation.irkutskoil.ru/'
XML_FILE_DIRECTORY = '//irkoil/dfs/WorkDATA/1C_OBMEN/ТОиР_Неосинтез/'


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

    get_new_data_adapter = data_sources.GetNewDataAdapter(file_directory=XML_FILE_DIRECTORY)

    with open('auth_data.txt') as f:
        aut_string = f.read()
    session = data_sources.GetSession.execute(URL, aut_string)
    try:
        get_current_data_adapter = data_sources.GetCurrentDataAdapter(url=URL, session=session)
        post_data_adapter = data_sources.PostDataAdapter(url=URL, session=session)
        operation_object_repository = repositories.OperationObjectsRepository(get_current_data_adapter)
        logging.info(f'Total objects {len(operation_object_repository.get())}')

        for operation_object in operation_object_repository.get():
            try:
                # new data
                new_repository = repositories.NewObjectsRepository(
                    operation_object=operation_object,
                    get_new_data_adapter=get_new_data_adapter,
                    post_data_adapter=post_data_adapter
                )
                logging.info(f'new entities: {len(new_repository.get())}')

                transformations.SetParentReference(operation_object=operation_object, repository=new_repository).execute()

                # current data
                current_repository = repositories.CurrentObjectsRepository(operation_object, get_current_data_adapter)

                transformations.MatchNewAndCurrentEntities(
                    new_entities_repository=new_repository,
                    current_entities_repository=current_repository,
                ).execute()

                logging.info('creating and updating')
                statistic = new_repository.save()
                log_statistic(statistic)

                logging.info('creating and updating nested objects')
                statistic = new_repository.save_nested_objects()
                log_statistic(statistic)

                # delete
                logging.info('deleting')
                statistic = new_repository.delete()
                log_statistic(statistic)
            except Exception as e:
                print(e)
                logging.exception('Exception occurred')
    finally:
        session.close()
        logging.info('Session is closed')


if __name__ == '__main__':
    start()
