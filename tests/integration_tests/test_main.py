import unittest
import main
from domain import entities
import data_sources


class TestMain(unittest.TestCase):

    def test_integrate_operation_object(self):
        # arrange
        URL = 'https://operation.irkutskoil.ru/'
        main.init_log()
        session = main.init_neosintez_session(URL, r'C:\Users\demid\Documents\python\work_projects\toir_integration\auth_data.txt')
        get_current_adapter = data_sources.GetCurrentDataAdapter(url=URL, session=session)
        post_data_adapter = data_sources.PostDataAdapter(url=URL, session=session)
        fake_operation_object = entities.OperationObject(
            name='forvalidation',
            self_id='1ac47979-dedc-ed11-916a-005056b6948b',
            toir_id='d799f194-fc65-11e5-81a1-005056a4190d',
            object_id='forvalidation',
            object_type='operation_object',
        )
        file_path = 'C:/Users/demid/Documents/python/work_projects/toir_integration/test_data/'
        get_new_adapter = data_sources.GetNewDataAdapter(file_path)
        # act
        main.integrate_operation_object(
            fake_operation_object,
            get_new_adapter,
            get_current_adapter,
            post_data_adapter
        )
