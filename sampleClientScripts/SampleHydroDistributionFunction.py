from rs2.modeler import properties
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties import *
from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.interpreter.InterpreterEnums import *
import os

modeler = RS2Modeler(port=60054)

path = r"C:\Users\GraceHu\Documents\interpreter_dummy_model.fez"
model = modeler.openFile(path)

material = model.getMaterialPropertyByName("Material 1")

fun1_name = "Function 1"
fun2_name = "New Function 2"
fun3_name = "Dummy Function"
fun4_name = "Dummy Function 2"

hydro_var_1 = HydraulicVariableTypes.KS_FUNC
hydro_var_2 = HydraulicVariableTypes.K2K1_FUNC
hydro_var_3 = HydraulicVariableTypes.K1_ANGLE_FUNC
hydro_var_4 = HydraulicVariableTypes.WC_SAT_FUNC
hydro_var_5 = HydraulicVariableTypes.WC_RES_FUNC
hydro_var_6 = HydraulicVariableTypes.DOS_SAT_FUNC
hydro_var_7 = HydraulicVariableTypes.DOS_RES_FUNC
hydro_var_8 = HydraulicVariableTypes.RELATIVE_KS_FUNC
hydro_var_9 = HydraulicVariableTypes.RELATIVE_WC_FUNC
hydro_type_1 = HydraulicDistributionTypes.MEAN_STRESS_DIST
hydro_type_2 = HydraulicDistributionTypes.COORDINATE_DIST
hydro_type_3 = HydraulicDistributionTypes.CONSTANT_DIST
hydro_type_4 = HydraulicDistributionTypes.HORIZONTAL_STRESS_DIST
hydro_type_5 = HydraulicDistributionTypes.VERTICAL_STRESS_DIST
hydro_type_6 = HydraulicDistributionTypes.VOLUMETRIC_STRAIN_DIST

# Create 2 new hydro distribution functions
model.createNewHydroDistributionFunction(hydro_var_1, hydro_type_1, fun1_name)
model.createNewHydroDistributionFunction(hydro_var_1, hydro_type_2, fun1_name)
model.createNewHydroDistributionFunction(hydro_var_2, hydro_type_4, fun3_name)
model.createNewHydroDistributionFunction(hydro_var_3, hydro_type_5, fun3_name)
model.createNewHydroDistributionFunction(hydro_var_4, hydro_type_6, fun3_name)
model.createNewHydroDistributionFunction(hydro_var_5, hydro_type_2, fun4_name)
model.createNewHydroDistributionFunction(hydro_var_6, hydro_type_5, fun4_name)
model.createNewHydroDistributionFunction(hydro_var_7, hydro_type_6, fun4_name)
model.createNewHydroDistributionFunction(hydro_var_8, hydro_type_4, fun4_name)
model.createNewHydroDistributionFunction(hydro_var_9, hydro_type_1, fun4_name)
# Check the list of available function for each variable
assert len(model.getHydroDistributionFunctions(hydro_var_1, hydro_type_1)) == 1
assert len(model.getHydroDistributionFunctions(hydro_var_1, hydro_type_2)) == 1

fun1 = model.getHydroDistributionFunctionByName(hydro_var_1, hydro_type_1, fun1_name)
# Set the parameter values based on the hydro distribution
point_ks1 = [[0.1, 12.2], [0.3, 14.4], [0.5, 14.6]]
fun1.setPointsParameter(point_ks1)
assert fun1.getPointsParameter() == point_ks1

# Rename the function to a new name
model.renameHydroDistributionFunction(hydro_var_1, hydro_type_2, fun1_name, fun2_name)

fun2 = model.getHydroDistributionFunctionByName(hydro_var_1, hydro_type_2, fun2_name)
# Set the parameter values based on the hydro distribution
point_ks2 = [[1.123, 2.123, 3.123], [2.234, 3.235, 4.456], [3.324, 1.256, 3.456]]
fun2.setPointsParameter(point_ks2)
assert fun2.getPointsParameter() == point_ks2

