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
        joint.DisplacementDependent.setNormalStiffness(1986.4)
        joint.DisplacementDependent.setShearStiffness(2064.3)
        joint.DisplacementDependent.setApplyPorePressure(1)
        joint.DisplacementDependent.setApplyAdditionalPressureInsideJoint(1)
        joint.DisplacementDependent.setAdditionalPressureType(AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        joint.DisplacementDependent.setAdditionalPressureInsideJoint(2728.3)
        joint.DisplacementDependent.setPiezoID(30581)
        joint.DisplacementDependent.setApplyPressureToLinerSideOnly(1)
        joint.DisplacementDependent.setApplyStageFactors(0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.DisplacementDependent.getNormalStiffness(), 1986.4)
        self.assertEqual(joint.DisplacementDependent.getShearStiffness(), 2064.3)
        self.assertEqual(joint.DisplacementDependent.getApplyPorePressure(), 1)
        self.assertEqual(joint.DisplacementDependent.getApplyAdditionalPressureInsideJoint(), 1)
        self.assertEqual(joint.DisplacementDependent.getAdditionalPressureType(), AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        self.assertEqual(joint.DisplacementDependent.getAdditionalPressureInsideJoint(), 2728.3)
        self.assertEqual(joint.DisplacementDependent.getPiezoID(), 30581)
        self.assertEqual(joint.DisplacementDependent.getApplyPressureToLinerSideOnly(), 1)
        self.assertEqual(joint.DisplacementDependent.getApplyStageFactors(), 0)
