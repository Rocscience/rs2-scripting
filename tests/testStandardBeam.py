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
        liner.StandardBeam.setUnitWeight(647)
        liner.StandardBeam.setIncludeWeightInAnalysis(1)
        liner.StandardBeam.setMethod(GeometryChoice.LNP_USE_THICKNESS)
        liner.StandardBeam.setThickness(2321)
        liner.StandardBeam.setArea(2386)
        liner.StandardBeam.setMomentOfInertia(1869)
        liner.StandardBeam.setYoungsModulus(655)
        liner.StandardBeam.setPoissonsRatio(2973)
        liner.StandardBeam.setMaterialType(MaterialType.PLASTIC)
        liner.StandardBeam.setCompressiveStrengthPeak(1293)
        liner.StandardBeam.setCompressiveStrengthResidual(2145)
        liner.StandardBeam.setTensileStrengthPeak(3178)
        liner.StandardBeam.setTensileStrengthResidual(163)
        liner.StandardBeam.setSlidingGap(1)
        liner.StandardBeam.setStrainAtLocking(1314)
        liner.StandardBeam.setBeamElementFormulation(LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
        liner.StandardBeam.setActivateThermal(0)
        liner.StandardBeam.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
        liner.StandardBeam.setStaticTemperature(2599)
        liner.StandardBeam.setConductivity(1125)
        liner.StandardBeam.setSpecificHeatCapacity(2850)
        liner.StandardBeam.setThermalExpansion(1)
        liner.StandardBeam.setExpansionCoefficient(2781)
        liner.StandardBeam.setStageLinerProperties(0)
        liner.StandardBeam.setStaticTemperatureGridToUse("None")
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        self.assertEqual(liner.StandardBeam.getUnitWeight(), 647)
        self.assertEqual(liner.StandardBeam.getIncludeWeightInAnalysis(), 1)
        self.assertEqual(liner.StandardBeam.getMethod(), GeometryChoice.LNP_USE_THICKNESS)
        self.assertEqual(liner.StandardBeam.getThickness(), 2321)
        self.assertEqual(liner.StandardBeam.getArea(), 2386)
        self.assertEqual(liner.StandardBeam.getMomentOfInertia(), 1869)
        self.assertEqual(liner.StandardBeam.getYoungsModulus(), 655)
        self.assertEqual(liner.StandardBeam.getPoissonsRatio(), 2973)
        self.assertEqual(liner.StandardBeam.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(liner.StandardBeam.getCompressiveStrengthPeak(), 1293)
        self.assertEqual(liner.StandardBeam.getCompressiveStrengthResidual(), 2145)
        self.assertEqual(liner.StandardBeam.getTensileStrengthPeak(), 3178)
        self.assertEqual(liner.StandardBeam.getTensileStrengthResidual(), 163)
        self.assertEqual(liner.StandardBeam.getSlidingGap(), 1)
        self.assertEqual(liner.StandardBeam.getStrainAtLocking(), 1314)
        self.assertEqual(liner.StandardBeam.getBeamElementFormulation(), LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
        self.assertEqual(liner.StandardBeam.getActivateThermal(), 0)
        self.assertEqual(liner.StandardBeam.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
        self.assertEqual(liner.StandardBeam.getStaticTemperature(), 2599)
        self.assertEqual(liner.StandardBeam.getConductivity(), 1125)
        self.assertEqual(liner.StandardBeam.getSpecificHeatCapacity(), 2850)
        self.assertEqual(liner.StandardBeam.getThermalExpansion(), 1)
        self.assertEqual(liner.StandardBeam.getExpansionCoefficient(), 2781)
        self.assertEqual(liner.StandardBeam.getStageLinerProperties(), 0)
        self.assertEqual(liner.StandardBeam.getStaticTemperatureGridToUse(), "None")
