import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestSoftSoilStrength(unittest.TestCase):
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
    def testSoftSoilStrengthProperty(self):
        strength = self.material.Strength
        strength.SoftSoilStrength.setFrictionAngle(836.5)
        strength.SoftSoilStrength.setCohesion(2628.5)
        strength.SoftSoilStrength.setTensileStrength(972.5)
        strength.SoftSoilStrength.setDilationAngle(86.7)
        strength.SoftSoilStrength.setLambda(762.9)
        strength.SoftSoilStrength.setKappa(1413.6)
        strength.SoftSoilStrength.setK0NormalConsolidation(468.3)
        strength.SoftSoilStrength.setInitialConsolidationCondition(InitialConsolidation.INITIAL_MEAN_STRESS)
        strength.SoftSoilStrength.setOCRStress(2350.4)
        strength.SoftSoilStrength.setInitialMeanStress(2598.3)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.SoftSoilStrength.getFrictionAngle(), 836.5)
        self.assertEqual(strength.SoftSoilStrength.getCohesion(), 2628.5)
        self.assertEqual(strength.SoftSoilStrength.getTensileStrength(), 972.5)
        self.assertEqual(strength.SoftSoilStrength.getDilationAngle(), 86.7)
        self.assertEqual(strength.SoftSoilStrength.getLambda(), 762.9)
        self.assertEqual(strength.SoftSoilStrength.getKappa(), 1413.6)
        self.assertEqual(strength.SoftSoilStrength.getK0NormalConsolidation(), 468.3)
        self.assertEqual(strength.SoftSoilStrength.getInitialConsolidationCondition(), InitialConsolidation.INITIAL_MEAN_STRESS)
        self.assertEqual(strength.SoftSoilStrength.getOCRStress(), 2350.4)
        self.assertEqual(strength.SoftSoilStrength.getInitialMeanStress(), 2598.3)
