import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestBartonBandisStrength(unittest.TestCase):
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
    def testBartonBandisStrengthProperty(self):
        strength = self.material.Strength
        strength.BartonBandisStrength.setMaterialType(MaterialType.PLASTIC)
        strength.BartonBandisStrength.setPhiR(836.5)
        strength.BartonBandisStrength.setJRC(2628.5)
        strength.BartonBandisStrength.setJCS(972.5)
        strength.BartonBandisStrength.setDilationRatio(86.7)
        strength.BartonBandisStrength.setResidualStrength(1)
        strength.BartonBandisStrength.setApplySSRShearStrengthReduction(0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.BartonBandisStrength.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(strength.BartonBandisStrength.getPhiR(), 836.5)
        self.assertEqual(strength.BartonBandisStrength.getJRC(), 2628.5)
        self.assertEqual(strength.BartonBandisStrength.getJCS(), 972.5)
        self.assertEqual(strength.BartonBandisStrength.getDilationRatio(), 86.7)
        self.assertEqual(strength.BartonBandisStrength.getResidualStrength(), 1)
        self.assertEqual(strength.BartonBandisStrength.getApplySSRShearStrengthReduction(), 0)
