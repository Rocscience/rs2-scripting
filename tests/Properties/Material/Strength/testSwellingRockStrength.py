import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestSwellingRockStrength(unittest.TestCase):
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
    def testSwellingRockStrengthProperty(self):
        strength = self.material.Strength
        strength.SwellingRockStrength.setFrictionAngle(836.5)
        strength.SwellingRockStrength.setCohesion(2628.5)
        strength.SwellingRockStrength.setTensileStrength(972.5)
        strength.SwellingRockStrength.setDilationAngle(86.7)
        strength.SwellingRockStrength.setA0(762.9)
        strength.SwellingRockStrength.setAElastic(1413.6)
        strength.SwellingRockStrength.setAPlastic(468.3)
        strength.SwellingRockStrength.setMaximumPlasticVolumetricStrainForAPlastic(2350.4)
        strength.SwellingRockStrength.setKSwellNormal(2598.3)
        strength.SwellingRockStrength.setKSwellTangential(2572.7)
        strength.SwellingRockStrength.setMaximumSwellingStressNormal(2605.0)
        strength.SwellingRockStrength.setMaximumSwellingStressTangential(3213.4)
        strength.SwellingRockStrength.setMinimumSwellingStress(176.8)
        strength.SwellingRockStrength.setSwellingFormulation(SwellingForm.ANAGNOSTOU)
        strength.SwellingRockStrength.setWaterCondition(WaterCondition.SWELLING_WITH_WATER)
        strength.SwellingRockStrength.setSigmaCoupling(1508.0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.SwellingRockStrength.getFrictionAngle(), 836.5)
        self.assertEqual(strength.SwellingRockStrength.getCohesion(), 2628.5)
        self.assertEqual(strength.SwellingRockStrength.getTensileStrength(), 972.5)
        self.assertEqual(strength.SwellingRockStrength.getDilationAngle(), 86.7)
        self.assertEqual(strength.SwellingRockStrength.getA0(), 762.9)
        self.assertEqual(strength.SwellingRockStrength.getAElastic(), 1413.6)
        self.assertEqual(strength.SwellingRockStrength.getAPlastic(), 468.3)
        self.assertEqual(strength.SwellingRockStrength.getMaximumPlasticVolumetricStrainForAPlastic(), 2350.4)
        self.assertEqual(strength.SwellingRockStrength.getKSwellNormal(), 2598.3)
        self.assertEqual(strength.SwellingRockStrength.getKSwellTangential(), 2572.7)
        self.assertEqual(strength.SwellingRockStrength.getMaximumSwellingStressNormal(), 2605.0)
        self.assertEqual(strength.SwellingRockStrength.getMaximumSwellingStressTangential(), 3213.4)
        self.assertEqual(strength.SwellingRockStrength.getMinimumSwellingStress(), 176.8)
        self.assertEqual(strength.SwellingRockStrength.getSwellingFormulation(), SwellingForm.ANAGNOSTOU)
        self.assertEqual(strength.SwellingRockStrength.getWaterCondition(), WaterCondition.SWELLING_WITH_WATER)
        self.assertEqual(strength.SwellingRockStrength.getSigmaCoupling(), 1508.0)
