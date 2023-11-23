from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
from rs2.ProxyObject import ProxyObject
class ForceDisplacementStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, property : PropertyProxy):
		super().__init__(client, ID)
		self.property = property
	def getXFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["PFP_FORCE_DISPLACEMENT_X", self.property._ID], proxyArgumentIndices=[1])
	def setXFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["PFP_FORCE_DISPLACEMENT_X", value, self.property._ID], proxyArgumentIndices=[2])
	def getYFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["PFP_FORCE_DISPLACEMENT_Y", self.property._ID], proxyArgumentIndices=[1])
	def setYFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["PFP_FORCE_DISPLACEMENT_Y", value, self.property._ID], proxyArgumentIndices=[2])
class ForceDisplacement(PropertyProxy):
	def getApply(self) -> PileEndCondition:
		return PileEndCondition(self._getEnumEPileEndConditionProperty("PFP_FORCE_DISPLACEMENT_TYPE"))
	def setApply(self, value: PileEndCondition):
		return self._setEnumEPileEndConditionProperty("PFP_FORCE_DISPLACEMENT_TYPE", value)
	def getApplyOn(self) -> PileForceApplicationPoint:
		return PileForceApplicationPoint(self._getEnumEPileForceDisplacemtnApplicationPointProperty("PFP_FORCE_DISPLACEMENT_APPLY_ON"))
	def setApplyOn(self, value: PileForceApplicationPoint):
		return self._setEnumEPileForceDisplacemtnApplicationPointProperty("PFP_FORCE_DISPLACEMENT_APPLY_ON", value)
	def getX(self) -> float:
		return self._getDoubleProperty("PFP_FORCE_DISPLACEMENT_X")
	def setX(self, value: float):
		return self._setDoubleProperty("PFP_FORCE_DISPLACEMENT_X", value)
	def getY(self) -> float:
		return self._getDoubleProperty("PFP_FORCE_DISPLACEMENT_Y")
	def setY(self, value: float):
		return self._setDoubleProperty("PFP_FORCE_DISPLACEMENT_Y", value)
	def getStageFactors(self) -> dict[int, ForceDisplacementStageFactor]:
		"""
		Returns a map of stage factors. The key is the absolute or relative stage at which the stage factor is applied. The value is the stage factor object
		"""
		stageFactorReferenceIds = self._callFunction('getStageFactors', [], keepReturnValueReference=True)
		stageFactors = {}
		for stageKey in stageFactorReferenceIds :
			stageFactors[stageKey] = ForceDisplacementStageFactor(self._client, stageFactorReferenceIds[stageKey], self)
		return stageFactors
	def setProperties(self, Apply : PileEndCondition = None, ApplyOn : PileForceApplicationPoint = None, X : float = None, Y : float = None):
		if Apply is not None:
			self._setEnumEPileEndConditionProperty("PFP_FORCE_DISPLACEMENT_TYPE", Apply)
		if ApplyOn is not None:
			self._setEnumEPileForceDisplacemtnApplicationPointProperty("PFP_FORCE_DISPLACEMENT_APPLY_ON", ApplyOn)
		if X is not None:
			self._setDoubleProperty("PFP_FORCE_DISPLACEMENT_X", X)
		if Y is not None:
			self._setDoubleProperty("PFP_FORCE_DISPLACEMENT_Y", Y)
	def getProperties(self):
		return {
		"Apply" : self.getApply(), 
		"ApplyOn" : self.getApplyOn(), 
		"X" : self.getX(), 
		"Y" : self.getY(), 
		}
