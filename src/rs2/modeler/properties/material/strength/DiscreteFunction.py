from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.AbsoluteStageFactorGettersInterface import AbsoluteStageFactorGettersInterface
class DiscreteFunctionStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getPeakTensileStrengthFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_PEAK_TENSILE_STRENGTH", self.propertyID], proxyArgumentIndices=[1])
	def getResidualTensileStrengthFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_TENSILE_STRENGTH_RES", self.propertyID], proxyArgumentIndices=[1])
class DiscreteFunctionDefinedStageFactor(DiscreteFunctionStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setPeakTensileStrengthFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_PEAK_TENSILE_STRENGTH", value, self.propertyID], proxyArgumentIndices=[2])
	def setResidualTensileStrengthFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_TENSILE_STRENGTH_RES", value, self.propertyID], proxyArgumentIndices=[2])
class DiscreteFunction(PropertyProxy):
	"""
	Attributes:
		stageFactorInterface (AbsoluteStageFactorGettersInterface[DiscreteFunctionDefinedStageFactor, DiscreteFunctionStageFactor]): Reference object for modifying stage factor property.

	Examples:
		:ref:`Material Property Strength Example`
	
	"""
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		super().__init__(client, ID, documentProxyID)
		self.stageFactorInterface = AbsoluteStageFactorGettersInterface[DiscreteFunctionDefinedStageFactor, DiscreteFunctionStageFactor](self._client, stageFactorInterfaceID, ID, DiscreteFunctionDefinedStageFactor, DiscreteFunctionStageFactor)
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
