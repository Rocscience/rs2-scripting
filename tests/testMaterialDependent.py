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
        joint.MaterialDependent.setInterfaceCoefficient(522.6)
        joint.MaterialDependent.setDefineStiffness(DefineStiffness.MATERIAL_DEPENDENT)
        joint.MaterialDependent.setNormalStiffness(2069.5)
        joint.MaterialDependent.setShearStiffness(2297.2)
        joint.MaterialDependent.setStiffnessCoefficient(2974.9)
        joint.MaterialDependent.setApplyPorePressure(0)
        joint.MaterialDependent.setApplyAdditionalPressureInsideJoint(1)
        joint.MaterialDependent.setAdditionalPressureType(AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        joint.MaterialDependent.setAdditionalPressureInsideJoint(1690.9)
        joint.MaterialDependent.setPiezoID(692)
        joint.MaterialDependent.setApplyPressureToLinerSideOnly(1)
        joint.MaterialDependent.setApplyStageFactors(1)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.MaterialDependent.getInterfaceCoefficient(), 522.6)
        self.assertEqual(joint.MaterialDependent.getDefineStiffness(), DefineStiffness.MATERIAL_DEPENDENT)
        self.assertEqual(joint.MaterialDependent.getNormalStiffness(), 2069.5)
        self.assertEqual(joint.MaterialDependent.getShearStiffness(), 2297.2)
        self.assertEqual(joint.MaterialDependent.getStiffnessCoefficient(), 2974.9)
        self.assertEqual(joint.MaterialDependent.getApplyPorePressure(), 0)
        self.assertEqual(joint.MaterialDependent.getApplyAdditionalPressureInsideJoint(), 1)
        self.assertEqual(joint.MaterialDependent.getAdditionalPressureType(), AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        self.assertEqual(joint.MaterialDependent.getAdditionalPressureInsideJoint(), 1690.9)
        self.assertEqual(joint.MaterialDependent.getPiezoID(), 692)
        self.assertEqual(joint.MaterialDependent.getApplyPressureToLinerSideOnly(), 1)
        self.assertEqual(joint.MaterialDependent.getApplyStageFactors(), 1)
