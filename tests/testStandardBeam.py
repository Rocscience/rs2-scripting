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
        liner.StandardBeam.setUnitWeight(1786.0)
        liner.StandardBeam.setIncludeWeightInAnalysis(0)
        liner.StandardBeam.setMethod(GeometryChoice.LNP_USE_THICKNESS)
        liner.StandardBeam.setThickness(519.1)
        liner.StandardBeam.setArea(358.2)
        liner.StandardBeam.setMomentOfInertia(957.8)
        liner.StandardBeam.setYoungsModulus(2661.5)
        liner.StandardBeam.setPoissonsRatio(2461.8)
        liner.StandardBeam.setMaterialType(MaterialType.PLASTIC)
        liner.StandardBeam.setCompressiveStrengthPeak(2345.5)
        liner.StandardBeam.setCompressiveStrengthResidual(2445.0)
        liner.StandardBeam.setTensileStrengthPeak(799.3)
        liner.StandardBeam.setTensileStrengthResidual(3262.1)
        liner.StandardBeam.setSlidingGap(0)
        liner.StandardBeam.setStrainAtLocking(2134.6)
        liner.StandardBeam.setBeamElementFormulation(LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
        liner.StandardBeam.setActivateThermal(1)
        liner.StandardBeam.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
        liner.StandardBeam.setStaticTemperature(686.7)
        liner.StandardBeam.setConductivity(1629.6)
        liner.StandardBeam.setSpecificHeatCapacity(1314.9)
        liner.StandardBeam.setThermalExpansion(0)
        liner.StandardBeam.setExpansionCoefficient(42.4)
        liner.StandardBeam.setStageLinerProperties(1)
        liner.StandardBeam.setStaticTemperatureGridToUse("None")
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        self.assertEqual(liner.StandardBeam.getUnitWeight(), 1786.0)
        self.assertEqual(liner.StandardBeam.getIncludeWeightInAnalysis(), 0)
        self.assertEqual(liner.StandardBeam.getMethod(), GeometryChoice.LNP_USE_THICKNESS)
        self.assertEqual(liner.StandardBeam.getThickness(), 519.1)
        self.assertEqual(liner.StandardBeam.getArea(), 358.2)
        self.assertEqual(liner.StandardBeam.getMomentOfInertia(), 957.8)
        self.assertEqual(liner.StandardBeam.getYoungsModulus(), 2661.5)
        self.assertEqual(liner.StandardBeam.getPoissonsRatio(), 2461.8)
        self.assertEqual(liner.StandardBeam.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(liner.StandardBeam.getCompressiveStrengthPeak(), 2345.5)
        self.assertEqual(liner.StandardBeam.getCompressiveStrengthResidual(), 2445.0)
        self.assertEqual(liner.StandardBeam.getTensileStrengthPeak(), 799.3)
        self.assertEqual(liner.StandardBeam.getTensileStrengthResidual(), 3262.1)
        self.assertEqual(liner.StandardBeam.getSlidingGap(), 0)
        self.assertEqual(liner.StandardBeam.getStrainAtLocking(), 2134.6)
        self.assertEqual(liner.StandardBeam.getBeamElementFormulation(), LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
        self.assertEqual(liner.StandardBeam.getActivateThermal(), 1)
        self.assertEqual(liner.StandardBeam.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
        self.assertEqual(liner.StandardBeam.getStaticTemperature(), 686.7)
        self.assertEqual(liner.StandardBeam.getConductivity(), 1629.6)
        self.assertEqual(liner.StandardBeam.getSpecificHeatCapacity(), 1314.9)
        self.assertEqual(liner.StandardBeam.getThermalExpansion(), 0)
        self.assertEqual(liner.StandardBeam.getExpansionCoefficient(), 42.4)
        self.assertEqual(liner.StandardBeam.getStageLinerProperties(), 1)
        self.assertEqual(liner.StandardBeam.getStaticTemperatureGridToUse(), "None")
