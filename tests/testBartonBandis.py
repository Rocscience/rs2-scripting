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
        self.joint = self.model.getAllJointProperties()[0]
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testBartonBandisProperty(self):
        joint = self.joint
        self.joint.setSlipCriterion(JointTypes.JOINT_BARTON_BANDIS)
        joint.BartonBandis.setJCS(1525.5)
        joint.BartonBandis.setJRC(1068.4)
        joint.BartonBandis.setResidualFrictionAngle(2610.1)
        joint.BartonBandis.setResidualStrength(0)
        joint.BartonBandis.setNormalStiffness(1829.8)
        joint.BartonBandis.setShearStiffness(603.0)
        joint.BartonBandis.setApplyPorePressure(1)
        joint.BartonBandis.setApplyAdditionalPressureInsideJoint(0)
        joint.BartonBandis.setAdditionalPressureType(AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        joint.BartonBandis.setAdditionalPressureInsideJoint(1927.8)
        joint.BartonBandis.setPiezoID(10976)
        joint.BartonBandis.setApplyPressureToLinerSideOnly(1)
        joint.BartonBandis.setApplyStageFactors(0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.BartonBandis.getJCS(), 1525.5)
        self.assertEqual(joint.BartonBandis.getJRC(), 1068.4)
        self.assertEqual(joint.BartonBandis.getResidualFrictionAngle(), 2610.1)
        self.assertEqual(joint.BartonBandis.getResidualStrength(), 0)
        self.assertEqual(joint.BartonBandis.getNormalStiffness(), 1829.8)
        self.assertEqual(joint.BartonBandis.getShearStiffness(), 603.0)
        self.assertEqual(joint.BartonBandis.getApplyPorePressure(), 1)
        self.assertEqual(joint.BartonBandis.getApplyAdditionalPressureInsideJoint(), 0)
        self.assertEqual(joint.BartonBandis.getAdditionalPressureType(), AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        self.assertEqual(joint.BartonBandis.getAdditionalPressureInsideJoint(), 1927.8)
        self.assertEqual(joint.BartonBandis.getPiezoID(), 10976)
        self.assertEqual(joint.BartonBandis.getApplyPressureToLinerSideOnly(), 1)
        self.assertEqual(joint.BartonBandis.getApplyStageFactors(), 0)
