from rs2.RS2Interpreter import RS2Interpreter
from rs2.InterpreterEnums import *

interpreter = RS2Interpreter()
model = interpreter.openFile("S:\willSati\Scripting\TestModels\Profiles_and_Boreholes.fez")

# Setting and Retrieving results for built-in type
model.SetResultType(ExportResultType.SOLID_EFFECTIVE_STRESS_EFFECTIVE_SIGMA_Z)
exportResult1 = model.GetMeshResults()
# Setting and Retrieving results for user-defined type
model.SetUserDefinedResultType("Sin(dy)")
exportResult2 = model.GetMeshResults()

# Extracting results for specific vertex
x_coord = exportResult1.getXCoordinate(0)
y_coord = exportResult1.getYCoordiante(0)
value = exportResult1.getValue(0)
