import unittest
import os
from rs2.interpreter.RS2Interpreter import RS2Interpreter
import parentDirectoryHelper
import shutil

parentDirectoryHelper.addParentDirectoryToPath()

class TesOpenFileNoResults(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/noResults.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"

        shutil.copy(blankModelPath, self.copiedModelPath)
        self.interpreter = RS2Interpreter()
    def tearDown(self):
        os.remove(self.copiedModelPath)
        self.interpreter.client.closeConnection()

    def testOpenFileNoResultsException(self):
        with self.assertRaises(Exception):
            self.interpreter.openFile(self.copiedModelPath)
        
