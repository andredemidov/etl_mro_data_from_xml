import unittest
from collections import Counter
import data_sources
from domain import entities, repositories, transformations


class TestMatchNewAndCurrentEntities(unittest.TestCase):

    def test_execute(self):
        # arrange
        URL = 'https://operation.irkutskoil.ru/'
        with open('auth_data.txt') as f:
            aut_string = f.read()
        session = data_sources.GetSession.execute(URL, aut_string)
        get_current_adapter = data_sources.GetCurrentDataAdapter(url=URL, session=session)
        # котельная УПН в тестовом расположении
        fake_operation_object = entities.OperationObject(
            'forvalidation',
            'e82ff66b-a1b9-ed11-915f-005056b6948b',
            '81066aeb-ca71-11ea-8528-005056a40062',
            'forvalidation',
        )
        fake_current_repository = repositories.CurrentObjectsRepository(
            operation_object=fake_operation_object,
            get_current_data_adapter=get_current_adapter
        )

        file_path = 'C:/Users/demid/Documents/python/work_projects/toir_integration/test_data/'
        get_new_adapter = data_sources.GetNewDataAdapter(file_path)

        fake_new_repository = repositories.NewObjectsRepository(
            operation_object=fake_operation_object,
            get_new_data_adapter=get_new_adapter,
            post_data_adapter=None,
        )

        # act
        transformations.MatchNewAndCurrentEntities(
            new_entities_repository=fake_new_repository,
            current_entities_repository=fake_current_repository,
        ).execute()

        # assert
        statuses = list(map(lambda x: x.update_status, fake_new_repository.get()))
        counter = Counter(statuses)
        self.assertIn('new', counter)
        self.assertIn('updated', counter)