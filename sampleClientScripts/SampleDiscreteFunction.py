from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\Users\WilliamSati\Downloads\discretefunctions.fez")

discreteFunctions = model.getDiscreteFunctions()

df1 = discreteFunctions[0]
df1.setName("F1")

print(df1.getName())

df1.setFunctionParameters(1, True, 0.5, 0.6, 0.7)
print(df1.getFunctionParameters())

df1.setInterpolationMethod(3)
print(df1.getInterpolationMethod())

df1.setSymbolDrawing(1, 0xff2211, True, 0)
print(df1.getSymbolDrawing())

df1.setPointLocations([(0,1), (1,2), (2,3)])
print(df1.getPointLocations())

df1.setPointsC([0.1, 0.2, 0.3])
print(df1.getPointsC())

df1.setPointsPhi([0.4, 0.5, 0.6])
print(df1.getPointsPhi())

df1.setPointsModulus([0.7, 0.8, 0.9])
print(df1.getPointsModulus())

df1.setPointsModulusResidual([0.1, 0.2, 0.3])
print(df1.getPointsModulusResidual())


mat1 = model.getAllMaterialProperties()[0]

print(mat1.Strength.DiscreteFunction.getSelectedDiscreteFunctionName())
mat1.Strength.DiscreteFunction.setSelectedDiscreteFunctionByName("F1")
print(mat1.Strength.DiscreteFunction.getSelectedDiscreteFunctionName())
