from rs2.modeler import properties
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties import *
from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.interpreter.InterpreterEnums import *
import os

starting_stage = 1
end_stage = 2


modeler = RS2Modeler(port=60054)

path = r"C:\scriptingModels\HydroDistributionFunction.fez"
txt_path = r"C:\scriptingModels\HydroDistributionFunction.txt"
model = modeler.openFile(path)

# Save model and run compute
model.save()
model.compute()


# ---------------------------------------- Interpreter ------------------------------------------

# Open Interpretor
interpreter = RS2Interpreter(port=60055)
interpretModel = interpreter.openFile(path)

# Add material query
points_making_line = [[0.5, -9.2], [0.5, -7.2], [0.5, -5.5], [0.5, -3.5], [0.5,-1.5]]
lineID = interpretModel.AddMaterialQuery(points=points_making_line)

# # Access Spatial Distribution Results
seepageTypes = [ExportResultType.SEEPAGE_HORIZONTAL_PERMEABILITY,
                ExportResultType.SEEPAGE_VERTICAL_PERMEABILITY,
                ExportResultType.SEEPAGE_SPATIAL_PERM,
                ExportResultType.SEEPAGE_SPATIAL_WC,
                ExportResultType.SEEPAGE_SPATIAL_WC_RES,
                ExportResultType.SEEPAGE_SPATIAL_CONDY,
                ExportResultType.SEEPAGE_SPATIAL_ANGLE,
                ]


data = []
# Compare results
for seepageType in seepageTypes:
    interpretModel.SetResultType(seepageType)
    for stageNum in range(starting_stage, end_stage+1):
        data.append(f"\n{seepageType}")
        data.append("\tStage \tStages \tMaterial_Query_ID \tPoint_x \tPoint_y \tDistance \tValue")
        interpretModel.SetActiveStage(stageNum)
        results = interpretModel.GetMaterialQueryResults()
        for mat_query_data in results:
            # unique_ID = mat_query_data.GetUniqueIdentifier()
            unique_ID = 1
            material_ID = mat_query_data.GetMaterialID()
            query_results = mat_query_data.GetAllValues()
            for result in query_results:
                x = result.GetXCoordinate()
                y = result.GetYCoordinate()
                distance = result.GetDistance()
                value = result.GetValue()
                data.append(f"\t{stageNum} \t{end_stage} \t{unique_ID} \t{x} \t{y} \t{distance} \t{value}")

with open(txt_path, "w") as file:
    for line in data:
        file.write(line + "\n")