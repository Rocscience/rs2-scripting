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
        self.joint = self.model.getAllJointProperties()[0]
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testMaterialDependentProperty(self):
        joint = self.joint
        self.joint.setSlipCriterion(JointTypes.JOINT_MATERIAL_DEPENDENT)
        joint.MaterialDependent.setInterfaceCoefficient(3268.3)
        joint.MaterialDependent.setDefineStiffness(DefineStiffness.MATERIAL_DEPENDENT)
        joint.MaterialDependent.setNormalStiffness(2369.9)
        joint.MaterialDependent.setShearStiffness(1496.4)
        joint.MaterialDependent.setStiffnessCoefficient(352.9)
        joint.MaterialDependent.setApplyPorePressure(1)
        joint.MaterialDependent.setApplyAdditionalPressureInsideJoint(0)
        joint.MaterialDependent.setAdditionalPressureType(AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        joint.MaterialDependent.setAdditionalPressureInsideJoint(949.2)
        joint.MaterialDependent.setPiezoID(29876)
        joint.MaterialDependent.setApplyPressureToLinerSideOnly(1)
        joint.MaterialDependent.setApplyStageFactors(1)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.MaterialDependent.getInterfaceCoefficient(), 3268.3)
        self.assertEqual(joint.MaterialDependent.getDefineStiffness(), DefineStiffness.MATERIAL_DEPENDENT)
        self.assertEqual(joint.MaterialDependent.getNormalStiffness(), 2369.9)
        self.assertEqual(joint.MaterialDependent.getShearStiffness(), 1496.4)
        self.assertEqual(joint.MaterialDependent.getStiffnessCoefficient(), 352.9)
        self.assertEqual(joint.MaterialDependent.getApplyPorePressure(), 1)
        self.assertEqual(joint.MaterialDependent.getApplyAdditionalPressureInsideJoint(), 0)
        self.assertEqual(joint.MaterialDependent.getAdditionalPressureType(), AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        self.assertEqual(joint.MaterialDependent.getAdditionalPressureInsideJoint(), 949.2)
        self.assertEqual(joint.MaterialDependent.getPiezoID(), 29876)
        self.assertEqual(joint.MaterialDependent.getApplyPressureToLinerSideOnly(), 1)
        self.assertEqual(joint.MaterialDependent.getApplyStageFactors(), 1)
