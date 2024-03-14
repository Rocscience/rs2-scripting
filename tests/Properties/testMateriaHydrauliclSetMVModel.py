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
        material.Hydraulic.FEAGroundwater.setMvModel(MVModel.MV_NONE)
        self.assertEqual(material.Hydraulic.FEAGroundwater.getMvModel(), MVModel.MV_NONE)
        material.Hydraulic.FEAGroundwater.setMvModel(MVModel.MV_CONSTANT)
        self.assertEqual(material.Hydraulic.FEAGroundwater.getMvModel(), MVModel.MV_CONSTANT)
        material.Hydraulic.FEAGroundwater.setMvModel(MVModel.MV_FLUID)
        self.assertEqual(material.Hydraulic.FEAGroundwater.getMvModel(), MVModel.MV_FLUID)
        material.Hydraulic.FEAGroundwater.setMvModel(MVModel.MV_1D_ELASTIC)
        self.assertEqual(material.Hydraulic.FEAGroundwater.getMvModel(), MVModel.MV_1D_ELASTIC)
        material.Hydraulic.FEAGroundwater.setMvModel(MVModel.MV_2D_ELASTIC)
        self.assertEqual(material.Hydraulic.FEAGroundwater.getMvModel(), MVModel.MV_2D_ELASTIC)
        