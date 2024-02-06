import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

parentDirectoryHelper.addParentDirectoryToPath()

class TestShearNormalFunction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        cls.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, cls.copiedModelPath)
        cls.modeler = RS2Modeler()
        cls.model = cls.modeler.openFile(cls.copiedModelPath)
    @classmethod
    def tearDownClass(cls):
        cls.model.close()
        os.remove(cls.copiedModelPath)

    def testSetPropertiesSuccess(self):
        #should start with no functions
        self.assertEqual(len(self.model.getShearNormalFunctions()), 0)

        #create a new function
        self.model.createNewShearNormalFunction("testFunction")
        self.assertEqual(len(self.model.getShearNormalFunctions()), 1)

        #get the function by name
        function = self.model.getShearNormalFunctionByName("testFunction")
        self.assertEqual(function.getName(), "testFunction")

        #set the material type
        function.setMaterialType(MaterialType.PLASTIC)
        self.assertEqual(function.getMaterialType(), MaterialType.PLASTIC)

        #set the use calculated tensile strength
        function.setUseCalculatedTensileStrength(False)
        self.assertEqual(function.getUseCalculatedTensileStrength(), False)
        
        #set the peak tensile strength
        function.setPeakTensileStrength(1.0)
        self.assertEqual(function.getPeakTensileStrength(), 1.0)

        #set the residual tensile strength
        function.setResidualTensileStrength(0.2)
        self.assertEqual(function.getResidualTensileStrength(), 0.2)

        #set the dilation ratio
        function.setDilationRatio(0.4)
        self.assertEqual(function.getDilationRatio(), 0.4)

        function.setFunctionPoints([(1,2,1),(4,5,2)])
        self.assertEqual(function.getFunctionPoints(), [(1,2,1),(4,5,2)])

        self.model.deleteShearNormalFunction("testFunction")
        self.assertEqual(len(self.model.getShearNormalFunctions()), 0)

    def testPropertiesFailure(self):
        #should start with no functions
        self.assertEqual(len(self.model.getShearNormalFunctions()), 0)

        #create a new function
        self.model.createNewShearNormalFunction("testFunction")
        self.assertEqual(len(self.model.getShearNormalFunctions()), 1)

        #get the function by name
        function = self.model.getShearNormalFunctionByName("testFunction")
        self.assertEqual(function.getName(), "testFunction")

        function.setMaterialType(MaterialType.PLASTIC)
        self.assertEqual(function.getMaterialType(), MaterialType.PLASTIC)
        
        function.setUseCalculatedTensileStrength(False)
        self.assertEqual(function.getUseCalculatedTensileStrength(), False)

        #residual tensile strength cannot be greater than peak tensile strength. Residual violator
        with self.assertRaises(Exception):
            function.setPeakTensileStrength(1.0)
            function.setResidualTensileStrength(1.1)
        
        #residual tensile strength cannot be greater than peak tensile strength. Peak violator
        with self.assertRaises(Exception):
            function.setResidualTensileStrength(0.2)
            function.setPeakTensileStrength(0.1)

        #residual tensile strength must be graeter than 0
        with self.assertRaises(Exception):
            function.setResidualTensileStrength(-0.1)

        #cannot set residual tensile strength for elastic material
        with self.assertRaises(Exception):
            function.setMaterialType(MaterialType.ELASTIC)
            function.setResidualTensileStrength(0.2)
        
        #cannot set dilation ratio for elastic material
        with self.assertRaises(Exception):
            function.setMaterialType(MaterialType.ELASTIC)
            function.setDilationRatio(0.2)
        
        function.setMaterialType(MaterialType.PLASTIC)

        #dilation ratio must be between 0 and 1
        with self.assertRaises(Exception):
            function.setDilationRatio(-0.1)
        with self.assertRaises(Exception):
            function.setDilationRatio(1.1)
        
        #cannot have less than 2 function points
        with self.assertRaises(Exception):
            function.setFunctionPoints([(1,2,1)])

        #cannot input points with normal not in ascending order
        with self.assertRaises(Exception):
            function.setFunctionPoints([(4,5,2),(1,2,1)])

        self.model.deleteShearNormalFunction("testFunction")
        self.assertEqual(len(self.model.getShearNormalFunctions()), 0)

    def testGetDoesNotExist(self):
        self.model.createNewShearNormalFunction("f1")

        with self.assertRaises(Exception):
            self.model.getShearNormalFunctionByName("f2")
        
        self.model.deleteShearNormalFunction("f1")
    
    def testGetAllFunctions(self):
        self.model.createNewShearNormalFunction("f1")
        self.model.getShearNormalFunctionByName("f1").setPeakTensileStrength(1.1)

        self.model.createNewShearNormalFunction("f2")
        self.model.getShearNormalFunctionByName("f2").setPeakTensileStrength(1.2)

        self.model.createNewShearNormalFunction("f3")
        self.model.getShearNormalFunctionByName("f3").setPeakTensileStrength(1.3)

        functions = self.model.getShearNormalFunctions()
        self.assertEqual(functions[0].getPeakTensileStrength(), 1.1)
        self.assertEqual(functions[1].getPeakTensileStrength(), 1.2)
        self.assertEqual(functions[2].getPeakTensileStrength(), 1.3)

        self.model.deleteShearNormalFunction("f1")
        self.model.deleteShearNormalFunction("f2")
        self.model.deleteShearNormalFunction("f3")

    def testRename(self):
        self.model.createNewShearNormalFunction("f1")
        self.model.getShearNormalFunctionByName("f1").setPeakTensileStrength(1.11)

        self.model.renameShearNormalFunction("f1", "f2")

        self.assertEqual(self.model.getShearNormalFunctionByName("f2").getPeakTensileStrength(), 1.11)

        self.model.deleteShearNormalFunction("f2")

    def testRenameNameInUse(self):
        self.model.createNewShearNormalFunction("f1")
        self.model.createNewShearNormalFunction("f2")

        with self.assertRaises(Exception):
            self.model.renameShearNormalFunction("f1", "f2")
        
        self.model.deleteShearNormalFunction("f1")
        self.model.deleteShearNormalFunction("f2")

    def testCreateAlreadyExists(self):
        self.model.createNewShearNormalFunction("f1")

        with self.assertRaises(Exception):
            self.model.createNewShearNormalFunction("f1")
        
        self.model.deleteShearNormalFunction("f1")
    
    def testDeleteUsedProperty(self):
        self.model.createNewShearNormalFunction("f1")
        strength = self.model.getAllMaterialProperties()[0].Strength
        strength.setFailureCriterion(StrengthCriteriaTypes.SHEAR_NORMAL_FUNCTION)
        strength.ShearNormalFunction.setShearNormalFunctionByName("f1")

        with self.assertRaises(Exception):
            self.model.deleteShearNormalFunction("f1")
        
        strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
        self.model.deleteShearNormalFunction("f1")

        self.assertEqual(len(self.model.getShearNormalFunctions()), 0)

        self.model.getAllMaterialProperties()[0].setMaterialName