import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestDiscreteFunctionManager(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProjectTransientGroundwater.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)

    @classmethod
    def tearDownClass(self):
        self.model.close()
        os.remove(self.copiedModelPath)

    def testGetNonExistant(self):
        model = self.model

        with self.assertRaises(Exception):
            model.getDiscreteFunctionByName("nonExistant")

    def testCreateDeleteDiscreteFunction(self):
        model = self.model

        with self.assertRaises(Exception):
            model.getDiscreteFunctionByName("testDiscreteFunction")

        model.createNewDiscreteFunction("testDiscreteFunction")
        model.getDiscreteFunctionByName("testDiscreteFunction")
        model.deleteDiscreteFunction("testDiscreteFunction")

        with self.assertRaises(Exception):
            model.getDiscreteFunctionByName("testDiscreteFunction")

    def testCreateFailureDuplicate(self):
        model = self.model

        model.createNewDiscreteFunction("testDiscreteFunction")
        with self.assertRaises(Exception):
            model.createNewDiscreteFunction("testDiscreteFunction")
        model.deleteDiscreteFunction("testDiscreteFunction")
    
    def testDeleteFailureNonexistant(self):
        model = self.model

        with self.assertRaises(Exception):
            model.deleteDiscreteFunction("testDiscreteFunction")

    def testDeleteFailureUsedByMaterial(self):
        self.model.createNewDiscreteFunction("testDiscreteFunction1")
        self.model.createNewDiscreteFunction("testDiscreteFunction2")

        mat1 = self.model.getAllMaterialProperties()[0]
        mat1.Strength.setFailureCriterion(StrengthCriteriaTypes.DISCRETE_FUNCTION)
        mat1.Strength.DiscreteFunction.setSelectedDiscreteFunctionByName("testDiscreteFunction1")

        with self.assertRaises(Exception):
            self.model.deleteDiscreteFunction("testDiscreteFunction1")

        self.model.deleteDiscreteFunction("testDiscreteFunction2")

        mat1.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
        self.model.deleteDiscreteFunction("testDiscreteFunction1")

    

class TestDiscreteFunctionFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProjectTransientGroundwater.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.model.createNewDiscreteFunction("testDiscreteFunction1")

        mat1 = self.model.getAllMaterialProperties()[0]
        mat1.Strength.setFailureCriterion(StrengthCriteriaTypes.DISCRETE_FUNCTION)
        mat1.Strength.DiscreteFunction.setSelectedDiscreteFunctionByName("testDiscreteFunction1")

        self.df = self.model.getDiscreteFunctionByName("testDiscreteFunction1")

        self.df.setFunctionParameters()
    @classmethod
    def tearDownClass(self):
        self.model.close()
        os.remove(self.copiedModelPath)

    def testSetFunctionParameters(self):
        self.df

        