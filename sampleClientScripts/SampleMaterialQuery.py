from rs2.RS2Interpreter import RS2Interpreter
from rs2.InterpreterEnums import *
from rs2.PropertyEnums import *

interpreter = RS2Interpreter()
model = interpreter.openFile("C:\scriptingModels\Profiles_and_Boreholes.fez")

# Add a material query point to model
pointID = model.AddMaterialQueryPoint(5.5, 5.5)
# Add a material query line to model
points_making_line = [[4.5, 4.5], [-2.5, 4.5], [-2.5, 2.5], [-6, 2.5]]
lineID = model.AddMaterialQueryLine(points=points_making_line)

print("Unique Identifier for Point = ", pointID)
print("Unique Identifier for Line = ", lineID)

# Remove material query point from model
model.RemoveMaterialQuery(pointID)

# Get results for all material queries from model
results = model.GetMaterialQueryResults(stages=[1, 2])
# Extracting data for all material queries from model
stage_number = 1
results_for_stage_1 = results[stage_number]

for stage_data in results.values():
    for mat_query_data in stage_data:
        for node_value in mat_query_data:
            print("----------------------")
            material_id = node_value.GetMaterialID()
            x_coord = node_value.GetXCoordinate()
            y_coord = node_value.GetYCoordinate()
            distance = node_value.GetDistance()
            value = node_value.GetValue()
            stats_base = node_value.GetBaseStats()
            stats_mean = node_value.GetMeanStats()
            stats_stddv = node_value.GetStandardDeviationStats()
            stats_cov = node_value.GetCovarianceStats()
            print(material_id, x_coord, y_coord, distance, value)
        print("END OF MATERIAL DATA\n")
    print("END OF STAGE DATA\n")

    

