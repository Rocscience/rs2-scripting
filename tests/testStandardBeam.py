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
        liner.StandardBeam.setUnitWeight(10.1)
        liner.StandardBeam.setIncludeWeightInAnalysis(True)
        liner.StandardBeam.setYoungsModulus(10.1)
        liner.StandardBeam.setMethod(GeometryChoice.LNP_USE_THICKNESS)
        liner.StandardBeam.setThickness(10.1)
        liner.StandardBeam.setPoissonsRatio(10.1)
        liner.StandardBeam.setArea(10.1)
        liner.StandardBeam.setMomentOfInertia(10.1)
        liner.StandardBeam.setMaterialType(MaterialType.PLASTIC)
        liner.StandardBeam.setCompressiveStrengthPeak(10.1)
        liner.StandardBeam.setCompressiveStrengthResidual(10.1)
        liner.StandardBeam.setTensileStrengthPeak(10.1)
        liner.StandardBeam.setTensileStrengthResidual(10.1)
        liner.StandardBeam.setSlidingGap(True)
        liner.StandardBeam.setStrainAtLocking(10.1)
        liner.StandardBeam.setBeamElementFormulation(LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
        liner.StandardBeam.setActivateThermal(True)
        liner.StandardBeam.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
        liner.StandardBeam.setStaticTemperature(10.1)
        liner.StandardBeam.setConductivity(10.1)
        liner.StandardBeam.setSpecificHeatCapacity(10.1)
        liner.StandardBeam.setThermalExpansion(True)
        liner.StandardBeam.setExpansionCoefficient(10.1)
        liner.StandardBeam.setStageLinerProperties(True)
        liner.StandardBeam.setStaticTemperatureGridToUse("None")
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        self.assertEqual(liner.StandardBeam.getUnitWeight(), 10.1)
        self.assertEqual(liner.StandardBeam.getIncludeWeightInAnalysis(), True)
        self.assertEqual(liner.StandardBeam.getYoungsModulus(), 10.1)
        self.assertEqual(liner.StandardBeam.getMethod(), GeometryChoice.LNP_USE_THICKNESS)
        self.assertEqual(liner.StandardBeam.getThickness(), 10.1)
        self.assertEqual(liner.StandardBeam.getPoissonsRatio(), 10.1)
        self.assertEqual(liner.StandardBeam.getArea(), 10.1)
        self.assertEqual(liner.StandardBeam.getMomentOfInertia(), 10.1)
        self.assertEqual(liner.StandardBeam.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(liner.StandardBeam.getCompressiveStrengthPeak(), 10.1)
        self.assertEqual(liner.StandardBeam.getCompressiveStrengthResidual(), 10.1)
        self.assertEqual(liner.StandardBeam.getTensileStrengthPeak(), 10.1)
        self.assertEqual(liner.StandardBeam.getTensileStrengthResidual(), 10.1)
        self.assertEqual(liner.StandardBeam.getSlidingGap(), True)
        self.assertEqual(liner.StandardBeam.getStrainAtLocking(), 10.1)
        self.assertEqual(liner.StandardBeam.getBeamElementFormulation(), LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
        self.assertEqual(liner.StandardBeam.getActivateThermal(), True)
        self.assertEqual(liner.StandardBeam.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
        self.assertEqual(liner.StandardBeam.getStaticTemperature(), 10.1)
        self.assertEqual(liner.StandardBeam.getConductivity(), 10.1)
        self.assertEqual(liner.StandardBeam.getSpecificHeatCapacity(), 10.1)
        self.assertEqual(liner.StandardBeam.getThermalExpansion(), True)
        self.assertEqual(liner.StandardBeam.getExpansionCoefficient(), 10.1)
        self.assertEqual(liner.StandardBeam.getStageLinerProperties(), True)
        self.assertEqual(liner.StandardBeam.getStaticTemperatureGridToUse(), "None")
