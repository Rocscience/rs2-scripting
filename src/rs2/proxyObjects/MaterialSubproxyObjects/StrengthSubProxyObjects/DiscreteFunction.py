from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class DiscreteFunction(PropertyProxy):
	def getApplySSRShearStrengthReduction(self) -> bool:
		return self._getBoolProperty("MP_APPLY_SSR")
	def setApplySSRShearStrengthReduction(self, value: bool):
		return self._setBoolProperty("MP_APPLY_SSR", value)
	def setSelectedDiscreteFunctionByName(self, name: str):
		return self._callFunction("setSelectedDiscreteFunctionByName", [name])
	def getSelectedDiscreteFunctionName(self) -> str:
		return self._callFunction("getSelectedDiscreteFunctionName", [])
	def setProperties(self, ApplySSRShearStrengthReduction : bool = None):
		if ApplySSRShearStrengthReduction is not None:
			self._setBoolProperty("MP_APPLY_SSR", ApplySSRShearStrengthReduction)
	def getProperties(self):
		return {
		"ApplySSRShearStrengthReduction" : self.getApplySSRShearStrengthReduction(), 
		}
