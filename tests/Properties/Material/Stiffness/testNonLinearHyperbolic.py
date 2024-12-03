import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestNonLinearHyperbolic(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
    def tearDown(self):
        self.model.close()
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)
    def testNonLinearHyperbolicProperty(self):
        stiffness = self.material.Stiffness
        stiffness.NonLinearHyperbolic.setModulusNumber(836.5)
        stiffness.NonLinearHyperbolic.setPoissonRatioType(PoissonRatioType.STRESS_DEPENDENT)
        stiffness.NonLinearHyperbolic.setBulkModulusNumber(2628.5)
        stiffness.NonLinearHyperbolic.setBulkModulusExpM(972.5)
        stiffness.NonLinearHyperbolic.setPoissonsRatio(86.7)
        stiffness.NonLinearHyperbolic.setModulusExpN(762.9)
        stiffness.NonLinearHyperbolic.setAtmosphericPressure(1413.6)
        stiffness.NonLinearHyperbolic.setFailureRatioRf(468.3)
        stiffness.NonLinearHyperbolic.setUnloadingModulusNumber(2350.4)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        stiffness = self.material.Stiffness
        self.assertEqual(stiffness.NonLinearHyperbolic.getModulusNumber(), 836.5)
        self.assertEqual(stiffness.NonLinearHyperbolic.getPoissonRatioType(), PoissonRatioType.STRESS_DEPENDENT)
        self.assertEqual(stiffness.NonLinearHyperbolic.getBulkModulusNumber(), 2628.5)
        self.assertEqual(stiffness.NonLinearHyperbolic.getBulkModulusExpM(), 972.5)
        self.assertEqual(stiffness.NonLinearHyperbolic.getPoissonsRatio(), 86.7)
        self.assertEqual(stiffness.NonLinearHyperbolic.getModulusExpN(), 762.9)
        self.assertEqual(stiffness.NonLinearHyperbolic.getAtmosphericPressure(), 1413.6)
        self.assertEqual(stiffness.NonLinearHyperbolic.getFailureRatioRf(), 468.3)
        self.assertEqual(stiffness.NonLinearHyperbolic.getUnloadingModulusNumber(), 2350.4)
    def testNonLinearHyperbolicStageFactors(self):
        stiffness = self.material.Stiffness
        stageFactor = stiffness.NonLinearHyperbolic.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setAtmosphericPressureFactor(2598.3)
        stageFactor.setBulkModulusExpMFactor(2572.7)
        stageFactor.setBulkModulusNumberFactor(2605.0)
        stageFactor.setFailureRatioRfFactor(3213.4)
        stageFactor.setModulusExpNFactor(176.8)
        stageFactor.setModulusNumberFactor(1508.0)
        stageFactor.setPoissonsRatioFactor(857.2)
        stageFactor.setUnloadingModulusNumberFactor(3215.6)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        stiffness = self.material.Stiffness
        stageFactor = stiffness.NonLinearHyperbolic.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getAtmosphericPressureFactor(), 2598.3)
        self.assertEqual(stageFactor.getBulkModulusExpMFactor(), 2572.7)
        self.assertEqual(stageFactor.getBulkModulusNumberFactor(), 2605.0)
        self.assertEqual(stageFactor.getFailureRatioRfFactor(), 3213.4)
        self.assertEqual(stageFactor.getModulusExpNFactor(), 176.8)
        self.assertEqual(stageFactor.getModulusNumberFactor(), 1508.0)
        self.assertEqual(stageFactor.getPoissonsRatioFactor(), 857.2)
        self.assertEqual(stageFactor.getUnloadingModulusNumberFactor(), 3215.6)
