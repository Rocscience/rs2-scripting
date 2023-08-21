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
        liner.Geosynthetic.setInitialTemperature(2802)
        liner.Geosynthetic.setTensileModulus(2384)
        liner.Geosynthetic.setMaterialType(MaterialType.PLASTIC)
        liner.Geosynthetic.setTensileStrengthPeak(2091)
        liner.Geosynthetic.setTensileStrengthResidual(497)
        liner.Geosynthetic.setActivateThermal(1)
        liner.Geosynthetic.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
        liner.Geosynthetic.setStaticTemperature(1594)
        liner.Geosynthetic.setConductivity(960)
        liner.Geosynthetic.setSpecificHeatCapacity(2976)
        liner.Geosynthetic.setThermalExpansion(1)
        liner.Geosynthetic.setExpansionCoefficient(1263)
        liner.Geosynthetic.setStageGeosyntheticProperties(0)
        liner.Geosynthetic.setStaticTemperatureGridToUse("None")
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        self.assertEqual(liner.Geosynthetic.getInitialTemperature(), 2802)
        self.assertEqual(liner.Geosynthetic.getTensileModulus(), 2384)
        self.assertEqual(liner.Geosynthetic.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(liner.Geosynthetic.getTensileStrengthPeak(), 2091)
        self.assertEqual(liner.Geosynthetic.getTensileStrengthResidual(), 497)
        self.assertEqual(liner.Geosynthetic.getActivateThermal(), 1)
        self.assertEqual(liner.Geosynthetic.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
        self.assertEqual(liner.Geosynthetic.getStaticTemperature(), 1594)
        self.assertEqual(liner.Geosynthetic.getConductivity(), 960)
        self.assertEqual(liner.Geosynthetic.getSpecificHeatCapacity(), 2976)
        self.assertEqual(liner.Geosynthetic.getThermalExpansion(), 1)
        self.assertEqual(liner.Geosynthetic.getExpansionCoefficient(), 1263)
        self.assertEqual(liner.Geosynthetic.getStageGeosyntheticProperties(), 0)
        self.assertEqual(liner.Geosynthetic.getStaticTemperatureGridToUse(), "None")
