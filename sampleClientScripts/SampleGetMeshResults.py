from rs2.RS2Interpreter import RS2Interpreter
from rs2.InterpreterPropertyEnums import *

interpreter = RS2Interpreter()
model = interpreter.openFile("C:\scriptingModels\Profiles_and_Boreholes.fez")
exportResult = interpreter.GetMeshResults(ExportResultType.SOLID_EFF_STRESS_SIGMA_THREE_EFF)
print("Total Data Points = ", len(exportResult))
model.close()

