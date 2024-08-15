from src.rs2.modeler import properties
from src.rs2.modeler.properties import DiscreteFunction
from src.rs2.modeler.properties.PropertyEnums import *
from tests import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties import *


"""
1 create new discrete function with new points
2 assign discrete function to material 1.
3 delete discrete function
"""


modeler = RS2Modeler()

parentDirectory = parentDirectoryHelper.getParentDirectory()
blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
model = modeler.openFile(blankModelPath)

material = model.getMaterialPropertyByName("Material 1")

# Create 2 new discrete function
model.createNewDiscreteFunction("func1")
model.createNewDiscreteFunction("func2")
print(model.getDiscreteFunctions())


fun1 = model.getDiscreteFunctionByName("func1")
# Set some points on the discrete function
fun1.setPointLocations([(1, 1), (2, 2), (3, 3)])
# Set the Cu values for those points
fun1.setPointsC([0.5, 1, 0.2])
print(fun1.getPointLocations())
print(fun1.getPointsC())

# Assign the new created discrete function to Material 1
material.Strength.DiscreteFunction.setSelectedDiscreteFunctionByName("func1")
print(material.Strength.DiscreteFunction.getSelectedDiscreteFunctionName())

# Set the failure criterion to be discrete function
material.Strength.setFailureCriterion(StrengthCriteriaTypes.DISCRETE_FUNCTION)
print(material.Strength.getFailureCriterion())

# Delete one of the new discrete functions
model.deleteDiscreteFunction("func2")
print(model.getDiscreteFunctions())

# Set the failure criterion to be Mohr Coulomb
material.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
print(material.Strength.getFailureCriterion())

# Delete another discrete function
model.deleteDiscreteFunction("func1")
print(model.getDiscreteFunctions())
