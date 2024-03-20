from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.interpreter.InterpreterEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
interpreter = RS2Interpreter()
model = interpreter.openFile(rf"{current_dir}\example_models\ExampleModel.fez")

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
    print(f"Query Unique ID = {unique_ID}, MaterialID = {material_ID}")
    print("----------------")
    query_results = mat_query_data.GetAllValues()
    for result in query_results:
        x = result.GetXCoordinate()
        y = result.GetYCoordinate()
        distance = result.GetDistance()
        value = result.GetValue()
        print(f"X-Coord ={x}, Y-Coordinate = {y}, Distance = {distance}, Result Type Node Value = {value}")