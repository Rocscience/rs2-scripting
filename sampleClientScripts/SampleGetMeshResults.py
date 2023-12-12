from rs2.RS2Interpreter import RS2Interpreter
from rs2.generatedInterpreterClientScripts.PropertyEnums import *
from rs2.PropertyEnums import *

interpreter = RS2Interpreter()
# model = interpreter.openFile("C:\scriptingModels\Profiles_and_Boreholes.fez")
# model.close()
exportResult = interpreter.getMeshResults(ExportResultType.SOLID_EFF_STRESS_SIGMA_THREE_EFF)
print("Total Data Points = ", len(exportResult))

