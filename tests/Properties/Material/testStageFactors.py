import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestStageFactors(unittest.TestCase):

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
        self.model._client.closeConnection()
        os.remove(self.copiedModelPath)

    def testSetStageStrengthStiffnessStageFactors(self):
        self.material.StageFactors.setStageStrengthStiffnessStageFactors(True)
        self.assertEqual(self.material.StageFactors.getStageStrengthStiffnessStageFactors(), True)
        self.material.StageFactors.setStageStrengthStiffnessStageFactors(False)
        self.assertEqual(self.material.StageFactors.getStageStrengthStiffnessStageFactors(), False)

    def testSetStageThermalStageFactors(self):
        self.material.StageFactors.setStageThermalStageFactors(True)
        self.assertEqual(self.material.StageFactors.getStageThermalStageFactors(), True)
        self.material.StageFactors.setStageThermalStageFactors(False)
        self.assertEqual(self.material.StageFactors.getStageThermalStageFactors(), False)

    def testSetStageHydraulicStageFactor(self):
        self.material.StageFactors.setStageHydraulicStageFactor(True)
        self.assertEqual(self.material.StageFactors.getStageHydraulicStageFactor(), True)
        self.material.StageFactors.setStageHydraulicStageFactor(False)
        self.assertEqual(self.material.StageFactors.getStageHydraulicStageFactor(), False)
    
    def testSetStageDatumStageFactor(self):
        self.material.StageFactors.setStageDatumStageFactor(True)
        self.assertEqual(self.material.StageFactors.getStageDatumStageFactor(), True)
        self.material.StageFactors.setStageDatumStageFactor(False)
        self.assertEqual(self.material.StageFactors.getStageDatumStageFactor(), False)

    def testSetResetStress(self):
        self.material.StageFactors.setResetStress(True)
        self.assertEqual(self.material.StageFactors.getResetStress(), True)
        self.material.StageFactors.setResetStress(False)
        self.assertEqual(self.material.StageFactors.getResetStress(), False)