import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

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
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)
    def testGeosyntheticProperty(self):
        liner = self.liner
        self.liner.setLinerType(LinerTypes.GEOSYNTHETIC)
        liner.Geosynthetic.setGeosyntheticUnitWeight(836.5)
        liner.Geosynthetic.setInitialTemperature(2628.5)
        liner.Geosynthetic.setTensileModulus(972.5)
        liner.Geosynthetic.setMaterialType(MaterialType.PLASTIC)
        liner.Geosynthetic.setTensileStrengthPeak(86.7)
        liner.Geosynthetic.setTensileStrengthResidual(762.9)
        liner.Geosynthetic.setActivateThermal(0)
        liner.Geosynthetic.setStaticTemperatureMode(StaticWaterModes.GRID)
        liner.Geosynthetic.setStaticTemperature(468.3)
        liner.Geosynthetic.setConductivity(2350.4)
        liner.Geosynthetic.setSpecificHeatCapacity(2598.3)
        liner.Geosynthetic.setThermalExpansion(0)
        liner.Geosynthetic.setExpansionCoefficient(2605.0)
        liner.Geosynthetic.setAxialStrainExpansion(3213.4)
        liner.Geosynthetic.setStageGeosyntheticProperties(1)
        liner.Geosynthetic.setStaticTemperatureGridToUse("None")
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        self.assertEqual(liner.Geosynthetic.getGeosyntheticUnitWeight(), 836.5)
        self.assertEqual(liner.Geosynthetic.getInitialTemperature(), 2628.5)
        self.assertEqual(liner.Geosynthetic.getTensileModulus(), 972.5)
        self.assertEqual(liner.Geosynthetic.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(liner.Geosynthetic.getTensileStrengthPeak(), 86.7)
        self.assertEqual(liner.Geosynthetic.getTensileStrengthResidual(), 762.9)
        self.assertEqual(liner.Geosynthetic.getActivateThermal(), 0)
        self.assertEqual(liner.Geosynthetic.getStaticTemperatureMode(), StaticWaterModes.GRID)
        self.assertEqual(liner.Geosynthetic.getStaticTemperature(), 468.3)
        self.assertEqual(liner.Geosynthetic.getConductivity(), 2350.4)
        self.assertEqual(liner.Geosynthetic.getSpecificHeatCapacity(), 2598.3)
        self.assertEqual(liner.Geosynthetic.getThermalExpansion(), 0)
        self.assertEqual(liner.Geosynthetic.getExpansionCoefficient(), 2605.0)
        self.assertEqual(liner.Geosynthetic.getAxialStrainExpansion(), 3213.4)
        self.assertEqual(liner.Geosynthetic.getStageGeosyntheticProperties(), 1)
        self.assertEqual(liner.Geosynthetic.getStaticTemperatureGridToUse(), "None")
    def testGeosyntheticStageFactors(self):
        liner = self.liner
        self.liner.setLinerType(LinerTypes.GEOSYNTHETIC)
        stageFactor = liner.Geosynthetic.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setGeosyntheticUnitWeightFactor(1508.0)
        stageFactor.setTensileModulusFactor(857.2)
        stageFactor.setAxialStrainExpansionFactor(3215.6)
        stageFactor.setTensileStrengthPeakFactor(1475.5)
        stageFactor.setTensileStrengthResidualFactor(2227.9)
        stageFactor.setConductivityFactor(3008.6)
        stageFactor.setSpecificHeatCapacityFactor(2917.7)
        stageFactor.setExpansionCoefficientFactor(1006.5)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        stageFactor = liner.Geosynthetic.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getGeosyntheticUnitWeightFactor(), 1508.0)
        self.assertEqual(stageFactor.getTensileModulusFactor(), 857.2)
        self.assertEqual(stageFactor.getAxialStrainExpansionFactor(), 3215.6)
        self.assertEqual(stageFactor.getTensileStrengthPeakFactor(), 1475.5)
        self.assertEqual(stageFactor.getTensileStrengthResidualFactor(), 2227.9)
        self.assertEqual(stageFactor.getConductivityFactor(), 3008.6)
        self.assertEqual(stageFactor.getSpecificHeatCapacityFactor(), 2917.7)
        self.assertEqual(stageFactor.getExpansionCoefficientFactor(), 1006.5)
