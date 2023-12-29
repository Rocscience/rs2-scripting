from rs2.RS2Interpreter import RS2Interpreter
from rs2.InterpreterPropertyEnums import *

interpreter = RS2Interpreter()
model = interpreter.openFile("S:\willSati\Scripting\TestModels\Profiles_and_Boreholes.fez")

model.SetExportResultType(ExportResultType.SOLID_EFF_STRESS_SIGMA_Z_EFF)
exportResult1 = model.GetMeshResults()
model.SetUserDefinedExportResultType("Keff")
exportResult2 = model.GetMeshResults()

model.close()

