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
        bolt.FullyBonded.setBoltDiameter(10.1)
        bolt.FullyBonded.setOutofPlaneSpacing(10.1)
        bolt.FullyBonded.setBoltModulusE(10.1)
        bolt.FullyBonded.setTensileCapacity(10.1)
        bolt.FullyBonded.setPreTensioningForce(10.1)
        bolt.FullyBonded.setResidualTensileCapacity(10.1)
        bolt.FullyBonded.setConstantPretensioningForceInInstallStage(True)
        bolt.FullyBonded.setJointShear(True)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertEqual(bolt.FullyBonded.getBoltDiameter(), 10.1)
        self.assertEqual(bolt.FullyBonded.getOutofPlaneSpacing(), 10.1)
        self.assertEqual(bolt.FullyBonded.getBoltModulusE(), 10.1)
        self.assertEqual(bolt.FullyBonded.getTensileCapacity(), 10.1)
        self.assertEqual(bolt.FullyBonded.getPreTensioningForce(), 10.1)
        self.assertEqual(bolt.FullyBonded.getResidualTensileCapacity(), 10.1)
        self.assertEqual(bolt.FullyBonded.getConstantPretensioningForceInInstallStage(), True)
        self.assertEqual(bolt.FullyBonded.getJointShear(), True)
