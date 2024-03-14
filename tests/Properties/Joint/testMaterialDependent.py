import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestMaterialDependent(unittest.TestCase):
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
    def testMaterialDependentProperty(self):
        joint = self.joint
        self.joint.setSlipCriterion(JointTypes.MATERIAL_DEPENDENT)
        joint.MaterialDependent.setInterfaceCoefficient(836.5)
        joint.MaterialDependent.setDefineStiffness(DefineStiffness.MATERIAL_DEPENDENT)
        joint.MaterialDependent.setNormalStiffness(2628.5)
        joint.MaterialDependent.setShearStiffness(972.5)
        joint.MaterialDependent.setStiffnessCoefficient(86.7)
        joint.MaterialDependent.setApplyPorePressure(1)
        joint.MaterialDependent.setApplyAdditionalPressureInsideJoint(0)
        joint.MaterialDependent.setAdditionalPressureType(AdditionalPressureType.PIEZOMETRIC_LINE)
        joint.MaterialDependent.setAdditionalPressureInsideJoint(468.3)
        joint.MaterialDependent.setApplyPressureToLinerSideOnly(0)
        joint.MaterialDependent.setApplyStageFactors(1)
        joint.MaterialDependent.setPiezoID(0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.MaterialDependent.getInterfaceCoefficient(), 836.5)
        self.assertEqual(joint.MaterialDependent.getDefineStiffness(), DefineStiffness.MATERIAL_DEPENDENT)
        self.assertEqual(joint.MaterialDependent.getNormalStiffness(), 2628.5)
        self.assertEqual(joint.MaterialDependent.getShearStiffness(), 972.5)
        self.assertEqual(joint.MaterialDependent.getStiffnessCoefficient(), 86.7)
        self.assertEqual(joint.MaterialDependent.getApplyPorePressure(), 1)
        self.assertEqual(joint.MaterialDependent.getApplyAdditionalPressureInsideJoint(), 0)
        self.assertEqual(joint.MaterialDependent.getAdditionalPressureType(), AdditionalPressureType.PIEZOMETRIC_LINE)
        self.assertEqual(joint.MaterialDependent.getAdditionalPressureInsideJoint(), 468.3)
        self.assertEqual(joint.MaterialDependent.getApplyPressureToLinerSideOnly(), 0)
        self.assertEqual(joint.MaterialDependent.getApplyStageFactors(), 1)
        self.assertEqual(joint.MaterialDependent.getPiezoID(), 0)
    def testMaterialDependentStageFactors(self):
        self.joint.setSlipCriterion(JointTypes.MATERIAL_DEPENDENT)
        stageFactor = self.joint.MaterialDependent.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setNormalStiffnessFactor(2572.7)
        stageFactor.setShearStiffnessFactor(2605.0)
        stageFactor.setInterfaceCoefficientFactor(3213.4)
        stageFactor.setAdditionalPressureInsideJointFactor(176.8)
        stageFactor.setGroundwaterPressureFactor(2.2)
        stageFactor.setJointPermeableFactor(True)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        stageFactor = self.joint.MaterialDependent.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getNormalStiffnessFactor(), 2572.7)
        self.assertEqual(stageFactor.getShearStiffnessFactor(), 2605.0)
        self.assertEqual(stageFactor.getInterfaceCoefficientFactor(), 3213.4)
        self.assertEqual(stageFactor.getAdditionalPressureInsideJointFactor(), 176.8)
        self.assertEqual(stageFactor.getGroundwaterPressureFactor(), 2.2)
        self.assertEqual(stageFactor.getJointPermeableFactor(), True)
