from rs2.RS2Interpreter import RS2Interpreter
from rs2.InterpreterEnums import *

interpreter = RS2Interpreter()

model = interpreter.openFile("S:\willSati\Scripting\TestModels\Profiles_and_Boreholes.fez")

# Add a material query point to model
pointID = model.AddMaterialQueryPoint(5.5, 5.5)

# Add a material query line to model
points_making_line = [[4.5, 4.5], [-2.5, 4.5], [-2.5, 2.5], [-6, 2.5]]
lineID = model.AddMaterialQueryLine(points=points_making_line)

# Remove Material Query Point in Modeler
model.RemoveMaterialQuery(pointID)

# Set model stage to desired stage number
model.ChangeModelStageReference(2)

# Get results for all material queries defined in your model
results = model.GetMaterialQueryResults()
# Extracting data for all material queries
for mat_query_data in results:
    for node_value in mat_query_data:
        material_id = node_value.GetMaterialID()
        x_coord = node_value.GetXCoordinate()
        y_coord = node_value.GetYCoordinate()
        distance = node_value.GetDistance()
        value = node_value.GetValue()
        print(material_id, x_coord, y_coord, distance, value)
    print("\n\n")