from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
RS2Modeler.startApplication(port=60066)
modeler = RS2Modeler(port=60066)
model = modeler.openFile(rf"{current_dir}\example_models\FEAGroundwater.fez")

material = model.getAllMaterialProperties()[0]
hydraulic = material.Hydraulic

hydraulic.setMaterialBehaviour(MaterialBehaviours.UNDRAINED)
hydraulic.setFluidBulkModulus(6)
hydraulic.setUseBiotsCoefficientForCalculatingEffectiveStress(True)

FEAGroundwater = hydraulic.FEAGroundwater
FEAGroundwater.setK2K1(2)
FEAGroundwater.setK1Definition(AnisotropyDefinitions.ANGLE)
FEAGroundwater.setK1Angle(30)
FEAGroundwater.setMvModel(MVModel.CONSTANT)
FEAGroundwater.setMv(0.05)
FEAGroundwater.Simple.setKs(0.005)
FEAGroundwater.Simple.setWCInputType(WCInputType.BY_WATER_CONTENT)
FEAGroundwater.Simple.setWCSat(0.5)
FEAGroundwater.Simple.setWCRes(0.3)
FEAGroundwater.Simple.setWCInputType(WCInputType.BY_DEGREE_OF_SATURATION)
FEAGroundwater.Simple.setDoSSat(0.3)
FEAGroundwater.Simple.setDoSRes(1)
print(f"Fluid Bulk Modulus = {hydraulic.getFluidBulkModulus()}, K2/K1 = {FEAGroundwater.getK2K1()}, K1 Definition = {FEAGroundwater.getK1Definition()}")
print(f"K1 Angle = {FEAGroundwater.getK1Angle()}, MV Model = {FEAGroundwater.getMvModel()}, Mv Value = {FEAGroundwater.getMv()}")
print(f"Ks Value = {FEAGroundwater.Simple.getKs()}, Water Content Sat = {FEAGroundwater.Simple.getWCSat()}, Water Content Res = {FEAGroundwater.Simple.getWCRes()}")
print(f"Degree of Saturation Sat = {FEAGroundwater.Simple.getDoSSat()}, Degree of Staturation Res = {FEAGroundwater.Simple.getDoSRes()}\n")

simple = FEAGroundwater.Simple
simple.setSoilType(EnhancedSimpleSoilTypes.SILT)
print(f"Soil Type = {simple.getSoilType()}\n")

fredlund = FEAGroundwater.Fredlund
fredlund.setA(8)
fredlund.setB(5)
fredlund.setC(6)
print(f"Fredlund Param A = {fredlund.getA()}, Fredlung Param B = {fredlund.getB()}, Fredlund Param C = {fredlund.getC()}\n")

genuchten = FEAGroundwater.Genuchten
genuchten.setAlpha(20)
genuchten.setN(3.13)
genuchten.setCustomM(True)
genuchten.setM(0.55)
print(f"Alpha = {genuchten.getAlpha()}, N = {genuchten.getN()}, Custom M Value = {genuchten.getM()}\n")

brooks = FEAGroundwater.Brooks
brooks.setPoreSizeIndex(2)
brooks.setBubblingPressure(3)
print(f"Pore Size Index = {brooks.getPoreSizeIndex()}, Bubbling Pressure = {brooks.getBubblingPressure()}\n")

gardener = FEAGroundwater.Gardner
gardener.setA(0.5)
gardener.setN(5)
print(f"Param A = {gardener.getA()}, Param N = {gardener.getN()}\n")

userDefined = FEAGroundwater.UserDefined
userDefined.setUserDefinedPermeabilityAndWaterContentFunction("User Defined 1")
print(f"User Defined Permeability And Water Content Function Name = {userDefined.getUserDefinedPermeabilityAndWaterContentFunction()}\n")

# Manipulation of FEAGroundwater Stage Factor Properties for stage 2
# Make sure to stage Hydraulic Stage Factor option before manipulating any factor properties
material.StageFactors.setStageHydraulicStageFactor(True)
definedStageFactors = material.StageFactors.getDefinedStageFactors()
newStageFactor = material.StageFactors.createStageFactor(2)
definedStageFactors[2] = newStageFactor
material.StageFactors.setDefinedStageFactors(definedStageFactors)
feaGroundwaterStageFactor = material.Hydraulic.FEAGroundwater.stageFactorInterface.getDefinedStageFactors()[2]

feaGroundwaterStageFactor.setK1AngleFactor(0.7)
feaGroundwaterStageFactor.setK2K1Factor(2.2)
feaGroundwaterStageFactor.setMvFactor(5)

print("\nFEAGroundwater Stage Factor Values") 
print(f"K1 Angle Factor = {feaGroundwaterStageFactor.getK1AngleFactor()}, K2/K1 Factor = {feaGroundwaterStageFactor.getK2K1Factor()}, MV Factor = {feaGroundwaterStageFactor.getMvFactor()}")

# Manipulation of FEAGroundwater Constant Model Stage Factor Properties for stage 2
constantModelStageFactor = material.Hydraulic.FEAGroundwater.Constant.stageFactorInterface.getDefinedStageFactors()[2]

constantModelStageFactor.setWCCurveSlopeFactor(1.7)

print("\nFEAGroundwater Constant Model Factor Values") 
print(f"Curve Slope Factor = {constantModelStageFactor.getWCCurveSlopeFactor()}")

fredlundModelStageFactor = material.Hydraulic.FEAGroundwater.Fredlund.stageFactorInterface.getDefinedStageFactors()[2]

fredlundModelStageFactor.setAFactor(0.7)
fredlundModelStageFactor.setBFactor(2.2)
fredlundModelStageFactor.setCFactor(5)
fredlundModelStageFactor.setKsFactor(5)

print("\nFEAGroundwater Fredlund Model Factor Values") 
print(f"A Factor = {fredlundModelStageFactor.getAFactor()}, B Factor = {fredlundModelStageFactor.getBFactor()}, C Factor = {fredlundModelStageFactor.getCFactor()}, Ks Factor = {fredlundModelStageFactor.getKsFactor()}")

model.close()
modeler.closeProgram()