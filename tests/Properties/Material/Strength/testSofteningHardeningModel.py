import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestSofteningHardeningModel(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        self.material.Strength.setFailureCriterion(StrengthCriteriaTypes.SOFTENING_HARDENING)
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testSofteningHardeningModelProperty(self):
        strength = self.material.Strength
        strength.SofteningHardeningModel.setPeakTensileStrength(836.5)
        strength.SofteningHardeningModel.setPeakFrictionAngle(2628.5)
        strength.SofteningHardeningModel.setPeakCohesion(972.5)
        strength.SofteningHardeningModel.setConeHardeningType(ConeHardeningTypes.CONE_HARDENING_TABULAR)
        strength.SofteningHardeningModel.setHardeningProperty(86.7)
        strength.SofteningHardeningModel.setDilationAngle(762.9)
        strength.SofteningHardeningModel.setConeDilationType(DilationTypes.DILATION_ANGLE)
        strength.SofteningHardeningModel.setCapType(CapTypes.MC_CAP_TYPE_VERTICAL)
        strength.SofteningHardeningModel.setInitialMeanStress(1413.6)
        strength.SofteningHardeningModel.setLambdaKappa(468.3)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.SofteningHardeningModel.getPeakTensileStrength(), 836.5)
        self.assertEqual(strength.SofteningHardeningModel.getPeakFrictionAngle(), 2628.5)
        self.assertEqual(strength.SofteningHardeningModel.getPeakCohesion(), 972.5)
        self.assertEqual(strength.SofteningHardeningModel.getConeHardeningType(), ConeHardeningTypes.CONE_HARDENING_TABULAR)
        self.assertEqual(strength.SofteningHardeningModel.getHardeningProperty(), 86.7)
        self.assertEqual(strength.SofteningHardeningModel.getDilationAngle(), 762.9)
        self.assertEqual(strength.SofteningHardeningModel.getConeDilationType(), DilationTypes.DILATION_ANGLE)
        self.assertEqual(strength.SofteningHardeningModel.getCapType(), CapTypes.MC_CAP_TYPE_VERTICAL)
        self.assertEqual(strength.SofteningHardeningModel.getInitialMeanStress(), 1413.6)
        self.assertEqual(strength.SofteningHardeningModel.getLambdaKappa(), 468.3)
    def testSofteningHardeningModelStageFactors(self):
        strength = self.material.Strength
        stageFactor = strength.SofteningHardeningModel.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setHardeningPropertyFactor(2350.4)
        stageFactor.setInitialMeanStressFactor(2598.3)
        stageFactor.setLambdaKappaFactor(2572.7)
        stageFactor.setPeakCohesionFactor(2605.0)
        stageFactor.setPeakFrictionAngleFactor(3213.4)
        stageFactor.setPeakTensileStrengthFactor(176.8)
        stageFactor.setDilationAngleFactor(1508.0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        stageFactor = strength.SofteningHardeningModel.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getHardeningPropertyFactor(), 2350.4)
        self.assertEqual(stageFactor.getInitialMeanStressFactor(), 2598.3)
        self.assertEqual(stageFactor.getLambdaKappaFactor(), 2572.7)
        self.assertEqual(stageFactor.getPeakCohesionFactor(), 2605.0)
        self.assertEqual(stageFactor.getPeakFrictionAngleFactor(), 3213.4)
        self.assertEqual(stageFactor.getPeakTensileStrengthFactor(), 176.8)
        self.assertEqual(stageFactor.getDilationAngleFactor(), 1508.0)
