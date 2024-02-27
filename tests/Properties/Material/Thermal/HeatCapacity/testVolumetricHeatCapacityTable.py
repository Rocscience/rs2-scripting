import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestVolumetricHeatCapacityTable(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProjectTransientGroundwaterAndThermal.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        self.material.Thermal.HeatCapacity.setType(ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CUSTOM)
    @classmethod
    def tearDownClass(self):
        self.model.close()
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)

    def testUnsaturatedZoneTableSuccess(self):
        newTableColA1 = [-1.11,0,1,2]
        newTableColA2 = [-1.22,0.2,1.3,2.4]

        newTableColB1 = [-1.13,0,1,2]
        newTableColB2 = [-1.24,0.2,1.3,2.4]

        self.material.Thermal.HeatCapacity.CustomHeatCapacity.setVolumetricHeatCapacityVsTemperatureTable(newTableColA1, newTableColA2)
        self.material.Thermal.HeatCapacity.CustomHeatCapacity.setVolumetricHeatCapacityVsWaterContentTable(newTableColB1, newTableColB2)

        result1 = self.material.Thermal.HeatCapacity.CustomHeatCapacity.getVolumetricHeatCapacityVsTemperatureTable()
        self.assertEqual(result1[0], newTableColA1)
        self.assertEqual(result1[1], newTableColA2)

        result2 =  self.material.Thermal.HeatCapacity.CustomHeatCapacity.getVolumetricHeatCapacityVsWaterContentTable()
        self.assertEqual(result2[0], newTableColB1)
        self.assertEqual(result2[1], newTableColB2)
    
    def testUnsaturatedZoneTableFailureDifferentSize(self):
        validCol1 = [-1.11,0,1,2]
        validCol2 = [-1.22,0.2,1.3,2.4]
        self.material.Thermal.HeatCapacity.CustomHeatCapacity.setVolumetricHeatCapacityVsTemperatureTable(validCol1, validCol2)
        self.material.Thermal.HeatCapacity.CustomHeatCapacity.setVolumetricHeatCapacityVsWaterContentTable(validCol1, validCol2)

        invalidCol1 = [-1.11,0,1]
        invalidCol2 = [-1.22,0.2,1.3,2.4]

        with self.assertRaises(Exception):
            self.material.Thermal.HeatCapacity.CustomHeatCapacity.setVolumetricHeatCapacityVsTemperatureTable(invalidCol1, invalidCol2)
        with self.assertRaises(Exception):
            self.material.Thermal.HeatCapacity.CustomHeatCapacity.setVolumetricHeatCapacityVsWaterContentTable(invalidCol1, invalidCol2)

        result1 = self.material.Thermal.HeatCapacity.CustomHeatCapacity.getVolumetricHeatCapacityVsTemperatureTable()
        result2 = self.material.Thermal.HeatCapacity.CustomHeatCapacity.getVolumetricHeatCapacityVsWaterContentTable()
        self.assertEqual(result1[0], validCol1)
        self.assertEqual(result1[1], validCol2)
        self.assertEqual(result2[0], validCol1)
        self.assertEqual(result2[1], validCol2)

    def testUnsaturatedZoneTableFailureNotEnoughRows(self):
        validCol1 = [-1.11,0,1,2]
        validCol2 = [-1.22,0.2,1.3,2.4]
        self.material.Thermal.HeatCapacity.CustomHeatCapacity.setVolumetricHeatCapacityVsTemperatureTable(validCol1, validCol2)
        self.material.Thermal.HeatCapacity.CustomHeatCapacity.setVolumetricHeatCapacityVsWaterContentTable(validCol1, validCol2)

        invalidCol1 = [-1.11]
        invalidCol2 = [-1.22]

        with self.assertRaises(Exception):
            self.material.Thermal.HeatCapacity.CustomHeatCapacity.setVolumetricHeatCapacityVsTemperatureTable(invalidCol1, invalidCol2)
        with self.assertRaises(Exception):
            self.material.Thermal.HeatCapacity.CustomHeatCapacity.setVolumetricHeatCapacityVsWaterContentTable(invalidCol1, invalidCol2)

        result1 = self.material.Thermal.HeatCapacity.CustomHeatCapacity.getVolumetricHeatCapacityVsTemperatureTable()
        result2 = self.material.Thermal.HeatCapacity.CustomHeatCapacity.getVolumetricHeatCapacityVsWaterContentTable()
        self.assertEqual(result1[0], validCol1)
        self.assertEqual(result1[1], validCol2)
        self.assertEqual(result2[0], validCol1)
        self.assertEqual(result2[1], validCol2)

