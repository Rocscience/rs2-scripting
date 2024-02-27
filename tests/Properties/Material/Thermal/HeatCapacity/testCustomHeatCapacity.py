import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestCustomHeatCapacity(unittest.TestCase):
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
    def testCustomHeatCapacityProperty(self):
        heatcapacity = self.material.Thermal.HeatCapacity
        heatcapacity.CustomHeatCapacity.setIncludeLatentHeat(0)
        heatcapacity.CustomHeatCapacity.setDependence(ThermalVolumetricDepencenceType.THERMAL_VOLUMETRIC_DEPENDENCE_WATER_CONTENT)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        heatcapacity = self.material.Thermal.HeatCapacity
        self.assertEqual(heatcapacity.CustomHeatCapacity.getIncludeLatentHeat(), 0)
        self.assertEqual(heatcapacity.CustomHeatCapacity.getDependence(), ThermalVolumetricDepencenceType.THERMAL_VOLUMETRIC_DEPENDENCE_WATER_CONTENT)
