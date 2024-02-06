from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class GenuchtenWaterContent(PropertyProxy):
	def getAlpha(self) -> float:
		return self._getDoubleProperty("MP_VAN_GENUCHTEN_ALPHA_THERMAL")
	def setAlpha(self, value: float):
		return self._setDoubleProperty("MP_VAN_GENUCHTEN_ALPHA_THERMAL", value)
	def getN(self) -> float:
		return self._getDoubleProperty("MP_VAN_GENUCHTEM_N_THERMAL")
	def setN(self, value: float):
		return self._setDoubleProperty("MP_VAN_GENUCHTEM_N_THERMAL", value)
	def getCustomM(self) -> bool:
		return self._getBoolProperty("MP_VAN_USE_CUSTOM_M_THERMAL")
	def setCustomM(self, value: bool):
		return self._setBoolProperty("MP_VAN_USE_CUSTOM_M_THERMAL", value)
	def getM(self) -> float:
		return self._getDoubleProperty("MP_VAN_CUSTOM_M_THERMAL")
	def setM(self, value: float):
		return self._setDoubleProperty("MP_VAN_CUSTOM_M_THERMAL", value)
	def setProperties(self, Alpha : float = None, N : float = None, CustomM : bool = None, M : float = None):
		if Alpha is not None:
			self._setDoubleProperty("MP_VAN_GENUCHTEN_ALPHA_THERMAL", Alpha)
		if N is not None:
			self._setDoubleProperty("MP_VAN_GENUCHTEM_N_THERMAL", N)
		if CustomM is not None:
			self._setBoolProperty("MP_VAN_USE_CUSTOM_M_THERMAL", CustomM)
		if M is not None:
			self._setDoubleProperty("MP_VAN_CUSTOM_M_THERMAL", M)
	def getProperties(self):
		return {
		"Alpha" : self.getAlpha(), 
		"N" : self.getN(), 
		"CustomM" : self.getCustomM(), 
		"M" : self.getM(), 
		}
