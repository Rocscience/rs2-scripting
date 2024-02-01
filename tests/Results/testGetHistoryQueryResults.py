import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Interpreter import RS2Interpreter
from rs2.InterpreterGraphEnums import *
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestGetHistoryQueryResults(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/example_computed_model.fez"
        modelWithoutHQPath = f"{parentDirectory}/resources/modelWithoutHistoryQuery.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        self.modelWithoutHQPath = f"{parentDirectory}/resources/testInvalidMeshModel.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        shutil.copy(modelWithoutHQPath, self.modelWithoutHQPath)
        self.interpreter = RS2Interpreter()
        self.model = self.interpreter.openFile(self.copiedModelPath)
        self.modelWithoutHQ = self.interpreter.openFile(self.modelWithoutHQPath)
    def tearDown(self):
        self.model.close()
        self.modelWithoutHQ.close()
        os.remove(self.copiedModelPath)
        os.remove(self.modelWithoutHQPath)
        self.model._client.closeConnection()
        self.modelWithoutHQ._client.closeConnection()

    def testGetHistoryQueryResultsSuccess(self):
        self.model.GetHistoryQueryResults(hq_name="HQ 1", horizontal_axis=HistoryQueryGraphEnums.HorizontalAxisTypes.TIME,
                                          vertical_axis=HistoryQueryGraphEnums.VerticalAxisTypes.HORIZONTAL_DISPLACEMENT, stages=[1, 2])
    
    def testGetHistoryQueryResultsAnyStagesOrderSuccess(self):
        result1 = self.model.GetHistoryQueryResults(hq_name="HQ 1", horizontal_axis=HistoryQueryGraphEnums.HorizontalAxisTypes.TIME,
                                          vertical_axis=HistoryQueryGraphEnums.VerticalAxisTypes.HORIZONTAL_DISPLACEMENT, stages=[1, 2])
        result2 = self.model.GetHistoryQueryResults(hq_name="HQ 1", horizontal_axis=HistoryQueryGraphEnums.HorizontalAxisTypes.TIME,
                                          vertical_axis=HistoryQueryGraphEnums.VerticalAxisTypes.HORIZONTAL_DISPLACEMENT, stages=[2, 1])
        structured_result_1, structured_result_2 = [], []

        for _, stage_data_lst in result1.items():
            for data in stage_data_lst:
                structured_result_1.append([data.GetXCoordinate(), data.GetYCoordinate(), data.GetHorizontalAxisResult(),
                                           data.GetVerticalAxisResult()])
        
        for _, stage_data_lst in result2.items():
            for data in stage_data_lst:
                structured_result_2.append([data.GetXCoordinate(), data.GetYCoordinate(), data.GetHorizontalAxisResult(),
                                           data.GetVerticalAxisResult()])
        
        self.assertEqual(structured_result_1, structured_result_2)

    def testGetHistoryQueryResultsWithoutQueriesFailure(self):
        try:
            self.modelWithoutHQ.GetHistoryQueryResults(hq_name="HQ 1", horizontal_axis=HistoryQueryGraphEnums.HorizontalAxisTypes.TIME,
                                          vertical_axis=HistoryQueryGraphEnums.VerticalAxisTypes.HORIZONTAL_DISPLACEMENT, stages=[1, 2])
            self.fail("Expected exception")
        except:
            pass

    def testGetHistoryQueryResultsInvalidHorizontalAxisFailure(self):
        try:
            self.modelWithoutHQ.GetHistoryQueryResults(hq_name="HQ 1", horizontal_axis=CompositeJointPlacementTypes.BETWEEN_FIRST_AND_SECOND_LINER,
                                          vertical_axis=HistoryQueryGraphEnums.VerticalAxisTypes.HORIZONTAL_DISPLACEMENT, stages=[1, 2])
            self.fail("Expected exception")
        except:
            pass

    def testGetHistoryQueryResultsInvalidVerticalAxisFailure(self):
        try:
            self.modelWithoutHQ.GetHistoryQueryResults(hq_name="HQ 1", horizontal_axis=HistoryQueryGraphEnums.HorizontalAxisTypes.STAGE_LOAD_PERCENTAGE,
                                          vertical_axis=HistoryQueryGraphEnums.VerticalAxisTypes.HORIZONTAL_THERMAL_GRADIENT, stages=[1, 2])
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
            self.model.GetHistoryQueryResults(hq_name="HQ 1", horizontal_axis=HistoryQueryGraphEnums.HorizontalAxisTypes.TIME,
                                          vertical_axis=HistoryQueryGraphEnums.VerticalAxisTypes.HORIZONTAL_DISPLACEMENT, stages=[])
            self.fail("Expected exception")
        except:
            pass
    
    def testGetHistoryQueryResultsMinStagesFailure(self):
        try:
            self.model.GetHistoryQueryResults(hq_name="HQ 1", horizontal_axis=HistoryQueryGraphEnums.HorizontalAxisTypes.TIME,
                                          vertical_axis=HistoryQueryGraphEnums.VerticalAxisTypes.HORIZONTAL_DISPLACEMENT, stages=[-1, 3])
            self.fail("Expected exception")
        except:
            pass

    def testGetHistoryQueryResultsMaxStagesFailure(self):
        try:
            self.model.GetHistoryQueryResults(hq_name="HQ 1", horizontal_axis=HistoryQueryGraphEnums.HorizontalAxisTypes.TIME,
                                          vertical_axis=HistoryQueryGraphEnums.VerticalAxisTypes.HORIZONTAL_DISPLACEMENT, stages=[1, 800])
            self.fail("Expected exception")
        except:
            pass