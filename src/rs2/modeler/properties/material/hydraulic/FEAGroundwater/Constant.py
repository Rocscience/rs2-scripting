from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.AbsoluteStageFactorGettersInterface import AbsoluteStageFactorGettersInterface
class ConstantStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getWCCurveSlopeFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_WC_SLOPE", self.propertyID], proxyArgumentIndices=[1])
class ConstantDefinedStageFactor(ConstantStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setWCCurveSlopeFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_WC_SLOPE", value, self.propertyID], proxyArgumentIndices=[2])
class Constant(PropertyProxy):
	"""
	Attributes:
		stageFactorInterface (AbsoluteStageFactorGettersInterface[ConstantDefinedStageFactor, ConstantStageFactor]): Reference object for modifying stage factor property.

	Examples:
		:ref:`Hydraulic Property FEAGroundwater Example`
	
	"""
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		super().__init__(client, ID, documentProxyID)
		self.stageFactorInterface = AbsoluteStageFactorGettersInterface[ConstantDefinedStageFactor, ConstantStageFactor](self._client, stageFactorInterfaceID, ID, ConstantDefinedStageFactor, ConstantStageFactor)
	def getUseCV(self) -> bool:
		return self._getBoolProperty("MP_USE_CV")
	def setUseCV(self, value: bool):
		return self._setBoolProperty("MP_USE_CV", value)
	def getCV(self) -> float:
		return self._getDoubleProperty("MP_CV")
	def setCV(self, value: float):
		return self._setDoubleProperty("MP_CV", value)
	def getInitialK(self) -> float:
		return self._getDoubleProperty("MP_INITIAL_K")
	def setInitialK(self, value: float):
		return self._setDoubleProperty("MP_INITIAL_K", value)
	def getWCCurveSlope(self) -> float:
		return self._getDoubleProperty("MP_WC_SLOPE")
	def setWCCurveSlope(self, value: float):
		return self._setDoubleProperty("MP_WC_SLOPE", value)
	def setProperties(self, UseCV : bool = None, CV : float = None, InitialK : float = None, WCCurveSlope : float = None):
		if UseCV is not None:
			self._setBoolProperty("MP_USE_CV", UseCV)
		if CV is not None:
			self._setDoubleProperty("MP_CV", CV)
		if InitialK is not None:
			self._setDoubleProperty("MP_INITIAL_K", InitialK)
		if WCCurveSlope is not None:
			self._setDoubleProperty("MP_WC_SLOPE", WCCurveSlope)
	def getProperties(self):
		return {
		"UseCV" : self.getUseCV(), 
		"CV" : self.getCV(), 
		"InitialK" : self.getInitialK(), 
		"WCCurveSlope" : self.getWCCurveSlope(), 
		}
