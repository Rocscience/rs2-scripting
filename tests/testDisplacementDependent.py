import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from src.rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestDisplacementDependent(unittest.TestCase):
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
    def testDisplacementDependentProperty(self):
        joint = self.joint
        self.joint.setJointType(JointTypes.JOINT_MATERIAL_DEPENDENT)
        joint.DisplacementDependent.setNormalStiffness(10.1)
        joint.DisplacementDependent.setInterfaceCoefficient(10.1)
        joint.DisplacementDependent.setShearStiffness(10.1)
        joint.DisplacementDependent.setDefineStiffness(JointStiffnessDefine.MATERIAL_DEPENDENT)
        joint.DisplacementDependent.setStiffnessCoefficient(10.1)
        joint.DisplacementDependent.setApplyPorePressure(True)
        joint.DisplacementDependent.setApplyAdditionalPressureInsideJoint(True)
        joint.DisplacementDependent.setAdditionalPressureType(JointWaterPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        joint.DisplacementDependent.setAdditionalPressureInsideJoint(10.1)
        joint.DisplacementDependent.setPiezoID(1)
        joint.DisplacementDependent.setApplyPressureToLinerSideOnly(True)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.DisplacementDependent.getNormalStiffness(), 10.1)
        self.assertEqual(joint.DisplacementDependent.getInterfaceCoefficient(), 10.1)
        self.assertEqual(joint.DisplacementDependent.getShearStiffness(), 10.1)
        self.assertEqual(joint.DisplacementDependent.getDefineStiffness(), JointStiffnessDefine.MATERIAL_DEPENDENT)
        self.assertEqual(joint.DisplacementDependent.getStiffnessCoefficient(), 10.1)
        self.assertEqual(joint.DisplacementDependent.getApplyPorePressure(), True)
        self.assertEqual(joint.DisplacementDependent.getApplyAdditionalPressureInsideJoint(), True)
        self.assertEqual(joint.DisplacementDependent.getAdditionalPressureType(), JointWaterPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        self.assertEqual(joint.DisplacementDependent.getAdditionalPressureInsideJoint(), 10.1)
        self.assertEqual(joint.DisplacementDependent.getPiezoID(), 1)
        self.assertEqual(joint.DisplacementDependent.getApplyPressureToLinerSideOnly(), True)
