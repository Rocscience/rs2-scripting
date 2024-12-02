from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.AbsoluteStageFactorInterface import AbsoluteStageFactorInterface
class ForceDisplacementStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getXFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["PFP_FORCE_DISPLACEMENT_X", self.propertyID], proxyArgumentIndices=[1])
	def getYFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["PFP_FORCE_DISPLACEMENT_Y", self.propertyID], proxyArgumentIndices=[1])
class ForceDisplacementDefinedStageFactor(ForceDisplacementStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setXFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["PFP_FORCE_DISPLACEMENT_X", value, self.propertyID], proxyArgumentIndices=[2])
	def setYFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["PFP_FORCE_DISPLACEMENT_Y", value, self.propertyID], proxyArgumentIndices=[2])
class ForceDisplacement(PropertyProxy):
	"""
	Attributes:
		stageFactorInterface (AbsoluteStageFactorInterface[ForceDisplacementDefinedStageFactor, ForceDisplacementStageFactor]): Reference object for modifying stage factor property.

	Examples:
		:ref:`Pile Stage Factor Example`
	
	"""
	def __init__(self, client : Client, ID, documentProxyID):
		super().__init__(client, ID, documentProxyID)
		stageFactorInterfaceID = self._callFunction("getStageFactorInterface", [], keepReturnValueReference=True)
		self.stageFactorInterface = AbsoluteStageFactorInterface[ForceDisplacementDefinedStageFactor, ForceDisplacementStageFactor](self._client, stageFactorInterfaceID, ID, ForceDisplacementDefinedStageFactor, ForceDisplacementStageFactor)
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
