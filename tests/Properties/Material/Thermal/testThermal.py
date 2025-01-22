import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestThermal(unittest.TestCase):
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
    def testThermalProperty(self):
        material = self.material
        material.Thermal.setStaticTemperatureMode(StaticWaterModes.PORE_WATER_PRESSURE)
        material.Thermal.setStaticTemperature(836.5)
        material.Thermal.setWaterContent(ThermalWaterContentMethodType.DEFINE)
        material.Thermal.setWaterContentValue(0.2)
        material.Thermal.setThermalExpansion(0)
        material.Thermal.setExpansionCoefficient(972.5)
        material.Thermal.setDispersivity(1)
        material.Thermal.setLongitudinalDispersivity(762.9)
        material.Thermal.setTransverseDispersivity(1413.6)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        material = self.material
        self.assertEqual(material.Thermal.getStaticTemperatureMode(), StaticWaterModes.PORE_WATER_PRESSURE)
        self.assertEqual(material.Thermal.getStaticTemperature(), 836.5)
        self.assertEqual(material.Thermal.getWaterContent(), ThermalWaterContentMethodType.DEFINE)
        self.assertEqual(material.Thermal.getWaterContentValue(), 0.2)
        self.assertEqual(material.Thermal.getThermalExpansion(), 0)
        self.assertEqual(material.Thermal.getExpansionCoefficient(), 972.5)
        self.assertEqual(material.Thermal.getDispersivity(), 1)
        self.assertEqual(material.Thermal.getLongitudinalDispersivity(), 762.9)
        self.assertEqual(material.Thermal.getTransverseDispersivity(), 1413.6)
