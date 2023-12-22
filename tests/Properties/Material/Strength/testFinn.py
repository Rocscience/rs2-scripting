import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestFinn(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testFinnProperty(self):
        strength = self.material.Strength
        strength.Finn.setPeakTensileStrength(836.5)
        strength.Finn.setPeakFrictionAngle(2628.5)
        strength.Finn.setPeakCohesion(972.5)
        strength.Finn.setResidualTensileStrength(86.7)
        strength.Finn.setResidualFrictionAngle(762.9)
        strength.Finn.setResidualCohesion(1413.6)
        strength.Finn.setDilationAngle(468.3)
        strength.Finn.setApplySSRShearStrengthReduction(0)
        strength.Finn.setFinnFormulation(FinnFormula.FINN_BYRNE)
        strength.Finn.setC1Parameter(2598.3)
        strength.Finn.setC2Parameter(2572.7)
        strength.Finn.setC3Parameter(2605.0)
        strength.Finn.setC4Parameter(3213.4)
        strength.Finn.setByrneDefinition(FinnByrneDefinition.FINN_BYRNE_N1)
        strength.Finn.setFinnByrneC1Parameter(176.8)
        strength.Finn.setFinnByrneC2Parameter(1508.0)
        strength.Finn.setN160(16759)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.Finn.getPeakTensileStrength(), 836.5)
        self.assertEqual(strength.Finn.getPeakFrictionAngle(), 2628.5)
        self.assertEqual(strength.Finn.getPeakCohesion(), 972.5)
        self.assertEqual(strength.Finn.getResidualTensileStrength(), 86.7)
        self.assertEqual(strength.Finn.getResidualFrictionAngle(), 762.9)
        self.assertEqual(strength.Finn.getResidualCohesion(), 1413.6)
        self.assertEqual(strength.Finn.getDilationAngle(), 468.3)
        self.assertEqual(strength.Finn.getApplySSRShearStrengthReduction(), 0)
        self.assertEqual(strength.Finn.getFinnFormulation(), FinnFormula.FINN_BYRNE)
        self.assertEqual(strength.Finn.getC1Parameter(), 2598.3)
        self.assertEqual(strength.Finn.getC2Parameter(), 2572.7)
        self.assertEqual(strength.Finn.getC3Parameter(), 2605.0)
        self.assertEqual(strength.Finn.getC4Parameter(), 3213.4)
        self.assertEqual(strength.Finn.getByrneDefinition(), FinnByrneDefinition.FINN_BYRNE_N1)
        self.assertEqual(strength.Finn.getFinnByrneC1Parameter(), 176.8)
        self.assertEqual(strength.Finn.getFinnByrneC2Parameter(), 1508.0)
        self.assertEqual(strength.Finn.getN160(), 16759)
