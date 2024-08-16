from rs2.modeler import properties
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties import *
import os, inspect


"""
1 create new discrete function with new points
2 assign discrete function to material 1.
3 delete discrete function
"""


modeler = RS2Modeler()

parentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
blankModelPath = f"{parentdir}/../tests/resources/starterProject.fez"
model = modeler.openFile(blankModelPath)

material = model.getMaterialPropertyByName("Material 1")

# Create 2 new discrete function
model.createNewDiscreteFunction("func1")
model.createNewDiscreteFunction("func2")
print(len(model.getDiscreteFunctions()), "discrete function(s) is/are in the list.")


fun1 = model.getDiscreteFunctionByName("func1")
# Set some points on the discrete function
fun1.setPointLocations([(1, 1), (2, 2), (3, 3)])
# Set the Cu values for those points
fun1.setPointsC([0.5, 1, 0.2])
try:
    assert fun1.getPointLocations() == [(1, 1), (2, 2), (3, 3)]
    print(fun1.getPointLocations(), "is correct.")
except:
    print(fun1.getPointLocations(), "is WRONG.")

try:
    assert fun1.getPointsC() == [0.5, 1, 0.2]
    print(fun1.getPointsC(), "is correct.")
except:
    print(fun1.getPointsC(), "is WRONG.")

# Assign the new created discrete function to Material 1
material.Strength.DiscreteFunction.setSelectedDiscreteFunctionByName("func1")
try:
    assert material.Strength.DiscreteFunction.getSelectedDiscreteFunctionName() == "func1"
    print(material.Strength.DiscreteFunction.getSelectedDiscreteFunctionName(), "is correct.")
except:
    print(material.Strength.DiscreteFunction.getSelectedDiscreteFunctionName(), "is WRONG.")

# Set the failure criterion to be discrete function
material.Strength.setFailureCriterion(StrengthCriteriaTypes.DISCRETE_FUNCTION)
try:
    assert material.Strength.getFailureCriterion() == StrengthCriteriaTypes.DISCRETE_FUNCTION
    print(material.Strength.getFailureCriterion(), "is correct.")
except:
    print(material.Strength.getFailureCriterion(), "is WRONG.")

# Delete one of the new discrete functions
model.deleteDiscreteFunction("func2")
print(len(model.getDiscreteFunctions()), "discrete function(s) is/are in the list.")

# Set the failure criterion to be Mohr Coulomb
material.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
try:
    assert material.Strength.getFailureCriterion() == StrengthCriteriaTypes.MOHR_COULOMB
    print(material.Strength.getFailureCriterion(), "is correct")
except:
    print(material.Strength.getFailureCriterion(), "is WRONG")

# Delete another discrete function
model.deleteDiscreteFunction("func1")
print(len(model.getDiscreteFunctions()), "discrete function(s) is/are in the list.")
