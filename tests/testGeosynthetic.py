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
        liner.Geosynthetic.setInitialTemperature(849.3)
        liner.Geosynthetic.setTensileModulus(1991.1)
        liner.Geosynthetic.setMaterialType(MaterialType.PLASTIC)
        liner.Geosynthetic.setTensileStrengthPeak(1236.8)
        liner.Geosynthetic.setTensileStrengthResidual(1018.9)
        liner.Geosynthetic.setActivateThermal(0)
        liner.Geosynthetic.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
        liner.Geosynthetic.setStaticTemperature(2451.4)
        liner.Geosynthetic.setConductivity(1946.8)
        liner.Geosynthetic.setSpecificHeatCapacity(2729.6)
        liner.Geosynthetic.setThermalExpansion(1)
        liner.Geosynthetic.setExpansionCoefficient(2532.8)
        liner.Geosynthetic.setStageGeosyntheticProperties(0)
        liner.Geosynthetic.setStaticTemperatureGridToUse("None")
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        self.assertEqual(liner.Geosynthetic.getInitialTemperature(), 849.3)
        self.assertEqual(liner.Geosynthetic.getTensileModulus(), 1991.1)
        self.assertEqual(liner.Geosynthetic.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(liner.Geosynthetic.getTensileStrengthPeak(), 1236.8)
        self.assertEqual(liner.Geosynthetic.getTensileStrengthResidual(), 1018.9)
        self.assertEqual(liner.Geosynthetic.getActivateThermal(), 0)
        self.assertEqual(liner.Geosynthetic.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
        self.assertEqual(liner.Geosynthetic.getStaticTemperature(), 2451.4)
        self.assertEqual(liner.Geosynthetic.getConductivity(), 1946.8)
        self.assertEqual(liner.Geosynthetic.getSpecificHeatCapacity(), 2729.6)
        self.assertEqual(liner.Geosynthetic.getThermalExpansion(), 1)
        self.assertEqual(liner.Geosynthetic.getExpansionCoefficient(), 2532.8)
        self.assertEqual(liner.Geosynthetic.getStageGeosyntheticProperties(), 0)
        self.assertEqual(liner.Geosynthetic.getStaticTemperatureGridToUse(), "None")
