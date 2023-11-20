import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestMaterialJointOptions(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.mat = self.model.getAllMaterialProperties()[0]
        self.matJointOptions = self.mat.Strength.JointedMohrCoulomb.getJointOptions()
    def tearDown(self):
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

    def testJointBartonBandis(self):
        self.matJointOptions.setNumberOfJoints(1)
        self.assertEqual(self.matJointOptions.getNumberOfJoints(), 1)

        joint = self.matJointOptions.getJoint(0)
        joint.setSlipCriterion(JointTypes.JOINT_BARTON_BANDIS)
        self.assertEqual(joint.getSlipCriterion(), JointTypes.JOINT_BARTON_BANDIS)

        #missing dilation angle?
        joint.BartonBandis.setJCS(0.1)
        self.assertEqual(joint.BartonBandis.getJCS(), 0.1)

        joint.BartonBandis.setJRC(0.2)
        self.assertEqual(joint.BartonBandis.getJRC(), 0.2)

        joint.BartonBandis.setResidualFrictionAngle(0.3)
        self.assertEqual(joint.BartonBandis.getResidualFrictionAngle(), 0.3)

        joint.BartonBandis.setResidualStrength(True)
        self.assertEqual(joint.BartonBandis.getResidualStrength(), True)

        joint.BartonBandis.setApplyStageFactors(True)
        self.assertEqual(joint.BartonBandis.getApplyStageFactors(), True)

    def testGeosyntheticHyperbolic(self):
        self.matJointOptions.setNumberOfJoints(1)
        self.assertEqual(self.matJointOptions.getNumberOfJoints(), 1)

        joint = self.matJointOptions.getJoint(0)
        joint.setSlipCriterion(JointTypes.JOINT_HYPERBOLIC_SIMPLE)
        self.assertEqual(joint.getSlipCriterion(), JointTypes.JOINT_HYPERBOLIC_SIMPLE)

        #missing dilation ratio?
        joint.GeosyntheticHyperbolic.setPeakAdhesionAtSigninf(0.1)
        joint.GeosyntheticHyperbolic.setPeakFrictionAngleAtSign0(0.2)
        joint.GeosyntheticHyperbolic.setResAdhesionAtSigninf(0.3)
        joint.GeosyntheticHyperbolic.setResFrictionAngleAtSign0(0.4)

        self.assertEqual(joint.GeosyntheticHyperbolic.getPeakAdhesionAtSigninf(), 0.1)
        self.assertEqual(joint.GeosyntheticHyperbolic.getPeakFrictionAngleAtSign0(), 0.2)
        self.assertEqual(joint.GeosyntheticHyperbolic.getResAdhesionAtSigninf(), 0.3)
        self.assertEqual(joint.GeosyntheticHyperbolic.getResFrictionAngleAtSign0(), 0.4)

    def testJointMohrCoulomb(self):
        self.matJointOptions.setNumberOfJoints(1)
        self.assertEqual(self.matJointOptions.getNumberOfJoints(), 1)

        joint = self.matJointOptions.getJoint(0)
        joint.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
        self.assertEqual(joint.getSlipCriterion(), JointTypes.JOINT_MOHR_COULOMB)
        
        joint.MohrCoulomb.setDilationAngle(0.1)
        self.assertEqual(joint.MohrCoulomb.getDilationAngle(), 0.1)

        joint.MohrCoulomb.setTensileStrength(0.2)
        self.assertEqual(joint.MohrCoulomb.getTensileStrength(), 0.2)

        joint.MohrCoulomb.setPeakFrictionAngle(0.3)
        self.assertEqual(joint.MohrCoulomb.getPeakFrictionAngle(), 0.3)

        joint.MohrCoulomb.setPeakCohesion(0.4)
        self.assertEqual(joint.MohrCoulomb.getPeakCohesion(), 0.4)
        
        joint.MohrCoulomb.setResidualStrength(True)
        self.assertEqual(joint.MohrCoulomb.getResidualStrength(), True)

        joint.MohrCoulomb.setResCohesion(0.1)
        self.assertEqual(joint.MohrCoulomb.getResCohesion(), 0.1)

        joint.MohrCoulomb.setResFrictionAngle(0.2)
        self.assertEqual(joint.MohrCoulomb.getResFrictionAngle(), 0.2)

        joint.MohrCoulomb.setResTensileStrength(0.3)
        self.assertEqual(joint.MohrCoulomb.getResTensileStrength(), 0.3)