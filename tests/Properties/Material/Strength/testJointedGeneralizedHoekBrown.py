import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestJointedGeneralizedHoekBrown(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        self.material.Strength.setFailureCriterion(StrengthCriteriaTypes.JOINTED_GENERALIZED_HOEK_BROWN)
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testJointedGeneralizedHoekBrownProperty(self):
        strength = self.material.Strength
        strength.JointedGeneralizedHoekBrown.setMaterialType(MaterialType.PLASTIC)
        strength.JointedGeneralizedHoekBrown.setCompressiveStrength(836.5)
        strength.JointedGeneralizedHoekBrown.setMbParameter(2628.5)
        strength.JointedGeneralizedHoekBrown.setSParameter(972.5)
        strength.JointedGeneralizedHoekBrown.setAParameter(86.7)
        strength.JointedGeneralizedHoekBrown.setGSIParameter(762.9)
        strength.JointedGeneralizedHoekBrown.setMiParameter(1413.6)
        strength.JointedGeneralizedHoekBrown.setDParameter(468.3)
        strength.JointedGeneralizedHoekBrown.setTensileCutoffType(TensileCutoffOptions.HOEK_MARTIN_2004)
        strength.JointedGeneralizedHoekBrown.setTensileCutoff(2350.4)
        strength.JointedGeneralizedHoekBrown.setHoekMartinMi(2598.3)
        strength.JointedGeneralizedHoekBrown.setResidualMbParameter(2572.7)
        strength.JointedGeneralizedHoekBrown.setResidualSParameter(2605.0)
        strength.JointedGeneralizedHoekBrown.setResidualAParameter(3213.4)
        strength.JointedGeneralizedHoekBrown.setResidualGSIParameter(176.8)
        strength.JointedGeneralizedHoekBrown.setResidualMiParameter(1508.0)
        strength.JointedGeneralizedHoekBrown.setResidualDParameter(857.2)
        strength.JointedGeneralizedHoekBrown.setDilationParameter(3215.6)
        strength.JointedGeneralizedHoekBrown.setApplySSRShearStrengthReduction(1)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.JointedGeneralizedHoekBrown.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(strength.JointedGeneralizedHoekBrown.getCompressiveStrength(), 836.5)
        self.assertEqual(strength.JointedGeneralizedHoekBrown.getMbParameter(), 2628.5)
        self.assertEqual(strength.JointedGeneralizedHoekBrown.getSParameter(), 972.5)
        self.assertEqual(strength.JointedGeneralizedHoekBrown.getAParameter(), 86.7)
        self.assertEqual(strength.JointedGeneralizedHoekBrown.getGSIParameter(), 762.9)
        self.assertEqual(strength.JointedGeneralizedHoekBrown.getMiParameter(), 1413.6)
        self.assertEqual(strength.JointedGeneralizedHoekBrown.getDParameter(), 468.3)
        self.assertEqual(strength.JointedGeneralizedHoekBrown.getTensileCutoffType(), TensileCutoffOptions.HOEK_MARTIN_2004)
        self.assertEqual(strength.JointedGeneralizedHoekBrown.getTensileCutoff(), 2350.4)
        self.assertEqual(strength.JointedGeneralizedHoekBrown.getHoekMartinMi(), 2598.3)
        self.assertEqual(strength.JointedGeneralizedHoekBrown.getResidualMbParameter(), 2572.7)
        self.assertEqual(strength.JointedGeneralizedHoekBrown.getResidualSParameter(), 2605.0)
        self.assertEqual(strength.JointedGeneralizedHoekBrown.getResidualAParameter(), 3213.4)
        self.assertEqual(strength.JointedGeneralizedHoekBrown.getResidualGSIParameter(), 176.8)
        self.assertEqual(strength.JointedGeneralizedHoekBrown.getResidualMiParameter(), 1508.0)
        self.assertEqual(strength.JointedGeneralizedHoekBrown.getResidualDParameter(), 857.2)
        self.assertEqual(strength.JointedGeneralizedHoekBrown.getDilationParameter(), 3215.6)
        self.assertEqual(strength.JointedGeneralizedHoekBrown.getApplySSRShearStrengthReduction(), 1)
    def testJointedGeneralizedHoekBrownStageFactors(self):
        strength = self.material.Strength
        stageFactor = strength.JointedGeneralizedHoekBrown.stageFactorInterface.getDefinedStageFactors()[1]
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
        stageFactor = strength.JointedGeneralizedHoekBrown.stageFactorInterface.getDefinedStageFactors()[1]
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
