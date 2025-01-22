import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestKonrad(unittest.TestCase):
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
    def testKonradProperty(self):
        soilunfrozenwatercontent = self.material.Thermal.SoilUnfrozenWaterContent
        soilunfrozenwatercontent.Konrad.setResidualWaterContent(0.1)
        soilunfrozenwatercontent.Konrad.setFrozenTemperature(836.5)
        soilunfrozenwatercontent.Konrad.setSolidusTemperature(2628.5)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        soilunfrozenwatercontent = self.material.Thermal.SoilUnfrozenWaterContent
        self.assertEqual(soilunfrozenwatercontent.Konrad.getResidualWaterContent(), 0.1)
        self.assertEqual(soilunfrozenwatercontent.Konrad.getFrozenTemperature(), 836.5)
        self.assertEqual(soilunfrozenwatercontent.Konrad.getSolidusTemperature(), 2628.5)
