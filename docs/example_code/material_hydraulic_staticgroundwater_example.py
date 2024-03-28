from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
modeler = RS2Modeler()
model = modeler.openFile(rf"{current_dir}\example_models\StaticGroundwater.fez")

material = model.getAllMaterialProperties()[0]

material.Hydraulic.setMaterialBehaviour(MaterialBehaviours.DRAINED)
material.Hydraulic.setFluidBulkModulus(5)
material.Hydraulic.setUseBiotsCoefficientForCalculatingEffectiveStress(True)

staticGroundwater = material.Hydraulic.StaticGroundwater
staticGroundwater.setStaticWaterMode(StaticWaterModes.PORE_WATER_PRESSURE)
staticGroundwater.setStaticPoreWaterPressure(5)
poreWaterPressure = staticGroundwater.getStaticPoreWaterPressure()
print(f"Static Pore Water Pressure = {poreWaterPressure}")

staticGroundwater.setStaticWaterMode(StaticWaterModes.RU)
staticGroundwater.setRuValue(5)
ruValue = staticGroundwater.getRuValue()
print(f"Ru Value = {ruValue}")

staticGroundwater.setStaticWaterMode(StaticWaterModes.PIEZO)
staticGroundwater.setPiezoToUse("1")
staticGroundwater.setHuType(HuTypes.CUSTOM)
staticGroundwater.setHuValue(5)
huValue = staticGroundwater.getHuValue()
print(f"Hu Value = {huValue}")

staticGroundwater.setStaticWaterMode(StaticWaterModes.GRID)
staticGroundwater.setGridToUse("Default Grid")

# Manipulation of StaticGroundwater Stage Factor Properties for stage 1
# Make sure to stage Hydraulic Stage Factor option before manipulating any factor properties
material.StageFactors.setStageHydraulicStageFactor(True)
staticGroundwaterStageFactor = material.Hydraulic.StaticGroundwater.stageFactorInterface.getDefinedStageFactors()[1]

staticGroundwaterStageFactor.setGridToUse("Default Grid")
staticGroundwaterStageFactor.setPiezoToUse("None")

print(f"StaticGroundwater Factor Grid To Use = {staticGroundwaterStageFactor.getGridToUse()}, Static Groundwater Piezo To Use = {staticGroundwaterStageFactor.getPiezoToUse()}")

model.close()