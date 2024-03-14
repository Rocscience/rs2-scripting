import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestFEAGroundwater(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProjectTransientGroundwater.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testFEAGroundwaterProperty(self):
        hydraulic = self.material.Hydraulic
        hydraulic.FEAGroundwater.setModel(GroundWaterModes.FREDLUND_AND_XING)
        hydraulic.FEAGroundwater.setK2K1(836.5)
        hydraulic.FEAGroundwater.setK1Definition(AnisotropyDefinitions.ANGLE)
        hydraulic.FEAGroundwater.setK1Angle(2628.5)
        hydraulic.FEAGroundwater.setMvModel(MVModel.CONSTANT)
        hydraulic.FEAGroundwater.setMv(972.5)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        hydraulic = self.material.Hydraulic
        self.assertEqual(hydraulic.FEAGroundwater.getModel(), GroundWaterModes.FREDLUND_AND_XING)
        self.assertEqual(hydraulic.FEAGroundwater.getK2K1(), 836.5)
        self.assertEqual(hydraulic.FEAGroundwater.getK1Definition(), AnisotropyDefinitions.ANGLE)
        self.assertEqual(hydraulic.FEAGroundwater.getK1Angle(), 2628.5)
        self.assertEqual(hydraulic.FEAGroundwater.getMvModel(), MVModel.CONSTANT)
        self.assertEqual(hydraulic.FEAGroundwater.getMv(), 972.5)
