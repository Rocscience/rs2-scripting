from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.interpreter.InterpreterEnums import *
from rs2.interpreter.InterpreterGraphEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
RS2Modeler.startApplication(port=60058)
modeler = RS2Modeler(port=60058)
RS2Interpreter.startApplication(port=60059)
interpreter = RS2Interpreter(port=60059)
modelPath = rf"{current_dir}\example_models\ExampleModel.fez"
modeler_model = modeler.openFile(modelPath)

modeler_model.AddHistoryQueryPoint(history_query_name="Testing Point 1", x=-3.1, y=2.8)

modeler_model.RemoveHistoryQueryPoint("HQ 1")

interpreter_model = interpreter.openFile(modelPath)
results = interpreter_model.GetHistoryQueryResults(hq_name="HQ 2", 
                                                   horizontal_axis=HistoryQueryGraphEnums.HorizontalAxisTypes.TIME,
                                                   vertical_axis=HistoryQueryGraphEnums.VerticalAxisTypes.EFFECTIVE_STRESS_YY, 
                                                   stages=[1, 2])

stage_number = 1
results_for_stage_1 = results[stage_number]

for data in results_for_stage_1:
    x_coord = data.GetXCoordinate()
    y_coord = data.GetYCoordinate()
    horizontal_result = data.GetHorizontalAxisResult()
    vertical_result = data.GetVerticalAxisResult()

modeler_model.close()
interpreter_model.close()
modeler.closeProgram()
interpreter.closeProgram()