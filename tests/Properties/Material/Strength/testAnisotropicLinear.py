import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestAnisotropicLinear(unittest.TestCase):
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
    def testAnisotropicLinearProperty(self):
        strength = self.material.Strength
        strength.AnisotropicLinear.setMaterialType(MaterialType.PLASTIC)
        strength.AnisotropicLinear.setA1Parameter(836.5)
        strength.AnisotropicLinear.setB1Parameter(2628.5)
        strength.AnisotropicLinear.setUseTensileStrength(0)
        strength.AnisotropicLinear.setCohesion1(86.7)
        strength.AnisotropicLinear.setCohesion2(762.9)
        strength.AnisotropicLinear.setFrictionAngle1(1413.6)
        strength.AnisotropicLinear.setFrictionAngle2(468.3)
        strength.AnisotropicLinear.setPeakTensileStrength(2350.4)
        strength.AnisotropicLinear.setResidualCohesion1(2598.3)
        strength.AnisotropicLinear.setResidualCohesion2(2572.7)
        strength.AnisotropicLinear.setResidualFrictionAngle1(2605.0)
        strength.AnisotropicLinear.setResidualFrictionAngle2(3213.4)
        strength.AnisotropicLinear.setDilationAngle1(176.8)
        strength.AnisotropicLinear.setDilationAngle2(1508.0)
        strength.AnisotropicLinear.setResidualTensileStrength(857.2)
        strength.AnisotropicLinear.setApplySSRShearStrengthReduction(0)
        strength.AnisotropicLinear.setAnisotropyDefinition(AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)
        strength.AnisotropicLinear.setAngleCcwTo1(1475.5)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.AnisotropicLinear.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(strength.AnisotropicLinear.getA1Parameter(), 836.5)
        self.assertEqual(strength.AnisotropicLinear.getB1Parameter(), 2628.5)
        self.assertEqual(strength.AnisotropicLinear.getUseTensileStrength(), 0)
        self.assertEqual(strength.AnisotropicLinear.getCohesion1(), 86.7)
        self.assertEqual(strength.AnisotropicLinear.getCohesion2(), 762.9)
        self.assertEqual(strength.AnisotropicLinear.getFrictionAngle1(), 1413.6)
        self.assertEqual(strength.AnisotropicLinear.getFrictionAngle2(), 468.3)
        self.assertEqual(strength.AnisotropicLinear.getPeakTensileStrength(), 2350.4)
        self.assertEqual(strength.AnisotropicLinear.getResidualCohesion1(), 2598.3)
        self.assertEqual(strength.AnisotropicLinear.getResidualCohesion2(), 2572.7)
        self.assertEqual(strength.AnisotropicLinear.getResidualFrictionAngle1(), 2605.0)
        self.assertEqual(strength.AnisotropicLinear.getResidualFrictionAngle2(), 3213.4)
        self.assertEqual(strength.AnisotropicLinear.getDilationAngle1(), 176.8)
        self.assertEqual(strength.AnisotropicLinear.getDilationAngle2(), 1508.0)
        self.assertEqual(strength.AnisotropicLinear.getResidualTensileStrength(), 857.2)
        self.assertEqual(strength.AnisotropicLinear.getApplySSRShearStrengthReduction(), 0)
        self.assertEqual(strength.AnisotropicLinear.getAnisotropyDefinition(), AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)
        self.assertEqual(strength.AnisotropicLinear.getAngleCcwTo1(), 1475.5)
