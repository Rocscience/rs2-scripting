import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestGeosynthetic(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
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
        liner.Geosynthetic.setInitialTemperature(836.5)
        liner.Geosynthetic.setTensileModulus(2628.5)
        liner.Geosynthetic.setMaterialType(MaterialType.PLASTIC)
        liner.Geosynthetic.setTensileStrengthPeak(972.5)
        liner.Geosynthetic.setTensileStrengthResidual(86.7)
        liner.Geosynthetic.setActivateThermal(1)
        liner.Geosynthetic.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
        liner.Geosynthetic.setStaticTemperature(1413.6)
        liner.Geosynthetic.setConductivity(468.3)
        liner.Geosynthetic.setSpecificHeatCapacity(2350.4)
        liner.Geosynthetic.setThermalExpansion(1)
        liner.Geosynthetic.setExpansionCoefficient(2572.7)
        liner.Geosynthetic.setStageGeosyntheticProperties(0)
        liner.Geosynthetic.setStaticTemperatureGridToUse("None")
        liner.Geosynthetic.setDefineRelativeStageFactors(True)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        self.assertEqual(liner.Geosynthetic.getInitialTemperature(), 836.5)
        self.assertEqual(liner.Geosynthetic.getTensileModulus(), 2628.5)
        self.assertEqual(liner.Geosynthetic.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(liner.Geosynthetic.getTensileStrengthPeak(), 972.5)
        self.assertEqual(liner.Geosynthetic.getTensileStrengthResidual(), 86.7)
        self.assertEqual(liner.Geosynthetic.getActivateThermal(), 1)
        self.assertEqual(liner.Geosynthetic.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
        self.assertEqual(liner.Geosynthetic.getStaticTemperature(), 1413.6)
        self.assertEqual(liner.Geosynthetic.getConductivity(), 468.3)
        self.assertEqual(liner.Geosynthetic.getSpecificHeatCapacity(), 2350.4)
        self.assertEqual(liner.Geosynthetic.getThermalExpansion(), 1)
        self.assertEqual(liner.Geosynthetic.getExpansionCoefficient(), 2572.7)
        self.assertEqual(liner.Geosynthetic.getStageGeosyntheticProperties(), 0)
        self.assertEqual(liner.Geosynthetic.getStaticTemperatureGridToUse(), "None")
        self.assertEqual(liner.Geosynthetic.getDefineRelativeStageFactors(), True)
    def testGeosyntheticStageFactors(self):
        self.liner.setLinerType(LinerTypes.P2_LINER_GEOSYNTHETIC)
        stageFactor = self.liner.Geosynthetic.getStageFactors()[0]
        stageFactor.setTensileModulusFactor(3213.4)
        stageFactor.setAxialStrainExpansionFactor(176.8)
        stageFactor.setTensileStrengthPeakFactor(1508.0)
        stageFactor.setTensileStrengthResidualFactor(857.2)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        stageFactor = self.liner.Geosynthetic.getStageFactors()[0]
        self.assertEqual(stageFactor.getTensileModulusFactor(), 3213.4)
        self.assertEqual(stageFactor.getAxialStrainExpansionFactor(), 176.8)
        self.assertEqual(stageFactor.getTensileStrengthPeakFactor(), 1508.0)
        self.assertEqual(stageFactor.getTensileStrengthResidualFactor(), 857.2)
