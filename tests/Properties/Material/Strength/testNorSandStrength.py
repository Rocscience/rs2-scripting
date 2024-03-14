import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestNorSandStrength(unittest.TestCase):
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
        os.remove(self.copiedModelPath)
    def testNorSandStrengthProperty(self):
        strength = self.material.Strength
        strength.NorSandStrength.setMTCCriticalFrictionRatio(836.5)
        strength.NorSandStrength.setLambdaSlopeOfCSLNaturalLog(2628.5)
        strength.NorSandStrength.setH0PlasticHardeningModulus(972.5)
        strength.NorSandStrength.setChiTCDilationCoefficient(86.7)
        strength.NorSandStrength.setNVolumetricCouplingCoefficient(762.9)
        strength.NorSandStrength.setHyChangeInHardeningModulus(1413.6)
        strength.NorSandStrength.setPsi0InitialStateParameter(468.3)
        strength.NorSandStrength.setGamaAltitudeOfCSLAt1KPa(2350.4)
        strength.NorSandStrength.setInitialConsolidationCondition(NorSandInitialConsolidationCondition.INITIAL_MEAN_STRESS)
        strength.NorSandStrength.setOCR(2598.3)
        strength.NorSandStrength.setInitialMeanStress(2572.7)
        strength.NorSandStrength.setCapSoftening(0)
        strength.NorSandStrength.setNorSandFluidBulkModulus(3213.4)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.NorSandStrength.getMTCCriticalFrictionRatio(), 836.5)
        self.assertEqual(strength.NorSandStrength.getLambdaSlopeOfCSLNaturalLog(), 2628.5)
        self.assertEqual(strength.NorSandStrength.getH0PlasticHardeningModulus(), 972.5)
        self.assertEqual(strength.NorSandStrength.getChiTCDilationCoefficient(), 86.7)
        self.assertEqual(strength.NorSandStrength.getNVolumetricCouplingCoefficient(), 762.9)
        self.assertEqual(strength.NorSandStrength.getHyChangeInHardeningModulus(), 1413.6)
        self.assertEqual(strength.NorSandStrength.getPsi0InitialStateParameter(), 468.3)
        self.assertEqual(strength.NorSandStrength.getGamaAltitudeOfCSLAt1KPa(), 2350.4)
        self.assertEqual(strength.NorSandStrength.getInitialConsolidationCondition(), NorSandInitialConsolidationCondition.INITIAL_MEAN_STRESS)
        self.assertEqual(strength.NorSandStrength.getOCR(), 2598.3)
        self.assertEqual(strength.NorSandStrength.getInitialMeanStress(), 2572.7)
        self.assertEqual(strength.NorSandStrength.getCapSoftening(), 0)
        self.assertEqual(strength.NorSandStrength.getNorSandFluidBulkModulus(), 3213.4)
