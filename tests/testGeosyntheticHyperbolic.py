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
        joint.GeosyntheticHyperbolic.setPeakAdhesionAtSigninf(843.7)
        joint.GeosyntheticHyperbolic.setPeakFrictionAngleAtSign0(1801.2)
        joint.GeosyntheticHyperbolic.setResAdhesionAtSigninf(3251.7)
        joint.GeosyntheticHyperbolic.setResFrictionAngleAtSign0(2197.0)
        joint.GeosyntheticHyperbolic.setNormalStiffness(554.1)
        joint.GeosyntheticHyperbolic.setShearStiffness(385.0)
        joint.GeosyntheticHyperbolic.setApplyPorePressure(0)
        joint.GeosyntheticHyperbolic.setApplyAdditionalPressureInsideJoint(1)
        joint.GeosyntheticHyperbolic.setAdditionalPressureType(AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        joint.GeosyntheticHyperbolic.setAdditionalPressureInsideJoint(612.6)
        joint.GeosyntheticHyperbolic.setPiezoID(15444)
        joint.GeosyntheticHyperbolic.setApplyPressureToLinerSideOnly(1)
        joint.GeosyntheticHyperbolic.setApplyStageFactors(1)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.GeosyntheticHyperbolic.getPeakAdhesionAtSigninf(), 843.7)
        self.assertEqual(joint.GeosyntheticHyperbolic.getPeakFrictionAngleAtSign0(), 1801.2)
        self.assertEqual(joint.GeosyntheticHyperbolic.getResAdhesionAtSigninf(), 3251.7)
        self.assertEqual(joint.GeosyntheticHyperbolic.getResFrictionAngleAtSign0(), 2197.0)
        self.assertEqual(joint.GeosyntheticHyperbolic.getNormalStiffness(), 554.1)
        self.assertEqual(joint.GeosyntheticHyperbolic.getShearStiffness(), 385.0)
        self.assertEqual(joint.GeosyntheticHyperbolic.getApplyPorePressure(), 0)
        self.assertEqual(joint.GeosyntheticHyperbolic.getApplyAdditionalPressureInsideJoint(), 1)
        self.assertEqual(joint.GeosyntheticHyperbolic.getAdditionalPressureType(), AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        self.assertEqual(joint.GeosyntheticHyperbolic.getAdditionalPressureInsideJoint(), 612.6)
        self.assertEqual(joint.GeosyntheticHyperbolic.getPiezoID(), 15444)
        self.assertEqual(joint.GeosyntheticHyperbolic.getApplyPressureToLinerSideOnly(), 1)
        self.assertEqual(joint.GeosyntheticHyperbolic.getApplyStageFactors(), 1)
