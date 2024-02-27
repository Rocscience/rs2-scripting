import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestBoundingSurfacePlasticity(unittest.TestCase):
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
    def testBoundingSurfacePlasticityProperty(self):
        strength = self.material.Strength
        strength.BoundingSurfacePlasticity.setPeakTensileStrength(836.5)
        strength.BoundingSurfacePlasticity.setPeakFrictionAngle(2628.5)
        strength.BoundingSurfacePlasticity.setPeakCohesion(972.5)
        strength.BoundingSurfacePlasticity.setCriticalFrictionAngleZeroDilation(86.7)
        strength.BoundingSurfacePlasticity.setHardeningProperty(762.9)
        strength.BoundingSurfacePlasticity.setUnloadingToLoadingPlasticModulusRatio(1413.6)
        strength.BoundingSurfacePlasticity.setPowerTerm(468.3)
        strength.BoundingSurfacePlasticity.setApplySSRShearStrengthReduction(0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.BoundingSurfacePlasticity.getPeakTensileStrength(), 836.5)
        self.assertEqual(strength.BoundingSurfacePlasticity.getPeakFrictionAngle(), 2628.5)
        self.assertEqual(strength.BoundingSurfacePlasticity.getPeakCohesion(), 972.5)
        self.assertEqual(strength.BoundingSurfacePlasticity.getCriticalFrictionAngleZeroDilation(), 86.7)
        self.assertEqual(strength.BoundingSurfacePlasticity.getHardeningProperty(), 762.9)
        self.assertEqual(strength.BoundingSurfacePlasticity.getUnloadingToLoadingPlasticModulusRatio(), 1413.6)
        self.assertEqual(strength.BoundingSurfacePlasticity.getPowerTerm(), 468.3)
        self.assertEqual(strength.BoundingSurfacePlasticity.getApplySSRShearStrengthReduction(), 0)
