from rs2.RS2Interpreter import RS2Interpreter
from rs2.InterpreterPropertyEnums import *
from rs2.PropertyEnums import *

interpreter = RS2Interpreter()
model = interpreter.openFile("C:\scriptingModels\Profiles_and_Boreholes.fez")
model.SetExportResultType(ExportResultType.HORIZONTAL_DISPLACEMENT_ABS)
exportResult1 = model.GetMeshResults()

