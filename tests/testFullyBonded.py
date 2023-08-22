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
        bolt.FullyBonded.setBoltDiameter(1995.4)
        bolt.FullyBonded.setBoltModulusE(553.7)
        bolt.FullyBonded.setTensileCapacity(993.0)
        bolt.FullyBonded.setResidualTensileCapacity(2677.7)
        bolt.FullyBonded.setOutofPlaneSpacing(1557.4)
        bolt.FullyBonded.setPreTensioningForce(1800.7)
        bolt.FullyBonded.setConstantPretensioningForceInInstallStage(0)
        bolt.FullyBonded.setJointShear(1)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertEqual(bolt.FullyBonded.getBoltDiameter(), 1995.4)
        self.assertEqual(bolt.FullyBonded.getBoltModulusE(), 553.7)
        self.assertEqual(bolt.FullyBonded.getTensileCapacity(), 993.0)
        self.assertEqual(bolt.FullyBonded.getResidualTensileCapacity(), 2677.7)
        self.assertEqual(bolt.FullyBonded.getOutofPlaneSpacing(), 1557.4)
        self.assertEqual(bolt.FullyBonded.getPreTensioningForce(), 1800.7)
        self.assertEqual(bolt.FullyBonded.getConstantPretensioningForceInInstallStage(), 0)
        self.assertEqual(bolt.FullyBonded.getJointShear(), 1)
