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
        bolt.Swellex.setTensileCapacity(524)
        bolt.Swellex.setResidualTensileCapacity(584)
        bolt.Swellex.setTributaryArea(1434)
        bolt.Swellex.setBoltModulusE(1345)
        bolt.Swellex.setOutofPlaneSpacing(2079)
        bolt.Swellex.setMaterialDependent(1)
        bolt.Swellex.setBondStrengthCoefficient(2288)
        bolt.Swellex.setBondShearStiffnessCoefficient(2032)
        bolt.Swellex.setBondShearStiffness(2014)
        bolt.Swellex.setBondStrength(1002)
        bolt.Swellex.setResidualBondStrength(1071)
        bolt.Swellex.setBoltModel(BoltModels.P2_BOLT_ELASTIC)
        bolt.Swellex.setJointShear(1)
        bolt.Swellex.setPreTensioningForce(416)
        bolt.Swellex.setConstantPretensioningForceInInstallStage(0)
        bolt.Swellex.setFacePlates(1)
        bolt.Swellex.setAddPullOutForce(1)
        bolt.Swellex.setPullOutForce(19)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertEqual(bolt.Swellex.getTensileCapacity(), 524)
        self.assertEqual(bolt.Swellex.getResidualTensileCapacity(), 584)
        self.assertEqual(bolt.Swellex.getTributaryArea(), 1434)
        self.assertEqual(bolt.Swellex.getBoltModulusE(), 1345)
        self.assertEqual(bolt.Swellex.getOutofPlaneSpacing(), 2079)
        self.assertEqual(bolt.Swellex.getMaterialDependent(), 1)
        self.assertEqual(bolt.Swellex.getBondStrengthCoefficient(), 2288)
        self.assertEqual(bolt.Swellex.getBondShearStiffnessCoefficient(), 2032)
        self.assertEqual(bolt.Swellex.getBondShearStiffness(), 2014)
        self.assertEqual(bolt.Swellex.getBondStrength(), 1002)
        self.assertEqual(bolt.Swellex.getResidualBondStrength(), 1071)
        self.assertEqual(bolt.Swellex.getBoltModel(), BoltModels.P2_BOLT_ELASTIC)
        self.assertEqual(bolt.Swellex.getJointShear(), 1)
        self.assertEqual(bolt.Swellex.getPreTensioningForce(), 416)
        self.assertEqual(bolt.Swellex.getConstantPretensioningForceInInstallStage(), 0)
        self.assertEqual(bolt.Swellex.getFacePlates(), 1)
        self.assertEqual(bolt.Swellex.getAddPullOutForce(), 1)
        self.assertEqual(bolt.Swellex.getPullOutForce(), 19)
