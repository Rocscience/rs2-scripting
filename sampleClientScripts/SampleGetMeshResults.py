from rs2.RS2Interpreter import RS2Interpreter
from rs2.InterpreterPropertyEnums import *
from rs2.PropertyEnums import *

interpreter = RS2Interpreter()
model = interpreter.openFile("C:\scriptingModels\Profiles_and_Boreholes.fez")
interpreter.SetExportResultType(ExportResultType.SOLID_EFF_STRESS_SIGMA_Z_EFF)
exportResult1 = interpreter.GetMeshResults()
interpreter.SetUserDefinedExportResultType("Random")
exportResult2 = interpreter.GetMeshResults()

