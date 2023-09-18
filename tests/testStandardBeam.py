import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestStandardBeam(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/BlankModelWithStageFactors.fez"
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
        self.liner.setLinerType(LinerTypes.P2_LINER_STANDARD_BEAM)
        liner.StandardBeam.setUnitWeight(208.8)
        liner.StandardBeam.setIncludeWeightInAnalysis(0)
        liner.StandardBeam.setMethod(GeometryChoice.LNP_USE_THICKNESS)
        liner.StandardBeam.setThickness(2706.7)
        liner.StandardBeam.setArea(1992.3)
        liner.StandardBeam.setMomentOfInertia(3100.1)
        liner.StandardBeam.setYoungsModulus(2194.8)
        liner.StandardBeam.setPoissonsRatio(3009.3)
        liner.StandardBeam.setMaterialType(MaterialType.PLASTIC)
        liner.StandardBeam.setCompressiveStrengthPeak(2048.2)
        liner.StandardBeam.setCompressiveStrengthResidual(165.0)
        liner.StandardBeam.setTensileStrengthPeak(1630.3)
        liner.StandardBeam.setTensileStrengthResidual(2108.0)
        liner.StandardBeam.setSlidingGap(0)
        liner.StandardBeam.setStrainAtLocking(1936.9)
        liner.StandardBeam.setBeamElementFormulation(LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
        liner.StandardBeam.setActivateThermal(1)
        liner.StandardBeam.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
        liner.StandardBeam.setStaticTemperature(996.1)
        liner.StandardBeam.setConductivity(1511.7)
        liner.StandardBeam.setSpecificHeatCapacity(2071.0)
        liner.StandardBeam.setThermalExpansion(0)
        liner.StandardBeam.setExpansionCoefficient(2136.3)
        liner.StandardBeam.setStageLinerProperties(1)
        liner.StandardBeam.setStaticTemperatureGridToUse("None")
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        self.assertEqual(liner.StandardBeam.getUnitWeight(), 208.8)
        self.assertEqual(liner.StandardBeam.getIncludeWeightInAnalysis(), 0)
        self.assertEqual(liner.StandardBeam.getMethod(), GeometryChoice.LNP_USE_THICKNESS)
        self.assertEqual(liner.StandardBeam.getThickness(), 2706.7)
        self.assertEqual(liner.StandardBeam.getArea(), 1992.3)
        self.assertEqual(liner.StandardBeam.getMomentOfInertia(), 3100.1)
        self.assertEqual(liner.StandardBeam.getYoungsModulus(), 2194.8)
        self.assertEqual(liner.StandardBeam.getPoissonsRatio(), 3009.3)
        self.assertEqual(liner.StandardBeam.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(liner.StandardBeam.getCompressiveStrengthPeak(), 2048.2)
        self.assertEqual(liner.StandardBeam.getCompressiveStrengthResidual(), 165.0)
        self.assertEqual(liner.StandardBeam.getTensileStrengthPeak(), 1630.3)
        self.assertEqual(liner.StandardBeam.getTensileStrengthResidual(), 2108.0)
        self.assertEqual(liner.StandardBeam.getSlidingGap(), 0)
        self.assertEqual(liner.StandardBeam.getStrainAtLocking(), 1936.9)
        self.assertEqual(liner.StandardBeam.getBeamElementFormulation(), LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
        self.assertEqual(liner.StandardBeam.getActivateThermal(), 1)
        self.assertEqual(liner.StandardBeam.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
        self.assertEqual(liner.StandardBeam.getStaticTemperature(), 996.1)
        self.assertEqual(liner.StandardBeam.getConductivity(), 1511.7)
        self.assertEqual(liner.StandardBeam.getSpecificHeatCapacity(), 2071.0)
        self.assertEqual(liner.StandardBeam.getThermalExpansion(), 0)
        self.assertEqual(liner.StandardBeam.getExpansionCoefficient(), 2136.3)
        self.assertEqual(liner.StandardBeam.getStageLinerProperties(), 1)
        self.assertEqual(liner.StandardBeam.getStaticTemperatureGridToUse(), "None")
    def testStandardBeamStageFactors(self):
        self.liner.setLinerType(LinerTypes.P2_LINER_STANDARD_BEAM)
        stageFactor = self.liner.StandardBeam.getStageFactors()[0]
        stageFactor.setThicknessFactor(3008.0)
        stageFactor.setAreaFactor(751.6)
        stageFactor.setMomentOfInertiaFactor(606.4)
        stageFactor.setYoungsModulusFactor(480.6)
        stageFactor.setPoissonsRatioFactor(2680.9)
        stageFactor.setAxialStrainExpansionFactor(749.1)
        stageFactor.setCompressiveStrengthPeakFactor(747.9)
        stageFactor.setCompressiveStrengthResidualFactor(1215.8)
        stageFactor.setTensileStrengthPeakFactor(2783.0)
        stageFactor.setTensileStrengthResidualFactor(876.2)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        stageFactor = self.liner.StandardBeam.getStageFactors()[0]
        self.assertEqual(stageFactor.getThicknessFactor(), 3008.0)
        self.assertEqual(stageFactor.getAreaFactor(), 751.6)
        self.assertEqual(stageFactor.getMomentOfInertiaFactor(), 606.4)
        self.assertEqual(stageFactor.getYoungsModulusFactor(), 480.6)
        self.assertEqual(stageFactor.getPoissonsRatioFactor(), 2680.9)
        self.assertEqual(stageFactor.getAxialStrainExpansionFactor(), 749.1)
        self.assertEqual(stageFactor.getCompressiveStrengthPeakFactor(), 747.9)
        self.assertEqual(stageFactor.getCompressiveStrengthResidualFactor(), 1215.8)
        self.assertEqual(stageFactor.getTensileStrengthPeakFactor(), 2783.0)
        self.assertEqual(stageFactor.getTensileStrengthResidualFactor(), 876.2)
