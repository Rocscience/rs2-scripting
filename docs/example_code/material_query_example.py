from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.interpreter.InterpreterEnums import *

interpreter = RS2Interpreter()

model = interpreter.openFile(r"S:\willSati\Scripting\TestModels\Profiles_and_Boreholes.fez")

# Add a material query point to model
pointID = model.AddMaterialQuery(points=[[3.3, -2.2]])

# Add a material query line to model
points_making_line = [[4.5, 4.5], [-2.5, 4.5], [-2.5, 2.5], [-6, 2.5]]
lineID = model.AddMaterialQuery(points=points_making_line)

# Remove Material Query Point in Modeler
model.RemoveMaterialQuery([pointID])

# Set model stage to desired stage number
model.SetActiveStage(2)

# Get results for all material queries defined in your model
results = model.GetMaterialQueryResults()
# Extracting data for all material queries from model
for mat_query_data in results:
    unique_ID = mat_query_data.GetUniqueIdentifier()
    material_ID = mat_query_data.GetMaterialID()
    print(unique_ID, material_ID)
    print("----------------")
    query_results = mat_query_data.GetAllValues()
    for result in query_results:
        print(type(result))
        x = result.GetXCoordinate()
        y = result.GetYCoordinate()
        distance = result.GetDistance()
        value = result.GetValue()
        print(x, y, distance, value)
    print()