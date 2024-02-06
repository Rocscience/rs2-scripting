from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class ConstantHeatCapacity(PropertyProxy):
	def getIncludeLatentHeat(self) -> bool:
		return self._getBoolProperty("MP_THERMAL_LATENT_HEAT")
	def setIncludeLatentHeat(self, value: bool):
		return self._setBoolProperty("MP_THERMAL_LATENT_HEAT", value)
	def getUnfrozenVolumetricHeatCapacity(self) -> float:
		return self._getDoubleProperty("MP_THERMAL_VOLUMETRIC_HEAT_CAPACITY_UNFROZEN")
	def setUnfrozenVolumetricHeatCapacity(self, value: float):
		return self._setDoubleProperty("MP_THERMAL_VOLUMETRIC_HEAT_CAPACITY_UNFROZEN", value)
	def getFrozenVolumetricHeatCapacity(self) -> float:
		return self._getDoubleProperty("MP_THERMAL_VOLUMETRIC_HEAT_CAPACITY_FROZEN")
	def setFrozenVolumetricHeatCapacity(self, value: float):
		return self._setDoubleProperty("MP_THERMAL_VOLUMETRIC_HEAT_CAPACITY_FROZEN", value)
	def getFrozenTemperature(self) -> float:
		return self._getDoubleProperty("MP_THERMAL_VOLUMETRIC_FROZEN_TEMPERATURE_UNITS")
	def setFrozenTemperature(self, value: float):
		return self._setDoubleProperty("MP_THERMAL_VOLUMETRIC_FROZEN_TEMPERATURE_UNITS", value)
	def setProperties(self, IncludeLatentHeat : bool = None, UnfrozenVolumetricHeatCapacity : float = None, FrozenVolumetricHeatCapacity : float = None, FrozenTemperature : float = None):
		if IncludeLatentHeat is not None:
			self._setBoolProperty("MP_THERMAL_LATENT_HEAT", IncludeLatentHeat)
		if UnfrozenVolumetricHeatCapacity is not None:
			self._setDoubleProperty("MP_THERMAL_VOLUMETRIC_HEAT_CAPACITY_UNFROZEN", UnfrozenVolumetricHeatCapacity)
		if FrozenVolumetricHeatCapacity is not None:
			self._setDoubleProperty("MP_THERMAL_VOLUMETRIC_HEAT_CAPACITY_FROZEN", FrozenVolumetricHeatCapacity)
		if FrozenTemperature is not None:
			self._setDoubleProperty("MP_THERMAL_VOLUMETRIC_FROZEN_TEMPERATURE_UNITS", FrozenTemperature)
	def getProperties(self):
		return {
		"IncludeLatentHeat" : self.getIncludeLatentHeat(), 
		"UnfrozenVolumetricHeatCapacity" : self.getUnfrozenVolumetricHeatCapacity(), 
		"FrozenVolumetricHeatCapacity" : self.getFrozenVolumetricHeatCapacity(), 
		"FrozenTemperature" : self.getFrozenTemperature(), 
		}
