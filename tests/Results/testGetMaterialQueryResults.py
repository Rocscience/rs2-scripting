import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.interpreter.RS2Interpreter import RS2Interpreter

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
        self.model.AddMaterialQuery([[3.5, 2.5]])
        result = self.model.GetMaterialQueryResults()
        self.assertEqual(len(result), 1)
    
    def testGetMaterialQueryResultsForAllQueriesSuccess(self):
        self.model.AddMaterialQuery([[3.5, 3.5]])
        self.model.AddMaterialQuery([[3.5, 2.5]])
        self.model.AddMaterialQuery([[3.5, 1.5]])
        results = self.model.GetMaterialQueryResults()
        self.assertEqual(len(results), 3)
    
    def testGetMaterialQueryResultsForPointsInsideMeshSuccess(self):
        # Points added outside model mesh
        self.model.AddMaterialQuery([[23.5, 40.5]])
        self.model.AddMaterialQuery([[23.5, 30.5]])
        self.model.AddMaterialQuery([[23.5, 20.5]])
        # Point added inside mesh
        self.model.AddMaterialQuery([[3.5, 2.5]])
        results = self.model.GetMaterialQueryResults()
        self.assertEqual(len(results), 1)

    def testGetMaterialQueryResultsWithoutQueriesFailure(self):
        try:
            self.modelWithoutMQ.GetMaterialQueryResults()
            self.fail("Expected exception")
        except:
            pass