# Assign the new created hydro distribution function to Material 1
mh = material.Hydraulic.HydroDistribution
mh.setHydroDistribution(hydro_var_1, hydro_type_2, fun2_name)
assert mh.getHydroDistributionFunctionName(hydro_var_1) == fun2_name

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
# Add Stage 1
definedStageFactors[stage_2] = newStageFactor_2
material.StageFactors.setDefinedStageFactors(definedStageFactors)

# Define stage factors at stage 1
feaGroundwaterStageFactor_2 = material.Hydraulic.FEAGroundwater.stageFactorInterface.getDefinedStageFactors()[stage_2]
hydroDistributionGroundwaterStageFactor_2 = material.Hydraulic.HydroDistribution.stageFactorInterface.getDefinedStageFactors()[stage_2]

# Set stage factors for different parameters
feaGroundwaterStageFactor_2.setK1AngleFactor(0.5)

fun3 = model.getHydroDistributionFunctionByName(hydro_var_4, hydro_type_6, fun3_name)
# Set the parameter values based on the hydro distribution
point_wc_sat3 = [[1.123, 0.01], [2.234, 0.05], [3.324, 0.15]]
fun3.setPointsParameter(point_wc_sat3)
assert fun3.getPointsParameter() == point_wc_sat3

# Switch stage hydraulic distribution function to a volumetric strain distribution
hydroDistributionGroundwaterStageFactor_2.setHydroDistributionStagedFunction(hydro_var_4, hydro_type_6, fun3_name)
hydroDistributionProp = hydroDistributionGroundwaterStageFactor_2.getHydroDistributionStagedFunction(hydro_var_4)
# Check assigned Hydraulic Distribution Type
assert hydroDistributionProp[0] == hydro_type_6
# Check assigned Hydraulic Distribution Function Name
assert hydroDistributionProp[1] == fun3_name

fun4 = model.getHydroDistributionFunctionByName(hydro_var_1, hydro_type_1, fun1_name)
# Set the parameter values based on the hydro distribution
point_ks4 = [[1.123, 1.23], [2.234, 2.34], [3.324, 3.45]]
fun4.setPointsParameter(point_ks4)
assert fun4.getPointsParameter() == point_ks4

# Get and Set Hydraulic Distribution Function in Stage Factor
hydroDistributionGroundwaterStageFactor_2.setHydroDistributionStagedFunction(hydro_var_1, hydro_type_1, fun1_name)
hydroDistributionProp = hydroDistributionGroundwaterStageFactor_2.getHydroDistributionStagedFunction(hydro_var_1)
# Check assigned Hydraulic Distribution Type
assert hydroDistributionProp[0] == hydro_type_1
# Check assigned Hydraulic Distribution Function Name
assert hydroDistributionProp[1] == fun1_name

# Add a new stage 4
newStageFactor_4 = material.StageFactors.createStageFactor(stage_4)
definedStageFactors[stage_4] = newStageFactor_4
material.StageFactors.setDefinedStageFactors(definedStageFactors)

# Define stage factors at stage 2
feaGroundwaterStageFactor_4 = material.Hydraulic.FEAGroundwater.stageFactorInterface.getDefinedStageFactors()[stage_4]
hydroDistributionGroundwaterStageFactor_4 = material.Hydraulic.HydroDistribution.stageFactorInterface.getDefinedStageFactors()[stage_4]

# Set stage factors for different parameters
feaGroundwaterStageFactor_4.setK2K1Factor(2.2)

# Get and Set Hydraulic Distribution Function in Stage Factor
hydroDistributionGroundwaterStageFactor_4.setHydroDistributionStagedFunction(hydro_var_1, hydro_type_1, fun1_name)
hydroDistributionProp = hydroDistributionGroundwaterStageFactor_4.getHydroDistributionStagedFunction(hydro_var_1)
# Check assigned Hydraulic Distribution Type
assert hydroDistributionProp[0] == hydro_type_1
# Check assigned Hydraulic Distribution Function Name
assert hydroDistributionProp[1] == fun1_name

# Switch stage hydraulic distribution function to a coordinate distribution
hydroDistributionGroundwaterStageFactor_4.setHydroDistributionStagedFunction(hydro_var_1, hydro_type_2, fun2_name)
hydroDistributionProp = hydroDistributionGroundwaterStageFactor_4.getHydroDistributionStagedFunction(hydro_var_1)
# Check assigned Hydraulic Distribution Type
assert hydroDistributionProp[0] == hydro_type_2
# Check assigned Hydraulic Distribution Function Name
assert hydroDistributionProp[1] == fun2_name

