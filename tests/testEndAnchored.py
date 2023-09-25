import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestEndAnchored(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/BlankModelWithStageFactors.fez"
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
        bolt.EndAnchored.setBoltDiameter(836.5)
        bolt.EndAnchored.setBoltModulusE(2628.5)
        bolt.EndAnchored.setTensileCapacity(972.5)
        bolt.EndAnchored.setResidualTensileCapacity(86.7)
        bolt.EndAnchored.setOutofPlaneSpacing(762.9)
        bolt.EndAnchored.setPreTensioningForce(1413.6)
        bolt.EndAnchored.setConstantPretensioningForceInInstallStage(0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertEqual(bolt.EndAnchored.getBoltDiameter(), 836.5)
        self.assertEqual(bolt.EndAnchored.getBoltModulusE(), 2628.5)
        self.assertEqual(bolt.EndAnchored.getTensileCapacity(), 972.5)
        self.assertEqual(bolt.EndAnchored.getResidualTensileCapacity(), 86.7)
        self.assertEqual(bolt.EndAnchored.getOutofPlaneSpacing(), 762.9)
        self.assertEqual(bolt.EndAnchored.getPreTensioningForce(), 1413.6)
        self.assertEqual(bolt.EndAnchored.getConstantPretensioningForceInInstallStage(), 0)
