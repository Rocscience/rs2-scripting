import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestGeneralizedHoekBrown(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        self.material.Strength.setFailureCriterion(StrengthCriteriaTypes.GENERALIZED_HOEK_BROWN)
    def tearDown(self):
        self.model.close()
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)
    def testGeneralizedHoekBrownProperty(self):
        strength = self.material.Strength
        strength.GeneralizedHoekBrown.setMaterialType(MaterialType.PLASTIC)
        strength.GeneralizedHoekBrown.setCompressiveStrength(836.5)
        strength.GeneralizedHoekBrown.setMbParameter(2628.5)
        strength.GeneralizedHoekBrown.setSParameter(972.5)
        strength.GeneralizedHoekBrown.setAParameter(86.7)
        strength.GeneralizedHoekBrown.setGSIParameter(762.9)
        strength.GeneralizedHoekBrown.setMiParameter(1413.6)
        strength.GeneralizedHoekBrown.setDParameter(468.3)
        strength.GeneralizedHoekBrown.setResidualMbParameter(2350.4)
        strength.GeneralizedHoekBrown.setResidualSParameter(2598.3)
        strength.GeneralizedHoekBrown.setResidualAParameter(2572.7)
        strength.GeneralizedHoekBrown.setResidualGSIParameter(2605.0)
        strength.GeneralizedHoekBrown.setResidualMiParameter(3213.4)
        strength.GeneralizedHoekBrown.setResidualDParameter(176.8)
        strength.GeneralizedHoekBrown.setDilationParameter(1508.0)
        strength.GeneralizedHoekBrown.setApplySSRShearStrengthReduction(0)
        strength.GeneralizedHoekBrown.setTensileCutoffType(TensileCutoffOptions.HOEK_MARTIN_2004)
        strength.GeneralizedHoekBrown.setTensileCutoff(3215.6)
        strength.GeneralizedHoekBrown.setHoekMartinMi(1475.5)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.GeneralizedHoekBrown.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(strength.GeneralizedHoekBrown.getCompressiveStrength(), 836.5)
        self.assertEqual(strength.GeneralizedHoekBrown.getMbParameter(), 2628.5)
        self.assertEqual(strength.GeneralizedHoekBrown.getSParameter(), 972.5)
        self.assertEqual(strength.GeneralizedHoekBrown.getAParameter(), 86.7)
        self.assertEqual(strength.GeneralizedHoekBrown.getGSIParameter(), 762.9)
        self.assertEqual(strength.GeneralizedHoekBrown.getMiParameter(), 1413.6)
        self.assertEqual(strength.GeneralizedHoekBrown.getDParameter(), 468.3)
        self.assertEqual(strength.GeneralizedHoekBrown.getResidualMbParameter(), 2350.4)
        self.assertEqual(strength.GeneralizedHoekBrown.getResidualSParameter(), 2598.3)
        self.assertEqual(strength.GeneralizedHoekBrown.getResidualAParameter(), 2572.7)
        self.assertEqual(strength.GeneralizedHoekBrown.getResidualGSIParameter(), 2605.0)
        self.assertEqual(strength.GeneralizedHoekBrown.getResidualMiParameter(), 3213.4)
        self.assertEqual(strength.GeneralizedHoekBrown.getResidualDParameter(), 176.8)
        self.assertEqual(strength.GeneralizedHoekBrown.getDilationParameter(), 1508.0)
        self.assertEqual(strength.GeneralizedHoekBrown.getApplySSRShearStrengthReduction(), 0)
        self.assertEqual(strength.GeneralizedHoekBrown.getTensileCutoffType(), TensileCutoffOptions.HOEK_MARTIN_2004)
        self.assertEqual(strength.GeneralizedHoekBrown.getTensileCutoff(), 3215.6)
        self.assertEqual(strength.GeneralizedHoekBrown.getHoekMartinMi(), 1475.5)
    def testGeneralizedHoekBrownStageFactors(self):
        strength = self.material.Strength
        stageFactor = strength.GeneralizedHoekBrown.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setAParameterFactor(2227.9)
        stageFactor.setResidualAParameterFactor(3008.6)
        stageFactor.setCompressiveStrengthFactor(2917.7)
        stageFactor.setDilationParameterFactor(1006.5)
        stageFactor.setMbParameterFactor(1374.4)
        stageFactor.setResidualMbParameterFactor(1257.7)
        stageFactor.setHoekMartinMiFactor(1702.5)
        stageFactor.setSParameterFactor(857.5)
        stageFactor.setResidualSParameterFactor(2489.6)
        stageFactor.setTensileCutoffFactor(1772.3)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        stageFactor = strength.GeneralizedHoekBrown.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getAParameterFactor(), 2227.9)
        self.assertEqual(stageFactor.getResidualAParameterFactor(), 3008.6)
        self.assertEqual(stageFactor.getCompressiveStrengthFactor(), 2917.7)
        self.assertEqual(stageFactor.getDilationParameterFactor(), 1006.5)
        self.assertEqual(stageFactor.getMbParameterFactor(), 1374.4)
        self.assertEqual(stageFactor.getResidualMbParameterFactor(), 1257.7)
        self.assertEqual(stageFactor.getHoekMartinMiFactor(), 1702.5)
        self.assertEqual(stageFactor.getSParameterFactor(), 857.5)
        self.assertEqual(stageFactor.getResidualSParameterFactor(), 2489.6)
        self.assertEqual(stageFactor.getTensileCutoffFactor(), 1772.3)
