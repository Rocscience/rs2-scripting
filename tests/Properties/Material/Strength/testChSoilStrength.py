import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestChSoilStrength(unittest.TestCase):
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
    def testChSoilStrengthProperty(self):
        strength = self.material.Strength
        strength.ChSoilStrength.setFrictionAngleFailure(836.5)
        strength.ChSoilStrength.setCohesion(2628.5)
        strength.ChSoilStrength.setFailureRatio(972.5)
        strength.ChSoilStrength.setFrictionAngleNormallyConsolidated(86.7)
        strength.ChSoilStrength.setTensileStrength(762.9)
        strength.ChSoilStrength.setDilationAngle(1413.6)
        strength.ChSoilStrength.setDilationOption(DilationOption.DILATION_ROWES)
        strength.ChSoilStrength.setConstantVolumeFrictionAngle(468.3)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.ChSoilStrength.getFrictionAngleFailure(), 836.5)
        self.assertEqual(strength.ChSoilStrength.getCohesion(), 2628.5)
        self.assertEqual(strength.ChSoilStrength.getFailureRatio(), 972.5)
        self.assertEqual(strength.ChSoilStrength.getFrictionAngleNormallyConsolidated(), 86.7)
        self.assertEqual(strength.ChSoilStrength.getTensileStrength(), 762.9)
        self.assertEqual(strength.ChSoilStrength.getDilationAngle(), 1413.6)
        self.assertEqual(strength.ChSoilStrength.getDilationOption(), DilationOption.DILATION_ROWES)
        self.assertEqual(strength.ChSoilStrength.getConstantVolumeFrictionAngle(), 468.3)
