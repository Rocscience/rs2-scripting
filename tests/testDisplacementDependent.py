import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestDisplacementDependent(unittest.TestCase):
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
    def testDisplacementDependentProperty(self):
        joint = self.joint
        self.joint.setSlipCriterion(JointTypes.JOINT_DISPLACEMENT_DEPENDENT)
        joint.DisplacementDependent.setNormalStiffness(836.5)
        joint.DisplacementDependent.setShearStiffness(2628.5)
        joint.DisplacementDependent.setApplyPorePressure(0)
        joint.DisplacementDependent.setApplyAdditionalPressureInsideJoint(1)
        joint.DisplacementDependent.setAdditionalPressureType(AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        joint.DisplacementDependent.setAdditionalPressureInsideJoint(762.9)
        joint.DisplacementDependent.setPiezoID(11649)
        joint.DisplacementDependent.setApplyPressureToLinerSideOnly(0)
        joint.DisplacementDependent.setApplyStageFactors(0)
        joint.DisplacementDependent.setDisplacementDependentTable([[1.2,2,3,4],[1.5,2,3,4]])
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.DisplacementDependent.getNormalStiffness(), 836.5)
        self.assertEqual(joint.DisplacementDependent.getShearStiffness(), 2628.5)
        self.assertEqual(joint.DisplacementDependent.getApplyPorePressure(), 0)
        self.assertEqual(joint.DisplacementDependent.getApplyAdditionalPressureInsideJoint(), 1)
        self.assertEqual(joint.DisplacementDependent.getAdditionalPressureType(), AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        self.assertEqual(joint.DisplacementDependent.getAdditionalPressureInsideJoint(), 762.9)
        self.assertEqual(joint.DisplacementDependent.getPiezoID(), 11649)
        self.assertEqual(joint.DisplacementDependent.getApplyPressureToLinerSideOnly(), 0)
        self.assertEqual(joint.DisplacementDependent.getApplyStageFactors(), 0)
        self.assertEqual(joint.DisplacementDependent.getDisplacementDependentTable(), [[1.2,2,3,4],[1.5,2,3,4]])
