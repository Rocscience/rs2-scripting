import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestCableTruss(unittest.TestCase):
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
    def testCableTrussProperty(self):
        liner = self.liner
        self.liner.setLinerType(LinerTypes.CABLE_TRUSS)
        liner.CableTruss.setUnitWeight(836.5)
        liner.CableTruss.setInitialTemperature(2628.5)
        liner.CableTruss.setCableDiameter(972.5)
        liner.CableTruss.setOutofplaneSpacing(86.7)
        liner.CableTruss.setYoungsModulus(762.9)
        liner.CableTruss.setMaterialType(MaterialType.PLASTIC)
        liner.CableTruss.setTensileStrengthPeak(1413.6)
        liner.CableTruss.setTensileStrengthResidual(468.3)
        liner.CableTruss.setPreTensioning(0)
        liner.CableTruss.setPreTensioningForce(2598.3)
        liner.CableTruss.setAxialStrainExpansion(2572.7)
        liner.CableTruss.setActivateThermal(0)
        liner.CableTruss.setStaticTemperatureMode(StaticWaterModes.GRID)
        liner.CableTruss.setStaticTemperature(3213.4)
        liner.CableTruss.setConductivity(176.8)
        liner.CableTruss.setSpecificHeatCapacity(1508.0)
        liner.CableTruss.setThermalExpansion(0)
        liner.CableTruss.setExpansionCoefficient(3215.6)
        liner.CableTruss.setStageCableProperties(1)
        liner.CableTruss.setStaticTemperatureGridToUse("None")
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        self.assertEqual(liner.CableTruss.getUnitWeight(), 836.5)
        self.assertEqual(liner.CableTruss.getInitialTemperature(), 2628.5)
        self.assertEqual(liner.CableTruss.getCableDiameter(), 972.5)
        self.assertEqual(liner.CableTruss.getOutofplaneSpacing(), 86.7)
        self.assertEqual(liner.CableTruss.getYoungsModulus(), 762.9)
        self.assertEqual(liner.CableTruss.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(liner.CableTruss.getTensileStrengthPeak(), 1413.6)
        self.assertEqual(liner.CableTruss.getTensileStrengthResidual(), 468.3)
        self.assertEqual(liner.CableTruss.getPreTensioning(), 0)
        self.assertEqual(liner.CableTruss.getPreTensioningForce(), 2598.3)
        self.assertEqual(liner.CableTruss.getAxialStrainExpansion(), 2572.7)
        self.assertEqual(liner.CableTruss.getActivateThermal(), 0)
        self.assertEqual(liner.CableTruss.getStaticTemperatureMode(), StaticWaterModes.GRID)
        self.assertEqual(liner.CableTruss.getStaticTemperature(), 3213.4)
        self.assertEqual(liner.CableTruss.getConductivity(), 176.8)
        self.assertEqual(liner.CableTruss.getSpecificHeatCapacity(), 1508.0)
        self.assertEqual(liner.CableTruss.getThermalExpansion(), 0)
        self.assertEqual(liner.CableTruss.getExpansionCoefficient(), 3215.6)
        self.assertEqual(liner.CableTruss.getStageCableProperties(), 1)
        self.assertEqual(liner.CableTruss.getStaticTemperatureGridToUse(), "None")
    def testCableTrussStageFactors(self):
        liner = self.liner
        self.liner.setLinerType(LinerTypes.CABLE_TRUSS)
        stageFactor = liner.CableTruss.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setUnitWeightFactor(2227.9)
        stageFactor.setCableDiameterFactor(3008.6)
        stageFactor.setYoungsModulusFactor(2917.7)
        stageFactor.setAxialStrainExpansionFactor(1006.5)
        stageFactor.setTensileStrengthPeakFactor(1374.4)
        stageFactor.setTensileStrengthResidualFactor(1257.7)
        stageFactor.setConductivityFactor(1702.5)
        stageFactor.setSpecificHeatCapacityFactor(857.5)
        stageFactor.setExpansionCoefficientFactor(2489.6)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        stageFactor = liner.CableTruss.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getUnitWeightFactor(), 2227.9)
        self.assertEqual(stageFactor.getCableDiameterFactor(), 3008.6)
        self.assertEqual(stageFactor.getYoungsModulusFactor(), 2917.7)
        self.assertEqual(stageFactor.getAxialStrainExpansionFactor(), 1006.5)
        self.assertEqual(stageFactor.getTensileStrengthPeakFactor(), 1374.4)
        self.assertEqual(stageFactor.getTensileStrengthResidualFactor(), 1257.7)
        self.assertEqual(stageFactor.getConductivityFactor(), 1702.5)
        self.assertEqual(stageFactor.getSpecificHeatCapacityFactor(), 857.5)
        self.assertEqual(stageFactor.getExpansionCoefficientFactor(), 2489.6)
