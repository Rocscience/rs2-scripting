import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Interpreter import RS2Interpreter
from rs2.InterpreterGraphEnums import *
from rs2.PropertyEnums import*
import time

parentDirectoryHelper.addParentDirectoryToPath()

class TestAddHistoryQuery(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/example_computed_model.fez"
        invalidModelPath = f"{parentDirectory}/resources/modelWithoutHistoryQuery.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        self.invalidModelMeshPath = f"{parentDirectory}/resources/testInvalidMeshModel.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        shutil.copy(invalidModelPath, self.invalidModelMeshPath)
        self.interpreter = RS2Interpreter()
        self.model = self.interpreter.openFile(self.copiedModelPath)
        self.invalidModel = self.interpreter.openFile(self.invalidModelMeshPath)
    def tearDown(self):
        self.model.close()
        self.invalidModel.close()
        os.remove(self.copiedModelPath)
        self.model._client.closeConnection()
        os.remove(self.invalidModelMeshPath)

    
    def testGetHistoryQueryResultsSuccess(self):
        self.model.GetHistoryQueryResults(hq_name="HQ 1", horizontal_axis=HistoryQueryGraphEnums.HorizontalAxisTypes.TIME,
                                          vertical_axis=HistoryQueryGraphEnums.VerticalAxisTypes.HORIZONTAL_DISPLACEMENT, stages=[1, 2])

    def testGetHistoryQueryResultsWithoutQueriesFailure(self):
        try:
            self.invalidModel.GetHistoryQueryResults(hq_name="HQ 1", horizontal_axis=HistoryQueryGraphEnums.HorizontalAxisTypes.TIME,
                                          vertical_axis=HistoryQueryGraphEnums.VerticalAxisTypes.HORIZONTAL_DISPLACEMENT, stages=[1, 2])
            self.fail("Expected exception")
        except:
            pass

    def testGetHistoryQueryResultsEmptyLabelNameFailure(self):
        try:
            self.model.GetHistoryQueryResults(hq_name="", horizontal_axis=HistoryQueryGraphEnums.HorizontalAxisTypes.TIME,
                                          vertical_axis=HistoryQueryGraphEnums.VerticalAxisTypes.HORIZONTAL_DISPLACEMENT, stages=[1, 2])
            self.fail("Expected exception")
        except:
            pass

    def testGetHistoryQueryResultsInvalidLabelNameFailure(self):
        try:
            self.model.GetHistoryQueryResults(hq_name="NonExistantLabelName", horizontal_axis=HistoryQueryGraphEnums.HorizontalAxisTypes.TIME,
                                          vertical_axis=HistoryQueryGraphEnums.VerticalAxisTypes.HORIZONTAL_DISPLACEMENT, stages=[1, 2])
            self.fail("Expected exception")
        except:
            pass

    def testGetHistoryQueryResultsEmptyStagesFailure(self):
        try:
            self.model.GetHistoryQueryResults(hq_name="New Label 1", horizontal_axis=HistoryQueryGraphEnums.HorizontalAxisTypes.TIME,
                                          vertical_axis=HistoryQueryGraphEnums.VerticalAxisTypes.HORIZONTAL_DISPLACEMENT, stages=[])
            self.fail("Expected exception")
        except:
            pass
    
    def testGetHistoryQueryResultsMinStagesFailure(self):
        try:
            self.model.GetHistoryQueryResults(hq_name="New Label 1", horizontal_axis=HistoryQueryGraphEnums.HorizontalAxisTypes.TIME,
                                          vertical_axis=HistoryQueryGraphEnums.VerticalAxisTypes.HORIZONTAL_DISPLACEMENT, stages=[-1, 3])
            self.fail("Expected exception")
        except:
            pass

    def testGetHistoryQueryResultsMaxStagesFailure(self):
        try:
            self.model.GetHistoryQueryResults(hq_name="New Label 1", horizontal_axis=HistoryQueryGraphEnums.HorizontalAxisTypes.TIME,
                                          vertical_axis=HistoryQueryGraphEnums.VerticalAxisTypes.HORIZONTAL_DISPLACEMENT, stages=[1, 800])
            self.fail("Expected exception")
        except:
            pass