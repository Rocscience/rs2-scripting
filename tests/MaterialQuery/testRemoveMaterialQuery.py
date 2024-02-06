import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Interpreter import RS2Interpreter
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestRemoveMaterialQuery(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/example_computed_model.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.interpreter = RS2Interpreter()
        self.model = self.interpreter.openFile(self.copiedModelPath)
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
        self.model._client.closeConnection()
    
    def testRemoveMaterialQueryPointSuccess(self):
        guid = self.model.AddMaterialQuery([[3.3, -2.2]])
        self.model.RemoveMaterialQuery(guid)
    
    def testRemoveMaterialQueryLineSuccess(self):
        points_making_line = [[4.5, 4.5], [-2.5, 4.5], [-2.5, 2.5], [-6, 2.5]]
        guid = self.model.AddMaterialQuery(points=points_making_line)
        self.model.RemoveMaterialQuery(guid)
    
    def testRemoveMaterialQueryFailure(self):
        try:
            self.model.RemoveMaterialQuery("Non-Existant GUID")
            self.fail("Expected exception")
        except:
            pass