from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.interpreter.InterpreterEnums import *

interpreter = RS2Interpreter()
model = interpreter.openFile(r"C:\scriptingModels\Profiles_and_Boreholes.fez")

# Add a material query point to model
pointID = model.AddMaterialQuery([[3.5, 4.5]])
pointID2 = model.AddMaterialQuery([[3.5, 3.5]])
pointID3 = model.AddMaterialQuery([[3.5, 2.5]])
pointID4 = model.AddMaterialQuery([[3.5, 1.5]])

# Add a material query line to model
points_making_line = [[0, -1], [0, -4]]
points_making_line2 = [[-2, -4], [-2, -1]]
lineID = model.AddMaterialQuery(points=points_making_line)
line2 = model.AddMaterialQuery(points_making_line2)

print("Unique Identifier for Point = ", pointID)
print("Unique Identifier for Line = ", lineID)

# Remove material query point from model
model.RemoveMaterialQuery([pointID])

# Set model stage to desired stage number
model.SetActiveStage(2)
# Get results for all material queries from model
results = model.GetMaterialQueryResults()
print("LEN OF RESULTS", len(results))
# Extracting data for all material queries from model
for mat_query_data in results:
    unique_ID = mat_query_data.GetUniqueIdentifier()
    material_ID = mat_query_data.GetMaterialID()
    print(unique_ID, material_ID)
    print("----------------")
    query_results = mat_query_data.GetAllValues()
    for result in query_results:
        x = result.GetXCoordinate()
        y = result.GetYCoordinate()
        distance = result.GetDistance()
        value = result.GetValue()
        print(x, y, distance, value)
    print()