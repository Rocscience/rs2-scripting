import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Interpreter import RS2Interpreter
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestGetMaterialQueryResults(unittest.TestCase):
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
        self.model.GetMaterialQueryResults()
    
    def testGetMaterialQueryResultsForAllQueriesSuccess(self):
        self.model.AddMaterialQueryPoint(3.5, 3.5)
        self.model.AddMaterialQueryPoint(3.5, 2.5)
        self.model.AddMaterialQueryPoint(3.5, 1.5)
        # The model already has 1 material query so in total we expect length of results returned to be 5
        results = self.model.GetMaterialQueryResults()
        self.assertEqual(len(results), 4)
    
    def testGetMaterialQueryResultsForPointsInsideMeshSuccess(self):
        # Points added outside model mesh
        self.model.AddMaterialQueryPoint(20.5, 14.5)
        self.model.AddMaterialQueryPoint(20.5, 13.5)
        self.model.AddMaterialQueryPoint(20.5, 12.5)
        self.model.AddMaterialQueryPoint(20.5, 11.5)
        # Result isn't calculated for points outside model mesh so we expect result length to be 1 since model already has 1 valid query
        results = self.model.GetMaterialQueryResults()
        self.assertEqual(len(results), 1)

    def testGetMaterialQueryResultsWithoutQueriesFailure(self):
        try:
            self.modelWithoutMQ.GetMaterialQueryResults()
            self.fail("Expected exception")
        except:
            pass