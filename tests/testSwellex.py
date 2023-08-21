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
        bolt.Swellex.setTensileCapacity(2869)
        bolt.Swellex.setResidualTensileCapacity(1613)
        bolt.Swellex.setTributaryArea(2319)
        bolt.Swellex.setBoltModulusE(3131)
        bolt.Swellex.setOutofPlaneSpacing(2094)
        bolt.Swellex.setMaterialDependent(0)
        bolt.Swellex.setBondStrengthCoefficient(2002)
        bolt.Swellex.setBondShearStiffnessCoefficient(1878)
        bolt.Swellex.setBondShearStiffness(2587)
        bolt.Swellex.setBondStrength(176)
        bolt.Swellex.setResidualBondStrength(262)
        bolt.Swellex.setBoltModel(BoltModels.P2_BOLT_ELASTIC)
        bolt.Swellex.setJointShear(0)
        bolt.Swellex.setPreTensioningForce(3097)
        bolt.Swellex.setConstantPretensioningForceInInstallStage(0)
        bolt.Swellex.setFacePlates(1)
        bolt.Swellex.setAddPullOutForce(1)
        bolt.Swellex.setPullOutForce(510)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertEqual(bolt.Swellex.getTensileCapacity(), 2869)
        self.assertEqual(bolt.Swellex.getResidualTensileCapacity(), 1613)
        self.assertEqual(bolt.Swellex.getTributaryArea(), 2319)
        self.assertEqual(bolt.Swellex.getBoltModulusE(), 3131)
        self.assertEqual(bolt.Swellex.getOutofPlaneSpacing(), 2094)
        self.assertEqual(bolt.Swellex.getMaterialDependent(), 0)
        self.assertEqual(bolt.Swellex.getBondStrengthCoefficient(), 2002)
        self.assertEqual(bolt.Swellex.getBondShearStiffnessCoefficient(), 1878)
        self.assertEqual(bolt.Swellex.getBondShearStiffness(), 2587)
        self.assertEqual(bolt.Swellex.getBondStrength(), 176)
        self.assertEqual(bolt.Swellex.getResidualBondStrength(), 262)
        self.assertEqual(bolt.Swellex.getBoltModel(), BoltModels.P2_BOLT_ELASTIC)
        self.assertEqual(bolt.Swellex.getJointShear(), 0)
        self.assertEqual(bolt.Swellex.getPreTensioningForce(), 3097)
        self.assertEqual(bolt.Swellex.getConstantPretensioningForceInInstallStage(), 0)
        self.assertEqual(bolt.Swellex.getFacePlates(), 1)
        self.assertEqual(bolt.Swellex.getAddPullOutForce(), 1)
        self.assertEqual(bolt.Swellex.getPullOutForce(), 510)
