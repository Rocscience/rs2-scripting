from rs2.modeler import properties
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties import *
from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.interpreter.InterpreterEnums import *
import os

modeler = RS2Modeler(port=60054)

path = r"C:\scriptingModels\HydroDistributionFunction.fez"
model = modeler.openFile(path)

material = model.getMaterialPropertyByName("Material 1")

fun1_name = "Function 1"
fun2_name = "Function 2"
fun1_new_name = "New Function 1"

hydro_var_1 = HydraulicVariableTypes.DOS_SAT_FUNCTION
hydro_type_1 = HydraulicDistributionTypes.VOLUMETRIC_STRAIN_DISTRIBUTION

model.createNewHydroDistributionFunction(hydro_var_1, hydro_type_1, fun1_name)
model.createNewHydroDistributionFunction(hydro_var_1, hydro_type_1, fun2_name)
assert len(model.getHydroDistributionFunctions(hydro_var_1, hydro_type_1)) == 2

fun1 = model.getHydroDistributionFunctionByName(hydro_var_1, hydro_type_1, fun1_name)
# Set the parameter values based on the hydro distribution
point_dos1 = [[0.1, 0.8], [0.3, 0.82], [0.5, 0.93]]
fun1.setPointsParameter(point_dos1)
assert fun1.getPointsParameter() == point_dos1

# Rename the function to a new name
model.renameHydroDistributionFunction(hydro_var_1, hydro_type_1, fun1_name, fun1_new_name)

fun2 = model.getHydroDistributionFunctionByName(hydro_var_1, hydro_type_1, fun2_name)
# Set the parameter values based on the hydro distribution
point_dos2 = [[0.1, 0.015], [0.3, 0.025], [0.5, 0.035]]
fun2.setPointsParameter(point_dos2)
assert fun2.getPointsParameter() == point_dos2

# Assign the new created hydro distribution function to Material 1
mh = material.Hydraulic.HydroDistribution
mh.setHydroDistribution(hydro_var_1, hydro_type_1, fun1_new_name)
assert mh.getHydroDistributionFunctionName(hydro_var_1) == fun1_new_name

# Apply Stage Hydraulic Properties and Stage Hydraulic Distribution
material.StageFactors.setStageHydraulicStageFactor(True)
material.StageFactors.setStageHydroDistributionStageFactor(True)
assert material.StageFactors.getStageHydroDistributionStageFactor() == True

# Define Stage Factors
definedStageFactors = material.StageFactors.getDefinedStageFactors()
stage_2 = 2
stage_4 = 4
# Create 2 stages with stage factor of initial values
newStageFactor_2 = material.StageFactors.createStageFactor(stage_2)
# Add Stage 2
definedStageFactors[stage_2] = newStageFactor_2
material.StageFactors.setDefinedStageFactors(definedStageFactors)

# Define stage factors at stage 2
feaGroundwaterStageFactor_2 = material.Hydraulic.FEAGroundwater.stageFactorInterface.getDefinedStageFactors()[stage_2]
hydroDistributionGroundwaterStageFactor_2 = material.Hydraulic.HydroDistribution.stageFactorInterface.getDefinedStageFactors()[stage_2]

# Switch stage hydraulic distribution function to a volumetric strain distribution
hydroDistributionGroundwaterStageFactor_2.setHydroDistributionStagedFunction(hydro_var_1, hydro_type_1, fun2_name)
hydroDistributionProp = hydroDistributionGroundwaterStageFactor_2.getHydroDistributionStagedFunction(hydro_var_1)
# Check assigned Hydraulic Distribution Type
assert hydroDistributionProp.distribution_type == hydro_type_1
# Check assigned Hydraulic Distribution Function Name
assert hydroDistributionProp.function_name == fun2_name

# Add a new stage 4
newStageFactor_4 = material.StageFactors.createStageFactor(stage_4)
definedStageFactors[stage_4] = newStageFactor_4
material.StageFactors.setDefinedStageFactors(definedStageFactors)

