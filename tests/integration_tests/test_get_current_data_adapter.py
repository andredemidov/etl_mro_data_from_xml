import unittest
import data_sources
from domain import entities, repositories


class TestGetCurrentDataAdapter(unittest.TestCase):

    def test_retrieve(self):
        # arrange
        URL = 'https://operation.irkutskoil.ru/'
        with open('auth_data.txt') as f:
            aut_string = f.read()
        session = data_sources.GetSession.execute(URL, aut_string)
        adapter = data_sources.GetCurrentDataAdapter(url=URL, session=session)
        # котельная УПН в тестовом расположении
        fake_operation_object = entities.OperationObject(
            'forvalidation',
            'e82ff66b-a1b9-ed11-915f-005056b6948b',
            '81066aeb-ca71-11ea-8528-005056a40062',
            'forvalidation',
        )
        fake_repository = repositories.CurrentObjectsRepository(
            operation_object=fake_operation_object,
            get_current_data_adapter=adapter
        )

        # act
        data = fake_repository.get()
        print(len(data))

        # assert
        self.assertNotEqual(len(data), 0)
