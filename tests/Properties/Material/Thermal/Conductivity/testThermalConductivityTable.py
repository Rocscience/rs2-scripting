import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestThermalConductivityTables(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProjectTransientGroundwaterAndThermal.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        self.material.Thermal.Conductivity.setMethod(ThermalType.CUSTOM)
    @classmethod
    def tearDownClass(self):
        self.model.close()
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)

    def testThermalConductivitySuccess(self):
        newTableColA1 = [-1.11,0,1,2]
        newTableColA2 = [-1.22,0.2,1.3,2.4]

        newTableColB1 = [-1.13,0,1,2]
        newTableColB2 = [-1.24,0.2,1.3,2.4]

        self.material.Thermal.Conductivity.Tabular.setThermalConductivityTemperatureFunction(newTableColA1, newTableColA2)
        self.material.Thermal.Conductivity.Tabular.setThermalConductivityWaterContentFunction(newTableColB1, newTableColB2)

        result1 = self.material.Thermal.Conductivity.Tabular.getThermalConductivityTemperatureFunction()
        self.assertEqual(result1[0], newTableColA1)
        self.assertEqual(result1[1], newTableColA2)

        result2 =  self.material.Thermal.Conductivity.Tabular.getThermalConductivityWaterContentFunction()
        self.assertEqual(result2[0], newTableColB1)
        self.assertEqual(result2[1], newTableColB2)
    
    def testThermalConductivityFailureDifferentSize(self):
        validCol1 = [-1.11,0,1,2]
        validCol2 = [-1.22,0.2,1.3,2.4]
        self.material.Thermal.Conductivity.Tabular.setThermalConductivityTemperatureFunction(validCol1, validCol2)
        self.material.Thermal.Conductivity.Tabular.setThermalConductivityWaterContentFunction(validCol1, validCol2)

        invalidCol1 = [-1.11,0,1]
        invalidCol2 = [-1.22,0.2,1.3,2.4]

        with self.assertRaises(Exception):
            self.material.Thermal.Conductivity.Tabular.setThermalConductivityTemperatureFunction(invalidCol1, invalidCol2)
        with self.assertRaises(Exception):
            self.material.Thermal.Conductivity.Tabular.setThermalConductivityWaterContentFunction(invalidCol1, invalidCol2)

        result1 = self.material.Thermal.Conductivity.Tabular.getThermalConductivityTemperatureFunction()
        result2 = self.material.Thermal.Conductivity.Tabular.getThermalConductivityWaterContentFunction()
        self.assertEqual(result1[0], validCol1)
        self.assertEqual(result1[1], validCol2)
        self.assertEqual(result2[0], validCol1)
        self.assertEqual(result2[1], validCol2)

    def testThermalConductivityFilureNonIncreasingColumn1(self):
        validCol1 = [-1.11,0,1,2]
        validCol2 = [-1.22,0.2,1.3,2.4]
        self.material.Thermal.Conductivity.Tabular.setThermalConductivityTemperatureFunction(validCol1, validCol2)
        self.material.Thermal.Conductivity.Tabular.setThermalConductivityWaterContentFunction(validCol1, validCol2)

        invalidCol1 = [-1.11,0,1,1]
        invalidCol2 = [-1.22,0.2,1.3,2.4]

        with self.assertRaises(Exception):
            self.material.Thermal.Conductivity.Tabular.setThermalConductivityTemperatureFunction(invalidCol1, invalidCol2)
        with self.assertRaises(Exception):
            self.material.Thermal.Conductivity.Tabular.setThermalConductivityWaterContentFunction(invalidCol1, invalidCol2)

        result1 = self.material.Thermal.Conductivity.Tabular.getThermalConductivityTemperatureFunction()
        result2 = self.material.Thermal.Conductivity.Tabular.getThermalConductivityWaterContentFunction()
        self.assertEqual(result1[0], validCol1)
        self.assertEqual(result1[1], validCol2)
        self.assertEqual(result2[0], validCol1)
        self.assertEqual(result2[1], validCol2)

    def testThermalConductivityFailureNotEnoughRows(self):
        validCol1 = [-1.11,0,1,2]
        validCol2 = [-1.22,0.2,1.3,2.4]
        self.material.Thermal.Conductivity.Tabular.setThermalConductivityTemperatureFunction(validCol1, validCol2)
        self.material.Thermal.Conductivity.Tabular.setThermalConductivityWaterContentFunction(validCol1, validCol2)

        invalidCol1 = [-1.11]
        invalidCol2 = [-1.22]

        with self.assertRaises(Exception):
            self.material.Thermal.Conductivity.Tabular.setThermalConductivityTemperatureFunction(invalidCol1, invalidCol2)
        with self.assertRaises(Exception):
            self.material.Thermal.Conductivity.Tabular.setThermalConductivityWaterContentFunction(invalidCol1, invalidCol2)

        result1 = self.material.Thermal.Conductivity.Tabular.getThermalConductivityTemperatureFunction()
        result2 = self.material.Thermal.Conductivity.Tabular.getThermalConductivityWaterContentFunction()
        self.assertEqual(result1[0], validCol1)
        self.assertEqual(result1[1], validCol2)
        self.assertEqual(result2[0], validCol1)
        self.assertEqual(result2[1], validCol2)

