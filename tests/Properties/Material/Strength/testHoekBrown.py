import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestHoekBrown(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        self.material.Strength.setFailureCriterion(StrengthCriteriaTypes.HOEK_BROWN)
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testHoekBrownProperty(self):
        strength = self.material.Strength
        strength.HoekBrown.setMaterialType(MaterialType.PLASTIC)
        strength.HoekBrown.setCompressiveStrength(836.5)
        strength.HoekBrown.setMbParameter(2628.5)
        strength.HoekBrown.setSParameter(972.5)
        strength.HoekBrown.setResidualMbParameter(86.7)
        strength.HoekBrown.setResidualSParameter(762.9)
        strength.HoekBrown.setDilationParameter(1413.6)
        strength.HoekBrown.setApplySSRShearStrengthReduction(0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.HoekBrown.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(strength.HoekBrown.getCompressiveStrength(), 836.5)
        self.assertEqual(strength.HoekBrown.getMbParameter(), 2628.5)
        self.assertEqual(strength.HoekBrown.getSParameter(), 972.5)
        self.assertEqual(strength.HoekBrown.getResidualMbParameter(), 86.7)
        self.assertEqual(strength.HoekBrown.getResidualSParameter(), 762.9)
        self.assertEqual(strength.HoekBrown.getDilationParameter(), 1413.6)
        self.assertEqual(strength.HoekBrown.getApplySSRShearStrengthReduction(), 0)