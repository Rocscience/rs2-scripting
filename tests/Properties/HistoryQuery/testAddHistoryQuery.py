import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestAddHistoryQuery(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/example_computed_model.fez"
        invalidModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        self.invalidModelMeshPath = f"{parentDirectory}/resources/testInvalidMeshModel.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        shutil.copy(invalidModelPath, self.invalidModelMeshPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.modelWithoutMesh = self.modeler.openFile(self.invalidModelMeshPath)
    def tearDown(self):
        self.model.close()
        self.modelWithoutMesh.close()
        os.remove(self.copiedModelPath)
        os.remove(self.invalidModelMeshPath)
        self.model._client.closeConnection()
        self.modelWithoutMesh._client.closeConnection()
    
    def testAddHistoryQuerySuccess(self):
        self.model.AddHistoryQueryPoint(x=4.4, y=-1.9, history_query_name="Example Label")
    
    def testAddHistoryQueryModelWithoutMeshFailure(self):
        try:
            self.modelWithoutMesh.AddHistoryQueryPoint(x=4.4, y=-1.9, history_query_name="Example Label")
            self.fail("Expected exception")
        except:
            pass
    
    def testAddHistoryQueryOutOfMeshBoundsFailure(self):
        try:
            self.model.AddHistoryQueryPoint(x=500.4, y=-190.9, history_query_name="Example Label")
            self.fail("Expected exception")
        except:
            pass
    
    def testAddHistoryQueryDuplicateCoordinatesFailure(self):
        try:
            self.model.AddHistoryQueryPoint(x=0, y=0, history_query_name="Example Label")
            self.fail("Expected exception")
        except:
            pass

    def testAddHistoryQueryDuplicateLabelNameFailure(self):
        try:
            self.model.AddHistoryQueryPoint(x=4.4, y=-1.9, history_query_name="HQ 1")
            self.fail("Expected exception")
        except:
            pass