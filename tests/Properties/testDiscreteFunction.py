import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*
from rs2.utilities.ColorPicker import ColorPicker

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

    @classmethod
    def tearDownClass(self):
        self.model.close()
        os.remove(self.copiedModelPath)

    def testFunctionParameters(self):
        self.df.setFunctionParameters(DiscreteDrainedMode.SL_DISCRETE_DRAINED, True, 1.1, 2.2, 3.3, True)
        self.assertEqual(self.df.getFunctionParameters(), (DiscreteDrainedMode.SL_DISCRETE_DRAINED, True, 1.1, 2.2, 3.3, True))

        self.df.setFunctionParameters(DiscreteDrainedMode.SL_DISCRETE_UNDRAINED, False, 1.1, 2.2, 3.3, False)
        self.assertEqual(self.df.getFunctionParameters(), (DiscreteDrainedMode.SL_DISCRETE_UNDRAINED, False, 1.1, 2.2, 3.3, False))

    def testInterpolationMethod(self):
        self.df.setInterpolationMethod(InterpolationMethod.BCINTERPOLATE_THINPLATESPLINE)
        self.assertEqual(self.df.getInterpolationMethod(), InterpolationMethod.BCINTERPOLATE_THINPLATESPLINE)

        self.df.setInterpolationMethod(InterpolationMethod.BCINTERPOLATE_ORIGINALCHUGH)
        self.assertEqual(self.df.getInterpolationMethod(), InterpolationMethod.BCINTERPOLATE_ORIGINALCHUGH)

    def testSetSymbolDrawing(self):
        self.df.setSymbolDrawing(SymbolTypes.SL_SYMBOL_TYPE_SQUARE, ColorPicker.Green, True, ColorPicker.Blue)
        self.assertEqual(self.df.getSymbolDrawing(), (SymbolTypes.SL_SYMBOL_TYPE_SQUARE, ColorPicker.Green, True, ColorPicker.Blue))

        self.df.setSymbolDrawing(SymbolTypes.SL_SYMBOL_TYPE_DOT, ColorPicker.Red, False, ColorPicker.Yellow)
        self.assertEqual(self.df.getSymbolDrawing(), (SymbolTypes.SL_SYMBOL_TYPE_DOT, ColorPicker.Red, False, ColorPicker.Yellow))

    def testSetPointLocations(self):
        self.df.setPointLocations([(0, 0), (1.1, 1.2), (2.1, 2.2)])
        self.assertEqual(self.df.getPointLocations(), [(0, 0), (1.1, 1.2), (2.1, 2.2)])
        
    def testSetPointsC(self):
        self.df.setPointsC([0, 1.1, 2.2])
        self.assertEqual(self.df.getPointsC(), [0, 1.1, 2.2])

    def testSetPointsPhi(self):
        self.df.setPointsPhi([0, 1.1, 2.2])
        self.assertEqual(self.df.getPointsPhi(), [0, 1.1, 2.2])

    def testSetPointsModulus(self):
        self.df.setPointsModulus([0, 1.1, 2.2])
        self.assertEqual(self.df.getPointsModulus(), [0, 1.1, 2.2])

    def testSetPointsModulusResidual(self):
        self.df.setPointsModulusResidual([0, 1.1, 2.2])
        self.assertEqual(self.df.getPointsModulusResidual(), [0, 1.1, 2.2])