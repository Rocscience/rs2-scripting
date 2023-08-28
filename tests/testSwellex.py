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
        bolt.Swellex.setTensileCapacity(2869.2)
        bolt.Swellex.setResidualTensileCapacity(1613.9)
        bolt.Swellex.setTributaryArea(2319.5)
        bolt.Swellex.setBoltModulusE(3131.6)
        bolt.Swellex.setOutofPlaneSpacing(2094.5)
        bolt.Swellex.setMaterialDependent(0)
        bolt.Swellex.setBondStrengthCoefficient(2002.4)
        bolt.Swellex.setBondShearStiffnessCoefficient(1878.7)
        bolt.Swellex.setBondShearStiffness(2587.4)
        bolt.Swellex.setBondStrength(176.3)
        bolt.Swellex.setResidualBondStrength(262.5)
        bolt.Swellex.setBoltModel(BoltModels.P2_BOLT_ELASTIC)
        bolt.Swellex.setJointShear(0)
        bolt.Swellex.setPreTensioningForce(3097.4)
        bolt.Swellex.setConstantPretensioningForceInInstallStage(0)
        bolt.Swellex.setFacePlates(1)
        bolt.Swellex.setAddPullOutForce(1)
        bolt.Swellex.setPullOutForce(510.9)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertEqual(bolt.Swellex.getTensileCapacity(), 2869.2)
        self.assertEqual(bolt.Swellex.getResidualTensileCapacity(), 1613.9)
        self.assertEqual(bolt.Swellex.getTributaryArea(), 2319.5)
        self.assertEqual(bolt.Swellex.getBoltModulusE(), 3131.6)
        self.assertEqual(bolt.Swellex.getOutofPlaneSpacing(), 2094.5)
        self.assertEqual(bolt.Swellex.getMaterialDependent(), 0)
        self.assertEqual(bolt.Swellex.getBondStrengthCoefficient(), 2002.4)
        self.assertEqual(bolt.Swellex.getBondShearStiffnessCoefficient(), 1878.7)
        self.assertEqual(bolt.Swellex.getBondShearStiffness(), 2587.4)
        self.assertEqual(bolt.Swellex.getBondStrength(), 176.3)
        self.assertEqual(bolt.Swellex.getResidualBondStrength(), 262.5)
        self.assertEqual(bolt.Swellex.getBoltModel(), BoltModels.P2_BOLT_ELASTIC)
        self.assertEqual(bolt.Swellex.getJointShear(), 0)
        self.assertEqual(bolt.Swellex.getPreTensioningForce(), 3097.4)
        self.assertEqual(bolt.Swellex.getConstantPretensioningForceInInstallStage(), 0)
        self.assertEqual(bolt.Swellex.getFacePlates(), 1)
        self.assertEqual(bolt.Swellex.getAddPullOutForce(), 1)
        self.assertEqual(bolt.Swellex.getPullOutForce(), 510.9)
