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
        bolt.EndAnchored.setBoltDiameter(10.1)
        bolt.EndAnchored.setOutofPlaneSpacing(10.1)
        bolt.EndAnchored.setBoltModulusE(10.1)
        bolt.EndAnchored.setTensileCapacity(10.1)
        bolt.EndAnchored.setPreTensioningForce(10.1)
        bolt.EndAnchored.setResidualTensileCapacity(10.1)
        bolt.EndAnchored.setConstantPretensioningForceInInstallStage(True)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertEqual(bolt.EndAnchored.getBoltDiameter(), 10.1)
        self.assertEqual(bolt.EndAnchored.getOutofPlaneSpacing(), 10.1)
        self.assertEqual(bolt.EndAnchored.getBoltModulusE(), 10.1)
        self.assertEqual(bolt.EndAnchored.getTensileCapacity(), 10.1)
        self.assertEqual(bolt.EndAnchored.getPreTensioningForce(), 10.1)
        self.assertEqual(bolt.EndAnchored.getResidualTensileCapacity(), 10.1)
        self.assertEqual(bolt.EndAnchored.getConstantPretensioningForceInInstallStage(), True)
