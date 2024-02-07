from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class GardnerWaterContent(PropertyProxy):
	def getA(self) -> float:
		return self._getDoubleProperty("MP_GARDNER_A_THERMAL")
	def setA(self, value: float):
		return self._setDoubleProperty("MP_GARDNER_A_THERMAL", value)
	def getN(self) -> float:
		return self._getDoubleProperty("MP_GARDNER_N_THERMAL")
	def setN(self, value: float):
		return self._setDoubleProperty("MP_GARDNER_N_THERMAL", value)
	def setProperties(self, A : float = None, N : float = None):
		if A is not None:
			self._setDoubleProperty("MP_GARDNER_A_THERMAL", A)
		if N is not None:
			self._setDoubleProperty("MP_GARDNER_N_THERMAL", N)
	def getProperties(self):
		return {
		"A" : self.getA(), 
		"N" : self.getN(), 
		}
