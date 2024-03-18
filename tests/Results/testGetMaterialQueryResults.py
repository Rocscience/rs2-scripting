import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.interpreter.RS2Interpreter import RS2Interpreter

parentDirectoryHelper.addParentDirectoryToPath()

class TestGetMaterialQueryResults(unittest.TestCase):
    @classmethod
    def setUpClass(self):
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
    @classmethod
    def tearDownClass(self):
        self.model.close()
        self.modelWithoutMQ.close()
        os.remove(self.copiedModelPath)
        os.remove(self.modelWithoutMQPath)
        self.model._client.closeConnection()
        self.modelWithoutMQ._client.closeConnection()

    def testGetMaterialQueryResultsSuccess(self):
        id = self.model.AddMaterialQuery([[3.5, 2.5]])
        result = self.model.GetMaterialQueryResults()
        self.model.RemoveMaterialQuery([id])
        self.assertEqual(len(result), 1)
    
    def testGetMaterialQueryResultsForAllQueriesSuccess(self):
        id1 = self.model.AddMaterialQuery([[3.5, 3.5]])
        id2 = self.model.AddMaterialQuery([[3.5, 2.5]])
        id3 = self.model.AddMaterialQuery([[3.5, 1.5]])
        results = self.model.GetMaterialQueryResults()
        self.model.RemoveMaterialQuery([id1, id2, id3])
        self.assertEqual(len(results), 3)
    
    def testGetMaterialQueryResultsConvertInvalidValueSuccess(self):
        id1 = self.model.AddMaterialQuery([[30.5, 30.5]])
        id2 = self.model.AddMaterialQuery([[-12, 6], [-10, 6]])
        results = self.model.GetMaterialQueryResults()
        self.model.RemoveMaterialQuery([id1, id2])
        for node in results:
            for value in node.GetAllValues():
                self.assertEqual(value.GetValue(), None)

    def testGetMaterialQueryResultsWithoutQueriesFailure(self):
        try:
            self.modelWithoutMQ.GetMaterialQueryResults()
            self.fail("Expected exception")
        except:
            pass