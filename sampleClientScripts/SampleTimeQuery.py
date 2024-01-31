from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\Profiles_and_Boreholes.fez")

points = [[2.2, 0], [2.2, -2]]
points_on_line = 5
guid = model.AddTimeQueryLine(points, points_on_line)
print("Unique Identifer for Time Query Line = ", guid)
