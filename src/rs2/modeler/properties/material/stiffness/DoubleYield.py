from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class DoubleYield(PropertyProxy):
	def getKRefiso(self) -> float:
		return self._getDoubleProperty("MP_CYS_K_REF_ISO")
	def setKRefiso(self, value: float):
		return self._setDoubleProperty("MP_CYS_K_REF_ISO", value)
	def getMK(self) -> float:
		return self._getDoubleProperty("MP_CYS_M_K")
	def setMK(self, value: float):
		return self._setDoubleProperty("MP_CYS_M_K", value)
	def getRK(self) -> float:
		return self._getDoubleProperty("MP_CYS_R_K")
	def setRK(self, value: float):
		return self._setDoubleProperty("MP_CYS_R_K", value)
	def getReferencePressure(self) -> float:
		return self._getDoubleProperty("MP_CYS_REF_PRESSURE")
	def setReferencePressure(self, value: float):
		return self._setDoubleProperty("MP_CYS_REF_PRESSURE", value)
	def getPoissonsRatio(self) -> float:
		return self._getDoubleProperty("MP_CYS_POISSON")
	def setPoissonsRatio(self, value: float):
		return self._setDoubleProperty("MP_CYS_POISSON", value)
	def setProperties(self, KRefiso : float = None, MK : float = None, RK : float = None, ReferencePressure : float = None, PoissonsRatio : float = None):
		if KRefiso is not None:
			self._setDoubleProperty("MP_CYS_K_REF_ISO", KRefiso)
		if MK is not None:
			self._setDoubleProperty("MP_CYS_M_K", MK)
		if RK is not None:
			self._setDoubleProperty("MP_CYS_R_K", RK)
		if ReferencePressure is not None:
			self._setDoubleProperty("MP_CYS_REF_PRESSURE", ReferencePressure)
		if PoissonsRatio is not None:
			self._setDoubleProperty("MP_CYS_POISSON", PoissonsRatio)
	def getProperties(self):
		return {
		"KRefiso" : self.getKRefiso(), 
		"MK" : self.getMK(), 
		"RK" : self.getRK(), 
		"ReferencePressure" : self.getReferencePressure(), 
		"PoissonsRatio" : self.getPoissonsRatio(), 
		}
