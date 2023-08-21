import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from src.rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestPlainStrandCable(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/blankProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testPlainStrandCableProperty(self):
        bolt = self.bolt
        self.bolt.setBoltType(BoltTypes.QUEENS_CABLE)
        bolt.PlainStrandCable.setBoreholeDiameter(230)
        bolt.PlainStrandCable.setCableDiameter(627)
        bolt.PlainStrandCable.setCableModulusE(1329)
        bolt.PlainStrandCable.setCablePeak(403)
        bolt.PlainStrandCable.setOutofPlaneSpacing(343)
        bolt.PlainStrandCable.setWaterCementRatio(2775)
        bolt.PlainStrandCable.setJointShear(0)
        bolt.PlainStrandCable.setFacePlates(1)
        bolt.PlainStrandCable.setAddPullOutForce(1)
        bolt.PlainStrandCable.setPullOutForce(1029)
        bolt.PlainStrandCable.setConstantShearStiffness(1)
        bolt.PlainStrandCable.setStiffness(2641)
        bolt.PlainStrandCable.setAddBulges(1)
        bolt.PlainStrandCable.setBulgeType(BulgeTypes.PHASE2_BULGE_NUTCASE_21)
        bolt.PlainStrandCable.setBulgeLocations([2.0, 3.1])
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertEqual(bolt.PlainStrandCable.getBoreholeDiameter(), 230)
        self.assertEqual(bolt.PlainStrandCable.getCableDiameter(), 627)
        self.assertEqual(bolt.PlainStrandCable.getCableModulusE(), 1329)
        self.assertEqual(bolt.PlainStrandCable.getCablePeak(), 403)
        self.assertEqual(bolt.PlainStrandCable.getOutofPlaneSpacing(), 343)
        self.assertEqual(bolt.PlainStrandCable.getWaterCementRatio(), 2775)
        self.assertEqual(bolt.PlainStrandCable.getJointShear(), 0)
        self.assertEqual(bolt.PlainStrandCable.getFacePlates(), 1)
        self.assertEqual(bolt.PlainStrandCable.getAddPullOutForce(), 1)
        self.assertEqual(bolt.PlainStrandCable.getPullOutForce(), 1029)
        self.assertEqual(bolt.PlainStrandCable.getConstantShearStiffness(), 1)
        self.assertEqual(bolt.PlainStrandCable.getStiffness(), 2641)
        self.assertEqual(bolt.PlainStrandCable.getAddBulges(), 1)
        self.assertEqual(bolt.PlainStrandCable.getBulgeType(), BulgeTypes.PHASE2_BULGE_NUTCASE_21)
        self.assertEqual(bolt.PlainStrandCable.getBulgeLocations(), [2.0, 3.1])
