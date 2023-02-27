import unittest
import xml.etree.ElementTree as ElementTree
from data_sources.xml_file.get_elements_by_parent import GetElementsByParent


class TestGetElementsByParent(unittest.TestCase):

    def test_execute(self):
        # arrange
        xml_iterator = ElementTree.iterparse(r'C:\Users\demid\Documents\INK\python_ink\toir_integration\test_data\test_toir_data.xml')
        elements = list()
        for _, element in xml_iterator:
            if 'ДанныеОР_' in element.tag:
                elements.append(element)

        # act
        result = GetElementsByParent(elements).execute('c38a1ee6-25f3-11ea-84c1-005056a40062', 'object_repair_group')

        # assert
        self.assertEqual(len(result), 9)
