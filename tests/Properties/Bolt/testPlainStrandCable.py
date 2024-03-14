import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestPlainStrandCable(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
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
        self.bolt.setBoltType(BoltTypes.PLAIN_STRAND_CABLE)
        bolt.PlainStrandCable.setBoreholeDiameter(836.5)
        bolt.PlainStrandCable.setCableDiameter(2628.5)
        bolt.PlainStrandCable.setCableModulusE(972.5)
        bolt.PlainStrandCable.setCablePeak(86.7)
        bolt.PlainStrandCable.setOutofPlaneSpacing(762.9)
        bolt.PlainStrandCable.setWaterCementRatio(1413.6)
        bolt.PlainStrandCable.setJointShear(0)
        bolt.PlainStrandCable.setFacePlates(0)
        bolt.PlainStrandCable.setAddPullOutForce(1)
        bolt.PlainStrandCable.setPullOutForce(2572.7)
        bolt.PlainStrandCable.setConstantShearStiffness(0)
        bolt.PlainStrandCable.setStiffness(3213.4)
        bolt.PlainStrandCable.setAddBulges(True)
        bolt.PlainStrandCable.setBulgeType(BulgeTypes.NUT_CASE_21MM)
        bolt.PlainStrandCable.setBulgeLocations([2.0, 3.1])
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertEqual(bolt.PlainStrandCable.getBoreholeDiameter(), 836.5)
        self.assertEqual(bolt.PlainStrandCable.getCableDiameter(), 2628.5)
        self.assertEqual(bolt.PlainStrandCable.getCableModulusE(), 972.5)
        self.assertEqual(bolt.PlainStrandCable.getCablePeak(), 86.7)
        self.assertEqual(bolt.PlainStrandCable.getOutofPlaneSpacing(), 762.9)
        self.assertEqual(bolt.PlainStrandCable.getWaterCementRatio(), 1413.6)
        self.assertEqual(bolt.PlainStrandCable.getJointShear(), 0)
        self.assertEqual(bolt.PlainStrandCable.getFacePlates(), 0)
        self.assertEqual(bolt.PlainStrandCable.getAddPullOutForce(), 1)
        self.assertEqual(bolt.PlainStrandCable.getPullOutForce(), 2572.7)
        self.assertEqual(bolt.PlainStrandCable.getConstantShearStiffness(), 0)
        self.assertEqual(bolt.PlainStrandCable.getStiffness(), 3213.4)
        self.assertEqual(bolt.PlainStrandCable.getAddBulges(), True)
        self.assertEqual(bolt.PlainStrandCable.getBulgeType(), BulgeTypes.NUT_CASE_21MM)
        self.assertEqual(bolt.PlainStrandCable.getBulgeLocations(), [2.0, 3.1])
