import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestTabularDefs(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]

    @classmethod
    def tearDownClass(self):
        self.model.close()
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)

    def testMohrCoulombCapMeanStress(self):
        newTable = [(1.1,2.2),(-3.3,4.4)]
        self.material.Strength.MohrCoulombWithCap.setMohrCoulombCapMeanStress(newTable)
        self.assertEqual(self.material.Strength.MohrCoulombWithCap.getMohrCoulombCapMeanStress(), newTable)

        invalidTable = [(1,2)]
        with self.assertRaises(Exception):
            self.material.Strength.MohrCoulombWithCap.setMohrCoulombCapMeanStress(invalidTable)
    
    def testSHConeHardening(self):
        newTable1 = [(1.1,2.2),(-3.3,4.4)]
        newTable2 = [(5.5,6.6),(-7.7,8.8)]

        self.material.Strength.SofteningHardeningModel.setSHConeHardening(newTable1, newTable2)
        self.assertEqual(self.material.Strength.SofteningHardeningModel.getSHConeHardening(), (newTable1, newTable2))

        invalidTable = [(1,2)]
        with self.assertRaises(Exception):
            self.material.Strength.SofteningHardeningModel.setSHConeHardening(invalidTable, newTable2)
        
        #check that when one table is not valid, the other table is not changed
        self.assertEqual(self.material.Strength.SofteningHardeningModel.getSHConeHardening(), (newTable1, newTable2))

        with self.assertRaises(Exception):
            self.material.Strength.SofteningHardeningModel.setSHConeHardening(newTable1, invalidTable)
    
        self.assertEqual(self.material.Strength.SofteningHardeningModel.getSHConeHardening(), (newTable1, newTable2))

    def testSHCapMeanStress(self):
        newTable = [(1,2),(3,4)]
        self.material.Strength.SofteningHardeningModel.setSHCapMeanStress(newTable)
        self.assertEqual(self.material.Strength.SofteningHardeningModel.getSHCapMeanStress(), newTable)

        invalidTable = [(1,2)]
        with self.assertRaises(Exception):
            self.material.Strength.SofteningHardeningModel.setSHCapMeanStress(invalidTable)
    
