import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

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
        self.material.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SIMPLE)
    def tearDown(self):
        self.model.close()
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)
    def testSimpleProperty(self):
        feagroundwater = self.material.Hydraulic.FEAGroundwater
        feagroundwater.Simple.setSoilType(EnhancedSimpleSoilTypes.SAND)
        feagroundwater.Simple.setKs(836.5)
        feagroundwater.Simple.setWCInputType(WCInputType.BY_DEGREE_OF_SATURATION)
        feagroundwater.Simple.setWCSat(0.15)
        feagroundwater.Simple.setWCRes(0.2)
        feagroundwater.Simple.setDoSSat(0.3)
        feagroundwater.Simple.setDoSRes(0.4)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        feagroundwater = self.material.Hydraulic.FEAGroundwater
        self.assertEqual(feagroundwater.Simple.getSoilType(), EnhancedSimpleSoilTypes.SAND)
        self.assertEqual(feagroundwater.Simple.getKs(), 836.5)
        self.assertEqual(feagroundwater.Simple.getWCInputType(), WCInputType.BY_DEGREE_OF_SATURATION)
        self.assertEqual(feagroundwater.Simple.getWCSat(), 0.15)
        self.assertEqual(feagroundwater.Simple.getWCRes(), 0.2)
        self.assertEqual(feagroundwater.Simple.getDoSSat(), 0.3)
        self.assertEqual(feagroundwater.Simple.getDoSRes(), 0.4)
    def testSimpleStageFactors(self):
        feagroundwater = self.material.Hydraulic.FEAGroundwater
        stageFactor = feagroundwater.Simple.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setKsFactor(2628.5)
        stageFactor.setWCSatFactor(0.11)
        stageFactor.setWCResFactor(0.22)
        stageFactor.setDoSSatFactor(0.33)
        stageFactor.setDoSResFactor(0.44)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        feagroundwater = self.material.Hydraulic.FEAGroundwater
        stageFactor = feagroundwater.Simple.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getKsFactor(), 2628.5)
        self.assertEqual(stageFactor.getWCSatFactor(), 0.11)
        self.assertEqual(stageFactor.getWCResFactor(), 0.22)
        self.assertEqual(stageFactor.getDoSSatFactor(), 0.33)
        self.assertEqual(stageFactor.getDoSResFactor(), 0.44)
