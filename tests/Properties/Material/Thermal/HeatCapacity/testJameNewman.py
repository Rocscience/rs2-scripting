import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestJameNewman(unittest.TestCase):
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
    def testJameNewmanProperty(self):
        heatcapacity = self.material.Thermal.HeatCapacity
        heatcapacity.JameNewman.setIncludeLatentHeat(0)
        heatcapacity.JameNewman.setSoilSpecificHeatCapacity(2628.5)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        heatcapacity = self.material.Thermal.HeatCapacity
        self.assertEqual(heatcapacity.JameNewman.getIncludeLatentHeat(), 0)
        self.assertEqual(heatcapacity.JameNewman.getSoilSpecificHeatCapacity(), 2628.5)
