import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestUnsaturatedZoneTable(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProjectTransientGroundwaterAndThermal.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        self.material.Strength.setUnsaturatedBehavior(UnsaturatedParameterType.SINGLE_EFFECTIVE_STRESS)
        self.material.Strength.setSingleEffectiveStressMethod(UnsaturatedSingleEffectiveStressMethod.TABULAR_VALUE)

    @classmethod
    def tearDownClass(self):
        self.model.close()
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)

    def testUnsaturatedZoneTableSuccess(self):
        newTableColA1 = [-1.16,0,1,2]
        newTableColA2 = [-1.15,0.2,1.3,2.4]

        newTableColB1 = [-1.14,0,1,2]
        newTableColB2 = [-1.13,0.2,1.3,2.4]

        newTableColC1 = [-1.12,0,1,2]
        newTableColC2 = [-1.11,0.2,1.3,2.4]

        self.material.Strength.setUnsaturatedZoneTableWithRespectToSuction(newTableColA1, newTableColA2)
        self.material.Strength.setUnsaturatedZoneTableWithRespectToDegreeOfSaturation(newTableColB1, newTableColB2)
        self.material.Strength.setUnsaturatedZoneTableWithRespectToEffectiveDegreeOfSaturation(newTableColC1, newTableColC2)

        result1 = self.material.Strength.getUnsaturatedZoneTableWithRespectToSuction()
        self.assertEqual(result1[0], newTableColA1)
        self.assertEqual(result1[1], newTableColA2)

        result2 = self.material.Strength.getUnsaturatedZoneTableWithRespectToDegreeOfSaturation()
        self.assertEqual(result2[0], newTableColB1)
        self.assertEqual(result2[1], newTableColB2)

        result3 = self.material.Strength.getUnsaturatedZoneTableWithRespectToEffectiveDegreeOfSaturation()
        self.assertEqual(result3[0], newTableColC1)
        self.assertEqual(result3[1], newTableColC2)
    
    def testUnsaturatedZoneTableFailureDifferentSize(self):
        validCol1 = [-1.16,0,1,2]
        validCol2 = [-1.15,0.2,1.3,2.4]
        self.material.Strength.setUnsaturatedZoneTableWithRespectToSuction(validCol1, validCol2)
        self.material.Strength.setUnsaturatedZoneTableWithRespectToDegreeOfSaturation(validCol1, validCol2)
        self.material.Strength.setUnsaturatedZoneTableWithRespectToEffectiveDegreeOfSaturation(validCol1, validCol2)

        invalidCol1 = [-1.14,0,1]
        invalidCol2 = [-1.13,0.2,1.3,2.4]

        with self.assertRaises(Exception):
            self.material.Strength.setUnsaturatedZoneTableWithRespectToSuction(invalidCol1, invalidCol2)
        with self.assertRaises(Exception):
            self.material.Strength.setUnsaturatedZoneTableWithRespectToDegreeOfSaturation(invalidCol1, invalidCol2)
        with self.assertRaises(Exception):
            self.material.Strength.setUnsaturatedZoneTableWithRespectToEffectiveDegreeOfSaturation(invalidCol1, invalidCol2)

        result1 = self.material.Strength.getUnsaturatedZoneTableWithRespectToSuction()
        result2 = self.material.Strength.getUnsaturatedZoneTableWithRespectToDegreeOfSaturation()
        result3 = self.material.Strength.getUnsaturatedZoneTableWithRespectToEffectiveDegreeOfSaturation()
        self.assertEqual(result1[0], validCol1)
        self.assertEqual(result1[1], validCol2)
        self.assertEqual(result2[0], validCol1)
        self.assertEqual(result2[1], validCol2)
        self.assertEqual(result3[0], validCol1)
        self.assertEqual(result3[1], validCol2)

    def testUnsaturatedZoneTableFailureNonIncreasing(self):
        validCol1 = [-1.16,0,1,2]
        validCol2 = [-1.15,0.2,1.3,2.4]
        self.material.Strength.setUnsaturatedZoneTableWithRespectToSuction(validCol1, validCol2)
        self.material.Strength.setUnsaturatedZoneTableWithRespectToDegreeOfSaturation(validCol1, validCol2)
        self.material.Strength.setUnsaturatedZoneTableWithRespectToEffectiveDegreeOfSaturation(validCol1, validCol2)

        invalidCol1 = [-1.14,-1.14,1,2]
        invalidCol2 = [-1.15,0.2,1.3,2.4]

        with self.assertRaises(Exception):
            self.material.Strength.setUnsaturatedZoneTableWithRespectToSuction(invalidCol1, invalidCol2)
        with self.assertRaises(Exception):
            self.material.Strength.setUnsaturatedZoneTableWithRespectToDegreeOfSaturation(invalidCol1, invalidCol2)
        with self.assertRaises(Exception):
            self.material.Strength.setUnsaturatedZoneTableWithRespectToEffectiveDegreeOfSaturation(invalidCol1, invalidCol2)

        result1 = self.material.Strength.getUnsaturatedZoneTableWithRespectToSuction()
        result2 = self.material.Strength.getUnsaturatedZoneTableWithRespectToDegreeOfSaturation()
        result3 = self.material.Strength.getUnsaturatedZoneTableWithRespectToEffectiveDegreeOfSaturation()
        self.assertEqual(result1[0], validCol1)
        self.assertEqual(result1[1], validCol2)
        self.assertEqual(result2[0], validCol1)
        self.assertEqual(result2[1], validCol2)
        self.assertEqual(result3[0], validCol1)
        self.assertEqual(result3[1], validCol2)

    def testUnsaturatedZoneTableFailureNotEnoughRows(self):
        validCol1 = [-1.16,0,1,2]
        validCol2 = [-1.15,0.2,1.3,2.4]
        self.material.Strength.setUnsaturatedZoneTableWithRespectToSuction(validCol1, validCol2)
        self.material.Strength.setUnsaturatedZoneTableWithRespectToDegreeOfSaturation(validCol1, validCol2)
        self.material.Strength.setUnsaturatedZoneTableWithRespectToEffectiveDegreeOfSaturation(validCol1, validCol2)

        invalidCol1 = [-1.14]
        invalidCol2 = [-1.13]

        with self.assertRaises(Exception):
            self.material.Strength.setUnsaturatedZoneTableWithRespectToSuction(invalidCol1, invalidCol2)
        with self.assertRaises(Exception):
            self.material.Strength.setUnsaturatedZoneTableWithRespectToDegreeOfSaturation(invalidCol1, invalidCol2)
        with self.assertRaises(Exception):
            self.material.Strength.setUnsaturatedZoneTableWithRespectToEffectiveDegreeOfSaturation(invalidCol1, invalidCol2)

        result1 = self.material.Strength.getUnsaturatedZoneTableWithRespectToSuction()
        result2 = self.material.Strength.getUnsaturatedZoneTableWithRespectToDegreeOfSaturation()
        result3 = self.material.Strength.getUnsaturatedZoneTableWithRespectToEffectiveDegreeOfSaturation()
        self.assertEqual(result1[0], validCol1)
        self.assertEqual(result1[1], validCol2)
        self.assertEqual(result2[0], validCol1)
        self.assertEqual(result2[1], validCol2)
        self.assertEqual(result3[0], validCol1)
        self.assertEqual(result3[1], validCol2)

