from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class TiceAnderson(PropertyProxy):
	def getInputAlpha(self) -> float:
		return self._getDoubleProperty("MP_THERMAL_INPUT_A")
	def setInputAlpha(self, value: float):
		return self._setDoubleProperty("MP_THERMAL_INPUT_A", value)
	def getInputBeta(self) -> float:
		return self._getDoubleProperty("MP_THERMAL_INPUT_B")
	def setInputBeta(self, value: float):
		return self._setDoubleProperty("MP_THERMAL_INPUT_B", value)
	def getFrozenTemperature(self) -> float:
		return self._getDoubleProperty("MP_THERMAL_WATER_CONTENT_FROZEN_TEMPERATURE")
	def setFrozenTemperature(self, value: float):
		return self._setDoubleProperty("MP_THERMAL_WATER_CONTENT_FROZEN_TEMPERATURE", value)
	def setProperties(self, InputAlpha : float = None, InputBeta : float = None, FrozenTemperature : float = None):
		if InputAlpha is not None:
			self._setDoubleProperty("MP_THERMAL_INPUT_A", InputAlpha)
		if InputBeta is not None:
			self._setDoubleProperty("MP_THERMAL_INPUT_B", InputBeta)
		if FrozenTemperature is not None:
			self._setDoubleProperty("MP_THERMAL_WATER_CONTENT_FROZEN_TEMPERATURE", FrozenTemperature)
	def getProperties(self):
		return {
		"InputAlpha" : self.getInputAlpha(), 
		"InputBeta" : self.getInputBeta(), 
		"FrozenTemperature" : self.getFrozenTemperature(), 
		}
