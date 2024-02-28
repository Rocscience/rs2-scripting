import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
parentDirectoryHelper.addParentDirectoryToPath()

class TestAddTimeQueryPoint(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/example_dynamic_model.fez"
        modelWithoutDynamicPath = f"{parentDirectory}/resources/example_computed_model.fez"
        modelWithoutMeshPath = f"{parentDirectory}/resources/empty_dynamic_model.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        self.modelWithoutDynamicPath = f"{parentDirectory}/resources/testProjectWithoutDynamic.fez"
        self.modelWithoutMeshPath = f"{parentDirectory}/resources/testProjectWithoutMesh.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        shutil.copy(modelWithoutDynamicPath, self.modelWithoutDynamicPath)
        shutil.copy(modelWithoutMeshPath, self.modelWithoutMeshPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.modelWithoutDynamic = self.modeler.openFile(self.modelWithoutDynamicPath)
        self.modelWithoutMesh = self.modeler.openFile(self.modelWithoutMeshPath)
    def tearDown(self):
        self.model.close()
        self.modelWithoutDynamic.close()
        self.modelWithoutMesh.close()
        self.model._client.closeConnection()
        self.modelWithoutDynamic._client.closeConnection()
        self.modelWithoutMesh._client.closeConnection()
        os.remove(self.copiedModelPath)
        os.remove(self.modelWithoutDynamicPath)
        os.remove(self.modelWithoutMeshPath)
        
    
    def testAddTimeQueryPointSuccess(self):
        self.model.AddTimeQueryPoint(3.3, -2.2)
    
    def testAddTimeQueryPointOverExcavationSuccess(self):
        self.model.AddTimeQueryPoint(6, 2.5)
    
    def testAddTimeQueryPointOverlappingCoordinatesFailure(self):
        try:
            self.model.AddTimeQueryPoint(3.3, -2.2)
            self.model.AddTimeQueryPoint(3.3, -2.2)
            self.fail("Expected exception")
        except:
            pass

    def testAddTimeQueryPointOutsideModelFailure(self):
        try:
            self.model.AddTimeQueryPoint(30, -20)
            self.fail("Expected exception")
        except:
            pass
    
    def testAddTimeQueryPointNoDynamicFailure(self):
        try:
            self.modelWithoutDynamic.AddTimeQueryPoint(3.3, -2.2)
            self.fail("Expected exception")
        except:
            pass

    def testAddTimeQueryPointNoMeshFailure(self):
        try:
            self.modelWithoutMesh.AddTimeQueryPoint(3.3, -2.2)
            self.fail("Expected exception")
        except:
            pass