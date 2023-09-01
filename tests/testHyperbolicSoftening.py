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
        joint.HyperbolicSoftening.setPeakCohesion(897.1)
        joint.HyperbolicSoftening.setPeakFriction(2950.3)
        joint.HyperbolicSoftening.setResCohesion(1556.1)
        joint.HyperbolicSoftening.setResFriction(2107.4)
        joint.HyperbolicSoftening.setTensileStrength(1316.3)
        joint.HyperbolicSoftening.setResTensileStrength(3209.1)
        joint.HyperbolicSoftening.setDeltaR(2545.6)
        joint.HyperbolicSoftening.setInitialSlope(797.6)
        joint.HyperbolicSoftening.setWorkSoftening(0)
        joint.HyperbolicSoftening.setNormalStiffness(364.4)
        joint.HyperbolicSoftening.setShearStiffness(2461.6)
        joint.HyperbolicSoftening.setApplyPorePressure(0)
        joint.HyperbolicSoftening.setApplyAdditionalPressureInsideJoint(1)
        joint.HyperbolicSoftening.setAdditionalPressureType(AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        joint.HyperbolicSoftening.setAdditionalPressureInsideJoint(12.1)
        joint.HyperbolicSoftening.setPiezoID(21873)
        joint.HyperbolicSoftening.setApplyPressureToLinerSideOnly(0)
        joint.HyperbolicSoftening.setApplyStageFactors(0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.HyperbolicSoftening.getPeakCohesion(), 897.1)
        self.assertEqual(joint.HyperbolicSoftening.getPeakFriction(), 2950.3)
        self.assertEqual(joint.HyperbolicSoftening.getResCohesion(), 1556.1)
        self.assertEqual(joint.HyperbolicSoftening.getResFriction(), 2107.4)
        self.assertEqual(joint.HyperbolicSoftening.getTensileStrength(), 1316.3)
        self.assertEqual(joint.HyperbolicSoftening.getResTensileStrength(), 3209.1)
        self.assertEqual(joint.HyperbolicSoftening.getDeltaR(), 2545.6)
        self.assertEqual(joint.HyperbolicSoftening.getInitialSlope(), 797.6)
        self.assertEqual(joint.HyperbolicSoftening.getWorkSoftening(), 0)
        self.assertEqual(joint.HyperbolicSoftening.getNormalStiffness(), 364.4)
        self.assertEqual(joint.HyperbolicSoftening.getShearStiffness(), 2461.6)
        self.assertEqual(joint.HyperbolicSoftening.getApplyPorePressure(), 0)
        self.assertEqual(joint.HyperbolicSoftening.getApplyAdditionalPressureInsideJoint(), 1)
        self.assertEqual(joint.HyperbolicSoftening.getAdditionalPressureType(), AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        self.assertEqual(joint.HyperbolicSoftening.getAdditionalPressureInsideJoint(), 12.1)
        self.assertEqual(joint.HyperbolicSoftening.getPiezoID(), 21873)
        self.assertEqual(joint.HyperbolicSoftening.getApplyPressureToLinerSideOnly(), 0)
        self.assertEqual(joint.HyperbolicSoftening.getApplyStageFactors(), 0)
