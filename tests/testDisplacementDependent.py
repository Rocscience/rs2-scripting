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
        self.joint = self.model.getAllJointProperties()[0]
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testDisplacementDependentProperty(self):
        joint = self.joint
        self.joint.setSlipCriterion(JointTypes.JOINT_DISPLACEMENT_DEPENDENT)
        joint.DisplacementDependent.setNormalStiffness(1563.8)
        joint.DisplacementDependent.setShearStiffness(824.5)
        joint.DisplacementDependent.setApplyPorePressure(0)
        joint.DisplacementDependent.setApplyAdditionalPressureInsideJoint(1)
        joint.DisplacementDependent.setAdditionalPressureType(AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        joint.DisplacementDependent.setAdditionalPressureInsideJoint(3157.9)
        joint.DisplacementDependent.setPiezoID(23425)
        joint.DisplacementDependent.setApplyPressureToLinerSideOnly(1)
        joint.DisplacementDependent.setApplyStageFactors(1)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.DisplacementDependent.getNormalStiffness(), 1563.8)
        self.assertEqual(joint.DisplacementDependent.getShearStiffness(), 824.5)
        self.assertEqual(joint.DisplacementDependent.getApplyPorePressure(), 0)
        self.assertEqual(joint.DisplacementDependent.getApplyAdditionalPressureInsideJoint(), 1)
        self.assertEqual(joint.DisplacementDependent.getAdditionalPressureType(), AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        self.assertEqual(joint.DisplacementDependent.getAdditionalPressureInsideJoint(), 3157.9)
        self.assertEqual(joint.DisplacementDependent.getPiezoID(), 23425)
        self.assertEqual(joint.DisplacementDependent.getApplyPressureToLinerSideOnly(), 1)
        self.assertEqual(joint.DisplacementDependent.getApplyStageFactors(), 1)
