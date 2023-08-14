import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from src.rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestMaterialDependent(unittest.TestCase):
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
    def testMaterialDependentProperty(self):
        joint = self.joint
        self.joint.setJointType(JointTypes.JOINT_HYPERBOLIC_SOFTENING)
        joint.MaterialDependent.setPeakCohesion(10.1)
        joint.MaterialDependent.setPeakFriction(10.1)
        joint.MaterialDependent.setResCohesion(10.1)
        joint.MaterialDependent.setResFriction(10.1)
        joint.MaterialDependent.setTensileStrength(10.1)
        joint.MaterialDependent.setResTensileStrength(10.1)
        joint.MaterialDependent.setDeltaR(10.1)
        joint.MaterialDependent.setInitialSlope(10.1)
        joint.MaterialDependent.setWorkSoftening(True)
        joint.MaterialDependent.setNormalStiffness(10.1)
        joint.MaterialDependent.setShearStiffness(10.1)
        joint.MaterialDependent.setApplyPorePressure(True)
        joint.MaterialDependent.setApplyAdditionalPressureInsideJoint(True)
        joint.MaterialDependent.setAdditionalPressureType(JointWaterPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        joint.MaterialDependent.setAdditionalPressureInsideJoint(10.1)
        joint.MaterialDependent.setPiezoID(1)
        joint.MaterialDependent.setApplyPressureToLinerSideOnly(True)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.MaterialDependent.getPeakCohesion(), 10.1)
        self.assertEqual(joint.MaterialDependent.getPeakFriction(), 10.1)
        self.assertEqual(joint.MaterialDependent.getResCohesion(), 10.1)
        self.assertEqual(joint.MaterialDependent.getResFriction(), 10.1)
        self.assertEqual(joint.MaterialDependent.getTensileStrength(), 10.1)
        self.assertEqual(joint.MaterialDependent.getResTensileStrength(), 10.1)
        self.assertEqual(joint.MaterialDependent.getDeltaR(), 10.1)
        self.assertEqual(joint.MaterialDependent.getInitialSlope(), 10.1)
        self.assertEqual(joint.MaterialDependent.getWorkSoftening(), True)
        self.assertEqual(joint.MaterialDependent.getNormalStiffness(), 10.1)
        self.assertEqual(joint.MaterialDependent.getShearStiffness(), 10.1)
        self.assertEqual(joint.MaterialDependent.getApplyPorePressure(), True)
        self.assertEqual(joint.MaterialDependent.getApplyAdditionalPressureInsideJoint(), True)
        self.assertEqual(joint.MaterialDependent.getAdditionalPressureType(), JointWaterPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        self.assertEqual(joint.MaterialDependent.getAdditionalPressureInsideJoint(), 10.1)
        self.assertEqual(joint.MaterialDependent.getPiezoID(), 1)
        self.assertEqual(joint.MaterialDependent.getApplyPressureToLinerSideOnly(), True)
