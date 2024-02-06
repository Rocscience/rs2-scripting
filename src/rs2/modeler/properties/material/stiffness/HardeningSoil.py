from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class HardeningSoil(PropertyProxy):
	def getERef50(self) -> float:
		return self._getDoubleProperty("MP_HS_E_REF_50")
	def setERef50(self, value: float):
		return self._setDoubleProperty("MP_HS_E_REF_50", value)
	def getERefoed(self) -> float:
		return self._getDoubleProperty("MP_HS_E_REF_OED")
	def setERefoed(self, value: float):
		return self._setDoubleProperty("MP_HS_E_REF_OED", value)
	def getERefur(self) -> float:
		return self._getDoubleProperty("MP_HS_E_REF_UR")
	def setERefur(self, value: float):
		return self._setDoubleProperty("MP_HS_E_REF_UR", value)
	def getM(self) -> float:
		return self._getDoubleProperty("MP_HS_M")
	def setM(self, value: float):
		return self._setDoubleProperty("MP_HS_M", value)
	def getReferencePressure(self) -> float:
		return self._getDoubleProperty("MP_HS_REF_PRESSURE")
	def setReferencePressure(self, value: float):
		return self._setDoubleProperty("MP_HS_REF_PRESSURE", value)
	def getPoissonsRatio(self) -> float:
		return self._getDoubleProperty("MP_HS_POISSON")
	def setPoissonsRatio(self, value: float):
		return self._setDoubleProperty("MP_HS_POISSON", value)
	def getPlimit(self) -> float:
		return self._getDoubleProperty("MP_HS_P_LIMIT")
	def setPlimit(self, value: float):
		return self._setDoubleProperty("MP_HS_P_LIMIT", value)
	def getG0ref(self) -> float:
		return self._getDoubleProperty("MP_HS_G0_REF")
	def setG0ref(self, value: float):
		return self._setDoubleProperty("MP_HS_G0_REF", value)
	def getGama07(self) -> float:
		return self._getDoubleProperty("MP_HS_GAMA_07")
	def setGama07(self, value: float):
		return self._setDoubleProperty("MP_HS_GAMA_07", value)
	def setProperties(self, ERef50 : float = None, ERefoed : float = None, ERefur : float = None, M : float = None, ReferencePressure : float = None, PoissonsRatio : float = None, Plimit : float = None, G0ref : float = None, Gama07 : float = None):
		if ERef50 is not None:
			self._setDoubleProperty("MP_HS_E_REF_50", ERef50)
		if ERefoed is not None:
			self._setDoubleProperty("MP_HS_E_REF_OED", ERefoed)
		if ERefur is not None:
			self._setDoubleProperty("MP_HS_E_REF_UR", ERefur)
		if M is not None:
			self._setDoubleProperty("MP_HS_M", M)
		if ReferencePressure is not None:
			self._setDoubleProperty("MP_HS_REF_PRESSURE", ReferencePressure)
		if PoissonsRatio is not None:
			self._setDoubleProperty("MP_HS_POISSON", PoissonsRatio)
		if Plimit is not None:
			self._setDoubleProperty("MP_HS_P_LIMIT", Plimit)
		if G0ref is not None:
			self._setDoubleProperty("MP_HS_G0_REF", G0ref)
		if Gama07 is not None:
			self._setDoubleProperty("MP_HS_GAMA_07", Gama07)
	def getProperties(self):
		return {
		"ERef50" : self.getERef50(), 
		"ERefoed" : self.getERefoed(), 
		"ERefur" : self.getERefur(), 
		"M" : self.getM(), 
		"ReferencePressure" : self.getReferencePressure(), 
		"PoissonsRatio" : self.getPoissonsRatio(), 
		"Plimit" : self.getPlimit(), 
		"G0ref" : self.getG0ref(), 
		"Gama07" : self.getGama07(), 
		}
