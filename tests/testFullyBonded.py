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
        bolt.FullyBonded.setBoltDiameter(3126.0)
        bolt.FullyBonded.setBoltModulusE(1333.6)
        bolt.FullyBonded.setTensileCapacity(3214.5)
        bolt.FullyBonded.setResidualTensileCapacity(869.2)
        bolt.FullyBonded.setOutofPlaneSpacing(339.4)
        bolt.FullyBonded.setPreTensioningForce(354.2)
        bolt.FullyBonded.setConstantPretensioningForceInInstallStage(1)
        bolt.FullyBonded.setJointShear(0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertEqual(bolt.FullyBonded.getBoltDiameter(), 3126.0)
        self.assertEqual(bolt.FullyBonded.getBoltModulusE(), 1333.6)
        self.assertEqual(bolt.FullyBonded.getTensileCapacity(), 3214.5)
        self.assertEqual(bolt.FullyBonded.getResidualTensileCapacity(), 869.2)
        self.assertEqual(bolt.FullyBonded.getOutofPlaneSpacing(), 339.4)
        self.assertEqual(bolt.FullyBonded.getPreTensioningForce(), 354.2)
        self.assertEqual(bolt.FullyBonded.getConstantPretensioningForceInInstallStage(), 1)
        self.assertEqual(bolt.FullyBonded.getJointShear(), 0)
