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
        bolt.FullyBonded.setBoltDiameter(2764)
        bolt.FullyBonded.setBoltModulusE(2752)
        bolt.FullyBonded.setTensileCapacity(3010)
        bolt.FullyBonded.setResidualTensileCapacity(1589)
        bolt.FullyBonded.setOutofPlaneSpacing(354)
        bolt.FullyBonded.setPreTensioningForce(496)
        bolt.FullyBonded.setConstantPretensioningForceInInstallStage(0)
        bolt.FullyBonded.setJointShear(0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertEqual(bolt.FullyBonded.getBoltDiameter(), 2764)
        self.assertEqual(bolt.FullyBonded.getBoltModulusE(), 2752)
        self.assertEqual(bolt.FullyBonded.getTensileCapacity(), 3010)
        self.assertEqual(bolt.FullyBonded.getResidualTensileCapacity(), 1589)
        self.assertEqual(bolt.FullyBonded.getOutofPlaneSpacing(), 354)
        self.assertEqual(bolt.FullyBonded.getPreTensioningForce(), 496)
        self.assertEqual(bolt.FullyBonded.getConstantPretensioningForceInInstallStage(), 0)
        self.assertEqual(bolt.FullyBonded.getJointShear(), 0)
