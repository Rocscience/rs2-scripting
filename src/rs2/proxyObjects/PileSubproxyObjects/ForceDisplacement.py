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
	def getYFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["PFP_FORCE_DISPLACEMENT_Y", self.property._ID], proxyArgumentIndices=[1])
class ForceDisplacementDefinedStageFactor(ForceDisplacementStageFactor):
	def __init__(self, client : Client, ID, property : PropertyProxy):
		super().__init__(client, ID, property)
	def setXFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["PFP_FORCE_DISPLACEMENT_X", value, self.property._ID], proxyArgumentIndices=[2])
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
	def getDefinedStageFactors(self) -> dict[int, ForceDisplacementDefinedStageFactor]:
		"""
		Returns a map of stage factors. The key is the absolute or relative stage at which the stage factor is applied. The value is the stage factor object
		"""
		stageFactorReferenceIds = self._callFunction('getDefinedStageFactors', [], keepReturnValueReference=True)
		stageFactors = {}
		for stageKey in stageFactorReferenceIds :
			stageFactors[stageKey] = ForceDisplacementDefinedStageFactor(self._client, stageFactorReferenceIds[stageKey], self)
		return stageFactors
	def getStageFactor(self, stage: int) -> ForceDisplacementStageFactor:
		"""
		Returns the stage factor for the given stage.
		"""
		factorReferenceID = self._callFunction('getStageFactor', [stage], keepReturnValueReference=True)
		return ForceDisplacementStageFactor(self._client, factorReferenceID, self)
	def createStageFactor(self, stage: int) -> ForceDisplacementDefinedStageFactor:
		"""
		Creates a stage factor for the given stage.

		NOTE: Invalidates any existing stage factor proxies. Get them again using getDefinedStageFactors or getStageFactor.
		"""
		factorReferenceID = self._callFunction('createStageFactor', [stage], keepReturnValueReference=True)
		return ForceDisplacementDefinedStageFactor(self._client, factorReferenceID, self)
	def setDefinedStageFactors(self, stageFactors: dict[int,ForceDisplacementStageFactor]):
		"""
		Sets the defined stage factors to those given.

		NOTE: Invalidates any existing stage factor proxies. Get them again using getDefinedStageFactors or getStageFactor.
		"""
		stageFactorIdMap = {}
		for stage in stageFactors :
			stageFactorIdMap[stage] = stageFactors[stage]._ID
		return self._callFunction("setDefinedStageFactors", [stageFactorIdMap], proxyArgumentIndices = [1])
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
