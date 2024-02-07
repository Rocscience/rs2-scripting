from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class Konrad(PropertyProxy):
	def getResidualWaterContent(self) -> float:
		return self._getDoubleProperty("MP_THERMAL_WATER_CONTENT_RESIDUAL_WATER_CONTENT")
	def setResidualWaterContent(self, value: float):
		return self._setDoubleProperty("MP_THERMAL_WATER_CONTENT_RESIDUAL_WATER_CONTENT", value)
	def getFrozenTemperature(self) -> float:
		return self._getDoubleProperty("MP_THERMAL_WATER_CONTENT_FROZEN_TEMPERATURE")
	def setFrozenTemperature(self, value: float):
		return self._setDoubleProperty("MP_THERMAL_WATER_CONTENT_FROZEN_TEMPERATURE", value)
	def getSolidusTemperature(self) -> float:
		return self._getDoubleProperty("MP_THERMAL_WATER_CONTENT_SOLIDUS_TEMPERATURE")
	def setSolidusTemperature(self, value: float):
		return self._setDoubleProperty("MP_THERMAL_WATER_CONTENT_SOLIDUS_TEMPERATURE", value)
	def setProperties(self, ResidualWaterContent : float = None, FrozenTemperature : float = None, SolidusTemperature : float = None):
		if ResidualWaterContent is not None:
			self._setDoubleProperty("MP_THERMAL_WATER_CONTENT_RESIDUAL_WATER_CONTENT", ResidualWaterContent)
		if FrozenTemperature is not None:
			self._setDoubleProperty("MP_THERMAL_WATER_CONTENT_FROZEN_TEMPERATURE", FrozenTemperature)
		if SolidusTemperature is not None:
			self._setDoubleProperty("MP_THERMAL_WATER_CONTENT_SOLIDUS_TEMPERATURE", SolidusTemperature)
	def getProperties(self):
		return {
		"ResidualWaterContent" : self.getResidualWaterContent(), 
		"FrozenTemperature" : self.getFrozenTemperature(), 
		"SolidusTemperature" : self.getSolidusTemperature(), 
		}
