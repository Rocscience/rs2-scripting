import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from src.rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestSwellex(unittest.TestCase):
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
    def testSwellexProperty(self):
        bolt = self.bolt
        self.bolt.setBoltType(BoltTypes.SHEAR_BOLT)
        bolt.Swellex.setTensileCapacity(1873.8)
        bolt.Swellex.setResidualTensileCapacity(179.0)
        bolt.Swellex.setTributaryArea(626.6)
        bolt.Swellex.setBoltModulusE(245.1)
        bolt.Swellex.setOutofPlaneSpacing(1426.2)
        bolt.Swellex.setMaterialDependent(1)
        bolt.Swellex.setBondStrengthCoefficient(816.0)
        bolt.Swellex.setBondShearStiffnessCoefficient(1235.6)
        bolt.Swellex.setBondShearStiffness(2577.6)
        bolt.Swellex.setBondStrength(1546.3)
        bolt.Swellex.setResidualBondStrength(133.4)
        bolt.Swellex.setBoltModel(BoltModels.P2_BOLT_ELASTIC)
        bolt.Swellex.setJointShear(0)
        bolt.Swellex.setPreTensioningForce(1143.4)
        bolt.Swellex.setConstantPretensioningForceInInstallStage(1)
        bolt.Swellex.setFacePlates(0)
        bolt.Swellex.setAddPullOutForce(0)
        bolt.Swellex.setPullOutForce(2656.9)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertEqual(bolt.Swellex.getTensileCapacity(), 1873.8)
        self.assertEqual(bolt.Swellex.getResidualTensileCapacity(), 179.0)
        self.assertEqual(bolt.Swellex.getTributaryArea(), 626.6)
        self.assertEqual(bolt.Swellex.getBoltModulusE(), 245.1)
        self.assertEqual(bolt.Swellex.getOutofPlaneSpacing(), 1426.2)
        self.assertEqual(bolt.Swellex.getMaterialDependent(), 1)
        self.assertEqual(bolt.Swellex.getBondStrengthCoefficient(), 816.0)
        self.assertEqual(bolt.Swellex.getBondShearStiffnessCoefficient(), 1235.6)
        self.assertEqual(bolt.Swellex.getBondShearStiffness(), 2577.6)
        self.assertEqual(bolt.Swellex.getBondStrength(), 1546.3)
        self.assertEqual(bolt.Swellex.getResidualBondStrength(), 133.4)
        self.assertEqual(bolt.Swellex.getBoltModel(), BoltModels.P2_BOLT_ELASTIC)
        self.assertEqual(bolt.Swellex.getJointShear(), 0)
        self.assertEqual(bolt.Swellex.getPreTensioningForce(), 1143.4)
        self.assertEqual(bolt.Swellex.getConstantPretensioningForceInInstallStage(), 1)
        self.assertEqual(bolt.Swellex.getFacePlates(), 0)
        self.assertEqual(bolt.Swellex.getAddPullOutForce(), 0)
        self.assertEqual(bolt.Swellex.getPullOutForce(), 2656.9)
