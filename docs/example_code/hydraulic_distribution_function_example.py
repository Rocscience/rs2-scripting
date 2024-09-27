from tkinter import FIRST
from rs2.modeler import properties
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties import *
from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.interpreter.InterpreterEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 

RS2Modeler.startApplication(port=60093)
modeler = RS2Modeler(port=60093)
model_path = rf"{current_dir}\example_models\FEAGroundwater.fez"
model = modeler.openFile(model_path)

material = model.getMaterialPropertyByName("Dense Sand")

function_name_1 = "Example Function 1"
function_name_2 = "Function 1 New Name"

variable_type = HydraulicVariableTypes.KS_FUNC
distribution_type = HydraulicDistributionTypes.MEAN_STRESS_DIST

model.createNewHydroDistributionFunction(variable_type, distribution_type, function_name_1)
function1 = model.getHydroDistributionFunctionByName(variable_type, distribution_type, function_name_1)
point_ks1 = [[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]]
function1.setPointsParameter(point_ks1)
print(function_name_1)
current_points = function1.getPointsParameter()
print(current_points)

hydroDistribution = material.Hydraulic.HydroDistribution
hydroDistribution.setHydroDistribution(variable_type, distribution_type, function_name_1)
model.renameHydroDistributionFunction(variable_type, distribution_type, function_name_1, function_name_2)
current_function_name = hydroDistribution.getHydroDistributionFunctionName(variable_type)
print(f"The current function name of {variable_type} is {current_function_name}")

material.StageFactors.setStageHydraulicStageFactor(True)
material.StageFactors.setStageHydroDistributionStageFactor(True)

stage_2 = 2
definedStageFactors = material.StageFactors.getDefinedStageFactors()
newStageFactor_2 = material.StageFactors.createStageFactor(stage_2)
definedStageFactors[stage_2] = newStageFactor_2
material.StageFactors.setDefinedStageFactors(definedStageFactors)

hydroDistributionGroundwaterStageFactor_2 = material.Hydraulic.HydroDistribution.stageFactorInterface.getDefinedStageFactors()[stage_2]
hydroDistributionGroundwaterStageFactor_2.setHydroDistributionStagedFunction(variable_type, distribution_type, function_name_2)
hydroDistributionProp = hydroDistributionGroundwaterStageFactor_2.getHydroDistributionStagedFunction(variable_type)
print(f"The stage hydraulic distribution of {variable_type} at stage {stage_2} is {hydroDistributionProp[0]}")
print(f"The stage hydraulic distribution function of {variable_type} at stage {stage_2} is {hydroDistributionProp[1]}")

model.save()
model.compute()


RS2Interpreter.startApplication(port=60094)
interpreter = RS2Interpreter(port=60094)
interpretModel = interpreter.openFile(model_path)

points_making_line = [[-2, -1.5], [3, -1.5], [3, 2]]
lineID = interpretModel.AddMaterialQuery(points=points_making_line)

seepageTypes = [ExportResultType.SEEPAGE_HORIZONTAL_PERMEABILITY,
                ExportResultType.SEEPAGE_VERTICAL_PERMEABILITY,
                ExportResultType.SEEPAGE_SPATIAL_PERM,
                ExportResultType.SEEPAGE_SPATIAL_WC,
                ExportResultType.SEEPAGE_SPATIAL_WC_RES,
                ExportResultType.SEEPAGE_SPATIAL_CONDY,
                ExportResultType.SEEPAGE_SPATIAL_ANGLE,
                ]

first_stage = 1
last_stage = 4

for stageNum in range(first_stage, last_stage + 1):
    print(f"\n\nStage {stageNum} Results\n")
    interpretModel.SetActiveStage(stageNum)

    for seepageType in seepageTypes:
        interpretModel.SetResultType(seepageType)
        results = interpretModel.GetMaterialQueryResults()
        mat_query_data = results[0]
        print(f"\nSeepage Result Type = {seepageType}")
        print("==============================================================================")
        unique_ID = mat_query_data.GetUniqueIdentifier()
        material_ID = mat_query_data.GetMaterialID()
        print(f"\nQuery Unique ID = {unique_ID}, MaterialID = {material_ID}")
        print("------------------------------------------------------------------------------")
        query_results = mat_query_data.GetAllValues()
        for result in query_results:
            x = result.GetXCoordinate()
            y = result.GetYCoordinate()
            distance = result.GetDistance()
            value = result.GetValue()
            print(f"X-Coord ={x}, Y-Coordinate = {y}, Distance = {distance}, Result Type Node Value = {value}")


constant_val = 0.1
constant_distribution_type = HydraulicDistributionTypes.CONSTANT_DIST
hydroDistribution.setHydroDistribution(variable_type, constant_distribution_type, constant_val)
current_distribution = hydroDistribution.getHydroDistribution(variable_type)
current_val = hydroDistribution.getHydroDistributionConstantVal(variable_type)
print(f"The current hydraulic distribution of {variable_type} is {current_distribution}")
print(f"The current hydraulic distribution value of {variable_type} is {current_val}")

model.deleteHydroDistributionFunction(variable_type, distribution_type, function_name_2)






