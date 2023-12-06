import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestNonLinearIsotropic(unittest.TestCase):
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
    def testNonLinearIsotropicProperty(self):
        stiffness = self.material.Stiffness
        stiffness.NonLinearIsotropic.setUseUnloadingCondition(0)
        stiffness.NonLinearIsotropic.setUnloadingCondition(UnloadingConditions.UC_DEVIATORIC_STRESS)
        stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA2)
        stiffness.NonLinearIsotropic.setPoissonsRatio(2628.5)
        stiffness.NonLinearIsotropic.setUseResidualYoungsModulus(0)
        stiffness.NonLinearIsotropic.setResidualYoungsModulus(86.7)
        stiffness.NonLinearIsotropic.setInitialE(762.9)
        stiffness.NonLinearIsotropic.setAlpha(1413.6)
        stiffness.NonLinearIsotropic.setPref(468.3)
        stiffness.NonLinearIsotropic.setAParameter(2350.4)
        stiffness.NonLinearIsotropic.setBParameter(2598.3)
        stiffness.NonLinearIsotropic.setMParameter(2572.7)
        stiffness.NonLinearIsotropic.setGMax(2605.0)
        stiffness.NonLinearIsotropic.setGammaY(3213.4)
        stiffness.NonLinearIsotropic.setRParameter(176.8)
        stiffness.NonLinearIsotropic.setUnloadingPoissonsRatio(1508.0)
        stiffness.NonLinearIsotropic.setUseUnloadingResidualYoungsModulus(0)
        stiffness.NonLinearIsotropic.setUnloadingResidualYoungsModulus(3215.6)
        stiffness.NonLinearIsotropic.setUnloadingInitialE(1475.5)
        stiffness.NonLinearIsotropic.setUnloadingAlpha(2227.9)
        stiffness.NonLinearIsotropic.setUnloadingPref(3008.6)
        stiffness.NonLinearIsotropic.setUnloadingAParameter(2917.7)
        stiffness.NonLinearIsotropic.setUnloadingBParameter(1006.5)
        stiffness.NonLinearIsotropic.setUnloadingMParameter(1374.4)
        stiffness.NonLinearIsotropic.setUnloadingGMax(1257.7)
        stiffness.NonLinearIsotropic.setUnloadingGammaY(1702.5)
        stiffness.NonLinearIsotropic.setUnloadingRParameter(857.5)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        stiffness = self.material.Stiffness
        self.assertEqual(stiffness.NonLinearIsotropic.getUseUnloadingCondition(), 0)
        self.assertEqual(stiffness.NonLinearIsotropic.getUnloadingCondition(), UnloadingConditions.UC_DEVIATORIC_STRESS)
        self.assertEqual(stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA2)
        self.assertEqual(stiffness.NonLinearIsotropic.getPoissonsRatio(), 2628.5)
        self.assertEqual(stiffness.NonLinearIsotropic.getUseResidualYoungsModulus(), 0)
        self.assertEqual(stiffness.NonLinearIsotropic.getResidualYoungsModulus(), 86.7)
        self.assertEqual(stiffness.NonLinearIsotropic.getInitialE(), 762.9)
        self.assertEqual(stiffness.NonLinearIsotropic.getAlpha(), 1413.6)
        self.assertEqual(stiffness.NonLinearIsotropic.getPref(), 468.3)
        self.assertEqual(stiffness.NonLinearIsotropic.getAParameter(), 2350.4)
        self.assertEqual(stiffness.NonLinearIsotropic.getBParameter(), 2598.3)
        self.assertEqual(stiffness.NonLinearIsotropic.getMParameter(), 2572.7)
        self.assertEqual(stiffness.NonLinearIsotropic.getGMax(), 2605.0)
        self.assertEqual(stiffness.NonLinearIsotropic.getGammaY(), 3213.4)
        self.assertEqual(stiffness.NonLinearIsotropic.getRParameter(), 176.8)
        self.assertEqual(stiffness.NonLinearIsotropic.getUnloadingPoissonsRatio(), 1508.0)
        self.assertEqual(stiffness.NonLinearIsotropic.getUseUnloadingResidualYoungsModulus(), 0)
        self.assertEqual(stiffness.NonLinearIsotropic.getUnloadingResidualYoungsModulus(), 3215.6)
        self.assertEqual(stiffness.NonLinearIsotropic.getUnloadingInitialE(), 1475.5)
        self.assertEqual(stiffness.NonLinearIsotropic.getUnloadingAlpha(), 2227.9)
        self.assertEqual(stiffness.NonLinearIsotropic.getUnloadingPref(), 3008.6)
        self.assertEqual(stiffness.NonLinearIsotropic.getUnloadingAParameter(), 2917.7)
        self.assertEqual(stiffness.NonLinearIsotropic.getUnloadingBParameter(), 1006.5)
        self.assertEqual(stiffness.NonLinearIsotropic.getUnloadingMParameter(), 1374.4)
        self.assertEqual(stiffness.NonLinearIsotropic.getUnloadingGMax(), 1257.7)
        self.assertEqual(stiffness.NonLinearIsotropic.getUnloadingGammaY(), 1702.5)
        self.assertEqual(stiffness.NonLinearIsotropic.getUnloadingRParameter(), 857.5)
