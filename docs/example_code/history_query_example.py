from rs2.RS2Modeler import RS2Modeler
from rs2.RS2Interpreter import RS2Interpreter
from rs2.InterpreterEnums import *
from rs2.InterpreterGraphEnums import *

modeler = RS2Modeler()
interpreter = RS2Interpreter()

modeler_model = modeler.openFile("S:\willSati\Scripting\TestModels\Profiles_and_Boreholes.fez")
interpreter_model = interpreter.openFile("S:\willSati\Scripting\TestModels\Profiles_and_Boreholes.fez")

# Add History Query Point in Modeler
modeler_model.AddHistoryQueryPoint(history_query_name="Example Point 1", x=-1.1, y=3.8)
# Remove History Query Point in Modeler
modeler_model.RemoveHistoryQueryPoint("HQ 1")
# Get Results for a specific History Query Point in Interpreter
results = interpreter_model.GetHistoryQueryResults(hq_name="HQ 2", horizontal_axis=HistoryQueryGraphEnums.HorizontalAxisTypes.TIME,
                                                   vertical_axis=HistoryQueryGraphEnums.VerticalAxisTypes.EFFECTIVE_STRESS_YY, stages=[1, 2])