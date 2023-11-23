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
        self.liner.setLinerType(LinerTypes.P2_LINER_STANDARD_BEAM)
        liner.StandardBeam.setUnitWeight(836.5)
        liner.StandardBeam.setIncludeWeightInStressAnalysis(0)
        liner.StandardBeam.setMethod(GeometryChoice.LNP_USE_THICKNESS)
        liner.StandardBeam.setThickness(972.5)
        liner.StandardBeam.setArea(86.7)
        liner.StandardBeam.setMomentOfInertia(762.9)
        liner.StandardBeam.setYoungsModulus(1413.6)
        liner.StandardBeam.setPoissonsRatio(468.3)
        liner.StandardBeam.setMaterialType(MaterialType.PLASTIC)
        liner.StandardBeam.setCompressiveStrengthPeak(2350.4)
        liner.StandardBeam.setCompressiveStrengthResidual(2598.3)
        liner.StandardBeam.setTensileStrengthPeak(2572.7)
        liner.StandardBeam.setTensileStrengthResidual(2605.0)
        liner.StandardBeam.setSlidingGap(1)
        liner.StandardBeam.setStrainAtLocking(176.8)
        liner.StandardBeam.setBeamElementFormulation(LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
        liner.StandardBeam.setActivateThermal(1)
        liner.StandardBeam.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
        liner.StandardBeam.setStaticTemperature(857.2)
        liner.StandardBeam.setConductivity(3215.6)
        liner.StandardBeam.setSpecificHeatCapacity(1475.5)
        liner.StandardBeam.setThermalExpansion(0)
        liner.StandardBeam.setExpansionCoefficient(3008.6)
        liner.StandardBeam.setStageLinerProperties(0)
        liner.StandardBeam.setStaticTemperatureGridToUse("None")
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        self.assertEqual(liner.StandardBeam.getUnitWeight(), 836.5)
        self.assertEqual(liner.StandardBeam.getIncludeWeightInStressAnalysis(), 0)
        self.assertEqual(liner.StandardBeam.getMethod(), GeometryChoice.LNP_USE_THICKNESS)
        self.assertEqual(liner.StandardBeam.getThickness(), 972.5)
        self.assertEqual(liner.StandardBeam.getArea(), 86.7)
        self.assertEqual(liner.StandardBeam.getMomentOfInertia(), 762.9)
        self.assertEqual(liner.StandardBeam.getYoungsModulus(), 1413.6)
        self.assertEqual(liner.StandardBeam.getPoissonsRatio(), 468.3)
        self.assertEqual(liner.StandardBeam.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(liner.StandardBeam.getCompressiveStrengthPeak(), 2350.4)
        self.assertEqual(liner.StandardBeam.getCompressiveStrengthResidual(), 2598.3)
        self.assertEqual(liner.StandardBeam.getTensileStrengthPeak(), 2572.7)
        self.assertEqual(liner.StandardBeam.getTensileStrengthResidual(), 2605.0)
        self.assertEqual(liner.StandardBeam.getSlidingGap(), 1)
        self.assertEqual(liner.StandardBeam.getStrainAtLocking(), 176.8)
        self.assertEqual(liner.StandardBeam.getBeamElementFormulation(), LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
        self.assertEqual(liner.StandardBeam.getActivateThermal(), 1)
        self.assertEqual(liner.StandardBeam.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
        self.assertEqual(liner.StandardBeam.getStaticTemperature(), 857.2)
        self.assertEqual(liner.StandardBeam.getConductivity(), 3215.6)
        self.assertEqual(liner.StandardBeam.getSpecificHeatCapacity(), 1475.5)
        self.assertEqual(liner.StandardBeam.getThermalExpansion(), 0)
        self.assertEqual(liner.StandardBeam.getExpansionCoefficient(), 3008.6)
        self.assertEqual(liner.StandardBeam.getStageLinerProperties(), 0)
        self.assertEqual(liner.StandardBeam.getStaticTemperatureGridToUse(), "None")
