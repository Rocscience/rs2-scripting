import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *

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

        #set the function name
        function.setName("newName")
        self.assertEqual(function.getName(), "newName")

        #set the material type
        function.setMaterialTypeByName(MaterialType.PLASTIC)
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

        self.model.deleteShearNormalFunction("newName")
        self.assertEqual(len(self.model.getShearNormalFunctions()), 0)