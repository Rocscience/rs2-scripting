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
        blankModelPath = f"{parentDirectory}/resources/blankProject.fez"
        self.bolt = self.model.getAllBoltProperties()[0]
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testSwellexProperty(self):
        bolt = self.bolt
        self.bolt.setBoltType(BoltTypes.SHEAR_BOLT)
        bolt.Swellex.setTensileCapacity(10.1)
        bolt.Swellex.setResidualTensileCapacity(10.1)
        bolt.Swellex.setMaterialDependent(True)
        bolt.Swellex.setTributaryArea(10.1)
        bolt.Swellex.setBoltModulusE(10.1)
        bolt.Swellex.setOutofPlaneSpacing(10.1)
        bolt.Swellex.setBondStrengthCoefficient(10.1)
        bolt.Swellex.setBondShearStiffnessCoefficient(10.1)
        bolt.Swellex.setBondShearStiffness(10.1)
        bolt.Swellex.setBondStrength(10.1)
        bolt.Swellex.setResidualBondStrength(10.1)
        bolt.Swellex.setBoltModel(BoltModels.P2_BOLT_ELASTIC)
        bolt.Swellex.setJointShear(True)
        bolt.Swellex.setPreTensioningForce(10.1)
        bolt.Swellex.setConstantPretensioningForceInInstallStage(True)
        bolt.Swellex.setFacePlates(True)
        bolt.Swellex.setAddPullOutForce(True)
        bolt.Swellex.setPullOutForce(10.1)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertEqual(bolt.Swellex.getTensileCapacity(), 10.1)
        self.assertEqual(bolt.Swellex.getResidualTensileCapacity(), 10.1)
        self.assertEqual(bolt.Swellex.getMaterialDependent(), True)
        self.assertEqual(bolt.Swellex.getTributaryArea(), 10.1)
        self.assertEqual(bolt.Swellex.getBoltModulusE(), 10.1)
        self.assertEqual(bolt.Swellex.getOutofPlaneSpacing(), 10.1)
        self.assertEqual(bolt.Swellex.getBondStrengthCoefficient(), 10.1)
        self.assertEqual(bolt.Swellex.getBondShearStiffnessCoefficient(), 10.1)
        self.assertEqual(bolt.Swellex.getBondShearStiffness(), 10.1)
        self.assertEqual(bolt.Swellex.getBondStrength(), 10.1)
        self.assertEqual(bolt.Swellex.getResidualBondStrength(), 10.1)
        self.assertEqual(bolt.Swellex.getBoltModel(), BoltModels.P2_BOLT_ELASTIC)
        self.assertEqual(bolt.Swellex.getJointShear(), True)
        self.assertEqual(bolt.Swellex.getPreTensioningForce(), 10.1)
        self.assertEqual(bolt.Swellex.getConstantPretensioningForceInInstallStage(), True)
        self.assertEqual(bolt.Swellex.getFacePlates(), True)
        self.assertEqual(bolt.Swellex.getAddPullOutForce(), True)
        self.assertEqual(bolt.Swellex.getPullOutForce(), 10.1)
