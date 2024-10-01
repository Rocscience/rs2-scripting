from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.AbsoluteStageFactorGettersInterface import AbsoluteStageFactorGettersInterface
class FredlundStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getAFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_FREDLUND_XING_A", self.propertyID], proxyArgumentIndices=[1])
	def getBFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_FREDLUND_XING_B", self.propertyID], proxyArgumentIndices=[1])
	def getCFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_FREDLUND_XING_C", self.propertyID], proxyArgumentIndices=[1])
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
class FredlundDefinedStageFactor(FredlundStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setAFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_FREDLUND_XING_A", value, self.propertyID], proxyArgumentIndices=[2])
	def setBFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_FREDLUND_XING_B", value, self.propertyID], proxyArgumentIndices=[2])
	def setCFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_FREDLUND_XING_C", value, self.propertyID], proxyArgumentIndices=[2])
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
class Fredlund(PropertyProxy):
	"""
	Attributes:
		stageFactorInterface (AbsoluteStageFactorGettersInterface[FredlundDefinedStageFactor, FredlundStageFactor]): Reference object for modifying stage factor property.

	Examples:
		:ref:`Hydraulic Property FEAGroundwater Example`
	
	"""
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		super().__init__(client, ID, documentProxyID)
		self.stageFactorInterface = AbsoluteStageFactorGettersInterface[FredlundDefinedStageFactor, FredlundStageFactor](self._client, stageFactorInterfaceID, ID, FredlundDefinedStageFactor, FredlundStageFactor)
	def getA(self) -> float:
		return self._getDoubleProperty("MP_FREDLUND_XING_A")
	def setA(self, value: float):
		return self._setDoubleProperty("MP_FREDLUND_XING_A", value)
	def getB(self) -> float:
		return self._getDoubleProperty("MP_FREDLUND_XING_B")
	def setB(self, value: float):
		return self._setDoubleProperty("MP_FREDLUND_XING_B", value)
	def getC(self) -> float:
		return self._getDoubleProperty("MP_FREDLUND_XING_C")
	def setC(self, value: float):
		return self._setDoubleProperty("MP_FREDLUND_XING_C", value)
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
	def setProperties(self, A : float = None, B : float = None, C : float = None, Ks : float = None, WCInputType : WCInputType = None, WCSat : float = None, WCRes : float = None, DoSSat : float = None, DoSRes : float = None):
		if A is not None:
			self._setDoubleProperty("MP_FREDLUND_XING_A", A)
		if B is not None:
			self._setDoubleProperty("MP_FREDLUND_XING_B", B)
		if C is not None:
			self._setDoubleProperty("MP_FREDLUND_XING_C", C)
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
		"B" : self.getB(), 
		"C" : self.getC(), 
		"Ks" : self.getKs(), 
		"WCInputType" : self.getWCInputType(), 
		"WCSat" : self.getWCSat(), 
		"WCRes" : self.getWCRes(), 
		"DoSSat" : self.getDoSSat(), 
		"DoSRes" : self.getDoSRes(), 
		}
