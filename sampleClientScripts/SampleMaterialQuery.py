from rs2.RS2Interpreter import RS2Interpreter
from rs2.InterpreterEnums import *
from rs2.PropertyEnums import *

interpreter = RS2Interpreter()
model = interpreter.openFile("C:\scriptingModels\Profiles_and_Boreholes.fez")

# Add a material query point to model
pointID = model.AddMaterialQueryPoint(3.5, 4.5)
pointID2 = model.AddMaterialQueryPoint(3.5, 3.5)
pointID3 = model.AddMaterialQueryPoint(3.5, 2.5)
pointID4 = model.AddMaterialQueryPoint(3.5, 1.5)

# Add a material query line to model
points_making_line = [[4.5, 4.5], [-2.5, 4.5], [-2.5, 2.5], [-6, 2.5]]
lineID = model.AddMaterialQueryLine(points=points_making_line)

print("Unique Identifier for Point = ", pointID)
print("Unique Identifier for Line = ", lineID)

# Remove material query point from model
model.RemoveMaterialQuery(pointID)

# Set model stage to desired stage number
model.SetActiveStage(2)
# Get results for all material queries from model
results = model.GetMaterialQueryResults()
# Extracting data for all material queries from model
for mat_query_data in results:
    for node_value in mat_query_data:
        print("----------------------")
        material_id = node_value.GetMaterialID()
        x_coord = node_value.GetXCoordinate()
        y_coord = node_value.GetYCoordinate()
        distance = node_value.GetDistance()
        value = node_value.GetValue()
        print(material_id, x_coord, y_coord, distance, value)
    print("\n")