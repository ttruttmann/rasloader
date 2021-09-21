import unittest
from numpy import NAN
from rasloader import *

class TestRasLoader(unittest.TestCase): # TODO: Test appending files.
    def test_constructor_1D(self):
        rasloader = RasLoader('example_scan.ras')
        self.assertEqual(rasloader.metadata['FILE_OPERATOR'],'7290_Tristan')
        self.assertEqual(rasloader.metadata['FILE_VERSION'],1)
        self.assertIsInstance(rasloader.metadata['FILE_VERSION'],int)
        self.assertEqual(rasloader.metadata['HW_GONIOMETER_RADIUS-1'],114.0)
        self.assertIsInstance(rasloader.metadata['HW_GONIOMETER_RADIUS-1'],float)
        self.assertEqual(rasloader.axisdata.loc['Omega','position'],0)
        self.assertEqual(rasloader.axisdata.loc['Omega','resolution'],0.0001)
        self.assertEqual(rasloader.axisdata.loc['Omega','state'],'Fixed')
        self.assertEqual(len(rasloader.intdata.columns),2)
        self.assertEqual(rasloader.intdata.columns[0],'TwoThetaOmega')
        self.assertEqual(rasloader.intdata.columns[1],'I')
        self.assertEqual(rasloader.intdata['TwoThetaOmega'][0],10.00)
        self.assertEqual(rasloader.intdata['I'][0],9.5853)

    def test_constructor_2D(self):
        rasloader = RasLoader('example_rsm.ras')
        self.assertEqual(rasloader.metadata['FILE_OPERATOR'],'7290_Tristan')
        self.assertEqual(rasloader.metadata['FILE_VERSION'],1)
        self.assertIsInstance(rasloader.metadata['FILE_VERSION'],int)
        self.assertEqual(rasloader.metadata['HW_GONIOMETER_RADIUS-1'],114.0)
        self.assertIsInstance(rasloader.metadata['HW_GONIOMETER_RADIUS-1'],float)
        self.assertIs(rasloader.axisdata.loc['Omega','position'],NAN)
        self.assertEqual(rasloader.axisdata.loc['Omega','resolution'],0.0001)
        self.assertEqual(rasloader.axisdata.loc['Phi','position'],-2.20)
        self.assertEqual(rasloader.axisdata.loc['Phi','resolution'],0.002)
        self.assertEqual(rasloader.axisdata.loc['Omega','state'],'Scan')
        self.assertEqual(len(rasloader.intdata.columns),3)
        self.assertEqual(rasloader.intdata.columns[0],'Omega')
        self.assertEqual(rasloader.intdata.columns[1],'TwoTheta')
        self.assertEqual(rasloader.intdata.columns[2],'I')
        self.assertEqual(rasloader.intdata['Omega'][0],15.0) 
        self.assertEqual(rasloader.intdata['TwoTheta'][0],83.5)
        self.assertEqual(rasloader.intdata['I'][0],231.292)
        
if __name__ == '__main__':
    unittest.main()