import unittest
import os
from rs2.interpreter.RS2Interpreter import RS2Interpreter
import parentDirectoryHelper
import shutil

parentDirectoryHelper.addParentDirectoryToPath()

class TesOpenFileNoResults(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        zipFilePath = f"{parentDirectory}/resources/noResults.fez"
        self.copiedZipFilePath = f"{parentDirectory}/resources/testProjectFez.fez"

        feaFilePath = f"{parentDirectory}/resources/noResults.fea"
        self.copiedFeaFilePath = f"{parentDirectory}/resources/testProjectFea.fea"

        shutil.copy(zipFilePath, self.copiedZipFilePath)
        shutil.copy(feaFilePath, self.copiedFeaFilePath)

        self.interpreter = RS2Interpreter()

    def tearDown(self):
        os.remove(self.copiedZipFilePath)
        os.remove(self.copiedFeaFilePath)

        self.interpreter.client.closeConnection()

    def testOpenFileNoResultsException(self):
        with self.assertRaises(Exception):
            self.interpreter.openFile(self.copiedZipFilePath)
        
    def testOpenFEANoResultsException(self):
        with self.assertRaises(Exception):
            self.interpreter.openFile(self.copiedFeaFilePath)