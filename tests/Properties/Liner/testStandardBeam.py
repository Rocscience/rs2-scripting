import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestStandardBeam(unittest.TestCase):
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
    def testStandardBeamProperty(self):
        liner = self.liner
        self.liner.setLinerType(LinerTypes.STANDARD_BEAM)
        liner.StandardBeam.setUnitWeight(836.5)
        liner.StandardBeam.setIncludeWeightInStressAnalysis(0)
        liner.StandardBeam.setInitialTemperature(972.5)
        liner.StandardBeam.setMethod(GeometryChoice.THICKNESS)
        liner.StandardBeam.setThickness(86.7)
        liner.StandardBeam.setArea(762.9)
        liner.StandardBeam.setMomentOfInertia(1413.6)
        liner.StandardBeam.setYoungsModulus(468.3)
        liner.StandardBeam.setPoissonsRatio(2350.4)
        liner.StandardBeam.setMaterialType(MaterialType.PLASTIC)
        liner.StandardBeam.setCompressiveStrengthPeak(2598.3)
        liner.StandardBeam.setCompressiveStrengthResidual(2572.7)
        liner.StandardBeam.setTensileStrengthPeak(2605.0)
        liner.StandardBeam.setTensileStrengthResidual(3213.4)
        liner.StandardBeam.setSlidingGap(1)
        liner.StandardBeam.setStrainAtLocking(1508.0)
        liner.StandardBeam.setBeamElementFormulation(LinerFormulation.TIMOSHENKO)
        liner.StandardBeam.setAxialStrainExpansion(857.2)
        liner.StandardBeam.setActivateThermal(0)
        liner.StandardBeam.setStaticTemperatureMode(StaticWaterModes.GRID)
        liner.StandardBeam.setStaticTemperature(1475.5)
        liner.StandardBeam.setConductivity(2227.9)
        liner.StandardBeam.setSpecificHeatCapacity(3008.6)
        liner.StandardBeam.setThermalExpansion(0)
        liner.StandardBeam.setExpansionCoefficient(1006.5)
        liner.StandardBeam.setStageLinerProperties(1)
        liner.StandardBeam.setStaticTemperatureGridToUse("None")
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        self.assertEqual(liner.StandardBeam.getUnitWeight(), 836.5)
        self.assertEqual(liner.StandardBeam.getIncludeWeightInStressAnalysis(), 0)
        self.assertEqual(liner.StandardBeam.getInitialTemperature(), 972.5)
        self.assertEqual(liner.StandardBeam.getMethod(), GeometryChoice.THICKNESS)
        self.assertEqual(liner.StandardBeam.getThickness(), 86.7)
        self.assertEqual(liner.StandardBeam.getArea(), 762.9)
        self.assertEqual(liner.StandardBeam.getMomentOfInertia(), 1413.6)
        self.assertEqual(liner.StandardBeam.getYoungsModulus(), 468.3)
        self.assertEqual(liner.StandardBeam.getPoissonsRatio(), 2350.4)
        self.assertEqual(liner.StandardBeam.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(liner.StandardBeam.getCompressiveStrengthPeak(), 2598.3)
        self.assertEqual(liner.StandardBeam.getCompressiveStrengthResidual(), 2572.7)
        self.assertEqual(liner.StandardBeam.getTensileStrengthPeak(), 2605.0)
        self.assertEqual(liner.StandardBeam.getTensileStrengthResidual(), 3213.4)
        self.assertEqual(liner.StandardBeam.getSlidingGap(), 1)
        self.assertEqual(liner.StandardBeam.getStrainAtLocking(), 1508.0)
        self.assertEqual(liner.StandardBeam.getBeamElementFormulation(), LinerFormulation.TIMOSHENKO)
        self.assertEqual(liner.StandardBeam.getAxialStrainExpansion(), 857.2)
        self.assertEqual(liner.StandardBeam.getActivateThermal(), 0)
        self.assertEqual(liner.StandardBeam.getStaticTemperatureMode(), StaticWaterModes.GRID)
        self.assertEqual(liner.StandardBeam.getStaticTemperature(), 1475.5)
        self.assertEqual(liner.StandardBeam.getConductivity(), 2227.9)
        self.assertEqual(liner.StandardBeam.getSpecificHeatCapacity(), 3008.6)
        self.assertEqual(liner.StandardBeam.getThermalExpansion(), 0)
        self.assertEqual(liner.StandardBeam.getExpansionCoefficient(), 1006.5)
        self.assertEqual(liner.StandardBeam.getStageLinerProperties(), 1)
        self.assertEqual(liner.StandardBeam.getStaticTemperatureGridToUse(), "None")
    def testStandardBeamStageFactors(self):
        liner = self.liner
        self.liner.setLinerType(LinerTypes.STANDARD_BEAM)
        stageFactor = liner.StandardBeam.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setUnitWeightFactor(1257.7)
        stageFactor.setThicknessFactor(1702.5)
        stageFactor.setAreaFactor(857.5)
        stageFactor.setMomentOfInertiaFactor(2489.6)
        stageFactor.setYoungsModulusFactor(1772.3)
        stageFactor.setPoissonsRatioFactor(2188.4)
        stageFactor.setAxialStrainExpansionFactor(812.6)
        stageFactor.setCompressiveStrengthPeakFactor(208.8)
        stageFactor.setCompressiveStrengthResidualFactor(2180.6)
        stageFactor.setTensileStrengthPeakFactor(84.0)
        stageFactor.setTensileStrengthResidualFactor(870.1)
        stageFactor.setConductivityFactor(223.6)
        stageFactor.setSpecificHeatCapacityFactor(453.6)
        stageFactor.setExpansionCoefficientFactor(3206.5)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        stageFactor = liner.StandardBeam.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getUnitWeightFactor(), 1257.7)
        self.assertEqual(stageFactor.getThicknessFactor(), 1702.5)
        self.assertEqual(stageFactor.getAreaFactor(), 857.5)
        self.assertEqual(stageFactor.getMomentOfInertiaFactor(), 2489.6)
        self.assertEqual(stageFactor.getYoungsModulusFactor(), 1772.3)
        self.assertEqual(stageFactor.getPoissonsRatioFactor(), 2188.4)
        self.assertEqual(stageFactor.getAxialStrainExpansionFactor(), 812.6)
        self.assertEqual(stageFactor.getCompressiveStrengthPeakFactor(), 208.8)
        self.assertEqual(stageFactor.getCompressiveStrengthResidualFactor(), 2180.6)
        self.assertEqual(stageFactor.getTensileStrengthPeakFactor(), 84.0)
        self.assertEqual(stageFactor.getTensileStrengthResidualFactor(), 870.1)
        self.assertEqual(stageFactor.getConductivityFactor(), 223.6)
        self.assertEqual(stageFactor.getSpecificHeatCapacityFactor(), 453.6)
        self.assertEqual(stageFactor.getExpansionCoefficientFactor(), 3206.5)
