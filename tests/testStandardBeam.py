import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from src.rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestStandardBeam(unittest.TestCase):
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
    def testStandardBeamProperty(self):
        liner = self.liner
        self.liner.setLinerType(LinerTypes.P2_LINER_STANDARD_BEAM)
        liner.StandardBeam.setUnitWeight(208)
        liner.StandardBeam.setIncludeWeightInAnalysis(0)
        liner.StandardBeam.setMethod(GeometryChoice.LNP_USE_THICKNESS)
        liner.StandardBeam.setThickness(2706)
        liner.StandardBeam.setArea(1992)
        liner.StandardBeam.setMomentOfInertia(3100)
        liner.StandardBeam.setYoungsModulus(2194)
        liner.StandardBeam.setPoissonsRatio(3009)
        liner.StandardBeam.setMaterialType(MaterialType.PLASTIC)
        liner.StandardBeam.setCompressiveStrengthPeak(2048)
        liner.StandardBeam.setCompressiveStrengthResidual(165)
        liner.StandardBeam.setTensileStrengthPeak(1630)
        liner.StandardBeam.setTensileStrengthResidual(2108)
        liner.StandardBeam.setSlidingGap(0)
        liner.StandardBeam.setStrainAtLocking(1936)
        liner.StandardBeam.setBeamElementFormulation(LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
        liner.StandardBeam.setActivateThermal(1)
        liner.StandardBeam.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
        liner.StandardBeam.setStaticTemperature(996)
        liner.StandardBeam.setConductivity(1511)
        liner.StandardBeam.setSpecificHeatCapacity(2071)
        liner.StandardBeam.setThermalExpansion(0)
        liner.StandardBeam.setExpansionCoefficient(2136)
        liner.StandardBeam.setStageLinerProperties(1)
        liner.StandardBeam.setStaticTemperatureGridToUse("None")
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        self.assertEqual(liner.StandardBeam.getUnitWeight(), 208)
        self.assertEqual(liner.StandardBeam.getIncludeWeightInAnalysis(), 0)
        self.assertEqual(liner.StandardBeam.getMethod(), GeometryChoice.LNP_USE_THICKNESS)
        self.assertEqual(liner.StandardBeam.getThickness(), 2706)
        self.assertEqual(liner.StandardBeam.getArea(), 1992)
        self.assertEqual(liner.StandardBeam.getMomentOfInertia(), 3100)
        self.assertEqual(liner.StandardBeam.getYoungsModulus(), 2194)
        self.assertEqual(liner.StandardBeam.getPoissonsRatio(), 3009)
        self.assertEqual(liner.StandardBeam.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(liner.StandardBeam.getCompressiveStrengthPeak(), 2048)
        self.assertEqual(liner.StandardBeam.getCompressiveStrengthResidual(), 165)
        self.assertEqual(liner.StandardBeam.getTensileStrengthPeak(), 1630)
        self.assertEqual(liner.StandardBeam.getTensileStrengthResidual(), 2108)
        self.assertEqual(liner.StandardBeam.getSlidingGap(), 0)
        self.assertEqual(liner.StandardBeam.getStrainAtLocking(), 1936)
        self.assertEqual(liner.StandardBeam.getBeamElementFormulation(), LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
        self.assertEqual(liner.StandardBeam.getActivateThermal(), 1)
        self.assertEqual(liner.StandardBeam.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
        self.assertEqual(liner.StandardBeam.getStaticTemperature(), 996)
        self.assertEqual(liner.StandardBeam.getConductivity(), 1511)
        self.assertEqual(liner.StandardBeam.getSpecificHeatCapacity(), 2071)
        self.assertEqual(liner.StandardBeam.getThermalExpansion(), 0)
        self.assertEqual(liner.StandardBeam.getExpansionCoefficient(), 2136)
        self.assertEqual(liner.StandardBeam.getStageLinerProperties(), 1)
        self.assertEqual(liner.StandardBeam.getStaticTemperatureGridToUse(), "None")
