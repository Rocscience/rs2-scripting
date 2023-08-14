import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from src.rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestBartonBandis(unittest.TestCase):
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
    def testBartonBandisProperty(self):
        joint = self.joint
        self.joint.setJointType(JointTypes.JOINT_BARTON_BANDIS)
        joint.BartonBandis.setJCS(10.1)
        joint.BartonBandis.setNormalStiffness(10.1)
        joint.BartonBandis.setJRC(10.1)
        joint.BartonBandis.setShearStiffness(10.1)
        joint.BartonBandis.setResidualFrictionAngle(10.1)
        joint.BartonBandis.setResidualStrength(True)
        joint.BartonBandis.setApplyPorePressure(True)
        joint.BartonBandis.setApplyAdditionalPressureInsideJoint(True)
        joint.BartonBandis.setAdditionalPressureType(JointWaterPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        joint.BartonBandis.setAdditionalPressureInsideJoint(10.1)
        joint.BartonBandis.setPiezoID(1)
        joint.BartonBandis.setApplyPressureToLinerSideOnly(True)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.BartonBandis.getJCS(), 10.1)
        self.assertEqual(joint.BartonBandis.getNormalStiffness(), 10.1)
        self.assertEqual(joint.BartonBandis.getJRC(), 10.1)
        self.assertEqual(joint.BartonBandis.getShearStiffness(), 10.1)
        self.assertEqual(joint.BartonBandis.getResidualFrictionAngle(), 10.1)
        self.assertEqual(joint.BartonBandis.getResidualStrength(), True)
        self.assertEqual(joint.BartonBandis.getApplyPorePressure(), True)
        self.assertEqual(joint.BartonBandis.getApplyAdditionalPressureInsideJoint(), True)
        self.assertEqual(joint.BartonBandis.getAdditionalPressureType(), JointWaterPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        self.assertEqual(joint.BartonBandis.getAdditionalPressureInsideJoint(), 10.1)
        self.assertEqual(joint.BartonBandis.getPiezoID(), 1)
        self.assertEqual(joint.BartonBandis.getApplyPressureToLinerSideOnly(), True)
