import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestGeosyntheticHyperbolicMaterial(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.mat = self.model.getAllMaterialProperties()[0]
        self.mat.Strength.setFailureCriterion(StrengthCriteriaTypes.JOINTED_MOHR_COULOMB)
        self.matJointOptions = self.mat.Strength.JointedMohrCoulomb.getJointOptions()
        self.jointmaterial = self.matJointOptions.getJoint(0)
        self.jointmaterial.BartonBandisMaterial.setApplyStageFactors(True)
        sf = self.jointmaterial.BartonBandisMaterial.stageFactorInterface.createStageFactor(1)
        self.jointmaterial.BartonBandisMaterial.stageFactorInterface.setDefinedStageFactors({ 1: sf })

    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testGeosyntheticHyperbolicMaterialProperty(self):
        jointmaterial = self.jointmaterial
        jointmaterial.GeosyntheticHyperbolicMaterial.setPeakAdhesionAtSigninf(836.5)
        jointmaterial.GeosyntheticHyperbolicMaterial.setPeakFrictionAngleAtSign0(2628.5)
        jointmaterial.GeosyntheticHyperbolicMaterial.setResAdhesionAtSigninf(972.5)
        jointmaterial.GeosyntheticHyperbolicMaterial.setResFrictionAngleAtSign0(86.7)
        jointmaterial.GeosyntheticHyperbolicMaterial.setApplyStageFactors(1)
        jointmaterial.GeosyntheticHyperbolicMaterial.setTensileStrength(1413.6)
        jointmaterial.GeosyntheticHyperbolicMaterial.setDilationRatio(2.2)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.mat = self.model.getAllMaterialProperties()[0]
        self.mat.Strength.setFailureCriterion(StrengthCriteriaTypes.JOINTED_MOHR_COULOMB)
        self.matJointOptions = self.mat.Strength.JointedMohrCoulomb.getJointOptions()
        self.jointmaterial = self.matJointOptions.getJoint(0)
        jointmaterial = self.jointmaterial
        self.assertEqual(jointmaterial.GeosyntheticHyperbolicMaterial.getPeakAdhesionAtSigninf(), 836.5)
        self.assertEqual(jointmaterial.GeosyntheticHyperbolicMaterial.getPeakFrictionAngleAtSign0(), 2628.5)
        self.assertEqual(jointmaterial.GeosyntheticHyperbolicMaterial.getResAdhesionAtSigninf(), 972.5)
        self.assertEqual(jointmaterial.GeosyntheticHyperbolicMaterial.getResFrictionAngleAtSign0(), 86.7)
        self.assertEqual(jointmaterial.GeosyntheticHyperbolicMaterial.getApplyStageFactors(), 1)
        self.assertEqual(jointmaterial.GeosyntheticHyperbolicMaterial.getTensileStrength(), 1413.6)
        self.assertEqual(jointmaterial.GeosyntheticHyperbolicMaterial.getDilationRatio(), 2.2)
    def testGeosyntheticHyperbolicMaterialStageFactors(self):
        jointmaterial = self.jointmaterial
        stageFactor = jointmaterial.GeosyntheticHyperbolicMaterial.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setPeakAdhesionAtSigninfFactor(468.3)
        stageFactor.setPeakFrictionAngleAtSign0Factor(2350.4)
        stageFactor.setResAdhesionAtSigninfFactor(2598.3)
        stageFactor.setResFrictionAngleAtSign0Factor(2572.7)
        stageFactor.setDilationRatioFactor(2.4)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.mat = self.model.getAllMaterialProperties()[0]
        self.mat.Strength.setFailureCriterion(StrengthCriteriaTypes.JOINTED_MOHR_COULOMB)
        self.matJointOptions = self.mat.Strength.JointedMohrCoulomb.getJointOptions()
        self.jointmaterial = self.matJointOptions.getJoint(0)
        jointmaterial = self.jointmaterial
        stageFactor = jointmaterial.GeosyntheticHyperbolicMaterial.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getPeakAdhesionAtSigninfFactor(), 468.3)
        self.assertEqual(stageFactor.getPeakFrictionAngleAtSign0Factor(), 2350.4)
        self.assertEqual(stageFactor.getResAdhesionAtSigninfFactor(), 2598.3)
        self.assertEqual(stageFactor.getResFrictionAngleAtSign0Factor(), 2572.7)
        self.assertEqual(stageFactor.getDilationRatioFactor(), 2.4)
