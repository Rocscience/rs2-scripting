import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestVerticalStressRatio(unittest.TestCase):
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
    def testVerticalStressRatioProperty(self):
        strength = self.material.Strength
        strength.VerticalStressRatio.setMaterialType(MaterialType.PLASTIC)
        strength.VerticalStressRatio.setUseMaximumShearStrength(0)
        strength.VerticalStressRatio.setUseTensileStrength(0)
        strength.VerticalStressRatio.setVerticalStressRatio(972.5)
        strength.VerticalStressRatio.setMinimumShearStrength(86.7)
        strength.VerticalStressRatio.setMaximumShearStrength(762.9)
        strength.VerticalStressRatio.setPeakTensileStrength(1413.6)
        strength.VerticalStressRatio.setResidualVerticalStressRatio(468.3)
        strength.VerticalStressRatio.setResidualMinimumShearStrength(2350.4)
        strength.VerticalStressRatio.setResidualMaximumShearStrength(2598.3)
        strength.VerticalStressRatio.setResidualTensileStrength(2572.7)
        strength.VerticalStressRatio.setApplySSRShearStrengthReduction(0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.VerticalStressRatio.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(strength.VerticalStressRatio.getUseMaximumShearStrength(), 0)
        self.assertEqual(strength.VerticalStressRatio.getUseTensileStrength(), 0)
        self.assertEqual(strength.VerticalStressRatio.getVerticalStressRatio(), 972.5)
        self.assertEqual(strength.VerticalStressRatio.getMinimumShearStrength(), 86.7)
        self.assertEqual(strength.VerticalStressRatio.getMaximumShearStrength(), 762.9)
        self.assertEqual(strength.VerticalStressRatio.getPeakTensileStrength(), 1413.6)
        self.assertEqual(strength.VerticalStressRatio.getResidualVerticalStressRatio(), 468.3)
        self.assertEqual(strength.VerticalStressRatio.getResidualMinimumShearStrength(), 2350.4)
        self.assertEqual(strength.VerticalStressRatio.getResidualMaximumShearStrength(), 2598.3)
        self.assertEqual(strength.VerticalStressRatio.getResidualTensileStrength(), 2572.7)
        self.assertEqual(strength.VerticalStressRatio.getApplySSRShearStrengthReduction(), 0)
