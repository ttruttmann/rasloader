import unittest
from rasloader import *

class TestRasLoader(unittest.TestCase):
    def test_constructor_1D(self):
        rasloader = RasLoader('example_scan.ras')
        self.assertEqual(rasloader.metadata['FILE_OPERATOR'],'7290_Tristan')
        self.assertEqual(rasloader.metadata['FILE_VERSION'],1)
        self.assertIsInstance(rasloader.metadata['FILE_VERSION'],int)
        self.assertEqual(rasloader.metadata['HW_GONIOMETER_RADIUS-1'],114.0)
        self.assertIsInstance(rasloader.metadata['HW_GONIOMETER_RADIUS-1'],float)
        

if __name__ == '__main__':
    unittest.main()