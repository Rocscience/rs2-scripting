from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class ConstantConductivity(PropertyProxy):
	def getUnfrozenConductivity(self) -> float:
		return self._getDoubleProperty("MP_THERMAL_UNFROZEN_CONDUCTIVITY")
	def setUnfrozenConductivity(self, value: float):
		return self._setDoubleProperty("MP_THERMAL_UNFROZEN_CONDUCTIVITY", value)
	def getFrozenConductivity(self) -> float:
		return self._getDoubleProperty("MP_THERMAL_FROZEN_CONDUCTIVITY")
	def setFrozenConductivity(self, value: float):
		return self._setDoubleProperty("MP_THERMAL_FROZEN_CONDUCTIVITY", value)
	def getFrozenTemperature(self) -> float:
		return self._getDoubleProperty("MP_THERMAL_FROZEN_TEMPERATURE")
	def setFrozenTemperature(self, value: float):
		return self._setDoubleProperty("MP_THERMAL_FROZEN_TEMPERATURE", value)
	def setProperties(self, UnfrozenConductivity : float = None, FrozenConductivity : float = None, FrozenTemperature : float = None):
		if UnfrozenConductivity is not None:
			self._setDoubleProperty("MP_THERMAL_UNFROZEN_CONDUCTIVITY", UnfrozenConductivity)
		if FrozenConductivity is not None:
			self._setDoubleProperty("MP_THERMAL_FROZEN_CONDUCTIVITY", FrozenConductivity)
		if FrozenTemperature is not None:
			self._setDoubleProperty("MP_THERMAL_FROZEN_TEMPERATURE", FrozenTemperature)
	def getProperties(self):
		return {
		"UnfrozenConductivity" : self.getUnfrozenConductivity(), 
		"FrozenConductivity" : self.getFrozenConductivity(), 
		"FrozenTemperature" : self.getFrozenTemperature(), 
		}
