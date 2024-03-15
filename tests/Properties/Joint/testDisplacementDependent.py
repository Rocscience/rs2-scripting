import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

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
        self.joint.setSlipCriterion(JointTypes.DISPLACEMENT_DEPENDENT)
        joint.DisplacementDependent.setNormalStiffness(836.5)
        joint.DisplacementDependent.setShearStiffness(2628.5)
        joint.DisplacementDependent.setApplyPorePressure(0)
        joint.DisplacementDependent.setApplyAdditionalPressureInsideJoint(1)
        joint.DisplacementDependent.setAdditionalPressureType(AdditionalPressureType.PIEZOMETRIC_LINE)
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
        self.assertEqual(joint.DisplacementDependent.getAdditionalPressureType(), AdditionalPressureType.PIEZOMETRIC_LINE)
        self.assertEqual(joint.DisplacementDependent.getAdditionalPressureInsideJoint(), 762.9)
        self.assertEqual(joint.DisplacementDependent.getPiezoID(), 11649)
        self.assertEqual(joint.DisplacementDependent.getApplyPressureToLinerSideOnly(), 0)
        self.assertEqual(joint.DisplacementDependent.getApplyStageFactors(), 0)
        self.assertEqual(joint.DisplacementDependent.getDisplacementDependentTable(), [[1.2,2,3,4],[1.5,2,3,4]])
    def testDisplacementDependentStageFactors(self):
        joint = self.joint
        self.joint.setSlipCriterion(JointTypes.DISPLACEMENT_DEPENDENT)
        stageFactor = joint.DisplacementDependent.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setNormalStiffnessFactor(2598.3)
        stageFactor.setShearStiffnessFactor(2572.7)
        stageFactor.setShearDisplacementFactor(2605.0)
        stageFactor.setCohesionFactor(3213.4)
        stageFactor.setFrictionAngleFactor(176.8)
        stageFactor.setTensileStrengthFactor(1508.0)
        stageFactor.setAdditionalPressureInsideJointFactor(857.2)
        stageFactor.setGroundwaterPressureFactor(2.2)
        stageFactor.setJointPermeableFactor(True)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        stageFactor = joint.DisplacementDependent.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getNormalStiffnessFactor(), 2598.3)
        self.assertEqual(stageFactor.getShearStiffnessFactor(), 2572.7)
        self.assertEqual(stageFactor.getShearDisplacementFactor(), 2605.0)
        self.assertEqual(stageFactor.getCohesionFactor(), 3213.4)
        self.assertEqual(stageFactor.getFrictionAngleFactor(), 176.8)
        self.assertEqual(stageFactor.getTensileStrengthFactor(), 1508.0)
        self.assertEqual(stageFactor.getAdditionalPressureInsideJointFactor(), 857.2)
        self.assertEqual(stageFactor.getGroundwaterPressureFactor(), 2.2)
        self.assertEqual(stageFactor.getJointPermeableFactor(), True)
