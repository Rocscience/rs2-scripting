from rs2.RS2Interpreter import RS2Interpreter
from rs2.InterpreterEnums import *
from rs2.PropertyEnums import *

interpreter = RS2Interpreter()
model = interpreter.openFile("S:\willSati\Scripting\TestModels\Profiles_and_Boreholes.fez")
model.SetResultType(ExportResultType.SOLID_DISPLACEMENT_HORIZONTAL_DISPLACEMENT)
exportResult1 = model.GetMeshResults()

