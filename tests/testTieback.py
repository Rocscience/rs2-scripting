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
        bolt.Tieback.setBoltDiameter(1628)
        bolt.Tieback.setBoltModulusE(578)
        bolt.Tieback.setBoltModel(BoltModels.P2_BOLT_ELASTIC)
        bolt.Tieback.setTensileCapacity(2364)
        bolt.Tieback.setResidualTensileCapacity(216)
        bolt.Tieback.setOutofPlaneSpacing(2629)
        bolt.Tieback.setMaterialDependent(0)
        bolt.Tieback.setBondStrengthCoefficient(1878)
        bolt.Tieback.setBondShearStiffnessCoefficient(441)
        bolt.Tieback.setBondShearStiffness(1183)
        bolt.Tieback.setBondStrength(3227)
        bolt.Tieback.setJointShear(1)
        bolt.Tieback.setBoreholeDiameter(192)
        bolt.Tieback.setPreTensioningForce(1750)
        bolt.Tieback.setConstantPretensioningForceInInstallStage(1)
        bolt.Tieback.setFacePlates(1)
        bolt.Tieback.setAddPullOutForce(0)
        bolt.Tieback.setPullOutForce(2801)
        bolt.Tieback.setUseBondPercentageLength(1)
        bolt.Tieback.setPercentageBondLength(2800)
        bolt.Tieback.setBondLength(475)
        bolt.Tieback.setUseSecondaryBondLength(0)
        bolt.Tieback.setSecondaryBondLengthType(SecondaryBondLengthType.P2_BOLT_TIEBACK_SECONDARY_PHYSICAL)
        bolt.Tieback.setPercentOfSecondaryBondLength(123)
        bolt.Tieback.setSecondaryBondLength(3252)
        bolt.Tieback.setDelayInstallAfterBolt(6411)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertEqual(bolt.Tieback.getBoltDiameter(), 1628)
        self.assertEqual(bolt.Tieback.getBoltModulusE(), 578)
        self.assertEqual(bolt.Tieback.getBoltModel(), BoltModels.P2_BOLT_ELASTIC)
        self.assertEqual(bolt.Tieback.getTensileCapacity(), 2364)
        self.assertEqual(bolt.Tieback.getResidualTensileCapacity(), 216)
        self.assertEqual(bolt.Tieback.getOutofPlaneSpacing(), 2629)
        self.assertEqual(bolt.Tieback.getMaterialDependent(), 0)
        self.assertEqual(bolt.Tieback.getBondStrengthCoefficient(), 1878)
        self.assertEqual(bolt.Tieback.getBondShearStiffnessCoefficient(), 441)
        self.assertEqual(bolt.Tieback.getBondShearStiffness(), 1183)
        self.assertEqual(bolt.Tieback.getBondStrength(), 3227)
        self.assertEqual(bolt.Tieback.getJointShear(), 1)
        self.assertEqual(bolt.Tieback.getBoreholeDiameter(), 192)
        self.assertEqual(bolt.Tieback.getPreTensioningForce(), 1750)
        self.assertEqual(bolt.Tieback.getConstantPretensioningForceInInstallStage(), 1)
        self.assertEqual(bolt.Tieback.getFacePlates(), 1)
        self.assertEqual(bolt.Tieback.getAddPullOutForce(), 0)
        self.assertEqual(bolt.Tieback.getPullOutForce(), 2801)
        self.assertEqual(bolt.Tieback.getUseBondPercentageLength(), 1)
        self.assertEqual(bolt.Tieback.getPercentageBondLength(), 2800)
        self.assertEqual(bolt.Tieback.getBondLength(), 475)
        self.assertEqual(bolt.Tieback.getUseSecondaryBondLength(), 0)
        self.assertEqual(bolt.Tieback.getSecondaryBondLengthType(), SecondaryBondLengthType.P2_BOLT_TIEBACK_SECONDARY_PHYSICAL)
        self.assertEqual(bolt.Tieback.getPercentOfSecondaryBondLength(), 123)
        self.assertEqual(bolt.Tieback.getSecondaryBondLength(), 3252)
        self.assertEqual(bolt.Tieback.getDelayInstallAfterBolt(), 6411)
