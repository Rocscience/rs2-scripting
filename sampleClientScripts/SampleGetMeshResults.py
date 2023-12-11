from rs2.RS2Interpreter import RS2Interpreter
from rs2.generatedInterpreterClientScripts.PropertyEnums import *

interpreter = RS2Interpreter()

exportResult = interpreter.getMeshResults(ExportResultType.HORIZONTAL_DISPLACEMENT.value)
print("Length = ", len(exportResult))

