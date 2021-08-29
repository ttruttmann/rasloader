import unittest
from rasdata import *

class TestRasData(unittest.TestCase):
    def test_constructor(self):
        test_rasdata = RasData('test_rsm.ras')