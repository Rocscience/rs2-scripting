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

fun1_name = "Function 2"
# fun2_name = "func2"

hydro_var_1 = HydraulicVariableTypes.KS_FUNC
hydro_var_2 = HydraulicVariableTypes.DOS_SAT_FUNC
hydro_type_1 = HydraulicDistributionTypes.MEAN_STRESS_DIST
hydro_type_2 = HydraulicDistributionTypes.COORDINATE_DIST
hydro_type_3 = HydraulicDistributionTypes.VERTICAL_STRESS_DIST

# # Create 2 new hydro distribution functions
# model.createNewHydroDistributionFunction(fun1_name, hydro_var_1, hydro_type_1)
# model.createNewHydroDistributionFunction(fun2_name, hydro_var_1, hydro_type_2)
# assert len(model.getHydroDistributionFunctions(hydro_var_1, hydro_type_1)) == 1
# assert len(model.getHydroDistributionFunctions(hydro_var_1, hydro_type_2)) == 1


# fun1 = model.getHydroDistributionFunctionByName(hydro_var_1, hydro_type_1, fun1_name)
# # Set the parameter values based on the hydro distribution
# POINTKS1 = [[0.1, 0.1], [0.2, 0.2], [0.3, 0.3]]
# fun1.setPointsParameter(POINTKS1)
# assert fun1.getPointsParameter() == POINTKS1


# fun2 = model.getHydroDistributionFunctionByName(hydro_var_1, hydro_type_2, fun2_name)
# # Set the parameter values based on the hydro distribution
# POINTKS2 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# fun2.setPointsParameter(POINTKS2)
# assert fun2.getPointsParameter() == POINTKS2

# # Assign the new created hydro distribution function to Material 1
mh = material.Hydraulic.HydroDistribution
# # material.Strength.getFailureCriterion()
mh.setHydroDistribution(hydro_var_1, hydro_type_3, fun1_name)
print(mh.getHydroDistributionVal(hydro_var_1))
# assert mh.getHydroDistribution(hydro_var_1) == fun1_name

# # Set new distribution type to constant
# hydro_type_3 = HydraulicDistributionTypes.HORIZONTAL_STRESS_DIST
# mh.setNewHydroDistribution(hydro_var_1, hydro_type_3)
# assert mh.getHydroDistribution(hydro_var_1) == hydro_type_3

# # Set the constant value of the new constant distribution
hydro_type_4 = HydraulicDistributionTypes.CONSTANT_DIST
constant_val = 0.1
mh.setHydroDistribution(hydro_var_1, hydro_type_4, constant_val)
print(mh.getHydroDistributionConstantVal(hydro_var_1))
# assert mh.getHydroDistribution(hydro_var_1) == hydro_type_4
# assert mh.getSelectedHydroDistributionVal(hydro_var_1, hydro_type_4) == constant_val

# # Delete one of the new hydro distribution functions
# model.deleteHydroDistributionFunction(hydro_var_1, hydro_type_2, fun2_name)
# assert len(model.getHydroDistributionFunctions(hydro_var_1, hydro_type_2)) == 0

# # Delete another hydro distribution function
# model.deleteHydroDistributionFunction(hydro_var_1, hydro_type_1, fun1_name)
# assert len(model.getHydroDistributionFunctions(hydro_var_1, hydro_type_1)) == 0
