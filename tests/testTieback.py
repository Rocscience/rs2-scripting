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
        bolt.Tieback.setOutofPlaneSpacing(10.1)
        bolt.Tieback.setBoltDiameter(10.1)
        bolt.Tieback.setBoltModulusE(10.1)
        bolt.Tieback.setMaterialDependent(True)
        bolt.Tieback.setBoltModel(BoltModels.P2_BOLT_ELASTIC)
        bolt.Tieback.setTensileCapacity(10.1)
        bolt.Tieback.setResidualTensileCapacity(10.1)
        bolt.Tieback.setBondStrengthCoefficient(10.1)
        bolt.Tieback.setBondShearStiffnessCoefficient(10.1)
        bolt.Tieback.setBondShearStiffness(10.1)
        bolt.Tieback.setBondStrength(10.1)
        bolt.Tieback.setJointShear(True)
        bolt.Tieback.setBoreholeDiameter(10.1)
        bolt.Tieback.setPreTensioningForce(10.1)
        bolt.Tieback.setConstantPretensioningForceInInstallStage(True)
        bolt.Tieback.setFacePlates(True)
        bolt.Tieback.setAddPullOutForce(True)
        bolt.Tieback.setPullOutForce(10.1)
        bolt.Tieback.setUseBondPercentageLength(True)
        bolt.Tieback.setPercentageBondLength(1)
        bolt.Tieback.setBondLength(10.1)
        bolt.Tieback.setUseSecondaryBondLength(True)
        bolt.Tieback.setSecondaryBondLengthType(SecondaryBondLengthType.P2_BOLT_TIEBACK_SECONDARY_PHYSICAL)
        bolt.Tieback.setPercentOfSecondaryBondLength(1)
        bolt.Tieback.setSecondaryBondLength(10.1)
        bolt.Tieback.setDelayInstallAfterBolt(1)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertEqual(bolt.Tieback.getOutofPlaneSpacing(), 10.1)
        self.assertEqual(bolt.Tieback.getBoltDiameter(), 10.1)
        self.assertEqual(bolt.Tieback.getBoltModulusE(), 10.1)
        self.assertEqual(bolt.Tieback.getMaterialDependent(), True)
        self.assertEqual(bolt.Tieback.getBoltModel(), BoltModels.P2_BOLT_ELASTIC)
        self.assertEqual(bolt.Tieback.getTensileCapacity(), 10.1)
        self.assertEqual(bolt.Tieback.getResidualTensileCapacity(), 10.1)
        self.assertEqual(bolt.Tieback.getBondStrengthCoefficient(), 10.1)
        self.assertEqual(bolt.Tieback.getBondShearStiffnessCoefficient(), 10.1)
        self.assertEqual(bolt.Tieback.getBondShearStiffness(), 10.1)
        self.assertEqual(bolt.Tieback.getBondStrength(), 10.1)
        self.assertEqual(bolt.Tieback.getJointShear(), True)
        self.assertEqual(bolt.Tieback.getBoreholeDiameter(), 10.1)
        self.assertEqual(bolt.Tieback.getPreTensioningForce(), 10.1)
        self.assertEqual(bolt.Tieback.getConstantPretensioningForceInInstallStage(), True)
        self.assertEqual(bolt.Tieback.getFacePlates(), True)
        self.assertEqual(bolt.Tieback.getAddPullOutForce(), True)
        self.assertEqual(bolt.Tieback.getPullOutForce(), 10.1)
        self.assertEqual(bolt.Tieback.getUseBondPercentageLength(), True)
        self.assertEqual(bolt.Tieback.getPercentageBondLength(), 1)
        self.assertEqual(bolt.Tieback.getBondLength(), 10.1)
        self.assertEqual(bolt.Tieback.getUseSecondaryBondLength(), True)
        self.assertEqual(bolt.Tieback.getSecondaryBondLengthType(), SecondaryBondLengthType.P2_BOLT_TIEBACK_SECONDARY_PHYSICAL)
        self.assertEqual(bolt.Tieback.getPercentOfSecondaryBondLength(), 1)
        self.assertEqual(bolt.Tieback.getSecondaryBondLength(), 10.1)
        self.assertEqual(bolt.Tieback.getDelayInstallAfterBolt(), 1)
