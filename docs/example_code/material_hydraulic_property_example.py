from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
modeler = RS2Modeler()
staticGroundwaterModel = modeler.openFile(rf"{current_dir}\example_models\StaticGroundwater.fez")
FEAGroundwaterModel = modeler.openFile(rf"{current_dir}\example_models\FEAGroundwater.fez")

material = staticGroundwaterModel.getAllMaterialProperties()[0]
hydraulic = material.Hydraulic

hydraulic.setMaterialBehaviour(MaterialBehaviours.UNDRAINED)
hydraulic.setFluidBulkModulus(6)
hydraulic.setUseBiotsCoefficientForCalculatingEffectiveStress(True)

# Manupulation of Static Groundwater properties
staticgroundwater = hydraulic.StaticGroundwater
staticgroundwater.setStaticWaterMode(StaticWaterModes.PIEZO)
staticgroundwater.setPiezoToUse("None")
print(f"Piezo To Use = {staticgroundwater.getPiezoToUse()}")
staticgroundwater.setStaticWaterMode(StaticWaterModes.RU)
staticgroundwater.setRuValue(4)

print(f"Static Water Mode = {staticgroundwater.getStaticWaterMode()}, RU Value = {staticgroundwater.getRuValue()}")

# Manipulation of FEA Groundwater properties for Simple Model
material = FEAGroundwaterModel.getAllMaterialProperties()[0]
FEAGroundwater = hydraulic.FEAGroundwater
FEAGroundwater.setK2K1(2)
FEAGroundwater.setK1Definition(AnisotropyDefinitions.ANGLE)
FEAGroundwater.setK1Angle(30)

print(f"K2/K1 = {FEAGroundwater.getK2K1()}, K1 Definition = {FEAGroundwater.getK1Definition()}, K1 Angle = {FEAGroundwater.getK1Angle()}\n")

