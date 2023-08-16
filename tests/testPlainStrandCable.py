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
        bolt.PlainStrandCable.setBoreholeDiameter(10.1)
        bolt.PlainStrandCable.setCableDiameter(10.1)
        bolt.PlainStrandCable.setCableModulusE(10.1)
        bolt.PlainStrandCable.setCablePeak(10.1)
        bolt.PlainStrandCable.setOutofPlaneSpacing(10.1)
        bolt.PlainStrandCable.setWaterCementRatio(10.1)
        bolt.PlainStrandCable.setJointShear(True)
        bolt.PlainStrandCable.setFacePlates(True)
        bolt.PlainStrandCable.setAddPullOutForce(True)
        bolt.PlainStrandCable.setPullOutForce(10.1)
        bolt.PlainStrandCable.setConstantShearStiffness(True)
        bolt.PlainStrandCable.setStiffness(10.1)
        bolt.PlainStrandCable.setAddBulges(True)
        bolt.PlainStrandCable.setBulgeType(BulgeTypes.PHASE2_BULGE_NUTCASE_21)
        bolt.PlainStrandCable.setBulgeLocations([2.0, 3.1])
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertEqual(bolt.PlainStrandCable.getBoreholeDiameter(), 10.1)
        self.assertEqual(bolt.PlainStrandCable.getCableDiameter(), 10.1)
        self.assertEqual(bolt.PlainStrandCable.getCableModulusE(), 10.1)
        self.assertEqual(bolt.PlainStrandCable.getCablePeak(), 10.1)
        self.assertEqual(bolt.PlainStrandCable.getOutofPlaneSpacing(), 10.1)
        self.assertEqual(bolt.PlainStrandCable.getWaterCementRatio(), 10.1)
        self.assertEqual(bolt.PlainStrandCable.getJointShear(), True)
        self.assertEqual(bolt.PlainStrandCable.getFacePlates(), True)
        self.assertEqual(bolt.PlainStrandCable.getAddPullOutForce(), True)
        self.assertEqual(bolt.PlainStrandCable.getPullOutForce(), 10.1)
        self.assertEqual(bolt.PlainStrandCable.getConstantShearStiffness(), True)
        self.assertEqual(bolt.PlainStrandCable.getStiffness(), 10.1)
        self.assertEqual(bolt.PlainStrandCable.getAddBulges(), True)
        self.assertEqual(bolt.PlainStrandCable.getBulgeType(), BulgeTypes.PHASE2_BULGE_NUTCASE_21)
        self.assertEqual(bolt.PlainStrandCable.getBulgeLocations(), [2.0, 3.1])
