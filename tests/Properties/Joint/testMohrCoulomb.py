import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestMohrCoulomb(unittest.TestCase):
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
    def testMohrCoulombProperty(self):
        joint = self.joint
        self.joint.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
        joint.MohrCoulomb.setTensileStrength(836.5)
        joint.MohrCoulomb.setPeakCohesion(2628.5)
        joint.MohrCoulomb.setPeakFrictionAngle(972.5)
        joint.MohrCoulomb.setIncludeDilation(1)
        joint.MohrCoulomb.setDilationAngle(762.9)
        joint.MohrCoulomb.setDMin(1413.6)
        joint.MohrCoulomb.setDMax(468.3)
        joint.MohrCoulomb.setDirectional(0)
        joint.MohrCoulomb.setResidualStrength(1)
        joint.MohrCoulomb.setResTensileStrength(2572.7)
        joint.MohrCoulomb.setResCohesion(2605.0)
        joint.MohrCoulomb.setResFrictionAngle(3213.4)
        joint.MohrCoulomb.setNormalStiffness(176.8)
        joint.MohrCoulomb.setShearStiffness(1508.0)
        joint.MohrCoulomb.setApplyPorePressure(0)
        joint.MohrCoulomb.setApplyAdditionalPressureInsideJoint(0)
        joint.MohrCoulomb.setAdditionalPressureType(AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        joint.MohrCoulomb.setAdditionalPressureInsideJoint(1475.5)
        joint.MohrCoulomb.setPiezoID(26556)
        joint.MohrCoulomb.setApplyPressureToLinerSideOnly(1)
        joint.MohrCoulomb.setApplyStageFactors(0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.MohrCoulomb.getTensileStrength(), 836.5)
        self.assertEqual(joint.MohrCoulomb.getPeakCohesion(), 2628.5)
        self.assertEqual(joint.MohrCoulomb.getPeakFrictionAngle(), 972.5)
        self.assertEqual(joint.MohrCoulomb.getIncludeDilation(), 1)
        self.assertEqual(joint.MohrCoulomb.getDilationAngle(), 762.9)
        self.assertEqual(joint.MohrCoulomb.getDMin(), 1413.6)
        self.assertEqual(joint.MohrCoulomb.getDMax(), 468.3)
        self.assertEqual(joint.MohrCoulomb.getDirectional(), 0)
        self.assertEqual(joint.MohrCoulomb.getResidualStrength(), 1)
        self.assertEqual(joint.MohrCoulomb.getResTensileStrength(), 2572.7)
        self.assertEqual(joint.MohrCoulomb.getResCohesion(), 2605.0)
        self.assertEqual(joint.MohrCoulomb.getResFrictionAngle(), 3213.4)
        self.assertEqual(joint.MohrCoulomb.getNormalStiffness(), 176.8)
        self.assertEqual(joint.MohrCoulomb.getShearStiffness(), 1508.0)
        self.assertEqual(joint.MohrCoulomb.getApplyPorePressure(), 0)
        self.assertEqual(joint.MohrCoulomb.getApplyAdditionalPressureInsideJoint(), 0)
        self.assertEqual(joint.MohrCoulomb.getAdditionalPressureType(), AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
        self.assertEqual(joint.MohrCoulomb.getAdditionalPressureInsideJoint(), 1475.5)
        self.assertEqual(joint.MohrCoulomb.getPiezoID(), 26556)
        self.assertEqual(joint.MohrCoulomb.getApplyPressureToLinerSideOnly(), 1)
        self.assertEqual(joint.MohrCoulomb.getApplyStageFactors(), 0)
    def testMohrCoulombStageFactors(self):
        joint = self.joint
        self.joint.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
        stageFactor = joint.MohrCoulomb.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setNormalStiffnessFactor(1006.5)
        stageFactor.setShearStiffnessFactor(1374.4)
        stageFactor.setTensileStrengthFactor(1257.7)
        stageFactor.setPeakCohesionFactor(1702.5)
        stageFactor.setPeakFrictionAngleFactor(857.5)
        stageFactor.setResCohesionFactor(2489.6)
        stageFactor.setResFrictionAngleFactor(1772.3)
        stageFactor.setResTensileStrengthFactor(2188.4)
        stageFactor.setAdditionalPressureInsideJointFactor(812.6)
        stageFactor.setGroundwaterPressureFactor(2.2)
        stageFactor.setJointPermeableFactor(True)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        stageFactor = joint.MohrCoulomb.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getNormalStiffnessFactor(), 1006.5)
        self.assertEqual(stageFactor.getShearStiffnessFactor(), 1374.4)
        self.assertEqual(stageFactor.getTensileStrengthFactor(), 1257.7)
        self.assertEqual(stageFactor.getPeakCohesionFactor(), 1702.5)
        self.assertEqual(stageFactor.getPeakFrictionAngleFactor(), 857.5)
        self.assertEqual(stageFactor.getResCohesionFactor(), 2489.6)
        self.assertEqual(stageFactor.getResFrictionAngleFactor(), 1772.3)
        self.assertEqual(stageFactor.getResTensileStrengthFactor(), 2188.4)
        self.assertEqual(stageFactor.getAdditionalPressureInsideJointFactor(), 812.6)
        self.assertEqual(stageFactor.getGroundwaterPressureFactor(), 2.2)
        self.assertEqual(stageFactor.getJointPermeableFactor(), True)
