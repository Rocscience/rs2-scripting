import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestInitialConditionSWMInterpolated(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProjectTransientGroundwater.fez"
        modelWithoutTransientGWPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        self.modelWithoutTransientGWPath = f"{parentDirectory}/resources/testProject2.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        shutil.copy(modelWithoutTransientGWPath, self.modelWithoutTransientGWPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.modelWithoutTransientGW = self.modeler.openFile(self.modelWithoutTransientGWPath)
    @classmethod
    def tearDownClass(self):
        self.model.close()
        self.modelWithoutTransientGW.close()
        os.remove(self.copiedModelPath)
        os.remove(self.modelWithoutTransientGWPath)

    def testInitialCondition_SWM_InterpolatedSuccess(self):
        material = self.model.getAllMaterialProperties()[0]
        material.InitialConditions.setInitialWaterCondition(StaticWaterModes.SWM_INTERPOLATED)
        self.assertEqual(material.InitialConditions.getInitialWaterCondition(), StaticWaterModes.SWM_INTERPOLATED)