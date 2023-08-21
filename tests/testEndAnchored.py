import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from src.rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestEndAnchored(unittest.TestCase):
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
    def testEndAnchoredProperty(self):
        bolt = self.bolt
        self.bolt.setBoltType(BoltTypes.END_ANCHORED)
        bolt.EndAnchored.setBoltDiameter(1147)
        bolt.EndAnchored.setBoltModulusE(1194)
        bolt.EndAnchored.setTensileCapacity(1971)
        bolt.EndAnchored.setResidualTensileCapacity(989)
        bolt.EndAnchored.setOutofPlaneSpacing(2554)
        bolt.EndAnchored.setPreTensioningForce(303)
        bolt.EndAnchored.setConstantPretensioningForceInInstallStage(0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertEqual(bolt.EndAnchored.getBoltDiameter(), 1147)
        self.assertEqual(bolt.EndAnchored.getBoltModulusE(), 1194)
        self.assertEqual(bolt.EndAnchored.getTensileCapacity(), 1971)
        self.assertEqual(bolt.EndAnchored.getResidualTensileCapacity(), 989)
        self.assertEqual(bolt.EndAnchored.getOutofPlaneSpacing(), 2554)
        self.assertEqual(bolt.EndAnchored.getPreTensioningForce(), 303)
        self.assertEqual(bolt.EndAnchored.getConstantPretensioningForceInInstallStage(), 0)
