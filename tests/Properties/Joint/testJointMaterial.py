import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestJointMaterial(unittest.TestCase):
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
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)
    def testJointMaterialProperty(self):
        jointmaterial = self.jointmaterial
        jointmaterial.setSlipCriterion(JointTypes.GEOSYNTHETIC_HYPERBOLIC)
        jointmaterial.SetApplySSR(True)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.mat = self.model.getAllMaterialProperties()[0]
        self.mat.Strength.setFailureCriterion(StrengthCriteriaTypes.JOINTED_MOHR_COULOMB)
        self.matJointOptions = self.mat.Strength.JointedMohrCoulomb.getJointOptions()
        self.jointmaterial = self.matJointOptions.getJoint(0)
        jointmaterial = self.jointmaterial
        self.assertEqual(jointmaterial.getSlipCriterion(), JointTypes.GEOSYNTHETIC_HYPERBOLIC)
        self.assertEqual(jointmaterial.GetApplySSR(), True)
