from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.interpreter.InterpreterEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
RS2Modeler.startApplication(port=60056)
modeler = RS2Modeler(port=60056)
RS2Interpreter.startApplication(port=60057)
interpreter = RS2Interpreter(port=60057)

model = modeler.openFile(rf"{current_dir}\example_models\ExampleModel.fez")
model.compute()

interpretModel = interpreter.openFile(rf"{current_dir}\example_models\ExampleModel.fez")

interpretModel.SetResultType(ExportResultType.SOLID_EFFECTIVE_STRESS_EFFECTIVE_SIGMA_Z)
exportResult = interpretModel.GetMeshResults()

# Extracting results for specific vertex index
x_coord = exportResult.getXCoordinate(0)
y_coord = exportResult.getYCoordinate(0)
value = exportResult.getValue(0)

print(f"Vertex 0 : (x-coord, y-coord, result type value) = ({x_coord, y_coord, value})")

model.close()
interpretModel.close()
modeler.closeProgram()
interpreter.closeProgram()