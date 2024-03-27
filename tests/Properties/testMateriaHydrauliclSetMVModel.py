import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestMaterialHydraulicMVModel(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProjectTransientGroundwater.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
    @classmethod
    def tearDownClass(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testMaterialHydraulicMV_ModelSuccess(self):
        material = self.material
        material.Hydraulic.FEAGroundwater.setMvModel(MVModel.NONE)
        self.assertEqual(material.Hydraulic.FEAGroundwater.getMvModel(), MVModel.NONE)
        material.Hydraulic.FEAGroundwater.setMvModel(MVModel.CONSTANT)
        self.assertEqual(material.Hydraulic.FEAGroundwater.getMvModel(), MVModel.CONSTANT)
        material.Hydraulic.FEAGroundwater.setMvModel(MVModel.FLUID)
        self.assertEqual(material.Hydraulic.FEAGroundwater.getMvModel(), MVModel.FLUID)
        material.Hydraulic.FEAGroundwater.setMvModel(MVModel.ELASTIC_CONSOLIDATION_1D)
        self.assertEqual(material.Hydraulic.FEAGroundwater.getMvModel(), MVModel.ELASTIC_CONSOLIDATION_1D)
        material.Hydraulic.FEAGroundwater.setMvModel(MVModel.ELASTIC_CONSOLIDATION_2D)
        self.assertEqual(material.Hydraulic.FEAGroundwater.getMvModel(), MVModel.ELASTIC_CONSOLIDATION_2D)
        