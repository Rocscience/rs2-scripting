import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestSwellex(unittest.TestCase):
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
    def testSwellexProperty(self):
        bolt = self.bolt
        self.bolt.setBoltType(BoltTypes.SHEAR_BOLT)
        bolt.Swellex.setTensileCapacity(836.5)
        bolt.Swellex.setResidualTensileCapacity(2628.5)
        bolt.Swellex.setTributaryArea(972.5)
        bolt.Swellex.setBoltModulusE(86.7)
        bolt.Swellex.setOutofPlaneSpacing(762.9)
        bolt.Swellex.setMaterialDependent(0)
        bolt.Swellex.setBondStrengthCoefficient(468.3)
        bolt.Swellex.setBondShearStiffnessCoefficient(2350.4)
        bolt.Swellex.setBondShearStiffness(2598.3)
        bolt.Swellex.setBondStrength(2572.7)
        bolt.Swellex.setResidualBondStrength(2605.0)
        bolt.Swellex.setBoltModel(BoltModels.P2_BOLT_ELASTIC)
        bolt.Swellex.setJointShear(1)
        bolt.Swellex.setPreTensioningForce(176.8)
        bolt.Swellex.setConstantPretensioningForceInInstallStage(1)
        bolt.Swellex.setFacePlates(0)
        bolt.Swellex.setAddPullOutForce(0)
        bolt.Swellex.setPullOutForce(1475.5)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertEqual(bolt.Swellex.getTensileCapacity(), 836.5)
        self.assertEqual(bolt.Swellex.getResidualTensileCapacity(), 2628.5)
        self.assertEqual(bolt.Swellex.getTributaryArea(), 972.5)
        self.assertEqual(bolt.Swellex.getBoltModulusE(), 86.7)
        self.assertEqual(bolt.Swellex.getOutofPlaneSpacing(), 762.9)
        self.assertEqual(bolt.Swellex.getMaterialDependent(), 0)
        self.assertEqual(bolt.Swellex.getBondStrengthCoefficient(), 468.3)
        self.assertEqual(bolt.Swellex.getBondShearStiffnessCoefficient(), 2350.4)
        self.assertEqual(bolt.Swellex.getBondShearStiffness(), 2598.3)
        self.assertEqual(bolt.Swellex.getBondStrength(), 2572.7)
        self.assertEqual(bolt.Swellex.getResidualBondStrength(), 2605.0)
        self.assertEqual(bolt.Swellex.getBoltModel(), BoltModels.P2_BOLT_ELASTIC)
        self.assertEqual(bolt.Swellex.getJointShear(), 1)
        self.assertEqual(bolt.Swellex.getPreTensioningForce(), 176.8)
        self.assertEqual(bolt.Swellex.getConstantPretensioningForceInInstallStage(), 1)
        self.assertEqual(bolt.Swellex.getFacePlates(), 0)
        self.assertEqual(bolt.Swellex.getAddPullOutForce(), 0)
        self.assertEqual(bolt.Swellex.getPullOutForce(), 1475.5)
