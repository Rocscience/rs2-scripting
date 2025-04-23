from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
RS2Modeler.startApplication(port=60065)
modeler = RS2Modeler(port=60065)
staticGroundwaterModel = modeler.openFile(rf"{current_dir}\example_models\StaticGroundwater.fez")
FEAGroundwaterModel = modeler.openFile(rf"{current_dir}\example_models\FEAGroundwater.fez")

material = staticGroundwaterModel.getAllMaterialProperties()[0]
hydraulic = material.Hydraulic

hydraulic.setMaterialBehaviour(MaterialBehaviours.UNDRAINED)
hydraulic.setFluidBulkModulus(6)
hydraulic.setUseBiotsCoefficientForCalculatingEffectiveStress(True)

staticgroundwater = hydraulic.StaticGroundwater
staticgroundwater.setStaticWaterMode(StaticWaterModes.PIEZO)
staticgroundwater.setPiezoToUse("None")
print(f"Piezo To Use = {staticgroundwater.getPiezoToUse()}")
staticgroundwater.setStaticWaterMode(StaticWaterModes.RU)
staticgroundwater.setRuValue(4)

print("\nStatic Groundwater Properties\n")
print(f"Static Water Mode = {staticgroundwater.getStaticWaterMode()}, RU Value = {staticgroundwater.getRuValue()}")

material = FEAGroundwaterModel.getAllMaterialProperties()[0]
FEAGroundwater = hydraulic.FEAGroundwater
FEAGroundwater.setK2K1(2)
FEAGroundwater.setK1Definition(AnisotropyDefinitions.ANGLE)
FEAGroundwater.setK1Angle(30)

print("\nFEA Groundwater Properties\n")
print(f"K2/K1 = {FEAGroundwater.getK2K1()}, K1 Definition = {FEAGroundwater.getK1Definition()}, K1 Angle = {FEAGroundwater.getK1Angle()}\n")

# Manipulation of Hydraulic Stage Factor Properties for FEAGroundwater model for stage 2
# Make sure to stage Hydraulic Stage Factor option before manipulating any factor properties
material.StageFactors.setStageHydraulicStageFactor(True)
definedStageFactors = material.StageFactors.getDefinedStageFactors()
newStageFactor = material.StageFactors.createStageFactor(2)
definedStageFactors[2] = newStageFactor
material.StageFactors.setDefinedStageFactors(definedStageFactors)
hydraulicStageFactor = material.Hydraulic.stageFactorInterface.getDefinedStageFactors()[2]

hydraulicStageFactor.setMaterialBehaviourFactor(MaterialBehaviours.UNDRAINED)

print(f"Hydraulic Material Behaviour Stage Factor Value = {hydraulicStageFactor.getMaterialBehaviourFactor()}")

staticGroundwaterModel.close()
FEAGroundwaterModel.close()

modeler.closeProgram()