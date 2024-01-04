from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class Gardner(PropertyProxy):
	def getA(self) -> float:
		return self._getDoubleProperty("MP_GARDNER_A")
	def setA(self, value: float):
		return self._setDoubleProperty("MP_GARDNER_A", value)
	def getN(self) -> float:
		return self._getDoubleProperty("MP_GARDNER_N")
	def setN(self, value: float):
		return self._setDoubleProperty("MP_GARDNER_N", value)
	def getKs(self) -> float:
		return self._getDoubleProperty("MP_KS")
	def setKs(self, value: float):
		return self._setDoubleProperty("MP_KS", value)
	def getWCInputType(self) -> WCInputType:
		return WCInputType(self._getEnumEWCInputTypeProperty("MP_WC_INPUT_TYPE"))
	def setWCInputType(self, value: WCInputType):
		return self._setEnumEWCInputTypeProperty("MP_WC_INPUT_TYPE", value)
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
	def setProperties(self, A : float = None, N : float = None, Ks : float = None, WCInputType : WCInputType = None, WCSat : float = None, WCRes : float = None, DoSSat : float = None, DoSRes : float = None):
		if A is not None:
			self._setDoubleProperty("MP_GARDNER_A", A)
		if N is not None:
			self._setDoubleProperty("MP_GARDNER_N", N)
		if Ks is not None:
			self._setDoubleProperty("MP_KS", Ks)
		if WCInputType is not None:
			self._setEnumEWCInputTypeProperty("MP_WC_INPUT_TYPE", WCInputType)
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
		"A" : self.getA(), 
		"N" : self.getN(), 
		"Ks" : self.getKs(), 
		"WCInputType" : self.getWCInputType(), 
		"WCSat" : self.getWCSat(), 
		"WCRes" : self.getWCRes(), 
		"DoSSat" : self.getDoSSat(), 
		"DoSRes" : self.getDoSRes(), 
		}
