import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.interpreter.RS2Interpreter import RS2Interpreter
parentDirectoryHelper.addParentDirectoryToPath()

class TestInterpreterSaveAs(unittest.TestCase):
    parentDirectory = parentDirectoryHelper.getParentDirectory()
    @classmethod
    def setUpClass(self):
        blankModelPath = f"{TestInterpreterSaveAs.parentDirectory}/resources/example_computed_model.fez"
        self.copiedModelPath = f"{TestInterpreterSaveAs.parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.interpreter = RS2Interpreter()
        self.model = self.interpreter.openFile(self.copiedModelPath)
    @classmethod
    def tearDownClass(self):
        self.model.close()
        os.remove(self.copiedModelPath)
        self.model._client.closeConnection()
    
    def testInterpreterSaveAsSuccess(self):
        self.saveAsPath = f"{TestInterpreterSaveAs.parentDirectory}/resources/testFileSaveAs.fez"
        self.model.saveAs(self.saveAsPath)
    
    def testInterpreterConsecutiveSaveAsSuccess(self):
        self.saveAsPath = f"{TestInterpreterSaveAs.parentDirectory}/resources/testFileSaveAs.fez"
        self.model.saveAs(self.saveAsPath)
        self.model.saveAs(self.saveAsPath)
        self.model.saveAs(self.saveAsPath)
    
    def testInterpeterSaveAsFailure(self):
        try:
            self.saveAsPath = f"{TestInterpreterSaveAs.parentDirectory}/resources/testProject.fez"
            self.model.saveAs(self.saveAsPath)
            self.fail("Expected exception")
        except:
            pass

    def testInterpeterSaveAsEmptyPathFailure(self):
        try:
            self.saveAsPath = ""
            self.model.saveAs(self.saveAsPath)
            self.fail("Expected exception")
        except:
            pass