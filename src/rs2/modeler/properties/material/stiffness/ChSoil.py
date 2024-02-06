from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class ChSoil(PropertyProxy):
	def getGRef(self) -> float:
		return self._getDoubleProperty("MP_CHS_G_REF")
	def setGRef(self, value: float):
		return self._setDoubleProperty("MP_CHS_G_REF", value)
	def getNG(self) -> float:
		return self._getDoubleProperty("MP_CHS_N_G")
	def setNG(self, value: float):
		return self._setDoubleProperty("MP_CHS_N_G", value)
	def getKRef(self) -> float:
		return self._getDoubleProperty("MP_CHS_K_REF")
	def setKRef(self, value: float):
		return self._setDoubleProperty("MP_CHS_K_REF", value)
	def getMK(self) -> float:
		return self._getDoubleProperty("MP_CHS_M_K")
	def setMK(self, value: float):
		return self._setDoubleProperty("MP_CHS_M_K", value)
	def getReferencePressure(self) -> float:
		return self._getDoubleProperty("MP_CHS_REF_PRESSURE")
	def setReferencePressure(self, value: float):
		return self._setDoubleProperty("MP_CHS_REF_PRESSURE", value)
	def setProperties(self, GRef : float = None, NG : float = None, KRef : float = None, MK : float = None, ReferencePressure : float = None):
		if GRef is not None:
			self._setDoubleProperty("MP_CHS_G_REF", GRef)
		if NG is not None:
			self._setDoubleProperty("MP_CHS_N_G", NG)
		if KRef is not None:
			self._setDoubleProperty("MP_CHS_K_REF", KRef)
		if MK is not None:
			self._setDoubleProperty("MP_CHS_M_K", MK)
		if ReferencePressure is not None:
			self._setDoubleProperty("MP_CHS_REF_PRESSURE", ReferencePressure)
	def getProperties(self):
		return {
		"GRef" : self.getGRef(), 
		"NG" : self.getNG(), 
		"KRef" : self.getKRef(), 
		"MK" : self.getMK(), 
		"ReferencePressure" : self.getReferencePressure(), 
		}
