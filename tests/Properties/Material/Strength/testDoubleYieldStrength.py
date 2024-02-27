import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestDoubleYieldStrength(unittest.TestCase):
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
    def testDoubleYieldStrengthProperty(self):
        strength = self.material.Strength
        strength.DoubleYieldStrength.setCap(CySoilCapOption.CYS_CAP_ELLIPTICAL)
        strength.DoubleYieldStrength.setAlfaCap(836.5)
        strength.DoubleYieldStrength.setNormallyConsolidatedCapPressure(2628.5)
        strength.DoubleYieldStrength.setFrictionAngleFailure(972.5)
        strength.DoubleYieldStrength.setCohesion(86.7)
        strength.DoubleYieldStrength.setFailureRatio(762.9)
        strength.DoubleYieldStrength.setFrictionAngleNormallyConsolidated(1413.6)
        strength.DoubleYieldStrength.setBetaShearCalibrationFactor(468.3)
        strength.DoubleYieldStrength.setTensileStrength(2350.4)
        strength.DoubleYieldStrength.setDilationAngle(2598.3)
        strength.DoubleYieldStrength.setDilationOption(DilationOption.DILATION_ROWES)
        strength.DoubleYieldStrength.setConstantVolumeFrictionAngle(2572.7)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.DoubleYieldStrength.getCap(), CySoilCapOption.CYS_CAP_ELLIPTICAL)
        self.assertEqual(strength.DoubleYieldStrength.getAlfaCap(), 836.5)
        self.assertEqual(strength.DoubleYieldStrength.getNormallyConsolidatedCapPressure(), 2628.5)
        self.assertEqual(strength.DoubleYieldStrength.getFrictionAngleFailure(), 972.5)
        self.assertEqual(strength.DoubleYieldStrength.getCohesion(), 86.7)
        self.assertEqual(strength.DoubleYieldStrength.getFailureRatio(), 762.9)
        self.assertEqual(strength.DoubleYieldStrength.getFrictionAngleNormallyConsolidated(), 1413.6)
        self.assertEqual(strength.DoubleYieldStrength.getBetaShearCalibrationFactor(), 468.3)
        self.assertEqual(strength.DoubleYieldStrength.getTensileStrength(), 2350.4)
        self.assertEqual(strength.DoubleYieldStrength.getDilationAngle(), 2598.3)
        self.assertEqual(strength.DoubleYieldStrength.getDilationOption(), DilationOption.DILATION_ROWES)
        self.assertEqual(strength.DoubleYieldStrength.getConstantVolumeFrictionAngle(), 2572.7)
