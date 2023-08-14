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
        blankModelPath = f"{parentDirectory}/resources/blankProject.fez"
        self.joint = self.model.getAllJointProperties()[0]
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testHyperbolicSofteningProperty(self):
        joint = self.joint
        self.joint.setJointType(JointTypes.JOINT_HYPERBOLIC_SIMPLE)
        joint.HyperbolicSoftening.setPeakCohesion(10.1)
        joint.HyperbolicSoftening.setPeakFriction(10.1)
        joint.HyperbolicSoftening.setResCohesion(10.1)
        joint.HyperbolicSoftening.setResFriction(10.1)
        joint.HyperbolicSoftening.setTensileStrength(10.1)
        joint.HyperbolicSoftening.setResTensileStrength(10.1)
        joint.HyperbolicSoftening.setDeltaR(10.1)
        joint.HyperbolicSoftening.setInitialSlope(10.1)
        joint.HyperbolicSoftening.setWorkSoftening(True)
        joint.HyperbolicSoftening.setNormalStiffness(10.1)
        joint.HyperbolicSoftening.setShearStiffness(10.1)
        joint.HyperbolicSoftening.setApplyPorePressure(True)
        joint.HyperbolicSoftening.setApplyAdditionalPressureInsideJoint(True)
        joint.HyperbolicSoftening.setAdditionalPressureType(JointWaterPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        joint.HyperbolicSoftening.setAdditionalPressureInsideJoint(10.1)
        joint.HyperbolicSoftening.setPiezoID(1)
        joint.HyperbolicSoftening.setApplyPressureToLinerSideOnly(True)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.HyperbolicSoftening.getPeakCohesion(), 10.1)
        self.assertEqual(joint.HyperbolicSoftening.getPeakFriction(), 10.1)
        self.assertEqual(joint.HyperbolicSoftening.getResCohesion(), 10.1)
        self.assertEqual(joint.HyperbolicSoftening.getResFriction(), 10.1)
        self.assertEqual(joint.HyperbolicSoftening.getTensileStrength(), 10.1)
        self.assertEqual(joint.HyperbolicSoftening.getResTensileStrength(), 10.1)
        self.assertEqual(joint.HyperbolicSoftening.getDeltaR(), 10.1)
        self.assertEqual(joint.HyperbolicSoftening.getInitialSlope(), 10.1)
        self.assertEqual(joint.HyperbolicSoftening.getWorkSoftening(), True)
        self.assertEqual(joint.HyperbolicSoftening.getNormalStiffness(), 10.1)
        self.assertEqual(joint.HyperbolicSoftening.getShearStiffness(), 10.1)
        self.assertEqual(joint.HyperbolicSoftening.getApplyPorePressure(), True)
        self.assertEqual(joint.HyperbolicSoftening.getApplyAdditionalPressureInsideJoint(), True)
        self.assertEqual(joint.HyperbolicSoftening.getAdditionalPressureType(), JointWaterPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        self.assertEqual(joint.HyperbolicSoftening.getAdditionalPressureInsideJoint(), 10.1)
        self.assertEqual(joint.HyperbolicSoftening.getPiezoID(), 1)
        self.assertEqual(joint.HyperbolicSoftening.getApplyPressureToLinerSideOnly(), True)
