import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestMaterialJointOptions(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.mat = self.model.getAllMaterialProperties()[0]
        self.matJointOptions = self.mat.Strength.JointedMohrCoulomb.getJointOptions()
    @classmethod
    def tearDownClass(self):
        self.model.close()
        os.remove(self.copiedModelPath)

    def testNumberOfJointsSuccess(self):
        self.matJointOptions.setNumberOfJoints(1)
        self.assertEqual(self.matJointOptions.getNumberOfJoints(), 1)

        self.matJointOptions.setNumberOfJoints(2)
        self.assertEqual(self.matJointOptions.getNumberOfJoints(), 2)

        self.matJointOptions.setNumberOfJoints(3)
        self.assertEqual(self.matJointOptions.getNumberOfJoints(), 3)

    def testNumberOfJointsFailure(self):
        with self.assertRaises(Exception):
            self.matJointOptions.setNumberOfJoints(0)
        with self.assertRaises(Exception):
            self.matJointOptions.setNumberOfJoints(4)
    
    def testSetInclination(self):
        self.matJointOptions.setNumberOfJoints(1)
        self.matJointOptions.setInclination(0, 0.1)

        self.assertEqual(self.matJointOptions.getNumberOfJoints(), 1)
        self.assertEqual(self.matJointOptions.getInclination(0), 0.1)


    def testSetTracePlane(self):
        self.matJointOptions.setNumberOfJoints(1)
        self.assertEqual(self.matJointOptions.getNumberOfJoints(), 1)

        self.matJointOptions.setUseTracePlane(0, True)
        self.assertEqual(self.matJointOptions.getUseTracePlane(0), True)

        self.matJointOptions.setTracePlaneProperties(0, 0.1, 0.2, 0.3)
        self.assertEqual(self.matJointOptions.getTracePlaneProperties(0), (0.1, 0.2, 0.3))

    def testSetSecondJointProperties(self):
        self.matJointOptions.setNumberOfJoints(2)
        self.assertEqual(self.matJointOptions.getNumberOfJoints(), 2)

        joint2 = self.matJointOptions.getJoint(1)
        joint2.setSlipCriterion(JointTypes.BARTON_BANDIS)
        joint2.BartonBandisMaterial.setDilationAngle(0.023)

        joint1 = self.matJointOptions.getJoint(0)
        joint1.setSlipCriterion(JointTypes.MOHR_COULOMB)
        joint1.MohrCoulombMaterial.setDilationAngle(0.024)

        self.assertEqual(joint2.getSlipCriterion(), JointTypes.BARTON_BANDIS)
        self.assertEqual(joint2.BartonBandisMaterial.getDilationAngle(), 0.023)
        self.assertEqual(joint1.getSlipCriterion(), JointTypes.MOHR_COULOMB)
        self.assertEqual(joint1.MohrCoulombMaterial.getDilationAngle(), 0.024)

    def testDilationAngleFailureLessThanZero(self):
        self.matJointOptions.setNumberOfJoints(1)
        joint = self.matJointOptions.getJoint(0)
        with self.assertRaises(Exception):
            joint.MohrCoulombMaterial.setDilationAngle(-0.1)

    def testDilationRatioFailureLessThanZero(self):
        self.matJointOptions.setNumberOfJoints(1)
        joint = self.matJointOptions.getJoint(0)
        with self.assertRaises(Exception):
            joint.GeosyntheticHyperbolicMaterial.setDilationRatio(-0.1)

    def testSetPermeabilityFactor(self):
        self.matJointOptions.setNumberOfJoints(1)
        joint = self.matJointOptions.getJoint(0)
        joint.setSlipCriterion(JointTypes.MOHR_COULOMB)
        joint.MohrCoulombMaterial.setApplyStageFactors(True)        
        fac1 = joint.MohrCoulombMaterial.stageFactorInterface.createStageFactor(1)
        fac1.setJointPermeableFactor(True)
        self.assertEqual(fac1.getJointPermeableFactor(),True)
        fac1.setJointPermeableFactor(False)
        self.assertEqual(fac1.getJointPermeableFactor(),False)

        joint.setSlipCriterion(JointTypes.BARTON_BANDIS)
        joint.BartonBandisMaterial.setApplyStageFactors(True)
        fac1 = joint.BartonBandisMaterial.stageFactorInterface.getDefinedStageFactors()[1]
        fac1.setJointPermeableFactor(True)
        self.assertEqual(fac1.getJointPermeableFactor(),True)
        fac1.setJointPermeableFactor(False)
        self.assertEqual(fac1.getJointPermeableFactor(),False)

        joint.setSlipCriterion(JointTypes.GEOSYNTHETIC_HYPERBOLIC)
        joint.GeosyntheticHyperbolicMaterial.setApplyStageFactors(True)
        fac1 = joint.GeosyntheticHyperbolicMaterial.stageFactorInterface.getDefinedStageFactors()[1]
        fac1.setJointPermeableFactor(True)
        self.assertEqual(fac1.getJointPermeableFactor(),True)
        fac1.setJointPermeableFactor(False)
        self.assertEqual(fac1.getJointPermeableFactor(),False)