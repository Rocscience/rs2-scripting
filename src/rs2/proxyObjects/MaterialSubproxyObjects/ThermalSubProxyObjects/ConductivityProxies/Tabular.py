from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class Tabular(PropertyProxy):
	def getDependence(self) -> ThermalVolumetricDepencenceType:
		return ThermalVolumetricDepencenceType(self._getEnumEThermalVolumetricDepencenceTypeProperty("MP_THERMAL_TABULAR_DEPENDENCE"))
	def setDependence(self, value: ThermalVolumetricDepencenceType):
		return self._setEnumEThermalVolumetricDepencenceTypeProperty("MP_THERMAL_TABULAR_DEPENDENCE", value)
	def setThermalConductivityTable(self, temperatureOrWaterContent: list[float], conductivity: list[float]):
		"""
		Depending on the type of thermal tabular dependence selected, the values are interpreted as temperature or water content.
		"""
		return self._callFunction("setThermalConductivityTable", [temperatureOrWaterContent, conductivity])
	def setProperties(self, Dependence : ThermalVolumetricDepencenceType = None):
		if Dependence is not None:
			self._setEnumEThermalVolumetricDepencenceTypeProperty("MP_THERMAL_TABULAR_DEPENDENCE", Dependence)
	def getProperties(self):
		return {
		"Dependence" : self.getDependence(), 
		}
