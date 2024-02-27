from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class JameNewman(PropertyProxy):
	def getIncludeLatentHeat(self) -> bool:
		return self._getBoolProperty("MP_THERMAL_LATENT_HEAT")
	def setIncludeLatentHeat(self, value: bool):
		return self._setBoolProperty("MP_THERMAL_LATENT_HEAT", value)
	def getSoilSpecificHeatCapacity(self) -> float:
		return self._getDoubleProperty("MP_THERMAL_SOIL_HEATING_CAPACITY")
	def setSoilSpecificHeatCapacity(self, value: float):
		return self._setDoubleProperty("MP_THERMAL_SOIL_HEATING_CAPACITY", value)
	def setProperties(self, IncludeLatentHeat : bool = None, SoilSpecificHeatCapacity : float = None):
		if IncludeLatentHeat is not None:
			self._setBoolProperty("MP_THERMAL_LATENT_HEAT", IncludeLatentHeat)
		if SoilSpecificHeatCapacity is not None:
			self._setDoubleProperty("MP_THERMAL_SOIL_HEATING_CAPACITY", SoilSpecificHeatCapacity)
	def getProperties(self):
		return {
		"IncludeLatentHeat" : self.getIncludeLatentHeat(), 
		"SoilSpecificHeatCapacity" : self.getSoilSpecificHeatCapacity(), 
		}
