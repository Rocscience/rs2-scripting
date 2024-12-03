import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

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
        self.material.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.BROOKS_AND_COREY)
    def tearDown(self):
        self.model.close()
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)
    def testBrooksProperty(self):
        feagroundwater = self.material.Hydraulic.FEAGroundwater
        feagroundwater.Brooks.setPoreSizeIndex(836.5)
        feagroundwater.Brooks.setBubblingPressure(2628.5)
        feagroundwater.Brooks.setKs(972.5)
        feagroundwater.Brooks.setWCInputType(WCInputType.BY_DEGREE_OF_SATURATION)
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
        self.assertEqual(feagroundwater.Brooks.getWCInputType(), WCInputType.BY_DEGREE_OF_SATURATION)
        self.assertEqual(feagroundwater.Brooks.getWCSat(), 0.15)
        self.assertEqual(feagroundwater.Brooks.getWCRes(), 0.2)
        self.assertEqual(feagroundwater.Brooks.getDoSSat(), 0.3)
        self.assertEqual(feagroundwater.Brooks.getDoSRes(), 0.4)
    def testBrooksStageFactors(self):
        feagroundwater = self.material.Hydraulic.FEAGroundwater
        stageFactor = feagroundwater.Brooks.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setBubblingPressureFactor(86.7)
        stageFactor.setPoreSizeIndexFactor(762.9)
        stageFactor.setKsFactor(1413.6)
        stageFactor.setWCSatFactor(0.11)
        stageFactor.setWCResFactor(0.22)
        stageFactor.setDoSSatFactor(0.33)
        stageFactor.setDoSResFactor(0.44)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        feagroundwater = self.material.Hydraulic.FEAGroundwater
        stageFactor = feagroundwater.Brooks.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getBubblingPressureFactor(), 86.7)
        self.assertEqual(stageFactor.getPoreSizeIndexFactor(), 762.9)
        self.assertEqual(stageFactor.getKsFactor(), 1413.6)
        self.assertEqual(stageFactor.getWCSatFactor(), 0.11)
        self.assertEqual(stageFactor.getWCResFactor(), 0.22)
        self.assertEqual(stageFactor.getDoSSatFactor(), 0.33)
        self.assertEqual(stageFactor.getDoSResFactor(), 0.44)
