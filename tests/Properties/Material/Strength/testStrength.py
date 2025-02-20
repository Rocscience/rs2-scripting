import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestStrength(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProjectTransientGroundwater.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
    def tearDown(self):
        self.model.close()
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)
    def testStrengthProperty(self):
        material = self.material
        material.Strength.setFailureCriterion(StrengthCriteriaTypes.FINN)
        material.Strength.setUnsaturatedBehavior(UnsaturatedParameterType.UNSATURATED_SHEAR_STRENGTH)
        material.Strength.setUnsaturatedShearStrengthType(UnsaturatedShearStrengthType.VANAPALLI)
        material.Strength.setUnsaturatedShearStrengthAngle(836.5)
        material.Strength.setAirEntryValue(2628.5)
        material.Strength.setSingleEffectiveStressMethod(UnsaturatedSingleEffectiveStressMethod.TABULAR_VALUE)
        material.Strength.setAlpha(972.5)
        material.Strength.setAirEntrySuction(86.7)
        material.Strength.setCriticalSuction(762.9)
        material.Strength.setMaterialParameter(1413.6)
        material.Strength.setUseCutoff(0)
        material.Strength.setCutoffValue(2350.4)
        material.Strength.setTabularValues(UnsaturatedTabularValueMethod.WITH_RESPECT_TO_DEGREE_OF_SATURATION)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        material = self.material
        self.assertEqual(material.Strength.getFailureCriterion(), StrengthCriteriaTypes.FINN)
        self.assertEqual(material.Strength.getUnsaturatedBehavior(), UnsaturatedParameterType.UNSATURATED_SHEAR_STRENGTH)
        self.assertEqual(material.Strength.getUnsaturatedShearStrengthType(), UnsaturatedShearStrengthType.VANAPALLI)
        self.assertEqual(material.Strength.getUnsaturatedShearStrengthAngle(), 836.5)
        self.assertEqual(material.Strength.getAirEntryValue(), 2628.5)
        self.assertEqual(material.Strength.getSingleEffectiveStressMethod(), UnsaturatedSingleEffectiveStressMethod.TABULAR_VALUE)
        self.assertEqual(material.Strength.getAlpha(), 972.5)
        self.assertEqual(material.Strength.getAirEntrySuction(), 86.7)
        self.assertEqual(material.Strength.getCriticalSuction(), 762.9)
        self.assertEqual(material.Strength.getMaterialParameter(), 1413.6)
        self.assertEqual(material.Strength.getUseCutoff(), 0)
        self.assertEqual(material.Strength.getCutoffValue(), 2350.4)
        self.assertEqual(material.Strength.getTabularValues(), UnsaturatedTabularValueMethod.WITH_RESPECT_TO_DEGREE_OF_SATURATION)
    def testStrengthStageFactors(self):
        material = self.material
        stageFactor = material.Strength.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setAirEntryValueFactor(2598.3)
        stageFactor.setUnsaturatedShearStrengthAngleFactor(2572.7)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        material = self.material
        stageFactor = material.Strength.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getAirEntryValueFactor(), 2598.3)
        self.assertEqual(stageFactor.getUnsaturatedShearStrengthAngleFactor(), 2572.7)
