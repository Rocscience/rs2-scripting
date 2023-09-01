import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from src.rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestHyperbolicSoftening(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/blankProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testHyperbolicSofteningProperty(self):
        joint = self.joint
        self.joint.setSlipCriterion(JointTypes.JOINT_HYPERBOLIC_SOFTENING)
        joint.HyperbolicSoftening.setPeakCohesion(1469.7)
        joint.HyperbolicSoftening.setPeakFriction(673.4)
        joint.HyperbolicSoftening.setResCohesion(1277.9)
        joint.HyperbolicSoftening.setResFriction(1073.7)
        joint.HyperbolicSoftening.setTensileStrength(590.7)
        joint.HyperbolicSoftening.setResTensileStrength(2307.2)
        joint.HyperbolicSoftening.setDeltaR(2700.5)
        joint.HyperbolicSoftening.setInitialSlope(2999.3)
        joint.HyperbolicSoftening.setWorkSoftening(0)
        joint.HyperbolicSoftening.setNormalStiffness(1841.3)
        joint.HyperbolicSoftening.setShearStiffness(2718.9)
        joint.HyperbolicSoftening.setApplyPorePressure(1)
        joint.HyperbolicSoftening.setApplyAdditionalPressureInsideJoint(0)
        joint.HyperbolicSoftening.setAdditionalPressureType(AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        joint.HyperbolicSoftening.setAdditionalPressureInsideJoint(1153.1)
        joint.HyperbolicSoftening.setPiezoID(7531)
        joint.HyperbolicSoftening.setApplyPressureToLinerSideOnly(1)
        joint.HyperbolicSoftening.setApplyStageFactors(0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.HyperbolicSoftening.getPeakCohesion(), 1469.7)
        self.assertEqual(joint.HyperbolicSoftening.getPeakFriction(), 673.4)
        self.assertEqual(joint.HyperbolicSoftening.getResCohesion(), 1277.9)
        self.assertEqual(joint.HyperbolicSoftening.getResFriction(), 1073.7)
        self.assertEqual(joint.HyperbolicSoftening.getTensileStrength(), 590.7)
        self.assertEqual(joint.HyperbolicSoftening.getResTensileStrength(), 2307.2)
        self.assertEqual(joint.HyperbolicSoftening.getDeltaR(), 2700.5)
        self.assertEqual(joint.HyperbolicSoftening.getInitialSlope(), 2999.3)
        self.assertEqual(joint.HyperbolicSoftening.getWorkSoftening(), 0)
        self.assertEqual(joint.HyperbolicSoftening.getNormalStiffness(), 1841.3)
        self.assertEqual(joint.HyperbolicSoftening.getShearStiffness(), 2718.9)
        self.assertEqual(joint.HyperbolicSoftening.getApplyPorePressure(), 1)
        self.assertEqual(joint.HyperbolicSoftening.getApplyAdditionalPressureInsideJoint(), 0)
        self.assertEqual(joint.HyperbolicSoftening.getAdditionalPressureType(), AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        self.assertEqual(joint.HyperbolicSoftening.getAdditionalPressureInsideJoint(), 1153.1)
        self.assertEqual(joint.HyperbolicSoftening.getPiezoID(), 7531)
        self.assertEqual(joint.HyperbolicSoftening.getApplyPressureToLinerSideOnly(), 1)
        self.assertEqual(joint.HyperbolicSoftening.getApplyStageFactors(), 0)
