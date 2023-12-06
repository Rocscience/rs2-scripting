import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestFredlung(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProjectTransientGroundwater.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        self.material.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_FREDLUND)
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testFredlungProperty(self):
        feagroundwater = self.material.Hydraulic.FEAGroundwater
        feagroundwater.Fredlung.setA(836.5)
        feagroundwater.Fredlung.setB(2628.5)
        feagroundwater.Fredlung.setC(972.5)
        feagroundwater.Fredlung.setKs(86.7)
        feagroundwater.Fredlung.setWCInputType(WCInputType.WC_INPUT_DOS)
        feagroundwater.Fredlung.setWCSat(0.15)
        feagroundwater.Fredlung.setWCRes(0.2)
        feagroundwater.Fredlung.setDoSSat(0.3)
        feagroundwater.Fredlung.setDoSRes(0.4)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        feagroundwater = self.material.Hydraulic.FEAGroundwater
        self.assertEqual(feagroundwater.Fredlung.getA(), 836.5)
        self.assertEqual(feagroundwater.Fredlung.getB(), 2628.5)
        self.assertEqual(feagroundwater.Fredlung.getC(), 972.5)
        self.assertEqual(feagroundwater.Fredlung.getKs(), 86.7)
        self.assertEqual(feagroundwater.Fredlung.getWCInputType(), WCInputType.WC_INPUT_DOS)
        self.assertEqual(feagroundwater.Fredlung.getWCSat(), 0.15)
        self.assertEqual(feagroundwater.Fredlung.getWCRes(), 0.2)
        self.assertEqual(feagroundwater.Fredlung.getDoSSat(), 0.3)
        self.assertEqual(feagroundwater.Fredlung.getDoSRes(), 0.4)
