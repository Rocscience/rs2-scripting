from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.interpreter.InterpreterEnums import *
from rs2.modeler.properties.PropertyEnums import *

interpreter = RS2Interpreter()
model = interpreter.openFile(r"S:\willSati\Scripting\TestModels\Profiles_and_Boreholes.fez")
model.SetResultType(ExportResultType.SOLID_DISPLACEMENT_HORIZONTAL_DISPLACEMENT)
results = model.GetMeshResults()

x_coord = results.getXCoordinate(0)
y_coord = results.getYCoordiante(0)
value = results.getValue(0)

print(x_coord, y_coord, value)