fun5 = model.getHydroDistributionFunctionByName(hydro_var_6, hydro_type_5, fun4_name)
# Set the parameter values based on the hydro distribution
point_dos5 = [[15.2, 0.1], [34.2, 0.15], [35.1, 0.25]]
fun5.setPointsParameter(point_dos5)
assert fun5.getPointsParameter() == point_dos5

# Switch stage hydraulic distribution function to a vertical stress distribution
hydroDistributionGroundwaterStageFactor_4.setHydroDistributionStagedFunction(hydro_var_6, hydro_type_5, fun4_name)
hydroDistributionProp = hydroDistributionGroundwaterStageFactor_4.getHydroDistributionStagedFunction(hydro_var_6)
# Check assigned Hydraulic Distribution Type
assert hydroDistributionProp[0] == hydro_type_5
# Check assigned Hydraulic Distribution Function Name
assert hydroDistributionProp[1] == fun4_name

fun6 = model.getHydroDistributionFunctionByName(hydro_var_3, hydro_type_5, fun3_name)
# Set the parameter values based on the hydro distribution
fun6.setPointsParameter(point_ks1)
assert fun6.getPointsParameter() == point_ks1

mh.setHydroDistribution(hydro_var_3, hydro_type_5, fun3_name)
assert mh.getHydroDistributionFunctionName(hydro_var_3) == fun3_name

fun7 = model.getHydroDistributionFunctionByName(hydro_var_5, hydro_type_2, fun4_name)
# Set the parameter values based on the hydro distribution
point_wc2 = [[1.123, 2.123, 0.123], [2.234, 3.235, 0.456], [3.324, 1.256, 0.456]]
fun7.setPointsParameter(point_wc2)
assert fun7.getPointsParameter() == point_wc2

mh.setHydroDistribution(hydro_var_5, hydro_type_2, fun4_name)
assert mh.getHydroDistributionFunctionName(hydro_var_5) == fun4_name

# Save model and run compute
model_path = r'C:\Users\GraceHu\Documents\post_modeling_dummy_model.fez'
model.saveAs(model_path)
model.compute()

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
                ExportResultType.SEEPAGE_SPATIAL_WC_R,
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

# Delete stage factors
stage_4 = 4
definedStageFactors.pop(stage_4)
material.StageFactors.setDefinedStageFactors(definedStageFactors)

# Apply Stage Hydraulic Properties and Stage Hydraulic Distribution
material.StageFactors.setStageHydroDistributionStageFactor(False)
assert material.StageFactors.getStageHydroDistributionStageFactor() == False

variable_list = [HydraulicVariableTypes.KS_FUNC,
                 HydraulicVariableTypes.K2K1_FUNC,
                 HydraulicVariableTypes.K1_ANGLE_FUNC,
                 HydraulicVariableTypes.WC_SAT_FUNC,
                 HydraulicVariableTypes.WC_RES_FUNC,  
                ]

for stage in range(2,3):
    print("Stage", stage)
    for variable in variable_list:
        print(variable)
        print(material.Hydraulic.HydroDistribution.stageFactorInterface.getStageFactor(stage).getHydroDistributionStagedFunction(variable))
    print()

# Set the constant value of the new constant distribution
constant_val = 0.1
mh.setHydroDistribution(hydro_var_1, hydro_type_3, constant_val)
assert mh.getHydroDistribution(hydro_var_1) == hydro_type_3
assert mh.getHydroDistributionConstantVal(hydro_var_1) == constant_val

# Delete one of the new hydro distribution functions
model.deleteHydroDistributionFunction(hydro_var_1, hydro_type_2, fun2_name)
assert len(model.getHydroDistributionFunctions(hydro_var_1, hydro_type_2)) == 0

# Delete another hydro distribution function
model.deleteHydroDistributionFunction(hydro_var_1, hydro_type_1, fun1_name)
assert len(model.getHydroDistributionFunctions(hydro_var_1, hydro_type_1)) == 0



