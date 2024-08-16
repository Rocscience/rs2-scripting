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

# Create 2 new discrete function
model.createNewDiscreteFunction("func1")
model.createNewDiscreteFunction("func2")
assert len(model.getDiscreteFunctions()) == 2


fun1 = model.getDiscreteFunctionByName("func1")
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
df.setSelectedDiscreteFunctionByName("func1")
assert df.getSelectedDiscreteFunctionName() == "func1"

# Set the failure criterion to be discrete function
strength = material.Strength
strength.setFailureCriterion(StrengthCriteriaTypes.DISCRETE_FUNCTION)
assert strength.getFailureCriterion() == StrengthCriteriaTypes.DISCRETE_FUNCTION

# Delete one of the new discrete functions
model.deleteDiscreteFunction("func2")
assert len(model.getDiscreteFunctions()) == 1

# Set the failure criterion to be Mohr Coulomb
strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
assert strength.getFailureCriterion() == StrengthCriteriaTypes.MOHR_COULOMB

# Delete another discrete function
model.deleteDiscreteFunction("func1")
assert len(model.getDiscreteFunctions()) == 0
