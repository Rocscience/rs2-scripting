import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestHardeningSoilStrength(unittest.TestCase):
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
    def testHardeningSoilStrengthProperty(self):
        strength = self.material.Strength
        strength.HardeningSoilStrength.setFrictionAngle(836.5)
        strength.HardeningSoilStrength.setCohesion(2628.5)
        strength.HardeningSoilStrength.setFailureRatio(972.5)
        strength.HardeningSoilStrength.setTensileStrength(86.7)
        strength.HardeningSoilStrength.setDilationAngle(762.9)
        strength.HardeningSoilStrength.setDilationOption(DilationOption.DILATION_ROWES)
        strength.HardeningSoilStrength.setDilatancyCutoff(Dilatancy.DILATANCY_ACTIVATED)
        strength.HardeningSoilStrength.setE0(1413.6)
        strength.HardeningSoilStrength.setEmax(468.3)
        strength.HardeningSoilStrength.setK0NormalConsolidation(2350.4)
        strength.HardeningSoilStrength.setInitialConsolidationCondition(InitialConsolidation.CONSOL_INITIAL_MEAN_STRESS)
        strength.HardeningSoilStrength.setOCRStress(2598.3)
        strength.HardeningSoilStrength.setInitialMeanStress(2572.7)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.HardeningSoilStrength.getFrictionAngle(), 836.5)
        self.assertEqual(strength.HardeningSoilStrength.getCohesion(), 2628.5)
        self.assertEqual(strength.HardeningSoilStrength.getFailureRatio(), 972.5)
        self.assertEqual(strength.HardeningSoilStrength.getTensileStrength(), 86.7)
        self.assertEqual(strength.HardeningSoilStrength.getDilationAngle(), 762.9)
        self.assertEqual(strength.HardeningSoilStrength.getDilationOption(), DilationOption.DILATION_ROWES)
        self.assertEqual(strength.HardeningSoilStrength.getDilatancyCutoff(), Dilatancy.DILATANCY_ACTIVATED)
        self.assertEqual(strength.HardeningSoilStrength.getE0(), 1413.6)
        self.assertEqual(strength.HardeningSoilStrength.getEmax(), 468.3)
        self.assertEqual(strength.HardeningSoilStrength.getK0NormalConsolidation(), 2350.4)
        self.assertEqual(strength.HardeningSoilStrength.getInitialConsolidationCondition(), InitialConsolidation.CONSOL_INITIAL_MEAN_STRESS)
        self.assertEqual(strength.HardeningSoilStrength.getOCRStress(), 2598.3)
        self.assertEqual(strength.HardeningSoilStrength.getInitialMeanStress(), 2572.7)
