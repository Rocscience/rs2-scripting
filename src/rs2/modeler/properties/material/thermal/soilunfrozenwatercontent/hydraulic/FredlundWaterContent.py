from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class FredlundWaterContent(PropertyProxy):
	def getA(self) -> float:
		return self._getDoubleProperty("MP_FREDLUND_XING_A_THERMAL")
	def setA(self, value: float):
		return self._setDoubleProperty("MP_FREDLUND_XING_A_THERMAL", value)
	def getB(self) -> float:
		return self._getDoubleProperty("MP_FREDLUND_XING_B_THERMAL")
	def setB(self, value: float):
		return self._setDoubleProperty("MP_FREDLUND_XING_B_THERMAL", value)
	def getC(self) -> float:
		return self._getDoubleProperty("MP_FREDLUND_XING_C_THERMAL")
	def setC(self, value: float):
		return self._setDoubleProperty("MP_FREDLUND_XING_C_THERMAL", value)
	def setProperties(self, A : float = None, B : float = None, C : float = None):
		if A is not None:
			self._setDoubleProperty("MP_FREDLUND_XING_A_THERMAL", A)
		if B is not None:
			self._setDoubleProperty("MP_FREDLUND_XING_B_THERMAL", B)
		if C is not None:
			self._setDoubleProperty("MP_FREDLUND_XING_C_THERMAL", C)
	def getProperties(self):
		return {
		"A" : self.getA(), 
		"B" : self.getB(), 
		"C" : self.getC(), 
		}
