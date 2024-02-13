from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\Profiles_and_Boreholes_2.fez")

# points1 = [[-12, -6], [-4, 5]]
# points2 = [[-2, -2], [2, 6]]
# points_on_line = 8
# guid1 = model.AddTimeQueryLine(points1, points_on_line)
# guid2 = model.AddTimeQueryLine(points2, points_on_line)
# print("Unique Identifer for Time Query Line = ", guid1)
# model.RemoveTimeQueryLine([guid1])

tq_point1 = [10, -2]
# id = model.AddTimeQueryPoint(10, -2)
# id2 = model.AddTimeQueryPoint(10, -2)
print("ID of new = ", id)
model.RemoveTimeQueryPoint([-5])
