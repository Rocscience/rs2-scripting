from rs2.modeler import properties
from rs2.modeler.properties.HydroDistributionFunction import *
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties import *
from rs2.modeler.properties.PropertyEnums import HydraulicVariableTypes, HydraulicDistributionTypes
from rs2.modeler.properties.material import *
import os

"""
1 create new hydro distribution function with new points
2 assign hydro distribution function to material 1.
3 delete hydro distribution function
"""


modeler = RS2Modeler()

relative_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../tests/resources/starterProject.fez")
model = modeler.openFile(relative_path)

material = model.getMaterialPropertyByName("Material 1")

fun1_name = "func1"
fun2_name = "func2"

hydro_var_1 = HydraulicVariableTypes.KS
hydro_type_1 = HydraulicDistributionTypes.MEAN_STRESS_DIST
hydro_type_2 = HydraulicDistributionTypes.COORDINATE_DIST

# Create 2 new hydro distribution functions
model.createNewHydroDistributionFunction(fun1_name, hydro_var_1, hydro_type_1)
model.createNewHydroDistributionFunction(fun2_name, hydro_var_1, hydro_type_2)
assert len(model.getHydroDistributionFunctions(hydro_var_1, hydro_type_1)) == 1
assert len(model.getHydroDistributionFunctions(hydro_var_1, hydro_type_2)) == 1


fun1 = model.getHydroDistributionFunctionByName(hydro_var_1, hydro_type_1, fun1_name)
# Set the Distribution values for those points
POINTDIST = [0.5, 1, 0.2]
fun1.setPointsDist(POINTDIST)
# Set the parameter values based on the hydro distribution
POINTKS1 = [0.1, 0.2, 0.3]
fun1.setPointsParameter(POINTKS1)
assert fun1.getPointsDist() == POINTDIST
assert fun1.getPointsParameter() == POINTKS1


fun2 = model.getHydroDistributionFunctionByName(hydro_var_1, hydro_type_2, fun2_name)
# Set some points on the hydro coordinate distribution function
POINTCOORDS = [(1, 1), (2, 2), (3, 3)]
fun2.setPointCoordinates(POINTCOORDS)
# Set the parameter values based on the hydro distribution
POINTKS2 = [0.5, 1.1, 2.3]
fun2.setPointsParameter(POINTKS2)
assert fun2.getPointsDist() == POINTCOORDS
assert fun2.getPointsParameter() == POINTKS2

# Assign the new created hydro distribution function to Material 1
mh = material.Hydraulic.HydroDistribution
mh.setSelectedHydroDistributionFunctionByName(hydro_var_1, hydro_type_1, fun1_name)
assert mh.getSelectedHydroDistributionFunctionName(hydro_var_1, hydro_type_1) == fun1_name

# Delete one of the new hydro distribution functions
model.deleteHydroDistributionFunction(hydro_var_1, hydro_type_2, fun2_name)
assert len(model.getHydroDistributionFunctions(hydro_var_1, hydro_type_2)) == 0

# Delete another hydro distribution function
model.deleteHydroDistributionFunction(hydro_var_1, hydro_type_1, fun1_name)
assert len(model.getHydroDistributionFunctions(hydro_var_1, hydro_type_1)) == 0
