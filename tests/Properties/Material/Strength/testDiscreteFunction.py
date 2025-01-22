import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestDiscreteFunction(unittest.TestCase):
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
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)
    def testDiscreteFunctionProperty(self):
        strength = self.material.Strength
        strength.DiscreteFunction.setApplySSRShearStrengthReduction(0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.DiscreteFunction.getApplySSRShearStrengthReduction(), 0)
    def testDiscreteFunctionStageFactors(self):
        strength = self.material.Strength
        stageFactor = strength.DiscreteFunction.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setPeakTensileStrengthFactor(2628.5)
        stageFactor.setResidualTensileStrengthFactor(972.5)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        stageFactor = strength.DiscreteFunction.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getPeakTensileStrengthFactor(), 2628.5)
        self.assertEqual(stageFactor.getResidualTensileStrengthFactor(), 972.5)
