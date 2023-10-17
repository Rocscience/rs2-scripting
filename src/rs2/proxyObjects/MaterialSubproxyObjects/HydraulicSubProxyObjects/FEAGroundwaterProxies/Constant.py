from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class Constant(PropertyProxy):
	def getUseCV(self) -> bool:
		return self._getBoolProperty("MP_USE_CV")
	def setUseCV(self, value: bool):
		return self._setBoolProperty("MP_USE_CV", value)
	def getCV(self) -> float:
		return self._getDoubleProperty("MP_CV")
	def setCV(self, value: float):
		return self._setDoubleProperty("MP_CV", value)
	def getInitialK(self) -> float:
		return self._getDoubleProperty("MP_INITIAL_K")
	def setInitialK(self, value: float):
		return self._setDoubleProperty("MP_INITIAL_K", value)
	def getWCSat(self) -> float:
		return self._getDoubleProperty("MP_WC_SLOPE")
	def setWCSat(self, value: float):
		return self._setDoubleProperty("MP_WC_SLOPE", value)
	def setProperties(self, UseCV : bool = None, CV : float = None, InitialK : float = None, WCSat : float = None):
		if UseCV is not None:
			self._setBoolProperty("MP_USE_CV", UseCV)
		if CV is not None:
			self._setDoubleProperty("MP_CV", CV)
		if InitialK is not None:
			self._setDoubleProperty("MP_INITIAL_K", InitialK)
		if WCSat is not None:
			self._setDoubleProperty("MP_WC_SLOPE", WCSat)
	def getProperties(self):
		return {
		"UseCV" : self.getUseCV(), 
		"CV" : self.getCV(), 
		"InitialK" : self.getInitialK(), 
		"WCSat" : self.getWCSat(), 
		}
