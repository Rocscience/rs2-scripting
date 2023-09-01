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
        joint.MohrCoulomb.setTensileStrength(892.2)
        joint.MohrCoulomb.setPeakCohesion(1579.1)
        joint.MohrCoulomb.setPeakFrictionAngle(23.6)
        joint.MohrCoulomb.setDilationAngle(2706.5)
        joint.MohrCoulomb.setDMin(2997.5)
        joint.MohrCoulomb.setDMax(1636.7)
        joint.MohrCoulomb.setDirectional(0)
        joint.MohrCoulomb.setResidualStrength(1)
        joint.MohrCoulomb.setResTensileStrength(1419.7)
        joint.MohrCoulomb.setResCohesion(913.5)
        joint.MohrCoulomb.setResFrictionAngle(815.3)
        joint.MohrCoulomb.setNormalStiffness(2636.3)
        joint.MohrCoulomb.setShearStiffness(269.9)
        joint.MohrCoulomb.setApplyPorePressure(0)
        joint.MohrCoulomb.setApplyAdditionalPressureInsideJoint(0)
        joint.MohrCoulomb.setAdditionalPressureType(AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        joint.MohrCoulomb.setAdditionalPressureInsideJoint(1478.8)
        joint.MohrCoulomb.setPiezoID(21617)
        joint.MohrCoulomb.setApplyPressureToLinerSideOnly(0)
        joint.MohrCoulomb.setApplyStageFactors(1)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.MohrCoulomb.getTensileStrength(), 892.2)
        self.assertEqual(joint.MohrCoulomb.getPeakCohesion(), 1579.1)
        self.assertEqual(joint.MohrCoulomb.getPeakFrictionAngle(), 23.6)
        self.assertEqual(joint.MohrCoulomb.getDilationAngle(), 2706.5)
        self.assertEqual(joint.MohrCoulomb.getDMin(), 2997.5)
        self.assertEqual(joint.MohrCoulomb.getDMax(), 1636.7)
        self.assertEqual(joint.MohrCoulomb.getDirectional(), 0)
        self.assertEqual(joint.MohrCoulomb.getResidualStrength(), 1)
        self.assertEqual(joint.MohrCoulomb.getResTensileStrength(), 1419.7)
        self.assertEqual(joint.MohrCoulomb.getResCohesion(), 913.5)
        self.assertEqual(joint.MohrCoulomb.getResFrictionAngle(), 815.3)
        self.assertEqual(joint.MohrCoulomb.getNormalStiffness(), 2636.3)
        self.assertEqual(joint.MohrCoulomb.getShearStiffness(), 269.9)
        self.assertEqual(joint.MohrCoulomb.getApplyPorePressure(), 0)
        self.assertEqual(joint.MohrCoulomb.getApplyAdditionalPressureInsideJoint(), 0)
        self.assertEqual(joint.MohrCoulomb.getAdditionalPressureType(), AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        self.assertEqual(joint.MohrCoulomb.getAdditionalPressureInsideJoint(), 1478.8)
        self.assertEqual(joint.MohrCoulomb.getPiezoID(), 21617)
        self.assertEqual(joint.MohrCoulomb.getApplyPressureToLinerSideOnly(), 0)
        self.assertEqual(joint.MohrCoulomb.getApplyStageFactors(), 1)
