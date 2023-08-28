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
        blankModelPath = f"{parentDirectory}/resources/blankProject.fez"
        self.bolt = self.model.getAllBoltProperties()[0]
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testTiebackProperty(self):
        bolt = self.bolt
        self.bolt.setBoltType(BoltTypes.TIEBACK_BOLT)
        bolt.Tieback.setBoltDiameter(2542.3)
        bolt.Tieback.setBoltModulusE(826.0)
        bolt.Tieback.setBoltModel(BoltModels.P2_BOLT_ELASTIC)
        bolt.Tieback.setTensileCapacity(2979.0)
        bolt.Tieback.setResidualTensileCapacity(1757.8)
        bolt.Tieback.setOutofPlaneSpacing(647.7)
        bolt.Tieback.setMaterialDependent(1)
        bolt.Tieback.setBondStrengthCoefficient(162.6)
        bolt.Tieback.setBondShearStiffnessCoefficient(1011.2)
        bolt.Tieback.setBondShearStiffness(2229.6)
        bolt.Tieback.setBondStrength(296.3)
        bolt.Tieback.setJointShear(1)
        bolt.Tieback.setBoreholeDiameter(3178.3)
        bolt.Tieback.setPreTensioningForce(1017.6)
        bolt.Tieback.setConstantPretensioningForceInInstallStage(0)
        bolt.Tieback.setFacePlates(0)
        bolt.Tieback.setAddPullOutForce(1)
        bolt.Tieback.setPullOutForce(2204.4)
        bolt.Tieback.setUseBondPercentageLength(1)
        bolt.Tieback.setPercentageBondLength(25561)
        bolt.Tieback.setBondLength(1575.9)
        bolt.Tieback.setUseSecondaryBondLength(1)
        bolt.Tieback.setSecondaryBondLengthType(SecondaryBondLengthType.P2_BOLT_TIEBACK_SECONDARY_PHYSICAL)
        bolt.Tieback.setPercentOfSecondaryBondLength(2363)
        bolt.Tieback.setSecondaryBondLength(30.3)
        bolt.Tieback.setDelayInstallAfterBolt(13648)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertEqual(bolt.Tieback.getBoltDiameter(), 2542.3)
        self.assertEqual(bolt.Tieback.getBoltModulusE(), 826.0)
        self.assertEqual(bolt.Tieback.getBoltModel(), BoltModels.P2_BOLT_ELASTIC)
        self.assertEqual(bolt.Tieback.getTensileCapacity(), 2979.0)
        self.assertEqual(bolt.Tieback.getResidualTensileCapacity(), 1757.8)
        self.assertEqual(bolt.Tieback.getOutofPlaneSpacing(), 647.7)
        self.assertEqual(bolt.Tieback.getMaterialDependent(), 1)
        self.assertEqual(bolt.Tieback.getBondStrengthCoefficient(), 162.6)
        self.assertEqual(bolt.Tieback.getBondShearStiffnessCoefficient(), 1011.2)
        self.assertEqual(bolt.Tieback.getBondShearStiffness(), 2229.6)
        self.assertEqual(bolt.Tieback.getBondStrength(), 296.3)
        self.assertEqual(bolt.Tieback.getJointShear(), 1)
        self.assertEqual(bolt.Tieback.getBoreholeDiameter(), 3178.3)
        self.assertEqual(bolt.Tieback.getPreTensioningForce(), 1017.6)
        self.assertEqual(bolt.Tieback.getConstantPretensioningForceInInstallStage(), 0)
        self.assertEqual(bolt.Tieback.getFacePlates(), 0)
        self.assertEqual(bolt.Tieback.getAddPullOutForce(), 1)
        self.assertEqual(bolt.Tieback.getPullOutForce(), 2204.4)
        self.assertEqual(bolt.Tieback.getUseBondPercentageLength(), 1)
        self.assertEqual(bolt.Tieback.getPercentageBondLength(), 25561)
        self.assertEqual(bolt.Tieback.getBondLength(), 1575.9)
        self.assertEqual(bolt.Tieback.getUseSecondaryBondLength(), 1)
        self.assertEqual(bolt.Tieback.getSecondaryBondLengthType(), SecondaryBondLengthType.P2_BOLT_TIEBACK_SECONDARY_PHYSICAL)
        self.assertEqual(bolt.Tieback.getPercentOfSecondaryBondLength(), 2363)
        self.assertEqual(bolt.Tieback.getSecondaryBondLength(), 30.3)
        self.assertEqual(bolt.Tieback.getDelayInstallAfterBolt(), 13648)
