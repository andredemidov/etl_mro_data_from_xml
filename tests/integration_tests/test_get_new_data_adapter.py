import unittest
import data_sources
from domain import entities


class TestGetNewDataAdapter(unittest.TestCase):

    def test_get_new_equipment(self):
        # arrange
        # parser = ElementTree.XMLParser(encoding='UTF-8')
        file_path = 'C:/Users/demid/Documents/python/work_projects/toir_integration/test_data/'
        adapter = data_sources.GetNewDataAdapter(file_path)
        fake_operation_object = entities.OperationObject(
            'forvalidation',
            'forvalidation',
            '81066aeb-ca71-11ea-8528-005056a40062',
            'forvalidation',
            'operation_object',
        )

        # act
        equipments = adapter.retrieve(fake_operation_object, 'equipment')
        print(len(equipments))
        # assert
        self.assertNotEqual(len(equipments), 0)
