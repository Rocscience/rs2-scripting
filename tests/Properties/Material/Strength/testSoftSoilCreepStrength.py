import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestSoftSoilCreepStrength(unittest.TestCase):
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
    def testSoftSoilCreepStrengthProperty(self):
        strength = self.material.Strength
        strength.SoftSoilCreepStrength.setFrictionAngle(836.5)
        strength.SoftSoilCreepStrength.setCohesion(2628.5)
        strength.SoftSoilCreepStrength.setTensileStrength(972.5)
        strength.SoftSoilCreepStrength.setDilationAngle(86.7)
        strength.SoftSoilCreepStrength.setLambda(762.9)
        strength.SoftSoilCreepStrength.setKappa(1413.6)
        strength.SoftSoilCreepStrength.setK0NormalConsolidation(468.3)
        strength.SoftSoilCreepStrength.setInitialConsolidationCondition(InitialConsolidation.INITIAL_MEAN_STRESS)
        strength.SoftSoilCreepStrength.setOCRStress(2350.4)
        strength.SoftSoilCreepStrength.setInitialMeanStress(2598.3)
        strength.SoftSoilCreepStrength.setMu(2572.7)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.SoftSoilCreepStrength.getFrictionAngle(), 836.5)
        self.assertEqual(strength.SoftSoilCreepStrength.getCohesion(), 2628.5)
        self.assertEqual(strength.SoftSoilCreepStrength.getTensileStrength(), 972.5)
        self.assertEqual(strength.SoftSoilCreepStrength.getDilationAngle(), 86.7)
        self.assertEqual(strength.SoftSoilCreepStrength.getLambda(), 762.9)
        self.assertEqual(strength.SoftSoilCreepStrength.getKappa(), 1413.6)
        self.assertEqual(strength.SoftSoilCreepStrength.getK0NormalConsolidation(), 468.3)
        self.assertEqual(strength.SoftSoilCreepStrength.getInitialConsolidationCondition(), InitialConsolidation.INITIAL_MEAN_STRESS)
        self.assertEqual(strength.SoftSoilCreepStrength.getOCRStress(), 2350.4)
        self.assertEqual(strength.SoftSoilCreepStrength.getInitialMeanStress(), 2598.3)
        self.assertEqual(strength.SoftSoilCreepStrength.getMu(), 2572.7)
