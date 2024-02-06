from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class ManzariAndDafalias(PropertyProxy):
	def getG0Parameter(self) -> float:
		return self._getDoubleProperty("MP_MD_G0")
	def setG0Parameter(self, value: float):
		return self._setDoubleProperty("MP_MD_G0", value)
	def getVParameter(self) -> float:
		return self._getDoubleProperty("MP_MD_V")
	def setVParameter(self, value: float):
		return self._setDoubleProperty("MP_MD_V", value)
	def getPatmParameter(self) -> float:
		return self._getDoubleProperty("MP_MD_PATM")
	def setPatmParameter(self, value: float):
		return self._setDoubleProperty("MP_MD_PATM", value)
	def getInitialVoidRatio(self) -> float:
		return self._getDoubleProperty("MP_MD_INITIAL_VOID_RATIO")
	def setInitialVoidRatio(self, value: float):
		return self._setDoubleProperty("MP_MD_INITIAL_VOID_RATIO", value)
	def setProperties(self, G0Parameter : float = None, VParameter : float = None, PatmParameter : float = None, InitialVoidRatio : float = None):
		if G0Parameter is not None:
			self._setDoubleProperty("MP_MD_G0", G0Parameter)
		if VParameter is not None:
			self._setDoubleProperty("MP_MD_V", VParameter)
		if PatmParameter is not None:
			self._setDoubleProperty("MP_MD_PATM", PatmParameter)
		if InitialVoidRatio is not None:
			self._setDoubleProperty("MP_MD_INITIAL_VOID_RATIO", InitialVoidRatio)
	def getProperties(self):
		return {
		"G0Parameter" : self.getG0Parameter(), 
		"VParameter" : self.getVParameter(), 
		"PatmParameter" : self.getPatmParameter(), 
		"InitialVoidRatio" : self.getInitialVoidRatio(), 
		}
