from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class Genuchten(PropertyProxy):
	def getAlpha(self) -> float:
		return self._getDoubleProperty("MP_VAN_GENUCHTEN_ALPHA")
	def setAlpha(self, value: float):
		return self._setDoubleProperty("MP_VAN_GENUCHTEN_ALPHA", value)
	def getN(self) -> float:
		return self._getDoubleProperty("MP_VAN_GENUCHTEM_N")
	def setN(self, value: float):
		return self._setDoubleProperty("MP_VAN_GENUCHTEM_N", value)
	def getCustomM(self) -> bool:
		return self._getBoolProperty("MP_VAN_USE_CUSTOM_M")
	def setCustomM(self, value: bool):
		return self._setBoolProperty("MP_VAN_USE_CUSTOM_M", value)
	def getM(self) -> float:
		return self._getDoubleProperty("MP_VAN_CUSTOM_M")
	def setM(self, value: float):
		return self._setDoubleProperty("MP_VAN_CUSTOM_M", value)
	def getKs(self) -> float:
		return self._getDoubleProperty("MP_KS")
	def setKs(self, value: float):
		return self._setDoubleProperty("MP_KS", value)
	def getWCSat(self) -> float:
		return self._getDoubleProperty("MP_WC_SAT")
	def setWCSat(self, value: float):
		return self._setDoubleProperty("MP_WC_SAT", value)
	def getWCRes(self) -> float:
		return self._getDoubleProperty("MP_WC_RES")
	def setWCRes(self, value: float):
		return self._setDoubleProperty("MP_WC_RES", value)
	def getDoSSat(self) -> float:
		return self._getDoubleProperty("MP_DOS_SAT")
	def setDoSSat(self, value: float):
		return self._setDoubleProperty("MP_DOS_SAT", value)
	def getDoSRes(self) -> float:
		return self._getDoubleProperty("MP_DOS_RES")
	def setDoSRes(self, value: float):
		return self._setDoubleProperty("MP_DOS_RES", value)
	def setProperties(self, Alpha : float = None, N : float = None, CustomM : bool = None, M : float = None, Ks : float = None, WCSat : float = None, WCRes : float = None, DoSSat : float = None, DoSRes : float = None):
		if Alpha is not None:
			self._setDoubleProperty("MP_VAN_GENUCHTEN_ALPHA", Alpha)
		if N is not None:
			self._setDoubleProperty("MP_VAN_GENUCHTEM_N", N)
		if CustomM is not None:
			self._setBoolProperty("MP_VAN_USE_CUSTOM_M", CustomM)
		if M is not None:
			self._setDoubleProperty("MP_VAN_CUSTOM_M", M)
		if Ks is not None:
			self._setDoubleProperty("MP_KS", Ks)
		if WCSat is not None:
			self._setDoubleProperty("MP_WC_SAT", WCSat)
		if WCRes is not None:
			self._setDoubleProperty("MP_WC_RES", WCRes)
		if DoSSat is not None:
			self._setDoubleProperty("MP_DOS_SAT", DoSSat)
		if DoSRes is not None:
			self._setDoubleProperty("MP_DOS_RES", DoSRes)
	def getProperties(self):
		return {
		"Alpha" : self.getAlpha(), 
		"N" : self.getN(), 
		"CustomM" : self.getCustomM(), 
		"M" : self.getM(), 
		"Ks" : self.getKs(), 
		"WCSat" : self.getWCSat(), 
		"WCRes" : self.getWCRes(), 
		"DoSSat" : self.getDoSSat(), 
		"DoSRes" : self.getDoSRes(), 
		}
