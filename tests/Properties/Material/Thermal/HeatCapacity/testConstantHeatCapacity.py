import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestConstantHeatCapacity(unittest.TestCase):
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
    def testConstantHeatCapacityProperty(self):
        heatcapacity = self.material.Thermal.HeatCapacity
        heatcapacity.ConstantHeatCapacity.setIncludeLatentHeat(0)
        heatcapacity.ConstantHeatCapacity.setUnfrozenVolumetricHeatCapacity(2628.5)
        heatcapacity.ConstantHeatCapacity.setFrozenVolumetricHeatCapacity(972.5)
        heatcapacity.ConstantHeatCapacity.setFrozenTemperature(86.7)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        heatcapacity = self.material.Thermal.HeatCapacity
        self.assertEqual(heatcapacity.ConstantHeatCapacity.getIncludeLatentHeat(), 0)
        self.assertEqual(heatcapacity.ConstantHeatCapacity.getUnfrozenVolumetricHeatCapacity(), 2628.5)
        self.assertEqual(heatcapacity.ConstantHeatCapacity.getFrozenVolumetricHeatCapacity(), 972.5)
        self.assertEqual(heatcapacity.ConstantHeatCapacity.getFrozenTemperature(), 86.7)
