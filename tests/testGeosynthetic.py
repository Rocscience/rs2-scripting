import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from src.rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestGeosynthetic(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/blankProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testGeosyntheticProperty(self):
        liner = self.liner
        self.liner.setLinerType(LinerTypes.P2_LINER_GEOSYNTHETIC)
        liner.Geosynthetic.setInitialTemperature(10.1)
        liner.Geosynthetic.setTensileModulus(10.1)
        liner.Geosynthetic.setMaterialType(MaterialType.PLASTIC)
        liner.Geosynthetic.setTensileStrengthPeak(10.1)
        liner.Geosynthetic.setTensileStrengthResidual(10.1)
        liner.Geosynthetic.setActivateThermal(True)
        liner.Geosynthetic.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
        liner.Geosynthetic.setStaticTemperature(10.1)
        liner.Geosynthetic.setConductivity(10.1)
        liner.Geosynthetic.setSpecificHeatCapacity(10.1)
        liner.Geosynthetic.setThermalExpansion(True)
        liner.Geosynthetic.setExpansionCoefficient(10.1)
        liner.Geosynthetic.setStageGeosyntheticProperties(True)
        liner.Geosynthetic.setStaticTemperatureGridToUse("None")
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        self.assertEqual(liner.Geosynthetic.getInitialTemperature(), 10.1)
        self.assertEqual(liner.Geosynthetic.getTensileModulus(), 10.1)
        self.assertEqual(liner.Geosynthetic.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(liner.Geosynthetic.getTensileStrengthPeak(), 10.1)
        self.assertEqual(liner.Geosynthetic.getTensileStrengthResidual(), 10.1)
        self.assertEqual(liner.Geosynthetic.getActivateThermal(), True)
        self.assertEqual(liner.Geosynthetic.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
        self.assertEqual(liner.Geosynthetic.getStaticTemperature(), 10.1)
        self.assertEqual(liner.Geosynthetic.getConductivity(), 10.1)
        self.assertEqual(liner.Geosynthetic.getSpecificHeatCapacity(), 10.1)
        self.assertEqual(liner.Geosynthetic.getThermalExpansion(), True)
        self.assertEqual(liner.Geosynthetic.getExpansionCoefficient(), 10.1)
        self.assertEqual(liner.Geosynthetic.getStageGeosyntheticProperties(), True)
        self.assertEqual(liner.Geosynthetic.getStaticTemperatureGridToUse(), "None")
