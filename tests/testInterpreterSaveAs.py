import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.interpreter.RS2Interpreter import RS2Interpreter
parentDirectoryHelper.addParentDirectoryToPath()

class TestInterpreterSaveAs(unittest.TestCase):
    parentDirectory = parentDirectoryHelper.getParentDirectory()
    modelSavePath = ""
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
        if os.path.exists(TestInterpreterSaveAs.modelSavePath):
            os.remove(TestInterpreterSaveAs.modelSavePath)
        self.model._client.closeConnection()
    
    def testInterpreterSaveAsSuccess(self):
        TestInterpreterSaveAs.modelSavePath = f"{TestInterpreterSaveAs.parentDirectory}/resources/testFileSaveAs.fez"
        self.model.saveAs(TestInterpreterSaveAs.modelSavePath)
    
    def testInterpreterConsecutiveSaveAsSuccess(self):
        TestInterpreterSaveAs.modelSavePath = f"{TestInterpreterSaveAs.parentDirectory}/resources/testFileSaveAs.fez"
        self.model.saveAs(TestInterpreterSaveAs.modelSavePath)
        self.model.saveAs(TestInterpreterSaveAs.modelSavePath)
        self.model.saveAs(TestInterpreterSaveAs.modelSavePath)

    def testInterpeterSaveAsFailure(self):
        try:
            TestInterpreterSaveAs.modelSavePath = f"{TestInterpreterSaveAs.parentDirectory}/resources/testProject.fez"
            self.model.saveAs(TestInterpreterSaveAs.modelSavePath)
            self.fail("Expected exception")
        except:
            pass

    def testInterpeterSaveAsEmptyPathFailure(self):
        try:
            self.model.saveAs("")
            self.fail("Expected exception")
        except:
            pass