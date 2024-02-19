import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestGenuchten(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProjectTransientGroundwater.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        self.material.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_VAN_GENUCHTEN)
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testGenuchtenProperty(self):
        feagroundwater = self.material.Hydraulic.FEAGroundwater
        feagroundwater.Genuchten.setAlpha(836.5)
        feagroundwater.Genuchten.setN(2628.5)
        feagroundwater.Genuchten.setCustomM(1)
        feagroundwater.Genuchten.setM(972.5)
        feagroundwater.Genuchten.setKs(86.7)
        feagroundwater.Genuchten.setWCInputType(WCInputType.WC_INPUT_DOS)
        feagroundwater.Genuchten.setWCSat(0.15)
        feagroundwater.Genuchten.setWCRes(0.2)
        feagroundwater.Genuchten.setDoSSat(0.3)
        feagroundwater.Genuchten.setDoSRes(0.4)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        feagroundwater = self.material.Hydraulic.FEAGroundwater
        self.assertEqual(feagroundwater.Genuchten.getAlpha(), 836.5)
        self.assertEqual(feagroundwater.Genuchten.getN(), 2628.5)
        self.assertEqual(feagroundwater.Genuchten.getCustomM(), 1)
        self.assertEqual(feagroundwater.Genuchten.getM(), 972.5)
        self.assertEqual(feagroundwater.Genuchten.getKs(), 86.7)
        self.assertEqual(feagroundwater.Genuchten.getWCInputType(), WCInputType.WC_INPUT_DOS)
        self.assertEqual(feagroundwater.Genuchten.getWCSat(), 0.15)
        self.assertEqual(feagroundwater.Genuchten.getWCRes(), 0.2)
        self.assertEqual(feagroundwater.Genuchten.getDoSSat(), 0.3)
        self.assertEqual(feagroundwater.Genuchten.getDoSRes(), 0.4)
    def testGenuchtenStageFactors(self):
        feagroundwater = self.material.Hydraulic.FEAGroundwater
        stageFactor = feagroundwater.Genuchten.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setMFactor(762.9)
        stageFactor.setNFactor(1413.6)
        stageFactor.setAlphaFactor(468.3)
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
        stageFactor = feagroundwater.Genuchten.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getMFactor(), 762.9)
        self.assertEqual(stageFactor.getNFactor(), 1413.6)
        self.assertEqual(stageFactor.getAlphaFactor(), 468.3)
        self.assertEqual(stageFactor.getKsFactor(), 2350.4)
        self.assertEqual(stageFactor.getWCSatFactor(), 0.11)
        self.assertEqual(stageFactor.getWCResFactor(), 0.22)
        self.assertEqual(stageFactor.getDoSSatFactor(), 0.33)
        self.assertEqual(stageFactor.getDoSResFactor(), 0.44)
