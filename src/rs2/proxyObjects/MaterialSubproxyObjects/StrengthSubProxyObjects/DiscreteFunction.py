from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class DiscreteFunction(PropertyProxy):
	def getDiscreteFunction(self) -> int:
		return int(self._getIntProperty("MP_DISCRETE_FUNCTION"))
	def setDiscreteFunction(self, value: int):
		return self._setIntProperty("MP_DISCRETE_FUNCTION", value)
	def getApplySSRShearStrengthReduction(self) -> bool:
		return self._getBoolProperty("MP_APPLY_SSR")
	def setApplySSRShearStrengthReduction(self, value: bool):
		return self._setBoolProperty("MP_APPLY_SSR", value)
	def setProperties(self, DiscreteFunction : int = None, ApplySSRShearStrengthReduction : bool = None):
		if DiscreteFunction is not None:
			self._setIntProperty("MP_DISCRETE_FUNCTION", DiscreteFunction)
		if ApplySSRShearStrengthReduction is not None:
			self._setBoolProperty("MP_APPLY_SSR", ApplySSRShearStrengthReduction)
	def getProperties(self):
		return {
		"DiscreteFunction" : self.getDiscreteFunction(), 
		"ApplySSRShearStrengthReduction" : self.getApplySSRShearStrengthReduction(), 
		}
