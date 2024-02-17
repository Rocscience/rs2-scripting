import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestFredlund(unittest.TestCase):
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
    def testFredlundProperty(self):
        feagroundwater = self.material.Hydraulic.FEAGroundwater
        feagroundwater.Fredlund.setA(836.5)
        feagroundwater.Fredlund.setB(2628.5)
        feagroundwater.Fredlund.setC(972.5)
        feagroundwater.Fredlund.setKs(86.7)
        feagroundwater.Fredlund.setWCInputType(WCInputType.WC_INPUT_DOS)
        feagroundwater.Fredlund.setWCSat(0.15)
        feagroundwater.Fredlund.setWCRes(0.2)
        feagroundwater.Fredlund.setDoSSat(0.3)
        feagroundwater.Fredlund.setDoSRes(0.4)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        feagroundwater = self.material.Hydraulic.FEAGroundwater
        self.assertEqual(feagroundwater.Fredlund.getA(), 836.5)
        self.assertEqual(feagroundwater.Fredlund.getB(), 2628.5)
        self.assertEqual(feagroundwater.Fredlund.getC(), 972.5)
        self.assertEqual(feagroundwater.Fredlund.getKs(), 86.7)
        self.assertEqual(feagroundwater.Fredlund.getWCInputType(), WCInputType.WC_INPUT_DOS)
        self.assertEqual(feagroundwater.Fredlund.getWCSat(), 0.15)
        self.assertEqual(feagroundwater.Fredlund.getWCRes(), 0.2)
        self.assertEqual(feagroundwater.Fredlund.getDoSSat(), 0.3)
        self.assertEqual(feagroundwater.Fredlund.getDoSRes(), 0.4)
    def testFredlundStageFactors(self):
        feagroundwater = self.material.Hydraulic.FEAGroundwater
        stageFactor = feagroundwater.Fredlund.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setAFactor(762.9)
        stageFactor.setBFactor(1413.6)
        stageFactor.setCFactor(468.3)
        stageFactor.setKsFactor(2350.4)
        stageFactor.setWCSatFactor(0.11)
        stageFactor.setWCResFactor(0.22)
        stageFactor.setDoSSatFactor(0.33)
        stageFactor.setDoSResFactor(0.44)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        feagroundwater = self.material.Hydraulic.FEAGroundwater
        stageFactor = feagroundwater.Fredlund.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getAFactor(), 762.9)
        self.assertEqual(stageFactor.getBFactor(), 1413.6)
        self.assertEqual(stageFactor.getCFactor(), 468.3)
        self.assertEqual(stageFactor.getKsFactor(), 2350.4)
        self.assertEqual(stageFactor.getWCSatFactor(), 0.11)
        self.assertEqual(stageFactor.getWCResFactor(), 0.22)
        self.assertEqual(stageFactor.getDoSSatFactor(), 0.33)
        self.assertEqual(stageFactor.getDoSResFactor(), 0.44)
