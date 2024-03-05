import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.interpreter.InterpreterEnums import *

parentDirectoryHelper.addParentDirectoryToPath()

class TestFileOpenWarning(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/modelWithLogFileWarning.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProjectWithWarning.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.interpreter = RS2Interpreter()
        self.model = None
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
        self.model._client.closeConnection()

    def testFileOpenWarningSuccess(self):
        self.model = self.interpreter.openFile(self.copiedModelPath)