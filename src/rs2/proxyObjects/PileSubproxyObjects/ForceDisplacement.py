from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
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
