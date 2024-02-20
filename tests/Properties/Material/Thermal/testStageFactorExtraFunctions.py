import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestStageFactorExtraFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProjectTransientGroundwaterAndThermal.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
    @classmethod
    def tearDownClass(self):
        self.model.close()
        self.model._client.closeConnection()
        os.remove(self.copiedModelPath)

    def testSetThermalGridFactor(self):
        sf1 = self.material.Thermal.stageFactorInterface.getDefinedStageFactors()[1]
        sf1.setThermalGridFactor("Grid 2")
        self.assertEqual(sf1.getThermalGridFactor(), "Grid 2")

        sf1.setThermalGridFactor("Grid 3")
        self.assertEqual(sf1.getThermalGridFactor(), "Grid 3")

        sf1.setThermalGridFactor("None")
        self.assertEqual(sf1.getThermalGridFactor(), "None")

        sf1.setThermalGridFactor("Default Grid")
        self.assertEqual(sf1.getThermalGridFactor(), "Default Grid")
    
    def testSetThermalGridFactorFailure(self):
        sf1 = self.material.Thermal.stageFactorInterface.getDefinedStageFactors()[1]
        with self.assertRaises(Exception):
            sf1.setThermalGridFactor("NonExistant Grid")
