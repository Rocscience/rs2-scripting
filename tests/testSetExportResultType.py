import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Interpreter import RS2Interpreter
from rs2.InterpreterPropertyEnums import *
from rs2.PropertyEnums import *
import time

parentDirectoryHelper.addParentDirectoryToPath()

class TestSetExportResultType(unittest.TestCase):
    pathToComputedModel = "S:\willSati\Scripting\TestModels\Profiles_and_Boreholes.fez"

    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = TestSetExportResultType.pathToComputedModel
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.interpreter = RS2Interpreter()
        self.model = self.interpreter.openFile(self.copiedModelPath)
    def tearDown(self):
        self.model.close()
        self.model._client.closeConnection()
        os.remove(self.copiedModelPath)
    
    @unittest.skipIf(not pathToComputedModel, "requires path to computed model for RS2 Interpreter")  
    def testSetExportResultTypeSuccess(self):
        interpreter = self.interpreter
        interpreter.SetExportResultType(ExportResultType.SOLID_EFF_STRESS_SIGMA_ONE_EFF)
    
    @unittest.skipIf(not pathToComputedModel, "requires path to computed model for RS2 Interpreter")  
    def testSetExportResultTypeFailure(self):
        try:
            interpreter = self.interpreter
            interpreter.SetExportResultType(CompositeJointPlacementTypes.BETWEEN_FIRST_AND_SECOND_LINER)
            self.fail("Expected exception")
        except:
            pass
    
    @unittest.skipIf(not pathToComputedModel, "requires path to computed model for RS2 Interpreter")  
    def testSetUserDefinedExportResultTypeSuccess(self):
        interpreter = self.interpreter
        interpreter.SetUserDefinedExportResultType("Keff")
    
    @unittest.skipIf(not pathToComputedModel, "requires path to computed model for RS2 Interpreter")  
    def testSetUserDefinedExportResultTypeFailure(self):
        try:
            interpreter = self.interpreter
            interpreter.SetUserDefinedExportResultType("Invalid Result Type")
            self.fail("Expected exception")
        except:
            pass