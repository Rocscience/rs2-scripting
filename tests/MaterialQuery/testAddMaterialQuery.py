import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.interpreter.RS2Interpreter import RS2Interpreter
parentDirectoryHelper.addParentDirectoryToPath()

class TestAddMaterialQuery(unittest.TestCase):
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
    
    def testAddMaterialQueryPointSuccess(self):
        self.model.AddMaterialQuery([[3.3, -2.2]])
    
    def testAddMaterialQueryLineSuccess(self):
        points_making_line = [[4.5, 4.5], [-2.5, 4.5], [-2.5, 2.5], [-6, 2.5]]
        self.model.AddMaterialQuery(points=points_making_line)
    
    def testAddMaterialQueryLineEmptyPointsFailure(self):
        try:
            self.model.AddMaterialQuery(points=[])
            self.fail("Expected exception")
        except:
            pass
    
    def testAddMaterialQueryLineNonePointsFailure(self):
        try:
            self.model.AddMaterialQuery(points=[None, None])
            self.fail("Expected exception")
        except:
            pass