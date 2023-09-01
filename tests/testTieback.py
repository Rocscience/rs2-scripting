import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from src.rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestTieback(unittest.TestCase):
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
    def testTiebackProperty(self):
        bolt = self.bolt
        self.bolt.setBoltType(BoltTypes.TIEBACK_BOLT)
        bolt.Tieback.setBoltDiameter(186.6)
        bolt.Tieback.setBoltModulusE(2731.1)
        bolt.Tieback.setBoltModel(BoltModels.P2_BOLT_ELASTIC)
        bolt.Tieback.setTensileCapacity(1337.7)
        bolt.Tieback.setResidualTensileCapacity(1825.9)
        bolt.Tieback.setOutofPlaneSpacing(2459.3)
        bolt.Tieback.setMaterialDependent(1)
        bolt.Tieback.setBondStrengthCoefficient(3226.1)
        bolt.Tieback.setBondShearStiffnessCoefficient(1446.9)
        bolt.Tieback.setBondShearStiffness(1813.5)
        bolt.Tieback.setBondStrength(251.2)
        bolt.Tieback.setJointShear(1)
        bolt.Tieback.setBoreholeDiameter(629.2)
        bolt.Tieback.setPreTensioningForce(1966.4)
        bolt.Tieback.setConstantPretensioningForceInInstallStage(1)
        bolt.Tieback.setFacePlates(0)
        bolt.Tieback.setAddPullOutForce(1)
        bolt.Tieback.setPullOutForce(2652.8)
        bolt.Tieback.setUseBondPercentageLength(0)
        bolt.Tieback.setPercentageBondLength(28765)
        bolt.Tieback.setBondLength(2333.2)
        bolt.Tieback.setUseSecondaryBondLength(1)
        bolt.Tieback.setSecondaryBondLengthType(SecondaryBondLengthType.P2_BOLT_TIEBACK_SECONDARY_PHYSICAL)
        bolt.Tieback.setPercentOfSecondaryBondLength(3659)
        bolt.Tieback.setSecondaryBondLength(287.2)
        bolt.Tieback.setDelayInstallAfterBolt(24395)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertEqual(bolt.Tieback.getBoltDiameter(), 186.6)
        self.assertEqual(bolt.Tieback.getBoltModulusE(), 2731.1)
        self.assertEqual(bolt.Tieback.getBoltModel(), BoltModels.P2_BOLT_ELASTIC)
        self.assertEqual(bolt.Tieback.getTensileCapacity(), 1337.7)
        self.assertEqual(bolt.Tieback.getResidualTensileCapacity(), 1825.9)
        self.assertEqual(bolt.Tieback.getOutofPlaneSpacing(), 2459.3)
        self.assertEqual(bolt.Tieback.getMaterialDependent(), 1)
        self.assertEqual(bolt.Tieback.getBondStrengthCoefficient(), 3226.1)
        self.assertEqual(bolt.Tieback.getBondShearStiffnessCoefficient(), 1446.9)
        self.assertEqual(bolt.Tieback.getBondShearStiffness(), 1813.5)
        self.assertEqual(bolt.Tieback.getBondStrength(), 251.2)
        self.assertEqual(bolt.Tieback.getJointShear(), 1)
        self.assertEqual(bolt.Tieback.getBoreholeDiameter(), 629.2)
        self.assertEqual(bolt.Tieback.getPreTensioningForce(), 1966.4)
        self.assertEqual(bolt.Tieback.getConstantPretensioningForceInInstallStage(), 1)
        self.assertEqual(bolt.Tieback.getFacePlates(), 0)
        self.assertEqual(bolt.Tieback.getAddPullOutForce(), 1)
        self.assertEqual(bolt.Tieback.getPullOutForce(), 2652.8)
        self.assertEqual(bolt.Tieback.getUseBondPercentageLength(), 0)
        self.assertEqual(bolt.Tieback.getPercentageBondLength(), 28765)
        self.assertEqual(bolt.Tieback.getBondLength(), 2333.2)
        self.assertEqual(bolt.Tieback.getUseSecondaryBondLength(), 1)
        self.assertEqual(bolt.Tieback.getSecondaryBondLengthType(), SecondaryBondLengthType.P2_BOLT_TIEBACK_SECONDARY_PHYSICAL)
        self.assertEqual(bolt.Tieback.getPercentOfSecondaryBondLength(), 3659)
        self.assertEqual(bolt.Tieback.getSecondaryBondLength(), 287.2)
        self.assertEqual(bolt.Tieback.getDelayInstallAfterBolt(), 24395)
