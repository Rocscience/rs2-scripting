import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestGardnerWaterContent(unittest.TestCase):
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
    def testGardnerWaterContentProperty(self):
        hydraulicmodel = self.material.Thermal.SoilUnfrozenWaterContent.HydraulicModel
        hydraulicmodel.GardnerWaterContent.setA(836.5)
        hydraulicmodel.GardnerWaterContent.setN(2628.5)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        hydraulicmodel = self.material.Thermal.SoilUnfrozenWaterContent.HydraulicModel
        self.assertEqual(hydraulicmodel.GardnerWaterContent.getA(), 836.5)
        self.assertEqual(hydraulicmodel.GardnerWaterContent.getN(), 2628.5)