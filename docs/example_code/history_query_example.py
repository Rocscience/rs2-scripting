from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.interpreter.InterpreterEnums import *
from rs2.interpreter.InterpreterGraphEnums import *

modeler = RS2Modeler()
interpreter = RS2Interpreter()
modelPath = r"S:\willSati\Scripting\TestModels\Profiles_and_Boreholes.fez"
modeler_model = modeler.openFile(modelPath)
interpreter_model = interpreter.openFile(modelPath)

# Add History Query Point in Modeler
modeler_model.AddHistoryQueryPoint(history_query_name="Testing Point 1", x=-3.1, y=2.8)
# Remove History Query Point in Modeler
modeler_model.RemoveHistoryQueryPoint("HQ 1")
# Get Results for a specific History Query Point in Interpreter
results = interpreter_model.GetHistoryQueryResults(hq_name="HQ 2", 
                                                   horizontal_axis=HistoryQueryGraphEnums.HorizontalAxisTypes.TIME,
                                                   vertical_axis=HistoryQueryGraphEnums.VerticalAxisTypes.EFFECTIVE_STRESS_YY, 
                                                   stages=[1, 2])

# Extracting data
stage_number = 1
results_for_stage_1 = results[stage_number]

for data in results_for_stage_1:
    x_coord = data.GetXCoordinate()
    y_coord = data.GetYCoordinate()
    horizontal_result = data.GetHorizontalAxisResult()
    vertical_result = data.GetVerticalAxisResult()