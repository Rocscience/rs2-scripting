import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.interpreter.RS2Interpreter import RS2Interpreter 
from rs2.interpreter.InterpreterGraphEnums import *

parentDirectoryHelper.addParentDirectoryToPath()

class TestGetTimeQueryResults(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/example_dynamic_model.fez"
        modelWithoutTQPath = f"{parentDirectory}/resources/example_computed_model.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        self.modelWithoutTQPath = f"{parentDirectory}/resources/testModelWithoutTQ.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        shutil.copy(modelWithoutTQPath, self.modelWithoutTQPath)
        self.interpreter = RS2Interpreter()
        self.model = self.interpreter.openFile(self.copiedModelPath) 
        self.modelWithoutTQ = self.interpreter.openFile(self.modelWithoutTQPath)
    def tearDown(self):
        self.model.close()
        self.modelWithoutTQ.close()
        os.remove(self.copiedModelPath)
        os.remove(self.modelWithoutTQPath)
        self.model._client.closeConnection()
        self.modelWithoutTQ._client.closeConnection()

    # Time Query Point Results Test
    def testGetTimeQueryPointResultsSuccess(self):
        result = self.model.GetAllTimeQueryPointResults(stages=[1, 2, 3, 4],
                                          vertical_axis=TimeQueryGraphEnums.VerticalAxisTypes.EFFECTIVE_STRESS_XX)
        self.assertGreater(len(result), 0)
    
    def testGetTimeQueryPointResultsOnExcavationSuccess(self):
        # A point over excavation should not return any result i.e empty list
        # For the example_dynamic_model, we have 2 time query points.
        # One of those points is over a tunnel excavation for which no result will be returned at stage #4

        result = self.model.GetAllTimeQueryPointResults(stages=[4],
                                          vertical_axis=TimeQueryGraphEnums.VerticalAxisTypes.EFFECTIVE_STRESS_XX)
        # Out of two points, only result for valid query point will be returned at stage 4
        self.assertEqual(len(result), 1)

    def testGetTimeQueryPointResultsWithoutQueriesFailure(self):
        try:
            self.modelWithoutTQ.GetAllTimeQueryPointResults(stages=[1, 2, 3, 4],
                                          vertical_axis=TimeQueryGraphEnums.VerticalAxisTypes.EFFECTIVE_STRESS_XX)
            self.fail("Expected exception")
        except:
            pass

    def testGetTimeQueryPointResultsInvalidVerticalAxisFailure(self):
        try:
            self.model.GetAllTimeQueryPointResults(stages=[1, 2, 3, 4],
                                          vertical_axis=HistoryQueryGraphEnums.VerticalAxisTypes.EFFECTIVE_STRESS_XX)
            self.fail("Expected exception")
        except:
            pass

    def testGetTimeQueryPointResultsEmptyStagesFailure(self):
        try:
            self.model.GetAllTimeQueryPointResults(stages=[],
                                          vertical_axis=TimeQueryGraphEnums.VerticalAxisTypes.EFFECTIVE_STRESS_XX)
            self.fail("Expected exception")
        except:
            pass
    
    def testGetTimeQueryPointResultsNoneStagesFailure(self):
        try:
            self.model.GetAllTimeQueryPointResults(stages=[None, None, None],
                                          vertical_axis=TimeQueryGraphEnums.VerticalAxisTypes.EFFECTIVE_STRESS_XX)
            self.fail("Expected exception")
        except:
            pass
    
    def testGetTimeQueryPointResultsMinStagesFailure(self):
        try:
            self.model.GetAllTimeQueryPointResults(stages=[2, 3, 0],
                                          vertical_axis=TimeQueryGraphEnums.VerticalAxisTypes.EFFECTIVE_STRESS_XX)
            self.fail("Expected exception")
        except:
            pass

    def testGetTimeQueryPointResultsMaxStagesFailure(self):
        try:
            self.model.GetAllTimeQueryPointResults(stages=[2, 7],
                                          vertical_axis=TimeQueryGraphEnums.VerticalAxisTypes.EFFECTIVE_STRESS_XX)
            self.fail("Expected exception")
        except:
            pass

    # Time Query Line Results Test
    def testGetTimeQueryLineResultsSuccess(self):
        self.model.GetAllTimeQueryLinesResults(stages=[1, 2, 3, 4],
                                          vertical_axis=TimeQueryGraphEnums.VerticalAxisTypes.EFFECTIVE_STRESS_XX,
                                          apply_post_process_scaling=False)
    
    def testGetTimeQueryLineResultsApplyPostProcessSuccess(self):
        self.model.GetAllTimeQueryLinesResults(stages=[1, 2, 3, 4],
                                          vertical_axis=TimeQueryGraphEnums.VerticalAxisTypes.EFFECTIVE_STRESS_XX,
                                          apply_post_process_scaling=True)

    def testGetTimeQueryLineResultsWithoutQueriesFailure(self):
        try:
            self.modelWithoutTQ.GetAllTimeQueryLinesResults(stages=[1, 2, 3, 4],
                                          vertical_axis=TimeQueryGraphEnums.VerticalAxisTypes.EFFECTIVE_STRESS_XX,
                                          apply_post_process_scaling=False)
            self.fail("Expected exception")
        except:
            pass

    def testGetTimeQueryLineResultsInvalidVerticalAxisFailure(self):
        try:
            self.model.GetAllTimeQueryLinesResults(stages=[1, 2, 3, 4],
                                          vertical_axis=HistoryQueryGraphEnums.VerticalAxisTypes.EFFECTIVE_STRESS_XX,
                                          apply_post_process_scaling=False)
            self.fail("Expected exception")
        except:
            pass

    def testGetTimeQueryLineResultsEmptyStagesFailure(self):
        try:
            self.model.GetAllTimeQueryLinesResults(stages=[],
                                          vertical_axis=TimeQueryGraphEnums.VerticalAxisTypes.EFFECTIVE_STRESS_XX,
                                          apply_post_process_scaling=False)
            self.fail("Expected exception")
        except:
            pass
    
    def testGetTimeQueryLineResultsNoneStagesFailure(self):
        try:
            self.model.GetAllTimeQueryLinesResults(stages=[None, None],
                                          vertical_axis=TimeQueryGraphEnums.VerticalAxisTypes.EFFECTIVE_STRESS_XX,
                                          apply_post_process_scaling=False)
            self.fail("Expected exception")
        except:
            pass
    
    def testGetTimeQueryLineResultsMinStagesFailure(self):
        try:
            self.model.GetAllTimeQueryLinesResults(stages=[2, 0, 4],
                                          vertical_axis=TimeQueryGraphEnums.VerticalAxisTypes.EFFECTIVE_STRESS_XX,
                                          apply_post_process_scaling=False)
            self.fail("Expected exception")
        except:
            pass

    def testGetTimeQueryLineResultsMaxStagesFailure(self):
        try:
            self.model.GetAllTimeQueryLinesResults(stages=[1, 8, 3, 4],
                                          vertical_axis=TimeQueryGraphEnums.VerticalAxisTypes.EFFECTIVE_STRESS_XX,
                                          apply_post_process_scaling=False)
            self.fail("Expected exception")
        except:
            pass