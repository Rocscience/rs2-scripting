import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestHyperbolicSoftening(unittest.TestCase):
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
    def testHyperbolicSofteningProperty(self):
        joint = self.joint
        self.joint.setSlipCriterion(JointTypes.JOINT_HYPERBOLIC_SOFTENING)
        joint.HyperbolicSoftening.setPeakCohesion(836.5)
        joint.HyperbolicSoftening.setPeakFriction(2628.5)
        joint.HyperbolicSoftening.setResCohesion(972.5)
        joint.HyperbolicSoftening.setResFriction(86.7)
        joint.HyperbolicSoftening.setTensileStrength(762.9)
        joint.HyperbolicSoftening.setResTensileStrength(1413.6)
        joint.HyperbolicSoftening.setDeltaR(468.3)
        joint.HyperbolicSoftening.setInitialSlope(2350.4)
        joint.HyperbolicSoftening.setWorkSoftening(1)
        joint.HyperbolicSoftening.setNormalStiffness(2572.7)
        joint.HyperbolicSoftening.setShearStiffness(2605.0)
        joint.HyperbolicSoftening.setApplyPorePressure(1)
        joint.HyperbolicSoftening.setApplyAdditionalPressureInsideJoint(1)
        joint.HyperbolicSoftening.setAdditionalPressureType(AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        joint.HyperbolicSoftening.setAdditionalPressureInsideJoint(1508.0)
        joint.HyperbolicSoftening.setPiezoID(16759)
        joint.HyperbolicSoftening.setApplyPressureToLinerSideOnly(0)
        joint.HyperbolicSoftening.setApplyStageFactors(1)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.HyperbolicSoftening.getPeakCohesion(), 836.5)
        self.assertEqual(joint.HyperbolicSoftening.getPeakFriction(), 2628.5)
        self.assertEqual(joint.HyperbolicSoftening.getResCohesion(), 972.5)
        self.assertEqual(joint.HyperbolicSoftening.getResFriction(), 86.7)
        self.assertEqual(joint.HyperbolicSoftening.getTensileStrength(), 762.9)
        self.assertEqual(joint.HyperbolicSoftening.getResTensileStrength(), 1413.6)
        self.assertEqual(joint.HyperbolicSoftening.getDeltaR(), 468.3)
        self.assertEqual(joint.HyperbolicSoftening.getInitialSlope(), 2350.4)
        self.assertEqual(joint.HyperbolicSoftening.getWorkSoftening(), 1)
        self.assertEqual(joint.HyperbolicSoftening.getNormalStiffness(), 2572.7)
        self.assertEqual(joint.HyperbolicSoftening.getShearStiffness(), 2605.0)
        self.assertEqual(joint.HyperbolicSoftening.getApplyPorePressure(), 1)
        self.assertEqual(joint.HyperbolicSoftening.getApplyAdditionalPressureInsideJoint(), 1)
        self.assertEqual(joint.HyperbolicSoftening.getAdditionalPressureType(), AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        self.assertEqual(joint.HyperbolicSoftening.getAdditionalPressureInsideJoint(), 1508.0)
        self.assertEqual(joint.HyperbolicSoftening.getPiezoID(), 16759)
        self.assertEqual(joint.HyperbolicSoftening.getApplyPressureToLinerSideOnly(), 0)
        self.assertEqual(joint.HyperbolicSoftening.getApplyStageFactors(), 1)
