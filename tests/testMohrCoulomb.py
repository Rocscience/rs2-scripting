import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from src.rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestMohrCoulomb(unittest.TestCase):
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
    def testMohrCoulombProperty(self):
        joint = self.joint
        self.joint.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
        joint.MohrCoulomb.setTensileStrength(836.5)
        joint.MohrCoulomb.setPeakCohesion(2628.5)
        joint.MohrCoulomb.setPeakFrictionAngle(972.5)
        joint.MohrCoulomb.setDilationAngle(86.7)
        joint.MohrCoulomb.setDMin(762.9)
        joint.MohrCoulomb.setDMax(1413.6)
        joint.MohrCoulomb.setDirectional(0)
        joint.MohrCoulomb.setResidualStrength(0)
        joint.MohrCoulomb.setResTensileStrength(2598.3)
        joint.MohrCoulomb.setResCohesion(2572.7)
        joint.MohrCoulomb.setResFrictionAngle(2605.0)
        joint.MohrCoulomb.setNormalStiffness(3213.4)
        joint.MohrCoulomb.setShearStiffness(176.8)
        joint.MohrCoulomb.setApplyPorePressure(1)
        joint.MohrCoulomb.setApplyAdditionalPressureInsideJoint(0)
        joint.MohrCoulomb.setAdditionalPressureType(AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        joint.MohrCoulomb.setAdditionalPressureInsideJoint(3215.6)
        joint.MohrCoulomb.setPiezoID(6388)
        joint.MohrCoulomb.setApplyPressureToLinerSideOnly(0)
        joint.MohrCoulomb.setApplyStageFactors(1)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.MohrCoulomb.getTensileStrength(), 836.5)
        self.assertEqual(joint.MohrCoulomb.getPeakCohesion(), 2628.5)
        self.assertEqual(joint.MohrCoulomb.getPeakFrictionAngle(), 972.5)
        self.assertEqual(joint.MohrCoulomb.getDilationAngle(), 86.7)
        self.assertEqual(joint.MohrCoulomb.getDMin(), 762.9)
        self.assertEqual(joint.MohrCoulomb.getDMax(), 1413.6)
        self.assertEqual(joint.MohrCoulomb.getDirectional(), 0)
        self.assertEqual(joint.MohrCoulomb.getResidualStrength(), 0)
        self.assertEqual(joint.MohrCoulomb.getResTensileStrength(), 2598.3)
        self.assertEqual(joint.MohrCoulomb.getResCohesion(), 2572.7)
        self.assertEqual(joint.MohrCoulomb.getResFrictionAngle(), 2605.0)
        self.assertEqual(joint.MohrCoulomb.getNormalStiffness(), 3213.4)
        self.assertEqual(joint.MohrCoulomb.getShearStiffness(), 176.8)
        self.assertEqual(joint.MohrCoulomb.getApplyPorePressure(), 1)
        self.assertEqual(joint.MohrCoulomb.getApplyAdditionalPressureInsideJoint(), 0)
        self.assertEqual(joint.MohrCoulomb.getAdditionalPressureType(), AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        self.assertEqual(joint.MohrCoulomb.getAdditionalPressureInsideJoint(), 3215.6)
        self.assertEqual(joint.MohrCoulomb.getPiezoID(), 6388)
        self.assertEqual(joint.MohrCoulomb.getApplyPressureToLinerSideOnly(), 0)
        self.assertEqual(joint.MohrCoulomb.getApplyStageFactors(), 1)
