import unittest
from rasloader import *

class TestRasLoader(unittest.TestCase):
    def test_constructor(self):
        rasloader = RasLoader('example_scan.ras')

if __name__ == '__main__':
    unittest.main()