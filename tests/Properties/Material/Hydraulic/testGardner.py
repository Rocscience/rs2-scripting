import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestGardner(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProjectTransientGroundwater.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        self.material.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_GARDNER)
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testGardnerProperty(self):
        feagroundwater = self.material.Hydraulic.FEAGroundwater
        feagroundwater.Gardner.setA(836.5)
        feagroundwater.Gardner.setN(2628.5)
        feagroundwater.Gardner.setKs(972.5)
        feagroundwater.Gardner.setWCInputType(WCInputType.WC_INPUT_DOS)
        feagroundwater.Gardner.setWCSat(0.15)
        feagroundwater.Gardner.setWCRes(0.2)
        feagroundwater.Gardner.setDoSSat(0.3)
        feagroundwater.Gardner.setDoSRes(0.4)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        feagroundwater = self.material.Hydraulic.FEAGroundwater
        self.assertEqual(feagroundwater.Gardner.getA(), 836.5)
        self.assertEqual(feagroundwater.Gardner.getN(), 2628.5)
        self.assertEqual(feagroundwater.Gardner.getKs(), 972.5)
        self.assertEqual(feagroundwater.Gardner.getWCInputType(), WCInputType.WC_INPUT_DOS)
        self.assertEqual(feagroundwater.Gardner.getWCSat(), 0.15)
        self.assertEqual(feagroundwater.Gardner.getWCRes(), 0.2)
        self.assertEqual(feagroundwater.Gardner.getDoSSat(), 0.3)
        self.assertEqual(feagroundwater.Gardner.getDoSRes(), 0.4)
