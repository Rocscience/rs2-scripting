import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestBartonBandisMaterial(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.mat = self.model.getAllMaterialProperties()[0]
        self.mat.Strength.setFailureCriterion(StrengthCriteriaTypes.JOINTED_MOHR_COULOMB)
        self.matJointOptions = self.mat.Strength.JointedMohrCoulomb.getJointOptions()
        self.jointmaterial = self.matJointOptions.getJoint(0)
        self.jointmaterial.BartonBandisMaterial.setApplyStageFactors(True)
        sf = self.jointmaterial.BartonBandisMaterial.stageFactorInterface.createStageFactor(1)
        self.jointmaterial.BartonBandisMaterial.stageFactorInterface.setDefinedStageFactors({ 1: sf })

    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testBartonBandisMaterialProperty(self):
        jointmaterial = self.jointmaterial
        jointmaterial.BartonBandisMaterial.setJCS(836.5)
        jointmaterial.BartonBandisMaterial.setJRC(2628.5)
        jointmaterial.BartonBandisMaterial.setResidualFrictionAngle(972.5)
        jointmaterial.BartonBandisMaterial.setResidualStrength(1)
        jointmaterial.BartonBandisMaterial.setApplyStageFactors(1)
        jointmaterial.BartonBandisMaterial.setDilationAngle(2.3)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.mat = self.model.getAllMaterialProperties()[0]
        self.mat.Strength.setFailureCriterion(StrengthCriteriaTypes.JOINTED_MOHR_COULOMB)
        self.matJointOptions = self.mat.Strength.JointedMohrCoulomb.getJointOptions()
        self.jointmaterial = self.matJointOptions.getJoint(0)
        jointmaterial = self.jointmaterial
        self.assertEqual(jointmaterial.BartonBandisMaterial.getJCS(), 836.5)
        self.assertEqual(jointmaterial.BartonBandisMaterial.getJRC(), 2628.5)
        self.assertEqual(jointmaterial.BartonBandisMaterial.getResidualFrictionAngle(), 972.5)
        self.assertEqual(jointmaterial.BartonBandisMaterial.getResidualStrength(), 1)
        self.assertEqual(jointmaterial.BartonBandisMaterial.getApplyStageFactors(), 1)
        self.assertEqual(jointmaterial.BartonBandisMaterial.getDilationAngle(), 2.3)
    def testBartonBandisMaterialStageFactors(self):
        stageFactor = self.jointmaterial.BartonBandisMaterial.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setJCSFactor(1413.6)
        stageFactor.setJRCFactor(468.3)
        stageFactor.setResidualFrictionAngleFactor(2350.4)
        stageFactor.setDilationAngleFactor(2.3)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.mat = self.model.getAllMaterialProperties()[0]
        self.mat.Strength.setFailureCriterion(StrengthCriteriaTypes.JOINTED_MOHR_COULOMB)
        self.matJointOptions = self.mat.Strength.JointedMohrCoulomb.getJointOptions()
        self.jointmaterial = self.matJointOptions.getJoint(0)
        stageFactor = self.jointmaterial.BartonBandisMaterial.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getJCSFactor(), 1413.6)
        self.assertEqual(stageFactor.getJRCFactor(), 468.3)
        self.assertEqual(stageFactor.getResidualFrictionAngleFactor(), 2350.4)
        self.assertEqual(stageFactor.getDilationAngleFactor(), 2.3)
