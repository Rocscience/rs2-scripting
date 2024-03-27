from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
modeler = RS2Modeler()
model = modeler.openFile(rf"{current_dir}\example_models\TransientGroundwaterAndThermal.fez")

material = model.getAllMaterialProperties()[0]
thermal = material.Thermal
thermal.setWaterContent(ThermalWaterContentMethodType.DEFINE)
thermal.setWaterContentValue(0.35)

# Manipulation of Thermal Conductivity Properties
conductivity = thermal.Conductivity
conductivity.setMethod(ThermalType.JOHANSEN_LU)
johansenLu = conductivity.JohansenLu
johansenLu.setSoilType(ThermalSoilType.CRUSHED_ROCK)
johansenLu.setQuartzContent(0.88)
print(f"Soil Type = {johansenLu.getSoilType()}, Quartz Content = {johansenLu.getQuartzContent()}")

conductivity.setMethod(ThermalType.CUSTOM)
conductivity.Tabular.setDependence(ThermalVolumetricDepencenceType.TEMPERATURE)
conductivity.Tabular.setThermalConductivityTemperatureFunction(temperature=[1, 2, 3],
                                                               conductivity=[1.5, 3.3, 4.8])
print(f"\nThermal Temp. Vs Conductivity Table Values = {conductivity.Tabular.getThermalConductivityTemperatureFunction()}")

# Manipulation of Thermal Heat Capacity Properties
heatCapacity = thermal.HeatCapacity
heatCapacity.setType(ThermalHeatCapacityType.JAME_NEWMAN)
jameNewman = thermal.HeatCapacity.JameNewman
jameNewman.setIncludeLatentHeat(True)
jameNewman.setSoilSpecificHeatCapacity(890)
print(f"Heat Capacity Type = {heatCapacity.getType()}, Include Latent = {jameNewman.getIncludeLatentHeat()}, Specific Heat Capacity = {jameNewman.getSoilSpecificHeatCapacity()}")

custom = heatCapacity.CustomHeatCapacity
custom.setDependence(ThermalVolumetricDepencenceType.WATER_CONTENT)
custom.setVolumetricHeatCapacityVsWaterContentTable(volumetricHeatCapacity=[1, 2.4],
                                                    waterContent=[7, 8.5])
print("Volumetric Heat Capacity VS Water Content Table", custom.getVolumetricHeatCapacityVsWaterContentTable())

# Manipulation of Thermal Soil Unfrozen Water Content Properties
soilUnfrozenWaterContent = thermal.SoilUnfrozenWaterContent
ticeAnderson = soilUnfrozenWaterContent.TiceAnderson
ticeAnderson.setFrozenTemperature(-0.05)
ticeAnderson.setInputAlpha(0.009)
ticeAnderson.setInputBeta(0.0085)
print(f"Input Alpha = {ticeAnderson.getInputAlpha()}, Input Beta = {ticeAnderson.getInputBeta()}, Frozen Temp = {ticeAnderson.getFrozenTemperature()}")

soilUnfrozenWaterContent.setType(ThermalWaterContentType.CUSTOM)
soilUnfrozenWaterContent.CustomWaterContent.setTemperatureVsUnfrozenWaterContentValues(temperature=[1, 2, 3],
                                                                                       unfrozenWaterContent=[4, 5, 6])
print("\nThermal Temperature vs Soil Unfrozen Water Content Table Values",
      soilUnfrozenWaterContent.CustomWaterContent.getTemperatureVsUnfrozenWaterContentValues())

# Manipulation of Thermal Hydraulic Model Soil Unfrozen Water Content Properties
soilUnfrozenWC = thermal.SoilUnfrozenWaterContent
# Make sure to set Soil Unfrozen Water Content type to Hydraulic Properties
soilUnfrozenWC.setType(ThermalWaterContentType.SOIL_WATER_CONTENT_IN_HYDRAULIC_PROPERTIES)
hydraulic_soilUnfrozenWC = soilUnfrozenWaterContent.HydraulicModel
# Make sure to set Hydraulic Model to your desired type
hydraulic_soilUnfrozenWC.setSelectHydraulicModel(GroundWaterModes.GARDNER)
hydraulic_soilUnfrozenWC.setFrozenTemperature(-0.015)
hydraulic_soilUnfrozenWC.setWCSat(0.34)
hydraulic_soilUnfrozenWC.setWCRes(0.01)
# Set properties for Gardener Hydraulic Model
gardenerWaterContent = hydraulic_soilUnfrozenWC.GardnerWaterContent
gardenerWaterContent.setA(8)
gardenerWaterContent.setN(3)

print(f"\n Thermal Soil Unfrozen Water Content Type = {soilUnfrozenWaterContent.getType()}, Hydraulic Model Type = {hydraulic_soilUnfrozenWC.getSelectHydraulicModel()}")
print(f"Frozen Temperature = {hydraulic_soilUnfrozenWC.getFrozenTemperature()}, WC Sat = {hydraulic_soilUnfrozenWC.getWCSat()}, WC Res = {hydraulic_soilUnfrozenWC.getWCRes()}")
print(f"Gardener Parameter A = {gardenerWaterContent.getA()}, Gardener Parameter N = {gardenerWaterContent.getN()}")

thermal.setThermalExpansion(True)
thermal.setExpansionCoefficient(0.0005)

thermal.setDispersivity(True)
thermal.setLongitudinalDispersivity(2)
thermal.setTransverseDispersivity(3)

print(f"Thermal Expansion Coeff. = {thermal.getExpansionCoefficient()}")
print(f"Longitudinal Dispersivity = {thermal.getLongitudinalDispersivity()}, Transverse Dispersivity = {thermal.getTransverseDispersivity()}\n")

# Manipulation of Thermal Stage Factor Properties
thermalStageFactors = material.Thermal.stageFactorInterface.getDefinedStageFactors()[1]

thermalStageFactors.setThermalGridFactor("Default Grid")

print(f"Thermal Stage Factor Grid To Use = {thermalStageFactors.getThermalGridFactor()}")

model.close()