# Define stage factors at stage 4
feaGroundwaterStageFactor_4 = material.Hydraulic.FEAGroundwater.stageFactorInterface.getDefinedStageFactors()[stage_4]
hydroDistributionGroundwaterStageFactor_4 = material.Hydraulic.HydroDistribution.stageFactorInterface.getDefinedStageFactors()[stage_4]

# Get and Set Hydraulic Distribution Function in Stage Factor
hydroDistributionGroundwaterStageFactor_4.setHydroDistributionStagedFunction(hydro_var_1, hydro_type_1, fun1_new_name)
hydroDistributionProp = hydroDistributionGroundwaterStageFactor_4.getHydroDistributionStagedFunction(hydro_var_1)
# Check assigned Hydraulic Distribution Type
assert hydroDistributionProp.distribution_type == hydro_type_1
# Check assigned Hydraulic Distribution Function Name
assert hydroDistributionProp.function_name == fun1_new_name

variable_list = [HydraulicVariableTypes.KS_FUNCTION,
                 HydraulicVariableTypes.RELATIVE_KS_FUNCTION,
                 HydraulicVariableTypes.K2K1_FUNCTION,
                 HydraulicVariableTypes.K1_ANGLE_FUNCTION,
                 HydraulicVariableTypes.WC_SAT_FUNCTION,
                 HydraulicVariableTypes.WC_RES_FUNCTION,  
                 HydraulicVariableTypes.RELATIVE_WC_DOS_FUNCTION,
                 HydraulicVariableTypes.DOS_SAT_FUNCTION,
                 HydraulicVariableTypes.DOS_RES_FUNCTION,
                ]

print("Model 1")
for stage in [2, 4]:
    print("Stage", stage)
    for variable in variable_list:
        print(variable)
        print(material.Hydraulic.HydroDistribution.stageFactorInterface.getStageFactor(stage).getHydroDistributionStagedFunction(variable))
    print()


# Save model and run compute
model_path = r'C:\scriptingModels\post_HydroDistributionFunction.fez'
model.saveAs(model_path)
model.compute()


# ---------------------------------------- Interpreter ------------------------------------------

# Open Interpretor
interpreter = RS2Interpreter(port=60055)
interpretModel = interpreter.openFile(model_path)

# Add material query
pointID = interpretModel.AddMaterialQuery(points=[[3.3, -2.2]])
points_making_line = [[40.52, 4.5], [-10.23, 4.5], [-10.23, -40.892], [-37.723, -40.892]]
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


for stageNum in range(1, 4):
    print(f"Stage {stageNum} Results\n")
    # Show result at stage 1 to 3
    interpretModel.SetActiveStage(stageNum)

    # Compare results
    for seepageType in seepageTypes:
        interpretModel.SetResultType(seepageType)
        results = interpretModel.GetMaterialQueryResults()
        print(f"\nSeepage Result Type = {seepageType}")
        print("=============================================================")
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


# ---------------------------------------- Modeler ------------------------------------------

# Delete stage factors
stage_4 = 4
definedStageFactors.pop(stage_4)
material.StageFactors.setDefinedStageFactors(definedStageFactors)

# Apply Stage Hydraulic Properties and Stage Hydraulic Distribution
material.StageFactors.setStageHydroDistributionStageFactor(False)
assert material.StageFactors.getStageHydroDistributionStageFactor() == False

print("Model 2")
for stage in [2, 4]:
    print("Stage", stage)
    for variable in variable_list:
        print(variable)
        print(material.Hydraulic.HydroDistribution.stageFactorInterface.getStageFactor(stage).getHydroDistributionStagedFunction(variable))
    print()

# Set the constant value of the new constant distribution
constant_val = 0.1
hydro_type_2 = HydraulicDistributionTypes.CONSTANT_DISTRIBUTION
mh.setHydroDistribution(hydro_var_1, hydro_type_2, constant_val)
assert mh.getHydroDistribution(hydro_var_1) == hydro_type_2
assert mh.getHydroDistributionConstantVal(hydro_var_1) == constant_val

# Delete one of the new hydro distribution functions
model.deleteHydroDistributionFunction(hydro_var_1, hydro_type_1, fun2_name)
assert len(model.getHydroDistributionFunctions(hydro_var_1, hydro_type_1)) == 1
