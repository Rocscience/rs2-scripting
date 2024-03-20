from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.interpreter.InterpreterGraphEnums import *
from pprint import pprint

modeler = RS2Modeler()
interpreter = RS2Interpreter()

filePath = r"C:\scriptingModels\Profiles_and_Boreholes.fez"
modeler_model = modeler.openFile(filePath)
interpreter_model = interpreter.openFile(filePath)

# Add a new history query point
modeler_model.AddHistoryQueryPoint(x=6.7654, y=-1.32, history_query_name="Test Point 1")
# Remove an existing history query point
modeler_model.RemoveHistoryQueryPoint(history_query_name="HQ 3")

# Getting history query results
hq_name = "HQ 1"
vertical_axis = HistoryQueryGraphEnums.VerticalAxisTypes.EFFECTIVE_STRESS_YY
horizontal_axis = HistoryQueryGraphEnums.HorizontalAxisTypes.STAGE_LOAD_PERCENTAGE
stages = [1, 2]

history_query_results = interpreter_model.GetHistoryQueryResults(hq_name=hq_name, 
                                                                 horizontal_axis=horizontal_axis, 
                                                                 vertical_axis=vertical_axis, 
                                                                 stages=stages)

# Extracting data
stage_number = 1
results_for_stage_1 = history_query_results[stage_number]

for data in results_for_stage_1:
    x_coord = data.GetXCoordinate()
    y_coord = data.GetYCoordinate()
    horizontal_result = data.GetHorizontalAxisResult()
    vertical_result = data.GetVerticalAxisResult()