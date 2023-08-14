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
        blankModelPath = f"{parentDirectory}/resources/blankProject.fez"
        self.joint = self.model.getAllJointProperties()[0]
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testMohrCoulombProperty(self):
        joint = self.joint
        self.joint.setJointType(JointTypes.JOINT_MOHR_COULOMB)
        joint.MohrCoulomb.setTensileStrength(10.1)
        joint.MohrCoulomb.setPeakCohesion(10.1)
        joint.MohrCoulomb.setPeakFrictionAngle(10.1)
        joint.MohrCoulomb.setDilationAngle(10.1)
        joint.MohrCoulomb.setDMin(10.1)
        joint.MohrCoulomb.setDMax(10.1)
        joint.MohrCoulomb.setDirectional(True)
        joint.MohrCoulomb.setResidualStrength(True)
        joint.MohrCoulomb.setResTensileStrength(10.1)
        joint.MohrCoulomb.setResCohesion(10.1)
        joint.MohrCoulomb.setResFrictionAngle(10.1)
        joint.MohrCoulomb.setNormalStiffness(10.1)
        joint.MohrCoulomb.setShearStiffness(10.1)
        joint.MohrCoulomb.setApplyPorePressure(True)
        joint.MohrCoulomb.setApplyAdditionalPressureInsideJoint(True)
        joint.MohrCoulomb.setAdditionalPressureType(JointWaterPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        joint.MohrCoulomb.setAdditionalPressureInsideJoint(10.1)
        joint.MohrCoulomb.setPiezoID(1)
        joint.MohrCoulomb.setApplyPressureToLinerSideOnly(True)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.MohrCoulomb.getTensileStrength(), 10.1)
        self.assertEqual(joint.MohrCoulomb.getPeakCohesion(), 10.1)
        self.assertEqual(joint.MohrCoulomb.getPeakFrictionAngle(), 10.1)
        self.assertEqual(joint.MohrCoulomb.getDilationAngle(), 10.1)
        self.assertEqual(joint.MohrCoulomb.getDMin(), 10.1)
        self.assertEqual(joint.MohrCoulomb.getDMax(), 10.1)
        self.assertEqual(joint.MohrCoulomb.getDirectional(), True)
        self.assertEqual(joint.MohrCoulomb.getResidualStrength(), True)
        self.assertEqual(joint.MohrCoulomb.getResTensileStrength(), 10.1)
        self.assertEqual(joint.MohrCoulomb.getResCohesion(), 10.1)
        self.assertEqual(joint.MohrCoulomb.getResFrictionAngle(), 10.1)
        self.assertEqual(joint.MohrCoulomb.getNormalStiffness(), 10.1)
        self.assertEqual(joint.MohrCoulomb.getShearStiffness(), 10.1)
        self.assertEqual(joint.MohrCoulomb.getApplyPorePressure(), True)
        self.assertEqual(joint.MohrCoulomb.getApplyAdditionalPressureInsideJoint(), True)
        self.assertEqual(joint.MohrCoulomb.getAdditionalPressureType(), JointWaterPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        self.assertEqual(joint.MohrCoulomb.getAdditionalPressureInsideJoint(), 10.1)
        self.assertEqual(joint.MohrCoulomb.getPiezoID(), 1)
        self.assertEqual(joint.MohrCoulomb.getApplyPressureToLinerSideOnly(), True)
