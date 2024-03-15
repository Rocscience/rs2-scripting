import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestOrthotropic(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testOrthotropicProperty(self):
        stiffness = self.material.Stiffness
        stiffness.Orthotropic.setUseUnloadingCondition(0)
        stiffness.Orthotropic.setUnloadingCondition(UnloadingConditions.DEVIATORIC_STRESS)
        stiffness.Orthotropic.setShearModulus(2628.5)
        stiffness.Orthotropic.setAngleCounterclockwiseFromHorizontalToE1(972.5)
        stiffness.Orthotropic.setYoungsModulusE1(86.7)
        stiffness.Orthotropic.setYoungsModulusE2(762.9)
        stiffness.Orthotropic.setYoungsModulusEZ(1413.6)
        stiffness.Orthotropic.setPoissonsRatioV12(468.3)
        stiffness.Orthotropic.setPoissonsRatioV2(2350.4)
        stiffness.Orthotropic.setPoissonsRatioV2z(2598.3)
        stiffness.Orthotropic.setUnloadingShearModulus(2572.7)
        stiffness.Orthotropic.setUnloadingAngleCounterclockwiseFromHorizontalToE1(2605.0)
        stiffness.Orthotropic.setUnloadingYoungsModulusE1(3213.4)
        stiffness.Orthotropic.setUnloadingYoungsModulusE2(176.8)
        stiffness.Orthotropic.setUnloadingYoungsModulusEZ(1508.0)
        stiffness.Orthotropic.setUnloadingPoissonsRatioV12(857.2)
        stiffness.Orthotropic.setUnloadingPoissonsRatioV2(3215.6)
        stiffness.Orthotropic.setUnloadingPoissonsRatioV2z(1475.5)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        stiffness = self.material.Stiffness
        self.assertEqual(stiffness.Orthotropic.getUseUnloadingCondition(), 0)
        self.assertEqual(stiffness.Orthotropic.getUnloadingCondition(), UnloadingConditions.DEVIATORIC_STRESS)
        self.assertEqual(stiffness.Orthotropic.getShearModulus(), 2628.5)
        self.assertEqual(stiffness.Orthotropic.getAngleCounterclockwiseFromHorizontalToE1(), 972.5)
        self.assertEqual(stiffness.Orthotropic.getYoungsModulusE1(), 86.7)
        self.assertEqual(stiffness.Orthotropic.getYoungsModulusE2(), 762.9)
        self.assertEqual(stiffness.Orthotropic.getYoungsModulusEZ(), 1413.6)
        self.assertEqual(stiffness.Orthotropic.getPoissonsRatioV12(), 468.3)
        self.assertEqual(stiffness.Orthotropic.getPoissonsRatioV2(), 2350.4)
        self.assertEqual(stiffness.Orthotropic.getPoissonsRatioV2z(), 2598.3)
        self.assertEqual(stiffness.Orthotropic.getUnloadingShearModulus(), 2572.7)
        self.assertEqual(stiffness.Orthotropic.getUnloadingAngleCounterclockwiseFromHorizontalToE1(), 2605.0)
        self.assertEqual(stiffness.Orthotropic.getUnloadingYoungsModulusE1(), 3213.4)
        self.assertEqual(stiffness.Orthotropic.getUnloadingYoungsModulusE2(), 176.8)
        self.assertEqual(stiffness.Orthotropic.getUnloadingYoungsModulusEZ(), 1508.0)
        self.assertEqual(stiffness.Orthotropic.getUnloadingPoissonsRatioV12(), 857.2)
        self.assertEqual(stiffness.Orthotropic.getUnloadingPoissonsRatioV2(), 3215.6)
        self.assertEqual(stiffness.Orthotropic.getUnloadingPoissonsRatioV2z(), 1475.5)
    def testOrthotropicStageFactors(self):
        stiffness = self.material.Stiffness
        stageFactor = stiffness.Orthotropic.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setAngleCounterclockwiseFromHorizontalToE1Factor(2227.9)
        stageFactor.setPoissonsRatioV12Factor(3008.6)
        stageFactor.setPoissonsRatioV2Factor(2917.7)
        stageFactor.setPoissonsRatioV2zFactor(1006.5)
        stageFactor.setShearModulusFactor(1374.4)
        stageFactor.setYoungsModulusE1Factor(1257.7)
        stageFactor.setYoungsModulusE2Factor(1702.5)
        stageFactor.setYoungsModulusEZFactor(857.5)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        stiffness = self.material.Stiffness
        stageFactor = stiffness.Orthotropic.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getAngleCounterclockwiseFromHorizontalToE1Factor(), 2227.9)
        self.assertEqual(stageFactor.getPoissonsRatioV12Factor(), 3008.6)
        self.assertEqual(stageFactor.getPoissonsRatioV2Factor(), 2917.7)
        self.assertEqual(stageFactor.getPoissonsRatioV2zFactor(), 1006.5)
        self.assertEqual(stageFactor.getShearModulusFactor(), 1374.4)
        self.assertEqual(stageFactor.getYoungsModulusE1Factor(), 1257.7)
        self.assertEqual(stageFactor.getYoungsModulusE2Factor(), 1702.5)
        self.assertEqual(stageFactor.getYoungsModulusEZFactor(), 857.5)
