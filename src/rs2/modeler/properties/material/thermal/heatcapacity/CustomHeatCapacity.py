from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class CustomHeatCapacity(PropertyProxy):
	def getIncludeLatentHeat(self) -> bool:
		return self._getBoolProperty("MP_THERMAL_LATENT_HEAT")
	def setIncludeLatentHeat(self, value: bool):
		return self._setBoolProperty("MP_THERMAL_LATENT_HEAT", value)
	def getDependence(self) -> ThermalVolumetricDepencenceType:
		return ThermalVolumetricDepencenceType(self._getEnumEThermalVolumetricDepencenceTypeProperty("MP_THERMAL_DEPENDENCE"))
	def setDependence(self, value: ThermalVolumetricDepencenceType):
		return self._setEnumEThermalVolumetricDepencenceTypeProperty("MP_THERMAL_DEPENDENCE", value)
	def setVolumetricHeatCapacityVsTemperatureTable(self, volumetricHeatCapacity: list[float], temperature: list[float]):
		return self._callFunction("setVolumetricHeatCapacityVsTemperatureTable", [volumetricHeatCapacity, temperature])
	def getVolumetricHeatCapacityVsTemperatureTable(self) -> tuple[list[float],list[float]]:
		"""
		Returns a tuple of lists ([volumetricHeatCapacity],[temperature])
		"""
		return self._callFunction("getVolumetricHeatCapacityVsTemperatureTable", [])
	def setVolumetricHeatCapacityVsWaterContentTable(self, volumetricHeatCapacity: list[float], waterContent: list[float]):
		return self._callFunction("setVolumetricHeatCapacityVsWaterContentTable", [volumetricHeatCapacity, waterContent])
	def getVolumetricHeatCapacityVsWaterContentTable(self) -> tuple[list[float],list[float]]:
		"""
		Returns a tuple of lists ([volumetricHeatCapacity],[waterContent])
		"""
		return self._callFunction("getVolumetricHeatCapacityVsWaterContentTable", [])
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
