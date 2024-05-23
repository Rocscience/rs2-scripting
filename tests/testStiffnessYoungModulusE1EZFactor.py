import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

parentDirectoryHelper.addParentDirectoryToPath()

class TestStiffnessYoungModulusE1EZFactor(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]

    @classmethod
    def tearDownClass(self):
        self.model.close()
        os.remove(self.copiedModelPath)

    def testStiffnessYoungModulusE1EZFactor(self):
        stiffness = self.material.Stiffness
        stageFactor = stiffness.TransverselyIsotropic.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setYoungsModulusE1AndEzFactor(300)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        stiffness = self.material.Stiffness
        stageFactor = stiffness.TransverselyIsotropic.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getYoungsModulusE1AndEzFactor(), 300)