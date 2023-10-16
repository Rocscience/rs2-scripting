from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class ShearNormalFunction(PropertyProxy):
	def getShearNormalFunction(self) -> int:
		return int(self._getIntProperty("MP_SHEAR_NORMAL_FUNCTION"))
	def setShearNormalFunction(self, value: int):
		return self._setIntProperty("MP_SHEAR_NORMAL_FUNCTION", value)
	def getApplySSRShearStrengthReduction(self) -> bool:
		return self._getBoolProperty("MP_APPLY_SSR")
	def setApplySSRShearStrengthReduction(self, value: bool):
		return self._setBoolProperty("MP_APPLY_SSR", value)
	def setProperties(self, ShearNormalFunction : int = None, ApplySSRShearStrengthReduction : bool = None):
		if ShearNormalFunction is not None:
			self._setIntProperty("MP_SHEAR_NORMAL_FUNCTION", ShearNormalFunction)
		if ApplySSRShearStrengthReduction is not None:
			self._setBoolProperty("MP_APPLY_SSR", ApplySSRShearStrengthReduction)
	def getProperties(self):
		return {
		"ShearNormalFunction" : self.getShearNormalFunction(), 
		"ApplySSRShearStrengthReduction" : self.getApplySSRShearStrengthReduction(), 
		}
