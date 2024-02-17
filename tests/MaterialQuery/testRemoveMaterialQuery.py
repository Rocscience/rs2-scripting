import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.interpreter.RS2Interpreter import RS2Interpreter

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
        self.model.RemoveMaterialQuery([guid])
    
    def testRemoveMaterialQueryLineSuccess(self):
        points_making_line = [[4.5, 4.5], [-2.5, 4.5], [-2.5, 2.5], [-6, 2.5]]
        guid = self.model.AddMaterialQuery(points=points_making_line)
        self.model.RemoveMaterialQuery([guid])
    
    def testRemoveMultipleMaterialQueryPointSuccess(self):
        guid1 = self.model.AddMaterialQuery(points=[[0.0, 1.0]])
        guid2 = self.model.AddMaterialQuery(points=[[1.3, -2.2]])
        self.model.RemoveMaterialQuery([guid1, guid2])

    def testRemoveMultipleMaterialQueryLineSuccess(self):
        points_making_line = [[4.5, 4.5], [-2.5, 4.5], [-2.5, 2.5], [-6, 2.5]]
        points_making_line2 = [[-2, -4], [-2, -1]]
        guid1 = self.model.AddMaterialQuery(points=points_making_line)
        guid2 = self.model.AddMaterialQuery(points=points_making_line2)
        self.model.RemoveMaterialQuery([guid1, guid2])
    
    def testRemoveMaterialQueryFailure(self):
        try:
            self.model.RemoveMaterialQuery(["Non-Existant GUID"])
            self.fail("Expected exception")
        except:
            pass

    def testRemoveMaterialQueryEmptyIDsFailure(self):
        try:
            self.model.RemoveMaterialQuery([])
            self.fail("Expected exception")
        except:
            pass
    
    def testRemoveMaterialQueryNoneIDsFailure(self):
        try:
            self.model.RemoveMaterialQuery([None, None, None])
            self.fail("Expected exception")
        except:
            pass
    
    def testRemoveMaterialQueryInvalidIDsFailure(self):
        try:
            guid1 = self.model.AddMaterialQuery(points=[[0.0, 1.0]])
            guid2 = self.model.AddMaterialQuery(points=[[1.3, -2.2]])
            self.model.RemoveMaterialQuery([guid1, guid2, "InvalidID"])
            self.fail("Expected exception")
        except:
            pass