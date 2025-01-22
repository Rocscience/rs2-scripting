import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestHyperbolic(unittest.TestCase):
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
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)
    def testHyperbolicProperty(self):
        strength = self.material.Strength
        strength.Hyperbolic.setMaterialType(MaterialType.PLASTIC)
        strength.Hyperbolic.setPeakFrictionAngle(836.5)
        strength.Hyperbolic.setPeakCohesion(2628.5)
        strength.Hyperbolic.setResidualFrictionAngle(972.5)
        strength.Hyperbolic.setResidualCohesion(86.7)
        strength.Hyperbolic.setDilationRatio(762.9)
        strength.Hyperbolic.setApplySSRShearStrengthReduction(0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.Hyperbolic.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(strength.Hyperbolic.getPeakFrictionAngle(), 836.5)
        self.assertEqual(strength.Hyperbolic.getPeakCohesion(), 2628.5)
        self.assertEqual(strength.Hyperbolic.getResidualFrictionAngle(), 972.5)
        self.assertEqual(strength.Hyperbolic.getResidualCohesion(), 86.7)
        self.assertEqual(strength.Hyperbolic.getDilationRatio(), 762.9)
        self.assertEqual(strength.Hyperbolic.getApplySSRShearStrengthReduction(), 0)
