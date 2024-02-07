from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class ShearNormalFunction(PropertyProxy):
	def getApplySSRShearStrengthReduction(self) -> bool:
		return self._getBoolProperty("MP_APPLY_SSR")
	def setApplySSRShearStrengthReduction(self, value: bool):
		return self._setBoolProperty("MP_APPLY_SSR", value)
	def setShearNormalFunctionByName(self, name: str):
		return self._callFunction("setShearNormalFunctionByName", [name])
	def getShearNormalFunctionName(self) -> str:
		return self._callFunction("getShearNormalFunctionName", [])
	def setProperties(self, ApplySSRShearStrengthReduction : bool = None):
		if ApplySSRShearStrengthReduction is not None:
			self._setBoolProperty("MP_APPLY_SSR", ApplySSRShearStrengthReduction)
	def getProperties(self):
		return {
		"ApplySSRShearStrengthReduction" : self.getApplySSRShearStrengthReduction(), 
		}
