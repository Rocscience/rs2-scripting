import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestHyperbolic(unittest.TestCase):
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
    def testHyperbolicProperty(self):
        strength = self.material.Strength
        strength.Hyperbolic.setMaterialType(MaterialType.PLASTIC)
        strength.Hyperbolic.setPeakFrictionAngle(836.5)
        strength.Hyperbolic.setPeakCohesion(2628.5)
        strength.Hyperbolic.setResidualFrictionAngle(972.5)
        strength.Hyperbolic.setResidualCohesion(86.7)
        strength.Hyperbolic.setDilationRatio(762.9)
        strength.Hyperbolic.setApplySSRShearStrengthReduction(0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.Hyperbolic.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(strength.Hyperbolic.getPeakFrictionAngle(), 836.5)
        self.assertEqual(strength.Hyperbolic.getPeakCohesion(), 2628.5)
        self.assertEqual(strength.Hyperbolic.getResidualFrictionAngle(), 972.5)
        self.assertEqual(strength.Hyperbolic.getResidualCohesion(), 86.7)
        self.assertEqual(strength.Hyperbolic.getDilationRatio(), 762.9)
        self.assertEqual(strength.Hyperbolic.getApplySSRShearStrengthReduction(), 0)
    def testHyperbolicStageFactors(self):
        strength = self.material.Strength
        stageFactor = strength.Hyperbolic.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setResidualCohesionFactor(468.3)
        stageFactor.setResidualFrictionAngleFactor(2350.4)
        stageFactor.setPeakCohesionFactor(2598.3)
        stageFactor.setPeakFrictionAngleFactor(2572.7)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        stageFactor = strength.Hyperbolic.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getResidualCohesionFactor(), 468.3)
        self.assertEqual(stageFactor.getResidualFrictionAngleFactor(), 2350.4)
        self.assertEqual(stageFactor.getPeakCohesionFactor(), 2598.3)
        self.assertEqual(stageFactor.getPeakFrictionAngleFactor(), 2572.7)
