from rs2.modeler import properties
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties import *
import os

"""
1 create new discrete function with new points
2 assign discrete function to material 1.
3 delete discrete function
"""


modeler = RS2Modeler()

relative_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../tests/resources/starterProject.fez")
model = modeler.openFile(relative_path)

material = model.getMaterialPropertyByName("Material 1")

fun1_name = "func1"
fun2_name = "func2"

# Create 2 new discrete function
model.createNewDiscreteFunction(fun1_name)
model.createNewDiscreteFunction(fun2_name)
assert len(model.getDiscreteFunctions()) == 2


fun1 = model.getDiscreteFunctionByName(fun1_name)
# Set some points on the discrete function
POINTLOCATIONS = [(1, 1), (2, 2), (3, 3)]
fun1.setPointLocations(POINTLOCATIONS)
# Set the Cu values for those points
POINTSC = [0.5, 1, 0.2]
fun1.setPointsC(POINTSC)
assert fun1.getPointLocations() == POINTLOCATIONS
assert fun1.getPointsC() == POINTSC

# Assign the new created discrete function to Material 1
df = material.Strength.DiscreteFunction
df.setSelectedDiscreteFunctionByName(fun1_name)
assert df.getSelectedDiscreteFunctionName() == fun1_name

# Set the failure criterion to be discrete function
strength = material.Strength
df_type = StrengthCriteriaTypes.DISCRETE_FUNCTION
strength.setFailureCriterion(df_type)
assert strength.getFailureCriterion() == df_type

# Delete one of the new discrete functions
model.deleteDiscreteFunction(fun2_name)
assert len(model.getDiscreteFunctions()) == 1

# Set the failure criterion to be Mohr Coulomb
mc_type = StrengthCriteriaTypes.MOHR_COULOMB
strength.setFailureCriterion(mc_type)
assert strength.getFailureCriterion() == mc_type

# Delete another discrete function
model.deleteDiscreteFunction(fun1_name)
assert len(model.getDiscreteFunctions()) == 0
