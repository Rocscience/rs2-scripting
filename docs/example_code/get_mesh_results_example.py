from rs2.RS2Interpreter import RS2Interpreter
from rs2.InterpreterEnums import *

interpreter = RS2Interpreter()
model = interpreter.openFile("S:\willSati\Scripting\TestModels\Profiles_and_Boreholes.fez")

model.SetResultType(ExportResultType.SOLID_EFFECTIVE_STRESS_EFFECTIVE_SIGMA_Z)
exportResult1 = model.GetMeshResults()
model.SetUserDefinedResultType("Sin(dy)")
exportResult2 = model.GetMeshResults()

