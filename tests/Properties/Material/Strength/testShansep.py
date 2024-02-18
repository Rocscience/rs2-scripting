import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestShansep(unittest.TestCase):
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
    def testShansepProperty(self):
        strength = self.material.Strength
        strength.Shansep.setMaterialType(MaterialType.PLASTIC)
        strength.Shansep.setUseMaterialDependentStress(0)
        strength.Shansep.setUseMaximumShearStrength(0)
        strength.Shansep.setUseTensileStrength(0)
        strength.Shansep.setAParameter(86.7)
        strength.Shansep.setSParameter(762.9)
        strength.Shansep.setMParameter(1413.6)
        strength.Shansep.setMaximumShearStrength(468.3)
        strength.Shansep.setPeakTensileStrength(2350.4)
        strength.Shansep.setResidualAParameter(2598.3)
        strength.Shansep.setResidualSParameter(2572.7)
        strength.Shansep.setResidualMParameter(2605.0)
        strength.Shansep.setResidualMaximumShearStrength(3213.4)
        strength.Shansep.setResidualTensileStrength(176.8)
        strength.Shansep.setApplySSRShearStrengthReduction(1)
        strength.Shansep.setStressHistoryType(StressHistoryTypes.SHT_PC)
        strength.Shansep.setOCRDefinitionMethod(StressHistoryDefinitionMethods.STRESS_HISTORY_DEPTH)
        strength.Shansep.setOCR(5.6)
        strength.Shansep.setPcDefinitionMethod(StressHistoryDefinitionMethods.STRESS_HISTORY_DEPTH)
        strength.Shansep.setPc(5.6)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.Shansep.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(strength.Shansep.getUseMaterialDependentStress(), 0)
        self.assertEqual(strength.Shansep.getUseMaximumShearStrength(), 0)
        self.assertEqual(strength.Shansep.getUseTensileStrength(), 0)
        self.assertEqual(strength.Shansep.getAParameter(), 86.7)
        self.assertEqual(strength.Shansep.getSParameter(), 762.9)
        self.assertEqual(strength.Shansep.getMParameter(), 1413.6)
        self.assertEqual(strength.Shansep.getMaximumShearStrength(), 468.3)
        self.assertEqual(strength.Shansep.getPeakTensileStrength(), 2350.4)
        self.assertEqual(strength.Shansep.getResidualAParameter(), 2598.3)
        self.assertEqual(strength.Shansep.getResidualSParameter(), 2572.7)
        self.assertEqual(strength.Shansep.getResidualMParameter(), 2605.0)
        self.assertEqual(strength.Shansep.getResidualMaximumShearStrength(), 3213.4)
        self.assertEqual(strength.Shansep.getResidualTensileStrength(), 176.8)
        self.assertEqual(strength.Shansep.getApplySSRShearStrengthReduction(), 1)
        self.assertEqual(strength.Shansep.getStressHistoryType(), StressHistoryTypes.SHT_PC)
        self.assertEqual(strength.Shansep.getOCRDefinitionMethod(), StressHistoryDefinitionMethods.STRESS_HISTORY_DEPTH)
        self.assertEqual(strength.Shansep.getOCR(), 5.6)
        self.assertEqual(strength.Shansep.getPcDefinitionMethod(), StressHistoryDefinitionMethods.STRESS_HISTORY_DEPTH)
        self.assertEqual(strength.Shansep.getPc(), 5.6)
    def testShansepStageFactors(self):
        strength = self.material.Strength
        stageFactor = strength.Shansep.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setPeakTensileStrengthFactor(857.2)
        stageFactor.setResidualTensileStrengthFactor(3215.6)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        stageFactor = strength.Shansep.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getPeakTensileStrengthFactor(), 857.2)
        self.assertEqual(stageFactor.getResidualTensileStrengthFactor(), 3215.6)
