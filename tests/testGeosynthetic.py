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
        liner.Geosynthetic.setInitialTemperature(3008.0)
        liner.Geosynthetic.setTensileModulus(751.6)
        liner.Geosynthetic.setMaterialType(MaterialType.PLASTIC)
        liner.Geosynthetic.setTensileStrengthPeak(606.4)
        liner.Geosynthetic.setTensileStrengthResidual(480.6)
        liner.Geosynthetic.setActivateThermal(0)
        liner.Geosynthetic.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
        liner.Geosynthetic.setStaticTemperature(749.1)
        liner.Geosynthetic.setConductivity(747.9)
        liner.Geosynthetic.setSpecificHeatCapacity(1215.8)
        liner.Geosynthetic.setThermalExpansion(0)
        liner.Geosynthetic.setExpansionCoefficient(876.2)
        liner.Geosynthetic.setStageGeosyntheticProperties(0)
        liner.Geosynthetic.setStaticTemperatureGridToUse("None")
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        self.assertEqual(liner.Geosynthetic.getInitialTemperature(), 3008.0)
        self.assertEqual(liner.Geosynthetic.getTensileModulus(), 751.6)
        self.assertEqual(liner.Geosynthetic.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(liner.Geosynthetic.getTensileStrengthPeak(), 606.4)
        self.assertEqual(liner.Geosynthetic.getTensileStrengthResidual(), 480.6)
        self.assertEqual(liner.Geosynthetic.getActivateThermal(), 0)
        self.assertEqual(liner.Geosynthetic.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
        self.assertEqual(liner.Geosynthetic.getStaticTemperature(), 749.1)
        self.assertEqual(liner.Geosynthetic.getConductivity(), 747.9)
        self.assertEqual(liner.Geosynthetic.getSpecificHeatCapacity(), 1215.8)
        self.assertEqual(liner.Geosynthetic.getThermalExpansion(), 0)
        self.assertEqual(liner.Geosynthetic.getExpansionCoefficient(), 876.2)
        self.assertEqual(liner.Geosynthetic.getStageGeosyntheticProperties(), 0)
        self.assertEqual(liner.Geosynthetic.getStaticTemperatureGridToUse(), "None")
