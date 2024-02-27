import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestShansepStressHistory(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)

        allMaterials = self.model.getAllMaterialProperties()
        self.material = allMaterials[0]
        self.material.Strength.Shansep.setStressHistoryType(StressHistoryTypes.SHT_OCR)

    @classmethod
    def tearDownClass(self):
        self.model.close()
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)
    
    def testSuccess(self):
        input = [(10000000.1,2.2),(-0.000000003,-4.5)]
        self.material.Strength.Shansep.setShansepStressHistory(input)
        self.assertEqual(self.material.Strength.Shansep.getShansepStressHistory(), input)
    
    def testFailEmpty(self):  
        with self.assertRaises(Exception):
            self.material.Strength.Shansep.setShansepStressHistory([])      
