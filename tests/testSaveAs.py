import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestMaterialJointOptions(unittest.TestCase):
    def setUp(self):
        self.parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{self.parentDirectory}/resources/example_computed_model.fez"
        self.copiedModelPath = f"{self.parentDirectory}/resources/testProject.fez"
        os.mkdir(f"{self.parentDirectory}/resources/fea")
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.interpreter = RS2Interpreter()

    def tearDown(self):
        os.remove(self.copiedModelPath)
        self.modeler.client.closeConnection()
        self.interpreter.client.closeConnection()
        shutil.rmtree(f"{self.parentDirectory}/resources/fea")

    def testSaveAsModeler(self):
        model = self.modeler.openFile(self.copiedModelPath)
        model.saveAs(f"{self.parentDirectory}/resources/fea/testProject1.fea")
        model.saveAs(f"{self.parentDirectory}/resources/testProject2.fez")
        with self.assertRaises(Exception):
            model.saveAs(f"{self.parentDirectory}/resources/testProject3.fed")
        
        model.close()
        os.remove(f"{self.parentDirectory}/resources/testProject2.fez")

    def testSaveAsInterpreter(self):
        model = self.interpreter.openFile(self.copiedModelPath)
        model.saveCopyAs(f"{self.parentDirectory}/resources/fea/testProject4.fea")
        model.saveCopyAs(f"{self.parentDirectory}/resources/testProject5.fez")
        with self.assertRaises(Exception):
            model.saveCopyAs(f"{self.parentDirectory}/resources/testProject6.fed")
        
        model.close()
        os.remove(f"{self.parentDirectory}/resources/testProject5.fez")
        