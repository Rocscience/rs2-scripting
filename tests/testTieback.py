import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestTieback(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
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
        bolt.Tieback.setBoltDiameter(836.5)
        bolt.Tieback.setBoltModulusE(2628.5)
        bolt.Tieback.setBoltModel(BoltModels.P2_BOLT_ELASTIC)
        bolt.Tieback.setTensileCapacity(972.5)
        bolt.Tieback.setResidualTensileCapacity(86.7)
        bolt.Tieback.setOutofPlaneSpacing(762.9)
        bolt.Tieback.setMaterialDependent(0)
        bolt.Tieback.setBondStrengthCoefficient(468.3)
        bolt.Tieback.setBondShearStiffnessCoefficient(2350.4)
        bolt.Tieback.setBondShearStiffness(2598.3)
        bolt.Tieback.setBondStrength(2572.7)
        bolt.Tieback.setJointShear(0)
        bolt.Tieback.setBoreholeDiameter(3213.4)
        bolt.Tieback.setPreTensioningForce(176.8)
        bolt.Tieback.setConstantPretensioningForceInInstallStage(1)
        bolt.Tieback.setFacePlates(0)
        bolt.Tieback.setAddPullOutForce(0)
        bolt.Tieback.setPullOutForce(1475.5)
        bolt.Tieback.setUseBondPercentageLength(0)
        bolt.Tieback.setPercentageBondLength(26665)
        bolt.Tieback.setBondLength(2917.7)
        bolt.Tieback.setUseSecondaryBondLength(1)
        bolt.Tieback.setSecondaryBondLengthType(SecondaryBondLengthType.P2_BOLT_TIEBACK_SECONDARY_PHYSICAL)
        bolt.Tieback.setPercentOfSecondaryBondLength(24233)
        bolt.Tieback.setSecondaryBondLength(1257.7)
        bolt.Tieback.setDelayInstallAfterBolt(18405)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertEqual(bolt.Tieback.getBoltDiameter(), 836.5)
        self.assertEqual(bolt.Tieback.getBoltModulusE(), 2628.5)
        self.assertEqual(bolt.Tieback.getBoltModel(), BoltModels.P2_BOLT_ELASTIC)
        self.assertEqual(bolt.Tieback.getTensileCapacity(), 972.5)
        self.assertEqual(bolt.Tieback.getResidualTensileCapacity(), 86.7)
        self.assertEqual(bolt.Tieback.getOutofPlaneSpacing(), 762.9)
        self.assertEqual(bolt.Tieback.getMaterialDependent(), 0)
        self.assertEqual(bolt.Tieback.getBondStrengthCoefficient(), 468.3)
        self.assertEqual(bolt.Tieback.getBondShearStiffnessCoefficient(), 2350.4)
        self.assertEqual(bolt.Tieback.getBondShearStiffness(), 2598.3)
        self.assertEqual(bolt.Tieback.getBondStrength(), 2572.7)
        self.assertEqual(bolt.Tieback.getJointShear(), 0)
        self.assertEqual(bolt.Tieback.getBoreholeDiameter(), 3213.4)
        self.assertEqual(bolt.Tieback.getPreTensioningForce(), 176.8)
        self.assertEqual(bolt.Tieback.getConstantPretensioningForceInInstallStage(), 1)
        self.assertEqual(bolt.Tieback.getFacePlates(), 0)
        self.assertEqual(bolt.Tieback.getAddPullOutForce(), 0)
        self.assertEqual(bolt.Tieback.getPullOutForce(), 1475.5)
        self.assertEqual(bolt.Tieback.getUseBondPercentageLength(), 0)
        self.assertEqual(bolt.Tieback.getPercentageBondLength(), 26665)
        self.assertEqual(bolt.Tieback.getBondLength(), 2917.7)
        self.assertEqual(bolt.Tieback.getUseSecondaryBondLength(), 1)
        self.assertEqual(bolt.Tieback.getSecondaryBondLengthType(), SecondaryBondLengthType.P2_BOLT_TIEBACK_SECONDARY_PHYSICAL)
        self.assertEqual(bolt.Tieback.getPercentOfSecondaryBondLength(), 24233)
        self.assertEqual(bolt.Tieback.getSecondaryBondLength(), 1257.7)
        self.assertEqual(bolt.Tieback.getDelayInstallAfterBolt(), 18405)
