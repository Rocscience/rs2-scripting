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
        bolt.EndAnchored.setBoltDiameter(144.3)
        bolt.EndAnchored.setBoltModulusE(3095.3)
        bolt.EndAnchored.setTensileCapacity(1609.0)
        bolt.EndAnchored.setResidualTensileCapacity(2780.9)
        bolt.EndAnchored.setOutofPlaneSpacing(2641.2)
        bolt.EndAnchored.setPreTensioningForce(2108.5)
        bolt.EndAnchored.setConstantPretensioningForceInInstallStage(1)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertEqual(bolt.EndAnchored.getBoltDiameter(), 144.3)
        self.assertEqual(bolt.EndAnchored.getBoltModulusE(), 3095.3)
        self.assertEqual(bolt.EndAnchored.getTensileCapacity(), 1609.0)
        self.assertEqual(bolt.EndAnchored.getResidualTensileCapacity(), 2780.9)
        self.assertEqual(bolt.EndAnchored.getOutofPlaneSpacing(), 2641.2)
        self.assertEqual(bolt.EndAnchored.getPreTensioningForce(), 2108.5)
        self.assertEqual(bolt.EndAnchored.getConstantPretensioningForceInInstallStage(), 1)
