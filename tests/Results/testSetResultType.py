import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Interpreter import RS2Interpreter
from rs2.InterpreterEnums import *
from rs2.PropertyEnums import *

parentDirectoryHelper.addParentDirectoryToPath()

class TestSetResultType(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/example_computed_model.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.interpreter = RS2Interpreter()
        self.model = self.interpreter.openFile(self.copiedModelPath)
    def tearDown(self):
        self.model.close()
        self.model._client.closeConnection()
        os.remove(self.copiedModelPath)
    
    def testSetResultTypeSuccess(self):
        self.model.SetResultType(ExportResultType.SOLID_EFFECTIVE_STRESS_EFFECTIVE_SIGMA_Z)
    
    def testSetResultTypeFailure(self):
        try:
            self.model.SetResultType(CompositeJointPlacementTypes.BETWEEN_FIRST_AND_SECOND_LINER)
            self.fail("Expected exception")
        except:
            pass
    
    # def testSetUserDefinedResultTypeSuccess(self):
    #     self.model.SetUserDefinedResultType("Sin(dy)")
    
    def testSetUserDefinedResultTypeFailure(self):
        try:
            self.model.SetUserDefinedResultType("Invalid Result Type")
            self.fail("Expected exception")
        except:
            pass