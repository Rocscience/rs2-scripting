from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\Users\WilliamSati\Downloads\discretefunctions.fez")

try:
    model.deleteDiscreteFunction("User Defined 2")#currently being used in the model. Should not work.
except Exception as e:
    print(e)

try:
    model.deleteDiscreteFunction("non existing name")#function with name that does not exist cannot be deleted
except Exception as e:
    print(e)


model.deleteDiscreteFunction("User Defined 1")#should work since no material is using it.

model.createNewDiscreteFunction("F3")
df3 = model.getDiscreteFunctionByName("F3")

print(df3.getName())

df3.setFunctionParameters(1, True, 0.5, 0.6, 0.7)
print(df3.getFunctionParameters())

df3.setInterpolationMethod(3)
print(df3.getInterpolationMethod())

df3.setSymbolDrawing(1, 0xff2211, True, 0)
print(df3.getSymbolDrawing())

df3.setPointLocations([(0,1), (1,2), (2,3)])
print(df3.getPointLocations())

df3.setPointsC([0.1, 0.2, 0.3])
print(df3.getPointsC())

df3.setPointsPhi([0.4, 0.5, 0.6])
print(df3.getPointsPhi())

df3.setPointsModulus([0.7, 0.8, 0.9])
print(df3.getPointsModulus())

df3.setPointsModulusResidual([0.1, 0.2, 0.3])
print(df3.getPointsModulusResidual())


mat1 = model.getAllMaterialProperties()[0]

print(mat1.Strength.DiscreteFunction.getSelectedDiscreteFunctionName())
mat1.Strength.DiscreteFunction.setSelectedDiscreteFunctionByName("F3")
print(mat1.Strength.DiscreteFunction.getSelectedDiscreteFunctionName())

#deleting User Defined 2 should work now since no one is using it
model.deleteDiscreteFunction("User Defined 2")
