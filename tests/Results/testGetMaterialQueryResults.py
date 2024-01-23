import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Interpreter import RS2Interpreter
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestGetHistoryQueryResults(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/example_computed_model.fez"
        modelWithoutMQPath = f"{parentDirectory}/resources/modelWithoutQuery.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        self.modelWithoutMQPath = f"{parentDirectory}/resources/testModelWithoutQuery.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        shutil.copy(modelWithoutMQPath, self.modelWithoutMQPath)
        self.interpreter = RS2Interpreter()
        self.model = self.interpreter.openFile(self.copiedModelPath)
        self.modelWithoutMQ = self.interpreter.openFile(self.modelWithoutMQPath)
    def tearDown(self):
        self.model.close()
        self.modelWithoutMQ.close()
        os.remove(self.copiedModelPath)
        os.remove(self.modelWithoutMQPath)
        self.model._client.closeConnection()
        self.modelWithoutMQ._client.closeConnection()

    def testGetMaterialQueryResultsSuccess(self):
        self.model.GetMaterialQueryResults(stages=[1, 2])

    def testGetMaterialQueryResultsWithoutQueriesFailure(self):
        try:
            self.modelWithoutMQ.GetMaterialQueryResults(stages=[1, 2])
            self.fail("Expected exception")
        except:
            pass

    def testGetMaterialQueryResultsEmptyStagesFailure(self):
        try:
            self.model.GetMaterialQueryResults(stages=[])
            self.fail("Expected exception")
        except:
            pass
    
    def testGetMaterialQueryResultsMinStagesFailure(self):
        try:
            self.model.GetMaterialQueryResults(stages=[-1, 3])
            self.fail("Expected exception")
        except:
            pass

    def testGetHistoryQueryResultsMaxStagesFailure(self):
        try:
            self.model.GetMaterialQueryResults(stages=[1, 800])
            self.fail("Expected exception")
        except:
            pass