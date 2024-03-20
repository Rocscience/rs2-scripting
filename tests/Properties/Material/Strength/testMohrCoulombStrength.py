import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestMohrCoulombStrength(unittest.TestCase):
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
    def testMohrCoulombStrengthProperty(self):
        strength = self.material.Strength
        strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
        strength.MohrCoulombStrength.setPeakTensileStrength(836.5)
        strength.MohrCoulombStrength.setPeakFrictionAngle(2628.5)
        strength.MohrCoulombStrength.setPeakCohesion(972.5)
        strength.MohrCoulombStrength.setResidualTensileStrength(86.7)
        strength.MohrCoulombStrength.setResidualFrictionAngle(762.9)
        strength.MohrCoulombStrength.setResidualCohesion(1413.6)
        strength.MohrCoulombStrength.setDilationAngle(468.3)
        strength.MohrCoulombStrength.setApplySSRShearStrengthReduction(0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.MohrCoulombStrength.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(strength.MohrCoulombStrength.getPeakTensileStrength(), 836.5)
        self.assertEqual(strength.MohrCoulombStrength.getPeakFrictionAngle(), 2628.5)
        self.assertEqual(strength.MohrCoulombStrength.getPeakCohesion(), 972.5)
        self.assertEqual(strength.MohrCoulombStrength.getResidualTensileStrength(), 86.7)
        self.assertEqual(strength.MohrCoulombStrength.getResidualFrictionAngle(), 762.9)
        self.assertEqual(strength.MohrCoulombStrength.getResidualCohesion(), 1413.6)
        self.assertEqual(strength.MohrCoulombStrength.getDilationAngle(), 468.3)
        self.assertEqual(strength.MohrCoulombStrength.getApplySSRShearStrengthReduction(), 0)
    def testMohrCoulombStrengthStageFactors(self):
        strength = self.material.Strength
        stageFactor = strength.MohrCoulombStrength.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setResidualCohesionFactor(2598.3)
        stageFactor.setDilationAngleFactor(2572.7)
        stageFactor.setResidualFrictionAngleFactor(2605.0)
        stageFactor.setPeakCohesionFactor(3213.4)
        stageFactor.setPeakFrictionAngleFactor(176.8)
        stageFactor.setPeakTensileStrengthFactor(1508.0)
        stageFactor.setResidualTensileStrengthFactor(857.2)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        stageFactor = strength.MohrCoulombStrength.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getResidualCohesionFactor(), 2598.3)
        self.assertEqual(stageFactor.getDilationAngleFactor(), 2572.7)
        self.assertEqual(stageFactor.getResidualFrictionAngleFactor(), 2605.0)
        self.assertEqual(stageFactor.getPeakCohesionFactor(), 3213.4)
        self.assertEqual(stageFactor.getPeakFrictionAngleFactor(), 176.8)
        self.assertEqual(stageFactor.getPeakTensileStrengthFactor(), 1508.0)
        self.assertEqual(stageFactor.getResidualTensileStrengthFactor(), 857.2)
