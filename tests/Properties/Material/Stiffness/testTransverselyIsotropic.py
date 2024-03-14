import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestTransverselyIsotropic(unittest.TestCase):
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
    def testTransverselyIsotropicProperty(self):
        stiffness = self.material.Stiffness
        stiffness.TransverselyIsotropic.setUseUnloadingCondition(0)
        stiffness.TransverselyIsotropic.setUnloadingCondition(UnloadingConditions.DEVIATORIC_STRESS)
        stiffness.TransverselyIsotropic.setShearModulus(2628.5)
        stiffness.TransverselyIsotropic.setAngleCounterclockwiseFromHorizontalToE1(972.5)
        stiffness.TransverselyIsotropic.setYoungsModulusE1AndEz(86.7)
        stiffness.TransverselyIsotropic.setYoungsModulusE2(762.9)
        stiffness.TransverselyIsotropic.setPoissonsRatioV12(1413.6)
        stiffness.TransverselyIsotropic.setPoissonsRatioVAndV1z(468.3)
        stiffness.TransverselyIsotropic.setUnloadingShearModulus(2350.4)
        stiffness.TransverselyIsotropic.setUnloadingAngleCounterclockwiseFromHorizontalToE1(2598.3)
        stiffness.TransverselyIsotropic.setUnloadingYoungsModulusE1AndEz(2572.7)
        stiffness.TransverselyIsotropic.setUnloadingYoungsModulusE2(2605.0)
        stiffness.TransverselyIsotropic.setUnloadingPoissonsRatioV12(3213.4)
        stiffness.TransverselyIsotropic.setUnloadingPoissonsRatioVAndV1z(176.8)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        stiffness = self.material.Stiffness
        self.assertEqual(stiffness.TransverselyIsotropic.getUseUnloadingCondition(), 0)
        self.assertEqual(stiffness.TransverselyIsotropic.getUnloadingCondition(), UnloadingConditions.DEVIATORIC_STRESS)
        self.assertEqual(stiffness.TransverselyIsotropic.getShearModulus(), 2628.5)
        self.assertEqual(stiffness.TransverselyIsotropic.getAngleCounterclockwiseFromHorizontalToE1(), 972.5)
        self.assertEqual(stiffness.TransverselyIsotropic.getYoungsModulusE1AndEz(), 86.7)
        self.assertEqual(stiffness.TransverselyIsotropic.getYoungsModulusE2(), 762.9)
        self.assertEqual(stiffness.TransverselyIsotropic.getPoissonsRatioV12(), 1413.6)
        self.assertEqual(stiffness.TransverselyIsotropic.getPoissonsRatioVAndV1z(), 468.3)
        self.assertEqual(stiffness.TransverselyIsotropic.getUnloadingShearModulus(), 2350.4)
        self.assertEqual(stiffness.TransverselyIsotropic.getUnloadingAngleCounterclockwiseFromHorizontalToE1(), 2598.3)
        self.assertEqual(stiffness.TransverselyIsotropic.getUnloadingYoungsModulusE1AndEz(), 2572.7)
        self.assertEqual(stiffness.TransverselyIsotropic.getUnloadingYoungsModulusE2(), 2605.0)
        self.assertEqual(stiffness.TransverselyIsotropic.getUnloadingPoissonsRatioV12(), 3213.4)
        self.assertEqual(stiffness.TransverselyIsotropic.getUnloadingPoissonsRatioVAndV1z(), 176.8)
