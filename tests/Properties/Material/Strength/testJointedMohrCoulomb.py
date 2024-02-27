import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestJointedMohrCoulomb(unittest.TestCase):
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
    def testJointedMohrCoulombProperty(self):
        strength = self.material.Strength
        strength.JointedMohrCoulomb.setMaterialType(MaterialType.PLASTIC)
        strength.JointedMohrCoulomb.setPeakTensileStrength(836.5)
        strength.JointedMohrCoulomb.setPeakFrictionAngle(2628.5)
        strength.JointedMohrCoulomb.setPeakCohesion(972.5)
        strength.JointedMohrCoulomb.setResidualTensileStrength(86.7)
        strength.JointedMohrCoulomb.setResidualFrictionAngle(762.9)
        strength.JointedMohrCoulomb.setResidualCohesion(1413.6)
        strength.JointedMohrCoulomb.setDilationAngle(468.3)
        strength.JointedMohrCoulomb.setApplySSRShearStrengthReduction(0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.JointedMohrCoulomb.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(strength.JointedMohrCoulomb.getPeakTensileStrength(), 836.5)
        self.assertEqual(strength.JointedMohrCoulomb.getPeakFrictionAngle(), 2628.5)
        self.assertEqual(strength.JointedMohrCoulomb.getPeakCohesion(), 972.5)
        self.assertEqual(strength.JointedMohrCoulomb.getResidualTensileStrength(), 86.7)
        self.assertEqual(strength.JointedMohrCoulomb.getResidualFrictionAngle(), 762.9)
        self.assertEqual(strength.JointedMohrCoulomb.getResidualCohesion(), 1413.6)
        self.assertEqual(strength.JointedMohrCoulomb.getDilationAngle(), 468.3)
        self.assertEqual(strength.JointedMohrCoulomb.getApplySSRShearStrengthReduction(), 0)
