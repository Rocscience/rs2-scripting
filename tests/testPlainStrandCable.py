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
        bolt.PlainStrandCable.setBoreholeDiameter(3083.6)
        bolt.PlainStrandCable.setCableDiameter(5.3)
        bolt.PlainStrandCable.setCableModulusE(2248.3)
        bolt.PlainStrandCable.setCablePeak(2060.0)
        bolt.PlainStrandCable.setOutofPlaneSpacing(3270.2)
        bolt.PlainStrandCable.setWaterCementRatio(1345.8)
        bolt.PlainStrandCable.setJointShear(0)
        bolt.PlainStrandCable.setFacePlates(0)
        bolt.PlainStrandCable.setAddPullOutForce(0)
        bolt.PlainStrandCable.setPullOutForce(355.7)
        bolt.PlainStrandCable.setConstantShearStiffness(1)
        bolt.PlainStrandCable.setStiffness(2861.7)
        bolt.PlainStrandCable.setAddBulges(True)
        bolt.PlainStrandCable.setBulgeType(BulgeTypes.PHASE2_BULGE_NUTCASE_21)
        bolt.PlainStrandCable.setBulgeLocations([2.0, 3.1])
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertEqual(bolt.PlainStrandCable.getBoreholeDiameter(), 3083.6)
        self.assertEqual(bolt.PlainStrandCable.getCableDiameter(), 5.3)
        self.assertEqual(bolt.PlainStrandCable.getCableModulusE(), 2248.3)
        self.assertEqual(bolt.PlainStrandCable.getCablePeak(), 2060.0)
        self.assertEqual(bolt.PlainStrandCable.getOutofPlaneSpacing(), 3270.2)
        self.assertEqual(bolt.PlainStrandCable.getWaterCementRatio(), 1345.8)
        self.assertEqual(bolt.PlainStrandCable.getJointShear(), 0)
        self.assertEqual(bolt.PlainStrandCable.getFacePlates(), 0)
        self.assertEqual(bolt.PlainStrandCable.getAddPullOutForce(), 0)
        self.assertEqual(bolt.PlainStrandCable.getPullOutForce(), 355.7)
        self.assertEqual(bolt.PlainStrandCable.getConstantShearStiffness(), 1)
        self.assertEqual(bolt.PlainStrandCable.getStiffness(), 2861.7)
        self.assertEqual(bolt.PlainStrandCable.getAddBulges(), True)
        self.assertEqual(bolt.PlainStrandCable.getBulgeType(), BulgeTypes.PHASE2_BULGE_NUTCASE_21)
        self.assertEqual(bolt.PlainStrandCable.getBulgeLocations(), [2.0, 3.1])