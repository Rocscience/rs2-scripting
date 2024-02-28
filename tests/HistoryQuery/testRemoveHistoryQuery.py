import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestRemoveHistoryQuery(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/example_computed_model.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
        self.model._client.closeConnection()
    
    def testRemoveHistoryQuerySuccess(self):
        self.model.RemoveHistoryQueryPoint(history_query_name="HQ 1")
    
    def testRemoveHistoryQueryEmptyLabelNameFailure(self):
        try:
            self.model.RemoveHistoryQueryPoint(history_query_name="")
            self.fail("Expected exception")
        except:
            pass
    
    def testRemoveHistoryQueryFailure(self):
        try:
            self.model.RemoveHistoryQueryPoint(history_query_name="NonExistantLabelName")
            self.fail("Expected exception")
        except:
            pass