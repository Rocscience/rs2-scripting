import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestGeosyntheticHyperbolic(unittest.TestCase):
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
    def testGeosyntheticHyperbolicProperty(self):
        joint = self.joint
        self.joint.setSlipCriterion(JointTypes.GEOSYNTHETIC_HYPERBOLIC)
        joint.GeosyntheticHyperbolic.setPeakAdhesionAtSigninf(836.5)
        joint.GeosyntheticHyperbolic.setPeakFrictionAngleAtSign0(2628.5)
        joint.GeosyntheticHyperbolic.setResAdhesionAtSigninf(972.5)
        joint.GeosyntheticHyperbolic.setResFrictionAngleAtSign0(86.7)
        joint.GeosyntheticHyperbolic.setNormalStiffness(762.9)
        joint.GeosyntheticHyperbolic.setShearStiffness(1413.6)
        joint.GeosyntheticHyperbolic.setApplyPorePressure(0)
        joint.GeosyntheticHyperbolic.setApplyAdditionalPressureInsideJoint(0)
        joint.GeosyntheticHyperbolic.setAdditionalPressureType(AdditionalPressureType.PIEZOMETRIC_LINE)
        joint.GeosyntheticHyperbolic.setAdditionalPressureInsideJoint(2598.3)
        joint.GeosyntheticHyperbolic.setPiezoID(12830)
        joint.GeosyntheticHyperbolic.setApplyPressureToLinerSideOnly(0)
        joint.GeosyntheticHyperbolic.setApplyStageFactors(1)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.GeosyntheticHyperbolic.getPeakAdhesionAtSigninf(), 836.5)
        self.assertEqual(joint.GeosyntheticHyperbolic.getPeakFrictionAngleAtSign0(), 2628.5)
        self.assertEqual(joint.GeosyntheticHyperbolic.getResAdhesionAtSigninf(), 972.5)
        self.assertEqual(joint.GeosyntheticHyperbolic.getResFrictionAngleAtSign0(), 86.7)
        self.assertEqual(joint.GeosyntheticHyperbolic.getNormalStiffness(), 762.9)
        self.assertEqual(joint.GeosyntheticHyperbolic.getShearStiffness(), 1413.6)
        self.assertEqual(joint.GeosyntheticHyperbolic.getApplyPorePressure(), 0)
        self.assertEqual(joint.GeosyntheticHyperbolic.getApplyAdditionalPressureInsideJoint(), 0)
        self.assertEqual(joint.GeosyntheticHyperbolic.getAdditionalPressureType(), AdditionalPressureType.PIEZOMETRIC_LINE)
        self.assertEqual(joint.GeosyntheticHyperbolic.getAdditionalPressureInsideJoint(), 2598.3)
        self.assertEqual(joint.GeosyntheticHyperbolic.getPiezoID(), 12830)
        self.assertEqual(joint.GeosyntheticHyperbolic.getApplyPressureToLinerSideOnly(), 0)
        self.assertEqual(joint.GeosyntheticHyperbolic.getApplyStageFactors(), 1)
    def testGeosyntheticHyperbolicStageFactors(self):
        joint = self.joint
        self.joint.setSlipCriterion(JointTypes.GEOSYNTHETIC_HYPERBOLIC)
        stageFactor = joint.GeosyntheticHyperbolic.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setNormalStiffnessFactor(176.8)
        stageFactor.setShearStiffnessFactor(1508.0)
        stageFactor.setPeakAdhesionAtSigninfFactor(857.2)
        stageFactor.setPeakFrictionAngleAtSign0Factor(3215.6)
        stageFactor.setResAdhesionAtSigninfFactor(1475.5)
        stageFactor.setResFrictionAngleAtSign0Factor(2227.9)
        stageFactor.setAdditionalPressureInsideJointFactor(3008.6)
        stageFactor.setGroundwaterPressureFactor(2.2)
        stageFactor.setJointPermeableFactor(True)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        stageFactor = joint.GeosyntheticHyperbolic.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getNormalStiffnessFactor(), 176.8)
        self.assertEqual(stageFactor.getShearStiffnessFactor(), 1508.0)
        self.assertEqual(stageFactor.getPeakAdhesionAtSigninfFactor(), 857.2)
        self.assertEqual(stageFactor.getPeakFrictionAngleAtSign0Factor(), 3215.6)
        self.assertEqual(stageFactor.getResAdhesionAtSigninfFactor(), 1475.5)
        self.assertEqual(stageFactor.getResFrictionAngleAtSign0Factor(), 2227.9)
        self.assertEqual(stageFactor.getAdditionalPressureInsideJointFactor(), 3008.6)
        self.assertEqual(stageFactor.getGroundwaterPressureFactor(), 2.2)
        self.assertEqual(stageFactor.getJointPermeableFactor(), True)
