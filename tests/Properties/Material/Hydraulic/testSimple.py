import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestSimple(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProjectTransientGroundwater.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        self.material.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_SIMPLE)
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testSimpleProperty(self):
        feagroundwater = self.material.Hydraulic.FEAGroundwater
        feagroundwater.Simple.setSoilType(EnhancedSimpleSoilTypes.SL_ES_SOIL_TYPE_SAND)
        feagroundwater.Simple.setKs(836.5)
        feagroundwater.Simple.setWCInputType(WCInputType.WC_INPUT_DOS)
        feagroundwater.Simple.setWCSat(0.15)
        feagroundwater.Simple.setWCRes(0.2)
        feagroundwater.Simple.setDoSSat(0.3)
        feagroundwater.Simple.setDoSRes(0.4)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        feagroundwater = self.material.Hydraulic.FEAGroundwater
        self.assertEqual(feagroundwater.Simple.getSoilType(), EnhancedSimpleSoilTypes.SL_ES_SOIL_TYPE_SAND)
        self.assertEqual(feagroundwater.Simple.getKs(), 836.5)
        self.assertEqual(feagroundwater.Simple.getWCInputType(), WCInputType.WC_INPUT_DOS)
        self.assertEqual(feagroundwater.Simple.getWCSat(), 0.15)
        self.assertEqual(feagroundwater.Simple.getWCRes(), 0.2)
        self.assertEqual(feagroundwater.Simple.getDoSSat(), 0.3)
        self.assertEqual(feagroundwater.Simple.getDoSRes(), 0.4)