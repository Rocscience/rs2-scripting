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
hydro_var_1 = HydraulicVariableTypes.RELATIVE_KS_FUNCTION
hydro_type_1 = HydraulicDistributionTypes.MEAN_STRESS_DISTRIBUTION
hydro_type_2 = HydraulicDistributionTypes.COORDINATE_DISTRIBUTION


model.createNewHydroDistributionFunction(hydro_var_1, hydro_type_1, fun1_name)
model.createNewHydroDistributionFunction(hydro_var_1, hydro_type_2, fun1_name)

# Check the list of available function for each variable
assert len(model.getHydroDistributionFunctions(hydro_var_1, hydro_type_1)) == 1
assert len(model.getHydroDistributionFunctions(hydro_var_1, hydro_type_2)) == 1

fun1 = model.getHydroDistributionFunctionByName(hydro_var_1, hydro_type_1, fun1_name)
# Set the parameter values based on the hydro distribution
point_ks1 = [[0.1, 12.2], [0.3, 14.4], [0.5, 14.6]]
fun1.setPointsParameter(point_ks1)
assert fun1.getPointsParameter() == point_ks1

fun2 = model.getHydroDistributionFunctionByName(hydro_var_1, hydro_type_2, fun1_name)
# Set the parameter values based on the hydro distribution
point_ks2 = [[1.123, 2.123, 3.123], [2.234, 3.235, 4.456], [3.324, 1.256, 3.456]]
fun2.setPointsParameter(point_ks2)
assert fun2.getPointsParameter() == point_ks2

# Assign the new created hydro distribution function to Material 1
mh = material.Hydraulic.HydroDistribution
mh.setHydroDistribution(hydro_var_1, hydro_type_1, fun1_name)
assert mh.getHydroDistributionFunctionName(hydro_var_1) == fun1_name

# End of Model 1
model_path = r'C:\scriptingModels\post_HydroDistributionFunction_1.fez'
model.saveAs(model_path)

# Apply Stage Hydraulic Properties and Stage Hydraulic Distribution
material.StageFactors.setStageHydraulicStageFactor(True)

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
hydroDistributionGroundwaterStageFactor_2 = material.Hydraulic.HydroDistribution.stageFactorInterface.getDefinedStageFactors()[stage_2]

# Switch stage hydraulic distribution function to a volumetric strain distribution
hydroDistributionGroundwaterStageFactor_2.setHydroDistributionStagedFunction(hydro_var_1, hydro_type_1, fun1_name)
hydroDistributionProp = hydroDistributionGroundwaterStageFactor_2.getHydroDistributionStagedFunction(hydro_var_1)
# Check assigned Hydraulic Distribution Type
assert hydroDistributionProp.distribution_type == hydro_type_1
# Check assigned Hydraulic Distribution Function Name
assert hydroDistributionProp.function_name == fun1_name

# Add a new stage 4
newStageFactor_4 = material.StageFactors.createStageFactor(stage_4)
definedStageFactors[stage_4] = newStageFactor_4
material.StageFactors.setDefinedStageFactors(definedStageFactors)

# Define stage factors at stage 4
hydroDistributionGroundwaterStageFactor_4 = material.Hydraulic.HydroDistribution.stageFactorInterface.getDefinedStageFactors()[stage_4]

# Get and Set Hydraulic Distribution Function in Stage Factor
hydroDistributionGroundwaterStageFactor_4.setHydroDistributionStagedFunction(hydro_var_1, hydro_type_2, fun1_name)
hydroDistributionProp = hydroDistributionGroundwaterStageFactor_4.getHydroDistributionStagedFunction(hydro_var_1)
# Check assigned Hydraulic Distribution Type
assert hydroDistributionProp.distribution_type == hydro_type_2
# Check assigned Hydraulic Distribution Function Name
assert hydroDistributionProp.function_name == fun1_name

# End of Model 2
model_path = r'C:\scriptingModels\post_HydroDistributionFunction_2.fez'
model.saveAs(model_path)

print("Model 2")
for stage in [1, 2, 3, 4]:
    print("Stage", stage)
    for variable in variable_list:
        print(variable)
        print(material.Hydraulic.HydroDistribution.stageFactorInterface.getStageFactor(stage).getHydroDistributionStagedFunction(variable))
    print()

material.StageFactors.setStageHydroDistributionStageFactor(False)
assert material.StageFactors.getStageHydroDistributionStageFactor() == False

print("Model 2")
for stage in [1, 2, 3, 4]:
    print("Stage", stage)
    for variable in variable_list:
        print(variable)
        print(material.Hydraulic.HydroDistribution.stageFactorInterface.getStageFactor(stage).getHydroDistributionStagedFunction(variable))
    print()
