from rs2.RS2Interpreter import RS2Interpreter
from rs2.InterpreterPropertyEnums import *

interpreter = RS2Interpreter()

model = interpreter.openFile(r"C:\scriptingModels\Profiles_and_Boreholes.fez")
result = interpreter.GetMeshResults(ExportResultType.MEAN_PRINCIPAL_PLASTIC_STRAIN)
model.close()

