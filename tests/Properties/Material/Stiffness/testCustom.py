import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestCustom(unittest.TestCase):
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
    def testCustomProperty(self):
        stiffness = self.material.Stiffness
        stiffness.Custom.setUseUnloadingCondition(0)
        stiffness.Custom.setUnloadingCondition(UnloadingConditions.UC_DEVIATORIC_STRESS)
        stiffness.Custom.setUseConstantPoissonsRatio(0)
        stiffness.Custom.setConstantPoissonsRatio(972.5)
        stiffness.Custom.setUnloadingUseConstantPoissonsRatio(1)
        stiffness.Custom.setUnloadingConstantPoissonsRatio(762.9)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        stiffness = self.material.Stiffness
        self.assertEqual(stiffness.Custom.getUseUnloadingCondition(), 0)
        self.assertEqual(stiffness.Custom.getUnloadingCondition(), UnloadingConditions.UC_DEVIATORIC_STRESS)
        self.assertEqual(stiffness.Custom.getUseConstantPoissonsRatio(), 0)
        self.assertEqual(stiffness.Custom.getConstantPoissonsRatio(), 972.5)
        self.assertEqual(stiffness.Custom.getUnloadingUseConstantPoissonsRatio(), 1)
        self.assertEqual(stiffness.Custom.getUnloadingConstantPoissonsRatio(), 762.9)
