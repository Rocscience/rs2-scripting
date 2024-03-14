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
        self.material.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.VAN_GENUCHTEN)
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
        feagroundwater.Genuchten.setWCInputType(WCInputType.BY_DEGREE_OF_SATURATION)
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
        self.assertEqual(feagroundwater.Genuchten.getWCInputType(), WCInputType.BY_DEGREE_OF_SATURATION)
        self.assertEqual(feagroundwater.Genuchten.getWCSat(), 0.15)
        self.assertEqual(feagroundwater.Genuchten.getWCRes(), 0.2)
        self.assertEqual(feagroundwater.Genuchten.getDoSSat(), 0.3)
        self.assertEqual(feagroundwater.Genuchten.getDoSRes(), 0.4)
