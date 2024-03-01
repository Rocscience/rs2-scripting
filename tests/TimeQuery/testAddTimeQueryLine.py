import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
parentDirectoryHelper.addParentDirectoryToPath()

class TestAddTimeQueryLine(unittest.TestCase):
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
    
    def testAddTimeQueryLineSuccess(self):
        self.model.AddTimeQueryLine([[-12, -6], [-4, 5]], 5)

    def testAddTimeQueryLineWithWarningSuccess(self):
        self.model.AddTimeQueryLine([[-12, -6], [-4, 5]], 50)
        self.model.AddTimeQueryLine([[-2, -2], [2, 6]], -3)
    
    def testAddTimeQueryLineClippedSuccess(self):
        # Line with end points outside model mesh but part of the line goes through mesh
        # In this case, the line get clipped to fit inside the model mesh along its path
        self.model.AddTimeQueryLine([[-15, -2.5], [5, 5]], 5)
    
    def testAddTimeQueryLineCompletelyOutsideMeshSuccess(self):
        # In this case, the line doesn't get added to model and UI doesn't throw any errors
        self.model.AddTimeQueryLine([[-15, -10], [-15, 0]], 5)
    
    def testAddTimeQueryLinePassingThroughExcavationSuccess(self):
        # In this case, part of the line passes through/resides within the excavation region
        self.model.AddTimeQueryLine([[6, -4], [6, 3.5]], 5)
    
    def testAddTimeQueryLineNoPointsFailure(self):
        try:
            self.model.AddTimeQueryLine([], 5)
            self.fail("Expected exception")
        except:
            pass
    
    def testAddTimeQueryLineSinglePointFailure(self):
        try:
            self.model.AddTimeQueryLine([[-12, -6]], 5)
            self.fail("Expected exception")
        except:
            pass
    
    def testAddTimeQueryLineIncompletePointsInputFailure(self):
        try:
            self.model.AddTimeQueryLine([[-12, -6], []], 5)
            self.fail("Expected exception")
        except:
            pass
    
    def testAddTimeQueryLineInvalidPointsFailure(self):
        try:
            self.model.AddTimeQueryLine([None, None], 5)
            self.fail("Expected exception")
        except:
            pass

    def testAddTimeQueryLineNoDynamicFailure(self):
        try:
            self.modelWithoutDynamic.AddTimeQueryLine([[-12, -6], [-4, 5]], 5)
            self.fail("Expected exception")
        except:
            pass

    def testAddTimeQueryLineNoMeshFailure(self):
        try:
            self.modelWithoutMesh.AddTimeQueryLine([[-12, -6], [-4, 5]], 5)
            self.fail("Expected exception")
        except:
            pass