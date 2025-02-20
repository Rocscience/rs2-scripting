from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.AbsoluteStageFactorGettersInterface import AbsoluteStageFactorGettersInterface
class GenuchtenStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getMFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_VAN_CUSTOM_M", self.propertyID], proxyArgumentIndices=[1])
	def getNFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_VAN_GENUCHTEM_N", self.propertyID], proxyArgumentIndices=[1])
	def getAlphaFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_VAN_GENUCHTEN_ALPHA", self.propertyID], proxyArgumentIndices=[1])
	def getKsFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_KS", self.propertyID], proxyArgumentIndices=[1])
	def getWCSatFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_WC_SAT", self.propertyID], proxyArgumentIndices=[1])
	def getWCResFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_WC_RES", self.propertyID], proxyArgumentIndices=[1])
	def getDoSSatFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_DOS_SAT", self.propertyID], proxyArgumentIndices=[1])
	def getDoSResFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_DOS_RES", self.propertyID], proxyArgumentIndices=[1])
class GenuchtenDefinedStageFactor(GenuchtenStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setMFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_VAN_CUSTOM_M", value, self.propertyID], proxyArgumentIndices=[2])
	def setNFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_VAN_GENUCHTEM_N", value, self.propertyID], proxyArgumentIndices=[2])
	def setAlphaFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_VAN_GENUCHTEN_ALPHA", value, self.propertyID], proxyArgumentIndices=[2])
	def setKsFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_KS", value, self.propertyID], proxyArgumentIndices=[2])
	def setWCSatFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_WC_SAT", value, self.propertyID], proxyArgumentIndices=[2])
	def setWCResFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_WC_RES", value, self.propertyID], proxyArgumentIndices=[2])
	def setDoSSatFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_DOS_SAT", value, self.propertyID], proxyArgumentIndices=[2])
	def setDoSResFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_DOS_RES", value, self.propertyID], proxyArgumentIndices=[2])
class Genuchten(PropertyProxy):
	"""
	Attributes:
		stageFactorInterface (AbsoluteStageFactorGettersInterface[GenuchtenDefinedStageFactor, GenuchtenStageFactor]): Reference object for modifying stage factor property.

	Examples:
		:ref:`Hydraulic Property FEAGroundwater Example`
	
	"""
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		super().__init__(client, ID, documentProxyID)
		self.stageFactorInterface = AbsoluteStageFactorGettersInterface[GenuchtenDefinedStageFactor, GenuchtenStageFactor](self._client, stageFactorInterfaceID, ID, GenuchtenDefinedStageFactor, GenuchtenStageFactor)
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
	def setProperties(self, Alpha : float = None, N : float = None, CustomM : bool = None, M : float = None, Ks : float = None, WCInputType : WCInputType = None, WCSat : float = None, WCRes : float = None, DoSSat : float = None, DoSRes : float = None):
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
		"Alpha" : self.getAlpha(), 
		"N" : self.getN(), 
		"CustomM" : self.getCustomM(), 
		"M" : self.getM(), 
		"Ks" : self.getKs(), 
		"WCInputType" : self.getWCInputType(), 
		"WCSat" : self.getWCSat(), 
		"WCRes" : self.getWCRes(), 
		"DoSSat" : self.getDoSSat(), 
		"DoSRes" : self.getDoSRes(), 
		}
