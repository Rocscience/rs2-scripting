import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestCySoilStrength(unittest.TestCase):
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
    def testCySoilStrengthProperty(self):
        strength = self.material.Strength
        strength.CySoilStrength.setCap(CySoilCapOption.ELLIPTICAL)
        strength.CySoilStrength.setAlfaCap(836.5)
        strength.CySoilStrength.setNormallyConsolidatedCapPressure(2628.5)
        strength.CySoilStrength.setFrictionAngleFailure(972.5)
        strength.CySoilStrength.setCohesion(86.7)
        strength.CySoilStrength.setFailureRatio(762.9)
        strength.CySoilStrength.setFrictionAngleNormallyConsolidated(1413.6)
        strength.CySoilStrength.setBetaShearCalibrationFactor(468.3)
        strength.CySoilStrength.setTensileStrength(2350.4)
        strength.CySoilStrength.setDilationAngle(2598.3)
        strength.CySoilStrength.setDilationOption(DilationOption.DILATION_ROWES)
        strength.CySoilStrength.setConstantVolumeFrictionAngle(2572.7)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.CySoilStrength.getCap(), CySoilCapOption.ELLIPTICAL)
        self.assertEqual(strength.CySoilStrength.getAlfaCap(), 836.5)
        self.assertEqual(strength.CySoilStrength.getNormallyConsolidatedCapPressure(), 2628.5)
        self.assertEqual(strength.CySoilStrength.getFrictionAngleFailure(), 972.5)
        self.assertEqual(strength.CySoilStrength.getCohesion(), 86.7)
        self.assertEqual(strength.CySoilStrength.getFailureRatio(), 762.9)
        self.assertEqual(strength.CySoilStrength.getFrictionAngleNormallyConsolidated(), 1413.6)
        self.assertEqual(strength.CySoilStrength.getBetaShearCalibrationFactor(), 468.3)
        self.assertEqual(strength.CySoilStrength.getTensileStrength(), 2350.4)
        self.assertEqual(strength.CySoilStrength.getDilationAngle(), 2598.3)
        self.assertEqual(strength.CySoilStrength.getDilationOption(), DilationOption.DILATION_ROWES)
        self.assertEqual(strength.CySoilStrength.getConstantVolumeFrictionAngle(), 2572.7)
