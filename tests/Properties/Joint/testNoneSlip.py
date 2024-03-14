import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestNoneSlip(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testNoneSlipProperty(self):
        joint = self.joint
        self.joint.setSlipCriterion(JointTypes.NONE)
        joint.NoneSlip.setNormalStiffness(836.5)
        joint.NoneSlip.setShearStiffness(2628.5)
        joint.NoneSlip.setApplyPorePressure(0)
        joint.NoneSlip.setApplyAdditionalPressureInsideJoint(1)
        joint.NoneSlip.setAdditionalPressureType(AdditionalPressureType.PIEZOMETRIC_LINE)
        joint.NoneSlip.setAdditionalPressureInsideJoint(762.9)
        joint.NoneSlip.setPiezoID(11649)
        joint.NoneSlip.setApplyPressureToLinerSideOnly(0)
        joint.NoneSlip.setApplyStageFactors(0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.NoneSlip.getNormalStiffness(), 836.5)
        self.assertEqual(joint.NoneSlip.getShearStiffness(), 2628.5)
        self.assertEqual(joint.NoneSlip.getApplyPorePressure(), 0)
        self.assertEqual(joint.NoneSlip.getApplyAdditionalPressureInsideJoint(), 1)
        self.assertEqual(joint.NoneSlip.getAdditionalPressureType(), AdditionalPressureType.PIEZOMETRIC_LINE)
        self.assertEqual(joint.NoneSlip.getAdditionalPressureInsideJoint(), 762.9)
        self.assertEqual(joint.NoneSlip.getPiezoID(), 11649)
        self.assertEqual(joint.NoneSlip.getApplyPressureToLinerSideOnly(), 0)
        self.assertEqual(joint.NoneSlip.getApplyStageFactors(), 0)
    def testNoneSlipStageFactors(self):
        self.joint.setSlipCriterion(JointTypes.NONE)
        stageFactor = self.joint.NoneSlip.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setNormalStiffnessFactor(2598.3)
        stageFactor.setShearStiffnessFactor(2572.7)
        stageFactor.setAdditionalPressureInsideJointFactor(2605.0)
        stageFactor.setGroundwaterPressureFactor(2.2)
        stageFactor.setJointPermeableFactor(True)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        stageFactor = self.joint.NoneSlip.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getNormalStiffnessFactor(), 2598.3)
        self.assertEqual(stageFactor.getShearStiffnessFactor(), 2572.7)
        self.assertEqual(stageFactor.getAdditionalPressureInsideJointFactor(), 2605.0)
        self.assertEqual(stageFactor.getGroundwaterPressureFactor(), 2.2)
        self.assertEqual(stageFactor.getJointPermeableFactor(), True)
