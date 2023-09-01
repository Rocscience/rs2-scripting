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
        self.joint = self.model.getAllJointProperties()[0]
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testGeosyntheticHyperbolicProperty(self):
        joint = self.joint
        self.joint.setSlipCriterion(JointTypes.JOINT_HYPERBOLIC_SIMPLE)
        joint.GeosyntheticHyperbolic.setPeakAdhesionAtSigninf(2479.1)
        joint.GeosyntheticHyperbolic.setPeakFrictionAngleAtSign0(1142.0)
        joint.GeosyntheticHyperbolic.setResAdhesionAtSigninf(2104.7)
        joint.GeosyntheticHyperbolic.setResFrictionAngleAtSign0(2927.1)
        joint.GeosyntheticHyperbolic.setNormalStiffness(2013.5)
        joint.GeosyntheticHyperbolic.setShearStiffness(1100.1)
        joint.GeosyntheticHyperbolic.setApplyPorePressure(0)
        joint.GeosyntheticHyperbolic.setApplyAdditionalPressureInsideJoint(0)
        joint.GeosyntheticHyperbolic.setAdditionalPressureType(AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        joint.GeosyntheticHyperbolic.setAdditionalPressureInsideJoint(2344.5)
        joint.GeosyntheticHyperbolic.setPiezoID(31812)
        joint.GeosyntheticHyperbolic.setApplyPressureToLinerSideOnly(1)
        joint.GeosyntheticHyperbolic.setApplyStageFactors(1)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.GeosyntheticHyperbolic.getPeakAdhesionAtSigninf(), 2479.1)
        self.assertEqual(joint.GeosyntheticHyperbolic.getPeakFrictionAngleAtSign0(), 1142.0)
        self.assertEqual(joint.GeosyntheticHyperbolic.getResAdhesionAtSigninf(), 2104.7)
        self.assertEqual(joint.GeosyntheticHyperbolic.getResFrictionAngleAtSign0(), 2927.1)
        self.assertEqual(joint.GeosyntheticHyperbolic.getNormalStiffness(), 2013.5)
        self.assertEqual(joint.GeosyntheticHyperbolic.getShearStiffness(), 1100.1)
        self.assertEqual(joint.GeosyntheticHyperbolic.getApplyPorePressure(), 0)
        self.assertEqual(joint.GeosyntheticHyperbolic.getApplyAdditionalPressureInsideJoint(), 0)
        self.assertEqual(joint.GeosyntheticHyperbolic.getAdditionalPressureType(), AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        self.assertEqual(joint.GeosyntheticHyperbolic.getAdditionalPressureInsideJoint(), 2344.5)
        self.assertEqual(joint.GeosyntheticHyperbolic.getPiezoID(), 31812)
        self.assertEqual(joint.GeosyntheticHyperbolic.getApplyPressureToLinerSideOnly(), 1)
        self.assertEqual(joint.GeosyntheticHyperbolic.getApplyStageFactors(), 1)
