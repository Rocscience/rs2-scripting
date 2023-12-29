import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

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
