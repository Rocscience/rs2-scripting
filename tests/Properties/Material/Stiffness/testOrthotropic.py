import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

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
        stiffness.Orthotropic.setUnloadingCondition(UnloadingConditions.UC_DEVIATORIC_STRESS)
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
        self.assertEqual(stiffness.Orthotropic.getUnloadingCondition(), UnloadingConditions.UC_DEVIATORIC_STRESS)
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
