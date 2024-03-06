import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
parentDirectoryHelper.addParentDirectoryToPath()

class TestRemoveTimeQueryLine(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/example_dynamic_model.fez"
        modelWithoutDynamicPath = f"{parentDirectory}/resources/example_computed_model.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        self.modelWithoutDynamicPath = f"{parentDirectory}/resources/testProjectWithoutDynamic.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        shutil.copy(modelWithoutDynamicPath, self.modelWithoutDynamicPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.modelWithoutDynamic = self.modeler.openFile(self.modelWithoutDynamicPath)
    def tearDown(self):
        self.model.close()
        self.modelWithoutDynamic.close()
        self.model._client.closeConnection()
        self.modelWithoutDynamic._client.closeConnection()
        os.remove(self.copiedModelPath)
        os.remove(self.modelWithoutDynamicPath)
        
    def testRemoveTimeQueryLineSuccess(self):
        id = self.model.AddTimeQueryLine([[-12, -6], [-4, 5]], 5)
        self.model.RemoveTimeQueryLine([id])
    
    def testRemoveTimeQueryLineNoQueriesFailure(self):
        try:
            self.model.RemoveTimeQueryLine(["non-existant-id"])
            self.fail("Expected exception")
        except:
            pass

    def testRemoveTimeQueryLineNoneIDsFailure(self):
        try:
            self.model.RemoveTimeQueryLine([None, None])
            self.fail("Expected exception")
        except:
            pass
    
    def testRemoveTimeQueryLineEmptyIDsFailure(self):
        try:
            self.model.RemoveTimeQueryLine([])
            self.fail("Expected exception")
        except:
            pass
    
    def testRemoveTimeQueryLineInvalidIDsFailure(self):
        try:
            self.model.RemoveTimeQueryLine(["non-existant-id", ["random"]])
            self.fail("Expected exception")
        except:
            pass

    def testRemoveTimeQueryNoDynamicFailure(self):
        try:
            self.modelWithoutDynamic.RemoveTimeQueryLine(["non-existant-id"])
            self.fail("Expected exception")
        except:
            pass