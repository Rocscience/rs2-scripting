import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestSoilUnfrozenWaterContent(unittest.TestCase):
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
        os.remove(self.copiedModelPath)
    def testSoilUnfrozenWaterContentProperty(self):
        thermal = self.material.Thermal
        thermal.SoilUnfrozenWaterContent.setType(ThermalWaterContentType.THERMAL_WATER_CONTENT_TICE_ANDERSON)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        thermal = self.material.Thermal
        self.assertEqual(thermal.SoilUnfrozenWaterContent.getType(), ThermalWaterContentType.THERMAL_WATER_CONTENT_TICE_ANDERSON)
