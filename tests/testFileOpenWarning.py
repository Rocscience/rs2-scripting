import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.interpreter.InterpreterEnums import *

parentDirectoryHelper.addParentDirectoryToPath()

class TestFileOpenWarning(unittest.TestCase):
    # Replace with model with warnings like thermal/log file.
    pathToModelWithWarning = ""
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = TestFileOpenWarning.pathToModelWithWarning
        self.copiedModelPath = f"{parentDirectory}/resources/testProjectWithWarning.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.interpreter = RS2Interpreter()
        self.model = None
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
        self.model._client.closeConnection()

    @unittest.skipIf(pathToModelWithWarning == "", "path to model with warnings not found")
    def testFileOpenWarningSuccess(self):
        self.model = self.interpreter.openFile(TestFileOpenWarning.pathToModelWithWarning)

    @unittest.skipIf(pathToModelWithWarning == "", "path to model with warnings not found")
    def testFileOpenWarningSetResultTypeOfModelView(self):
        self.model = self.interpreter.openFile(TestFileOpenWarning.pathToModelWithWarning)
        self.model.SetResultType(ExportResultType.SOLID_DISPLACEMENT_VERTICAL_DISPLACEMENT)