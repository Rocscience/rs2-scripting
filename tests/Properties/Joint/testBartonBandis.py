import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestBartonBandis(unittest.TestCase):
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
    def testBartonBandisProperty(self):
        joint = self.joint
        self.joint.setSlipCriterion(JointTypes.BARTON_BANDIS)
        joint.BartonBandis.setJCS(836.5)
        joint.BartonBandis.setJRC(2628.5)
        joint.BartonBandis.setResidualFrictionAngle(972.5)
        joint.BartonBandis.setResidualStrength(1)
        joint.BartonBandis.setNormalStiffness(762.9)
        joint.BartonBandis.setShearStiffness(1413.6)
        joint.BartonBandis.setApplyPorePressure(0)
        joint.BartonBandis.setApplyAdditionalPressureInsideJoint(0)
        joint.BartonBandis.setAdditionalPressureType(AdditionalPressureType.PIEZOMETRIC_LINE)
        joint.BartonBandis.setAdditionalPressureInsideJoint(2598.3)
        joint.BartonBandis.setPiezoID(12830)
        joint.BartonBandis.setApplyPressureToLinerSideOnly(0)
        joint.BartonBandis.setApplyStageFactors(1)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.BartonBandis.getJCS(), 836.5)
        self.assertEqual(joint.BartonBandis.getJRC(), 2628.5)
        self.assertEqual(joint.BartonBandis.getResidualFrictionAngle(), 972.5)
        self.assertEqual(joint.BartonBandis.getResidualStrength(), 1)
        self.assertEqual(joint.BartonBandis.getNormalStiffness(), 762.9)
        self.assertEqual(joint.BartonBandis.getShearStiffness(), 1413.6)
        self.assertEqual(joint.BartonBandis.getApplyPorePressure(), 0)
        self.assertEqual(joint.BartonBandis.getApplyAdditionalPressureInsideJoint(), 0)
        self.assertEqual(joint.BartonBandis.getAdditionalPressureType(), AdditionalPressureType.PIEZOMETRIC_LINE)
        self.assertEqual(joint.BartonBandis.getAdditionalPressureInsideJoint(), 2598.3)
        self.assertEqual(joint.BartonBandis.getPiezoID(), 12830)
        self.assertEqual(joint.BartonBandis.getApplyPressureToLinerSideOnly(), 0)
        self.assertEqual(joint.BartonBandis.getApplyStageFactors(), 1)
    def testBartonBandisStageFactors(self):
        joint = self.joint
        self.joint.setSlipCriterion(JointTypes.BARTON_BANDIS)
        stageFactor = joint.BartonBandis.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setNormalStiffnessFactor(176.8)
        stageFactor.setShearStiffnessFactor(1508.0)
        stageFactor.setJCSFactor(857.2)
        stageFactor.setJRCFactor(3215.6)
        stageFactor.setResidualFrictionAngleFactor(1475.5)
        stageFactor.setAdditionalPressureInsideJointFactor(2227.9)
        stageFactor.setGroundwaterPressureFactor(2.2)
        stageFactor.setJointPermeableFactor(True)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        stageFactor = joint.BartonBandis.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getNormalStiffnessFactor(), 176.8)
        self.assertEqual(stageFactor.getShearStiffnessFactor(), 1508.0)
        self.assertEqual(stageFactor.getJCSFactor(), 857.2)
        self.assertEqual(stageFactor.getJRCFactor(), 3215.6)
        self.assertEqual(stageFactor.getResidualFrictionAngleFactor(), 1475.5)
        self.assertEqual(stageFactor.getAdditionalPressureInsideJointFactor(), 2227.9)
        self.assertEqual(stageFactor.getGroundwaterPressureFactor(), 2.2)
        self.assertEqual(stageFactor.getJointPermeableFactor(), True)
