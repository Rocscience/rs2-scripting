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
        joint.MohrCoulomb.setTensileStrength(2311.6)
        joint.MohrCoulomb.setPeakCohesion(459.3)
        joint.MohrCoulomb.setPeakFrictionAngle(1039.0)
        joint.MohrCoulomb.setDilationAngle(825.2)
        joint.MohrCoulomb.setDMin(1121.1)
        joint.MohrCoulomb.setDMax(2315.8)
        joint.MohrCoulomb.setDirectional(0)
        joint.MohrCoulomb.setResidualStrength(1)
        joint.MohrCoulomb.setResTensileStrength(2632.1)
        joint.MohrCoulomb.setResCohesion(1099.9)
        joint.MohrCoulomb.setResFrictionAngle(1019.9)
        joint.MohrCoulomb.setNormalStiffness(2384.9)
        joint.MohrCoulomb.setShearStiffness(1171.4)
        joint.MohrCoulomb.setApplyPorePressure(1)
        joint.MohrCoulomb.setApplyAdditionalPressureInsideJoint(0)
        joint.MohrCoulomb.setAdditionalPressureType(AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        joint.MohrCoulomb.setAdditionalPressureInsideJoint(1748.0)
        joint.MohrCoulomb.setPiezoID(16657)
        joint.MohrCoulomb.setApplyPressureToLinerSideOnly(0)
        joint.MohrCoulomb.setApplyStageFactors(0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.MohrCoulomb.getTensileStrength(), 2311.6)
        self.assertEqual(joint.MohrCoulomb.getPeakCohesion(), 459.3)
        self.assertEqual(joint.MohrCoulomb.getPeakFrictionAngle(), 1039.0)
        self.assertEqual(joint.MohrCoulomb.getDilationAngle(), 825.2)
        self.assertEqual(joint.MohrCoulomb.getDMin(), 1121.1)
        self.assertEqual(joint.MohrCoulomb.getDMax(), 2315.8)
        self.assertEqual(joint.MohrCoulomb.getDirectional(), 0)
        self.assertEqual(joint.MohrCoulomb.getResidualStrength(), 1)
        self.assertEqual(joint.MohrCoulomb.getResTensileStrength(), 2632.1)
        self.assertEqual(joint.MohrCoulomb.getResCohesion(), 1099.9)
        self.assertEqual(joint.MohrCoulomb.getResFrictionAngle(), 1019.9)
        self.assertEqual(joint.MohrCoulomb.getNormalStiffness(), 2384.9)
        self.assertEqual(joint.MohrCoulomb.getShearStiffness(), 1171.4)
        self.assertEqual(joint.MohrCoulomb.getApplyPorePressure(), 1)
        self.assertEqual(joint.MohrCoulomb.getApplyAdditionalPressureInsideJoint(), 0)
        self.assertEqual(joint.MohrCoulomb.getAdditionalPressureType(), AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        self.assertEqual(joint.MohrCoulomb.getAdditionalPressureInsideJoint(), 1748.0)
        self.assertEqual(joint.MohrCoulomb.getPiezoID(), 16657)
        self.assertEqual(joint.MohrCoulomb.getApplyPressureToLinerSideOnly(), 0)
        self.assertEqual(joint.MohrCoulomb.getApplyStageFactors(), 0)
