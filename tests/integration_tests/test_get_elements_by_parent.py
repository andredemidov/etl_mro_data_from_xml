import unittest
import xml.etree.ElementTree as ElementTree
from data_sources.xml_file.get_elements_by_parent import GetElementsByParent


class TestGetElementsByParent(unittest.TestCase):

    def test_execute(self):
        # arrange
        xml_iterator = ElementTree.iterparse(r'C:\Users\demid\Documents\python\work_projects\toir_integration\test_data\test_toir_data.xml')
        elements = list()
        for _, element in xml_iterator:
            if 'ДанныеОР_' in element.tag:
                elements.append(element)

        # act
        result = GetElementsByParent(elements).execute('d799f32a-fc65-11e5-81a1-005056a4190d', 'equipment')

        # assert
        self.assertEqual(3, len(result))
