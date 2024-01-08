import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestHardeningSoilWithSmallStrainStiffness(unittest.TestCase):
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
    def testHardeningSoilWithSmallStrainStiffnessProperty(self):
        strength = self.material.Strength
        strength.HardeningSoilWithSmallStrainStiffness.setFrictionAngle(836.5)
        strength.HardeningSoilWithSmallStrainStiffness.setCohesion(2628.5)
        strength.HardeningSoilWithSmallStrainStiffness.setFailureRatio(972.5)
        strength.HardeningSoilWithSmallStrainStiffness.setTensileStrength(86.7)
        strength.HardeningSoilWithSmallStrainStiffness.setDilationAngle(762.9)
        strength.HardeningSoilWithSmallStrainStiffness.setDilationOption(DilationOption.DILATION_ROWES)
        strength.HardeningSoilWithSmallStrainStiffness.setDilatancyCutoff(Dilatancy.DILATANCY_ACTIVATED)
        strength.HardeningSoilWithSmallStrainStiffness.setE0(1413.6)
        strength.HardeningSoilWithSmallStrainStiffness.setEmax(468.3)
        strength.HardeningSoilWithSmallStrainStiffness.setK0NormalConsolidation(2350.4)
        strength.HardeningSoilWithSmallStrainStiffness.setInitialConsolidationCondition(InitialConsolidation.CONSOL_INITIAL_MEAN_STRESS)
        strength.HardeningSoilWithSmallStrainStiffness.setOCRStress(2598.3)
        strength.HardeningSoilWithSmallStrainStiffness.setInitialMeanStress(2572.7)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.HardeningSoilWithSmallStrainStiffness.getFrictionAngle(), 836.5)
        self.assertEqual(strength.HardeningSoilWithSmallStrainStiffness.getCohesion(), 2628.5)
        self.assertEqual(strength.HardeningSoilWithSmallStrainStiffness.getFailureRatio(), 972.5)
        self.assertEqual(strength.HardeningSoilWithSmallStrainStiffness.getTensileStrength(), 86.7)
        self.assertEqual(strength.HardeningSoilWithSmallStrainStiffness.getDilationAngle(), 762.9)
        self.assertEqual(strength.HardeningSoilWithSmallStrainStiffness.getDilationOption(), DilationOption.DILATION_ROWES)
        self.assertEqual(strength.HardeningSoilWithSmallStrainStiffness.getDilatancyCutoff(), Dilatancy.DILATANCY_ACTIVATED)
        self.assertEqual(strength.HardeningSoilWithSmallStrainStiffness.getE0(), 1413.6)
        self.assertEqual(strength.HardeningSoilWithSmallStrainStiffness.getEmax(), 468.3)
        self.assertEqual(strength.HardeningSoilWithSmallStrainStiffness.getK0NormalConsolidation(), 2350.4)
        self.assertEqual(strength.HardeningSoilWithSmallStrainStiffness.getInitialConsolidationCondition(), InitialConsolidation.CONSOL_INITIAL_MEAN_STRESS)
        self.assertEqual(strength.HardeningSoilWithSmallStrainStiffness.getOCRStress(), 2598.3)
        self.assertEqual(strength.HardeningSoilWithSmallStrainStiffness.getInitialMeanStress(), 2572.7)
