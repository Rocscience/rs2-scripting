import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

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

    def testJointBartonBandisMaterial(self):
        self.matJointOptions.setNumberOfJoints(1)
        self.assertEqual(self.matJointOptions.getNumberOfJoints(), 1)

        joint = self.matJointOptions.getJoint(0)
        joint.setSlipCriterion(JointTypes.JOINT_BARTON_BANDIS)
        self.assertEqual(joint.getSlipCriterion(), JointTypes.JOINT_BARTON_BANDIS)

        joint.BartonBandisMaterial.setDilationAngle(0.05)
        self.assertEqual(joint.BartonBandisMaterial.getDilationAngle(), 0.05)
        
        joint.BartonBandisMaterial.setJCS(0.1)
        self.assertEqual(joint.BartonBandisMaterial.getJCS(), 0.1)

        joint.BartonBandisMaterial.setJRC(0.2)
        self.assertEqual(joint.BartonBandisMaterial.getJRC(), 0.2)

        joint.BartonBandisMaterial.setResidualFrictionAngle(0.3)
        self.assertEqual(joint.BartonBandisMaterial.getResidualFrictionAngle(), 0.3)

        joint.BartonBandisMaterial.setResidualStrength(True)
        self.assertEqual(joint.BartonBandisMaterial.getResidualStrength(), True)

        joint.BartonBandisMaterial.setApplyStageFactors(True)
        self.assertEqual(joint.BartonBandisMaterial.getApplyStageFactors(), True)

    def testGeosyntheticHyperbolicMaterial(self):
        self.matJointOptions.setNumberOfJoints(1)
        self.assertEqual(self.matJointOptions.getNumberOfJoints(), 1)

        joint = self.matJointOptions.getJoint(0)
        joint.setSlipCriterion(JointTypes.JOINT_HYPERBOLIC_SIMPLE)
        self.assertEqual(joint.getSlipCriterion(), JointTypes.JOINT_HYPERBOLIC_SIMPLE)

        joint.GeosyntheticHyperbolicMaterial.setDilationRatio(0.05)
        self.assertEqual(joint.GeosyntheticHyperbolicMaterial.getDilationRatio(), 0.05)
        joint.GeosyntheticHyperbolicMaterial.setPeakAdhesionAtSigninf(0.1)
        joint.GeosyntheticHyperbolicMaterial.setPeakFrictionAngleAtSign0(0.2)
        joint.GeosyntheticHyperbolicMaterial.setResAdhesionAtSigninf(0.3)
        joint.GeosyntheticHyperbolicMaterial.setResFrictionAngleAtSign0(0.4)

        self.assertEqual(joint.GeosyntheticHyperbolicMaterial.getPeakAdhesionAtSigninf(), 0.1)
        self.assertEqual(joint.GeosyntheticHyperbolicMaterial.getPeakFrictionAngleAtSign0(), 0.2)
        self.assertEqual(joint.GeosyntheticHyperbolicMaterial.getResAdhesionAtSigninf(), 0.3)
        self.assertEqual(joint.GeosyntheticHyperbolicMaterial.getResFrictionAngleAtSign0(), 0.4)

    def testJointMohrCoulombMaterial(self):
        self.matJointOptions.setNumberOfJoints(1)
        self.assertEqual(self.matJointOptions.getNumberOfJoints(), 1)

        joint = self.matJointOptions.getJoint(0)
        joint.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
        self.assertEqual(joint.getSlipCriterion(), JointTypes.JOINT_MOHR_COULOMB)
        
        joint.MohrCoulombMaterial.setDilationAngle(0.1)
        self.assertEqual(joint.MohrCoulombMaterial.getDilationAngle(), 0.1)

        joint.MohrCoulombMaterial.setTensileStrength(0.2)
        self.assertEqual(joint.MohrCoulombMaterial.getTensileStrength(), 0.2)

        joint.MohrCoulombMaterial.setPeakFrictionAngle(0.3)
        self.assertEqual(joint.MohrCoulombMaterial.getPeakFrictionAngle(), 0.3)

        joint.MohrCoulombMaterial.setPeakCohesion(0.4)
        self.assertEqual(joint.MohrCoulombMaterial.getPeakCohesion(), 0.4)
        
        joint.MohrCoulombMaterial.setResidualStrength(True)
        self.assertEqual(joint.MohrCoulombMaterial.getResidualStrength(), True)

        joint.MohrCoulombMaterial.setResCohesion(0.1)
        self.assertEqual(joint.MohrCoulombMaterial.getResCohesion(), 0.1)

        joint.MohrCoulombMaterial.setResFrictionAngle(0.2)
        self.assertEqual(joint.MohrCoulombMaterial.getResFrictionAngle(), 0.2)

        joint.MohrCoulombMaterial.setResTensileStrength(0.3)
        self.assertEqual(joint.MohrCoulombMaterial.getResTensileStrength(), 0.3)
