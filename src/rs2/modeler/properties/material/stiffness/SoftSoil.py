from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class SoftSoil(PropertyProxy):
	def getPoissonsRatio(self) -> float:
		return self._getDoubleProperty("MP_SS_POISSON")
	def setPoissonsRatio(self, value: float):
		return self._setDoubleProperty("MP_SS_POISSON", value)
	def getPlimit(self) -> float:
		return self._getDoubleProperty("MP_SS_P_LIMIT")
	def setPlimit(self, value: float):
		return self._setDoubleProperty("MP_SS_P_LIMIT", value)
	def setProperties(self, PoissonsRatio : float = None, Plimit : float = None):
		if PoissonsRatio is not None:
			self._setDoubleProperty("MP_SS_POISSON", PoissonsRatio)
		if Plimit is not None:
			self._setDoubleProperty("MP_SS_P_LIMIT", Plimit)
	def getProperties(self):
		return {
		"PoissonsRatio" : self.getPoissonsRatio(), 
		"Plimit" : self.getPlimit(), 
		}
