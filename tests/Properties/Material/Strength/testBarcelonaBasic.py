import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestBarcelonaBasic(unittest.TestCase):
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
    def testBarcelonaBasicProperty(self):
        strength = self.material.Strength
        strength.BarcelonaBasic.setSlopeOfCriticalStateLines(836.5)
        strength.BarcelonaBasic.setIncludeTheEffectOfLodesAngle(0)
        strength.BarcelonaBasic.setLambda(972.5)
        strength.BarcelonaBasic.setKappa(86.7)
        strength.BarcelonaBasic.setSpecificVolumeAtUnitPressure(762.9)
        strength.BarcelonaBasic.setInitialStateOfConsolidation(InitialStateOfConsolidation.OVERCONSOLIDATION_RATIO)
        strength.BarcelonaBasic.setOverConsolidationRatio(1413.6)
        strength.BarcelonaBasic.setPreconsolidationPressure(468.3)
        strength.BarcelonaBasic.setElasticParameters(ElasticParameters.CONSTANT_POISSON_RATIO)
        strength.BarcelonaBasic.setAutoCalculateAlfaFactor(0)
        strength.BarcelonaBasic.setAlfaFactor(2598.3)
        strength.BarcelonaBasic.setMinimumBulkModulus(2572.7)
        strength.BarcelonaBasic.setKTensionSuction(2605.0)
        strength.BarcelonaBasic.setKapaSuction(3213.4)
        strength.BarcelonaBasic.setRParameter(176.8)
        strength.BarcelonaBasic.setBetaParameter(1508.0)
        strength.BarcelonaBasic.setReferenceMeanStress(857.2)
        strength.BarcelonaBasic.setAtmosphericPressure(3215.6)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.BarcelonaBasic.getSlopeOfCriticalStateLines(), 836.5)
        self.assertEqual(strength.BarcelonaBasic.getIncludeTheEffectOfLodesAngle(), 0)
        self.assertEqual(strength.BarcelonaBasic.getLambda(), 972.5)
        self.assertEqual(strength.BarcelonaBasic.getKappa(), 86.7)
        self.assertEqual(strength.BarcelonaBasic.getSpecificVolumeAtUnitPressure(), 762.9)
        self.assertEqual(strength.BarcelonaBasic.getInitialStateOfConsolidation(), InitialStateOfConsolidation.OVERCONSOLIDATION_RATIO)
        self.assertEqual(strength.BarcelonaBasic.getOverConsolidationRatio(), 1413.6)
        self.assertEqual(strength.BarcelonaBasic.getPreconsolidationPressure(), 468.3)
        self.assertEqual(strength.BarcelonaBasic.getElasticParameters(), ElasticParameters.CONSTANT_POISSON_RATIO)
        self.assertEqual(strength.BarcelonaBasic.getAutoCalculateAlfaFactor(), 0)
        self.assertEqual(strength.BarcelonaBasic.getAlfaFactor(), 2598.3)
        self.assertEqual(strength.BarcelonaBasic.getMinimumBulkModulus(), 2572.7)
        self.assertEqual(strength.BarcelonaBasic.getKTensionSuction(), 2605.0)
        self.assertEqual(strength.BarcelonaBasic.getKapaSuction(), 3213.4)
        self.assertEqual(strength.BarcelonaBasic.getRParameter(), 176.8)
        self.assertEqual(strength.BarcelonaBasic.getBetaParameter(), 1508.0)
        self.assertEqual(strength.BarcelonaBasic.getReferenceMeanStress(), 857.2)
        self.assertEqual(strength.BarcelonaBasic.getAtmosphericPressure(), 3215.6)
    def testBarcelonaBasicStageFactors(self):
        strength = self.material.Strength
        stageFactor = strength.BarcelonaBasic.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setCriticalStateSlopeFactor(1475.5)
        stageFactor.setGammaFactor(2227.9)
        stageFactor.setKappaFactor(3008.6)
        stageFactor.setLambdaFactor(2917.7)
        stageFactor.setNParameterFactor(1006.5)
        stageFactor.setOverconsolidationRatioFactor(1374.4)
        stageFactor.setPreconsolidationStressFactor(1257.7)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        stageFactor = strength.BarcelonaBasic.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getCriticalStateSlopeFactor(), 1475.5)
        self.assertEqual(stageFactor.getGammaFactor(), 2227.9)
        self.assertEqual(stageFactor.getKappaFactor(), 3008.6)
        self.assertEqual(stageFactor.getLambdaFactor(), 2917.7)
        self.assertEqual(stageFactor.getNParameterFactor(), 1006.5)
        self.assertEqual(stageFactor.getOverconsolidationRatioFactor(), 1374.4)
        self.assertEqual(stageFactor.getPreconsolidationStressFactor(), 1257.7)
