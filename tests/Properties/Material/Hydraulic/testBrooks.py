import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestBrooks(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProjectTransientGroundwater.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        self.material.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_BROOK)
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testBrooksProperty(self):
        feagroundwater = self.material.Hydraulic.FEAGroundwater
        feagroundwater.Brooks.setPoreSizeIndex(836.5)
        feagroundwater.Brooks.setBubblingPressure(2628.5)
        feagroundwater.Brooks.setKs(972.5)
        feagroundwater.Brooks.setWCInputType(WCInputType.WC_INPUT_DOS)
        feagroundwater.Brooks.setWCSat(0.15)
        feagroundwater.Brooks.setWCRes(0.2)
        feagroundwater.Brooks.setDoSSat(0.3)
        feagroundwater.Brooks.setDoSRes(0.4)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        feagroundwater = self.material.Hydraulic.FEAGroundwater
        self.assertEqual(feagroundwater.Brooks.getPoreSizeIndex(), 836.5)
        self.assertEqual(feagroundwater.Brooks.getBubblingPressure(), 2628.5)
        self.assertEqual(feagroundwater.Brooks.getKs(), 972.5)
        self.assertEqual(feagroundwater.Brooks.getWCInputType(), WCInputType.WC_INPUT_DOS)
        self.assertEqual(feagroundwater.Brooks.getWCSat(), 0.15)
        self.assertEqual(feagroundwater.Brooks.getWCRes(), 0.2)
        self.assertEqual(feagroundwater.Brooks.getDoSSat(), 0.3)
        self.assertEqual(feagroundwater.Brooks.getDoSRes(), 0.4)