import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from src.rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestGeosyntheticHyperbolic(unittest.TestCase):
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
    def testGeosyntheticHyperbolicProperty(self):
        joint = self.joint
        self.joint.setJointType(JointTypes.JOINT_HYPERBOLIC_SIMPLE)
        joint.GeosyntheticHyperbolic.setApplyAdditionalPressureInsideJoint(True)
        joint.GeosyntheticHyperbolic.setPeakAdhesionAtSigninf(10.1)
        joint.GeosyntheticHyperbolic.setPeakFrictionAngleAtSign0(10.1)
        joint.GeosyntheticHyperbolic.setResAdhesionAtSigninf(10.1)
        joint.GeosyntheticHyperbolic.setResFrictionAngleAtSign0(10.1)
        joint.GeosyntheticHyperbolic.setNormalStiffness(10.1)
        joint.GeosyntheticHyperbolic.setShearStiffness(10.1)
        joint.GeosyntheticHyperbolic.setApplyPorePressure(True)
        joint.GeosyntheticHyperbolic.setAdditionalPressureType(JointWaterPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        joint.GeosyntheticHyperbolic.setAdditionalPressureInsideJoint(10.1)
        joint.GeosyntheticHyperbolic.setPiezoID(1)
        joint.GeosyntheticHyperbolic.setApplyPressureToLinerSideOnly(True)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.GeosyntheticHyperbolic.getApplyAdditionalPressureInsideJoint(), True)
        self.assertEqual(joint.GeosyntheticHyperbolic.getPeakAdhesionAtSigninf(), 10.1)
        self.assertEqual(joint.GeosyntheticHyperbolic.getPeakFrictionAngleAtSign0(), 10.1)
        self.assertEqual(joint.GeosyntheticHyperbolic.getResAdhesionAtSigninf(), 10.1)
        self.assertEqual(joint.GeosyntheticHyperbolic.getResFrictionAngleAtSign0(), 10.1)
        self.assertEqual(joint.GeosyntheticHyperbolic.getNormalStiffness(), 10.1)
        self.assertEqual(joint.GeosyntheticHyperbolic.getShearStiffness(), 10.1)
        self.assertEqual(joint.GeosyntheticHyperbolic.getApplyPorePressure(), True)
        self.assertEqual(joint.GeosyntheticHyperbolic.getAdditionalPressureType(), JointWaterPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        self.assertEqual(joint.GeosyntheticHyperbolic.getAdditionalPressureInsideJoint(), 10.1)
        self.assertEqual(joint.GeosyntheticHyperbolic.getPiezoID(), 1)
        self.assertEqual(joint.GeosyntheticHyperbolic.getApplyPressureToLinerSideOnly(), True)
