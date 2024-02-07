from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class Tabular(PropertyProxy):
	def getDependence(self) -> ThermalVolumetricDepencenceType:
		return ThermalVolumetricDepencenceType(self._getEnumEThermalVolumetricDepencenceTypeProperty("MP_THERMAL_TABULAR_DEPENDENCE"))
	def setDependence(self, value: ThermalVolumetricDepencenceType):
		return self._setEnumEThermalVolumetricDepencenceTypeProperty("MP_THERMAL_TABULAR_DEPENDENCE", value)
	def setThermalConductivityTemperatureFunction(self, temperature: list[float], conductivity: list[float]):
		return self._callFunction("setThermalConductivityTemperatureFunction", [temperature, conductivity])
	def getThermalConductivityTemperatureFunction(self) -> tuple[list[float],list[float]]:
		"""
		returns tuple (temperatureList, conductivityList).
		"""
		return self._callFunction("getThermalConductivityTemperatureFunction", [])
	def setThermalConductivityWaterContentFunction(self, waterContent: list[float], conductivity: list[float]):
		return self._callFunction("setThermalConductivityWaterContentFunction", [waterContent, conductivity])
	def getThermalConductivityWaterContentFunction(self) -> tuple[list[float],list[float]]:
		"""
		returns tuple (waterContentList, conductivityList).
		"""
		return self._callFunction("getThermalConductivityWaterContentFunction", [])
	def setProperties(self, Dependence : ThermalVolumetricDepencenceType = None):
		if Dependence is not None:
			self._setEnumEThermalVolumetricDepencenceTypeProperty("MP_THERMAL_TABULAR_DEPENDENCE", Dependence)
	def getProperties(self):
		return {
		"Dependence" : self.getDependence(), 
		}
