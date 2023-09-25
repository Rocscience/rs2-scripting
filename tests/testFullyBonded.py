import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from src.rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestFullyBonded(unittest.TestCase):
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
    def testFullyBondedProperty(self):
        bolt = self.bolt
        self.bolt.setBoltType(BoltTypes.FULLY_BONDED)
        bolt.FullyBonded.setBoltDiameter(836.5)
        bolt.FullyBonded.setBoltModulusE(2628.5)
        bolt.FullyBonded.setTensileCapacity(972.5)
        bolt.FullyBonded.setResidualTensileCapacity(86.7)
        bolt.FullyBonded.setOutofPlaneSpacing(762.9)
        bolt.FullyBonded.setPreTensioningForce(1413.6)
        bolt.FullyBonded.setConstantPretensioningForceInInstallStage(0)
        bolt.FullyBonded.setJointShear(0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertEqual(bolt.FullyBonded.getBoltDiameter(), 836.5)
        self.assertEqual(bolt.FullyBonded.getBoltModulusE(), 2628.5)
        self.assertEqual(bolt.FullyBonded.getTensileCapacity(), 972.5)
        self.assertEqual(bolt.FullyBonded.getResidualTensileCapacity(), 86.7)
        self.assertEqual(bolt.FullyBonded.getOutofPlaneSpacing(), 762.9)
        self.assertEqual(bolt.FullyBonded.getPreTensioningForce(), 1413.6)
        self.assertEqual(bolt.FullyBonded.getConstantPretensioningForceInInstallStage(), 0)
        self.assertEqual(bolt.FullyBonded.getJointShear(), 0)
