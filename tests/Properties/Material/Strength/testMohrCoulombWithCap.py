import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestMohrCoulombWithCap(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        self.material.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB_CAP)
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testMohrCoulombWithCapProperty(self):
        strength = self.material.Strength
        strength.MohrCoulombWithCap.setPeakTensileStrength(836.5)
        strength.MohrCoulombWithCap.setPeakFrictionAngle(2628.5)
        strength.MohrCoulombWithCap.setPeakCohesion(972.5)
        strength.MohrCoulombWithCap.setDilationAngle(86.7)
        strength.MohrCoulombWithCap.setCapType(MCCapType.MC_CAP_ELLIPTICAL)
        strength.MohrCoulombWithCap.setCapHardeningType(CapHardeningTypes.MC_CAP_HARDENING_TABULAR)
        strength.MohrCoulombWithCap.setInitialMeanStress(762.9)
        strength.MohrCoulombWithCap.setLambdaKappa(1413.6)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.MohrCoulombWithCap.getPeakTensileStrength(), 836.5)
        self.assertEqual(strength.MohrCoulombWithCap.getPeakFrictionAngle(), 2628.5)
        self.assertEqual(strength.MohrCoulombWithCap.getPeakCohesion(), 972.5)
        self.assertEqual(strength.MohrCoulombWithCap.getDilationAngle(), 86.7)
        self.assertEqual(strength.MohrCoulombWithCap.getCapType(), MCCapType.MC_CAP_ELLIPTICAL)
        self.assertEqual(strength.MohrCoulombWithCap.getCapHardeningType(), CapHardeningTypes.MC_CAP_HARDENING_TABULAR)
        self.assertEqual(strength.MohrCoulombWithCap.getInitialMeanStress(), 762.9)
        self.assertEqual(strength.MohrCoulombWithCap.getLambdaKappa(), 1413.6)
