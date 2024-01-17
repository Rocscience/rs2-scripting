from rs2.RS2Interpreter import RS2Interpreter
from rs2.InterpreterEnums import *
from rs2.PropertyEnums import *

interpreter = RS2Interpreter()
model = interpreter.openFile("C:\scriptingModels\Profiles_and_Boreholes.fez")
pointID = model.AddMaterialQueryPoint(5.5, 5.5)

points_making_line = [[4.5, 4.5], [-2.5, 4.5], [-2.5, 2.5], [-6, 2.5]]
lineID = model.AddMaterialQueryLine(points=points_making_line)

print("Unique Identifier for Point = ", pointID)
print("Unique Identifier for Line = ", lineID)

model.RemoveMaterialQueryPoint(lineID)

