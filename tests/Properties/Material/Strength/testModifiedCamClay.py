import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestModifiedCamClay(unittest.TestCase):
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
    def testModifiedCamClayProperty(self):
        strength = self.material.Strength
        strength.ModifiedCamClay.setCriticalStateSlope(836.5)
        strength.ModifiedCamClay.setSpecificVolumeAtUnitPressure(SpecificVolumeAtUnitPressure.NORMAL_COMPRESSION_LINE)
        strength.ModifiedCamClay.setNParameter(2628.5)
        strength.ModifiedCamClay.setGamma(972.5)
        strength.ModifiedCamClay.setKappa(86.7)
        strength.ModifiedCamClay.setInitialStateOfConsolidation(InitialStateOfConsolidation.OVERCONSOLIDATION_RATIO)
        strength.ModifiedCamClay.setOverconsolidationRatio(762.9)
        strength.ModifiedCamClay.setPreconsolidationStress(1413.6)
        strength.ModifiedCamClay.setLambda(468.3)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.ModifiedCamClay.getCriticalStateSlope(), 836.5)
        self.assertEqual(strength.ModifiedCamClay.getSpecificVolumeAtUnitPressure(), SpecificVolumeAtUnitPressure.NORMAL_COMPRESSION_LINE)
        self.assertEqual(strength.ModifiedCamClay.getNParameter(), 2628.5)
        self.assertEqual(strength.ModifiedCamClay.getGamma(), 972.5)
        self.assertEqual(strength.ModifiedCamClay.getKappa(), 86.7)
        self.assertEqual(strength.ModifiedCamClay.getInitialStateOfConsolidation(), InitialStateOfConsolidation.OVERCONSOLIDATION_RATIO)
        self.assertEqual(strength.ModifiedCamClay.getOverconsolidationRatio(), 762.9)
        self.assertEqual(strength.ModifiedCamClay.getPreconsolidationStress(), 1413.6)
        self.assertEqual(strength.ModifiedCamClay.getLambda(), 468.3)
    def testModifiedCamClayStageFactors(self):
        strength = self.material.Strength
        stageFactor = strength.ModifiedCamClay.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setCriticalStateSlopeFactor(2350.4)
        stageFactor.setGammaFactor(2598.3)
        stageFactor.setKappaFactor(2572.7)
        stageFactor.setLambdaFactor(2605.0)
        stageFactor.setNParameterFactor(3213.4)
        stageFactor.setOverconsolidationRatioFactor(176.8)
        stageFactor.setPreconsolidationStressFactor(1508.0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        stageFactor = strength.ModifiedCamClay.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getCriticalStateSlopeFactor(), 2350.4)
        self.assertEqual(stageFactor.getGammaFactor(), 2598.3)
        self.assertEqual(stageFactor.getKappaFactor(), 2572.7)
        self.assertEqual(stageFactor.getLambdaFactor(), 2605.0)
        self.assertEqual(stageFactor.getNParameterFactor(), 3213.4)
        self.assertEqual(stageFactor.getOverconsolidationRatioFactor(), 176.8)
        self.assertEqual(stageFactor.getPreconsolidationStressFactor(), 1508.0)
