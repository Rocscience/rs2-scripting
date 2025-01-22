import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestTiceAnderson(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
    def tearDown(self):
        self.model.close()
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)
    def testTiceAndersonProperty(self):
        soilunfrozenwatercontent = self.material.Thermal.SoilUnfrozenWaterContent
        soilunfrozenwatercontent.TiceAnderson.setInputAlpha(836.5)
        soilunfrozenwatercontent.TiceAnderson.setInputBeta(2628.5)
        soilunfrozenwatercontent.TiceAnderson.setFrozenTemperature(972.5)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        soilunfrozenwatercontent = self.material.Thermal.SoilUnfrozenWaterContent
        self.assertEqual(soilunfrozenwatercontent.TiceAnderson.getInputAlpha(), 836.5)
        self.assertEqual(soilunfrozenwatercontent.TiceAnderson.getInputBeta(), 2628.5)
        self.assertEqual(soilunfrozenwatercontent.TiceAnderson.getFrozenTemperature(), 972.5)
