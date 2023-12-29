from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class CustomHeatCapacity(PropertyProxy):
	def getIncludeLatentHeat(self) -> bool:
		return self._getBoolProperty("MP_THERMAL_LATENT_HEAT")
	def setIncludeLatentHeat(self, value: bool):
		return self._setBoolProperty("MP_THERMAL_LATENT_HEAT", value)
	def getDependence(self) -> ThermalVolumetricDepencenceType:
		return ThermalVolumetricDepencenceType(self._getEnumEThermalVolumetricDepencenceTypeProperty("MP_THERMAL_DEPENDENCE"))
	def setDependence(self, value: ThermalVolumetricDepencenceType):
		return self._setEnumEThermalVolumetricDepencenceTypeProperty("MP_THERMAL_DEPENDENCE", value)
	def setVolumetricHeatCapacityTable(self, volumetricHeatCapacity: list[float], temperatureOrWaterContent: list[float]):
		"""
		Depending on the type of thermal tabular dependence selected, the second argument is interpreted as temperature or water content.
		"""
		return self._callFunction("setVolumetricHeatCapacityTable", [volumetricHeatCapacity, temperatureOrWaterContent])
	def getVolumetricHeatCapacityTable(self) -> list[tuple[float,float]]:
		"""
		The first element in each tuple is the volumetric heat capacity.
		Depending on the type of thermal tabular dependence selected, the second element is interpreted as temperature or water content.
		"""
		return self._callFunction("getVolumetricHeatCapacityTable", [])
	def setProperties(self, IncludeLatentHeat : bool = None, Dependence : ThermalVolumetricDepencenceType = None):
		if IncludeLatentHeat is not None:
			self._setBoolProperty("MP_THERMAL_LATENT_HEAT", IncludeLatentHeat)
		if Dependence is not None:
			self._setEnumEThermalVolumetricDepencenceTypeProperty("MP_THERMAL_DEPENDENCE", Dependence)
	def getProperties(self):
		return {
		"IncludeLatentHeat" : self.getIncludeLatentHeat(), 
		"Dependence" : self.getDependence(), 
		}
