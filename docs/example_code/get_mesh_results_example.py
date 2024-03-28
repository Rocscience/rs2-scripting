from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.interpreter.InterpreterEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
interpreter = RS2Interpreter()
model = interpreter.openFile(rf"{current_dir}\example_models\ExampleModel.fez")

model.SetResultType(ExportResultType.SOLID_EFFECTIVE_STRESS_EFFECTIVE_SIGMA_Z)
exportResult1 = model.GetMeshResults()

# Extracting results for specific vertex index
x_coord = exportResult1.getXCoordinate(0)
y_coord = exportResult1.getYCoordinate(0)
value = exportResult1.getValue(0)

model.close()