from rs2.modeler import properties
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties import *
import os



"""
1 create new hydro distribution function with new points
2 assign hydro distribution function to material 1.
3 delete hydro distribution function
"""


modeler = RS2Modeler(port=60054)

# relative_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../tests/resources/starterProject.fez")
path = r"C:\Users\GraceHu\Documents\dummy_model.fez"
model = modeler.openFile(path)

material = model.getMaterialPropertyByName("Material 1")

fun1_name = "Function 1"
fun2_name = "New Function 2"

hydro_var_1 = HydraulicVariableTypes.KS_FUNC
hydro_var_2 = HydraulicVariableTypes.K2K1_FUNC
hydro_type_1 = HydraulicDistributionTypes.VERTICAL_STRESS_DIST
hydro_type_2 = HydraulicDistributionTypes.COORDINATE_DIST
hydro_type_3 = HydraulicDistributionTypes.CONSTANT_DIST

# Create 2 new hydro distribution functions
model.createNewHydroDistributionFunction(hydro_var_1, hydro_type_1, fun1_name)
model.createNewHydroDistributionFunction(hydro_var_1, hydro_type_2, fun1_name)
# Check the list of available function for each variable
assert len(model.getHydroDistributionFunctions(hydro_var_1, hydro_type_1)) == 1
assert len(model.getHydroDistributionFunctions(hydro_var_1, hydro_type_2)) == 1

fun1 = model.getHydroDistributionFunctionByName(hydro_var_1, hydro_type_1, fun1_name)
# Set the parameter values based on the hydro distribution
point_ks1 = [[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]]
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
stage = 2
newStageFactor = material.StageFactors.createStageFactor(stage)
definedStageFactors[2] = newStageFactor
material.StageFactors.setDefinedStageFactors(definedStageFactors)

# Define stage factors at stage 2
feaGroundwaterStageFactor = material.Hydraulic.FEAGroundwater.stageFactorInterface.getDefinedStageFactors()[stage]
hydroDistributionGroundwaterStageFactor = material.Hydraulic.HydroDistribution.stageFactorInterface.getDefinedStageFactors()[stage]

# Set stage factors for different parameters
feaGroundwaterStageFactor.setK1AngleFactor(0.7)
feaGroundwaterStageFactor.setK2K1Factor(2.2)
feaGroundwaterStageFactor.setMvFactor(5)

# Get and Set Hydraulic Distribution Function in Stage Factor
hydroDistributionGroundwaterStageFactor.setHydroDistributionStagedFunction(hydro_var_1, hydro_type_1, fun1_name)
hydroDistributionProp = hydroDistributionGroundwaterStageFactor.getHydroDistributionStagedFunction(hydro_var_1)
# Check assigned Hydraulic Distribution Type
assert hydroDistributionProp[0] == hydro_type_1
# Check assigned Hydraulic Distribution Function Name
assert hydroDistributionProp[1] == fun1_name

# Apply Stage Hydraulic Properties and Stage Hydraulic Distribution
material.StageFactors.setStageHydroDistributionStageFactor(False)
assert material.StageFactors.getStageHydroDistributionStageFactor() == False
material.StageFactors.setStageHydraulicStageFactor(False)

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
