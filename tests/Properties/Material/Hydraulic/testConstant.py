import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestConstant(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProjectTransientGroundwater.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        self.material.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_CONSTANT)
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testConstantProperty(self):
        feagroundwater = self.material.Hydraulic.FEAGroundwater
        feagroundwater.Constant.setUseCV(0)
        feagroundwater.Constant.setCV(2628.5)
        feagroundwater.Constant.setInitialK(972.5)
        feagroundwater.Constant.setWCCurveSlope(86.7)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        feagroundwater = self.material.Hydraulic.FEAGroundwater
        self.assertEqual(feagroundwater.Constant.getUseCV(), 0)
        self.assertEqual(feagroundwater.Constant.getCV(), 2628.5)
        self.assertEqual(feagroundwater.Constant.getInitialK(), 972.5)
        self.assertEqual(feagroundwater.Constant.getWCCurveSlope(), 86.7)
