import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestDruckerPrager(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        self.material.Strength.setFailureCriterion(StrengthCriteriaTypes.DRUCKER_PRAGER)
    def tearDown(self):
        self.model.close()
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)
    def testDruckerPragerProperty(self):
        strength = self.material.Strength
        strength.DruckerPrager.setMaterialType(MaterialType.PLASTIC)
        strength.DruckerPrager.setPeakQParameter(836.5)
        strength.DruckerPrager.setPeakKParameter(2628.5)
        strength.DruckerPrager.setPeakTensileStrength(972.5)
        strength.DruckerPrager.setResidualQParameter(86.7)
        strength.DruckerPrager.setResidualKParameter(762.9)
        strength.DruckerPrager.setResidualTensileStrength(1413.6)
        strength.DruckerPrager.setDilationParameter(468.3)
        strength.DruckerPrager.setApplySSRShearStrengthReduction(0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.DruckerPrager.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(strength.DruckerPrager.getPeakQParameter(), 836.5)
        self.assertEqual(strength.DruckerPrager.getPeakKParameter(), 2628.5)
        self.assertEqual(strength.DruckerPrager.getPeakTensileStrength(), 972.5)
        self.assertEqual(strength.DruckerPrager.getResidualQParameter(), 86.7)
        self.assertEqual(strength.DruckerPrager.getResidualKParameter(), 762.9)
        self.assertEqual(strength.DruckerPrager.getResidualTensileStrength(), 1413.6)
        self.assertEqual(strength.DruckerPrager.getDilationParameter(), 468.3)
        self.assertEqual(strength.DruckerPrager.getApplySSRShearStrengthReduction(), 0)
    def testDruckerPragerStageFactors(self):
        strength = self.material.Strength
        stageFactor = strength.DruckerPrager.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setDilationParameterFactor(2598.3)
        stageFactor.setPeakKParameterFactor(2572.7)
        stageFactor.setResidualKParameterFactor(2605.0)
        stageFactor.setPeakTensileStrengthFactor(3213.4)
        stageFactor.setPeakQParameterFactor(176.8)
        stageFactor.setResidualQParameterFactor(1508.0)
        stageFactor.setResidualTensileStrengthFactor(857.2)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        stageFactor = strength.DruckerPrager.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getDilationParameterFactor(), 2598.3)
        self.assertEqual(stageFactor.getPeakKParameterFactor(), 2572.7)
        self.assertEqual(stageFactor.getResidualKParameterFactor(), 2605.0)
        self.assertEqual(stageFactor.getPeakTensileStrengthFactor(), 3213.4)
        self.assertEqual(stageFactor.getPeakQParameterFactor(), 176.8)
        self.assertEqual(stageFactor.getResidualQParameterFactor(), 1508.0)
        self.assertEqual(stageFactor.getResidualTensileStrengthFactor(), 857.2)
