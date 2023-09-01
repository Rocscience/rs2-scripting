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
        joint.BartonBandis.setJCS(1760.4)
        joint.BartonBandis.setJRC(735.5)
        joint.BartonBandis.setResidualFrictionAngle(1748.2)
        joint.BartonBandis.setResidualStrength(1)
        joint.BartonBandis.setNormalStiffness(325.1)
        joint.BartonBandis.setShearStiffness(2793.6)
        joint.BartonBandis.setApplyPorePressure(0)
        joint.BartonBandis.setApplyAdditionalPressureInsideJoint(0)
        joint.BartonBandis.setAdditionalPressureType(AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        joint.BartonBandis.setAdditionalPressureInsideJoint(854.6)
        joint.BartonBandis.setPiezoID(23335)
        joint.BartonBandis.setApplyPressureToLinerSideOnly(1)
        joint.BartonBandis.setApplyStageFactors(1)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.BartonBandis.getJCS(), 1760.4)
        self.assertEqual(joint.BartonBandis.getJRC(), 735.5)
        self.assertEqual(joint.BartonBandis.getResidualFrictionAngle(), 1748.2)
        self.assertEqual(joint.BartonBandis.getResidualStrength(), 1)
        self.assertEqual(joint.BartonBandis.getNormalStiffness(), 325.1)
        self.assertEqual(joint.BartonBandis.getShearStiffness(), 2793.6)
        self.assertEqual(joint.BartonBandis.getApplyPorePressure(), 0)
        self.assertEqual(joint.BartonBandis.getApplyAdditionalPressureInsideJoint(), 0)
        self.assertEqual(joint.BartonBandis.getAdditionalPressureType(), AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        self.assertEqual(joint.BartonBandis.getAdditionalPressureInsideJoint(), 854.6)
        self.assertEqual(joint.BartonBandis.getPiezoID(), 23335)
        self.assertEqual(joint.BartonBandis.getApplyPressureToLinerSideOnly(), 1)
        self.assertEqual(joint.BartonBandis.getApplyStageFactors(), 1)
