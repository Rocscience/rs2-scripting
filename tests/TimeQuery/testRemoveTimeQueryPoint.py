import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
parentDirectoryHelper.addParentDirectoryToPath()

class TestRemoveTimeQueryPoint(unittest.TestCase):
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
        
    def testRemoveTimeQueryPointSuccess(self):
        id = self.model.AddTimeQueryPoint(3.3, -2.2)
        self.model.RemoveTimeQueryPoint([id])
    
    def testRemoveTimeQueryPointNoQueriesFailure(self):
        try:
            self.model.RemoveTimeQueryPoint(["non-existant-id"])
            self.fail("Expected exception")
        except:
            pass

    def testRemoveTimeQueryPointNoneIDsFailure(self):
        try:
            self.model.RemoveTimeQueryPoint([None, None])
            self.fail("Expected exception")
        except:
            pass
    
    def testRemoveTimeQueryPointEmptyIDsFailure(self):
        try:
            self.model.RemoveTimeQueryPoint([])
            self.fail("Expected exception")
        except:
            pass
    
    def testRemoveTimeQueryPointInvalidIDsFailure(self):
        try:
            self.model.RemoveTimeQueryPoint(["non-existant-id", ["random"]])
            self.fail("Expected exception")
        except:
            pass

    def testRemoveTimeQueryNoDynamicFailure(self):
        try:
            self.modelWithoutDynamic.RemoveTimeQueryPoint(["non-existant-id"])
            self.fail("Expected exception")
        except:
            pass