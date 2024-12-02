from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.AbsoluteStageFactorInterface import AbsoluteStageFactorInterface
class BartonBandisMaterialStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getJCSFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_JCS", self.propertyID], proxyArgumentIndices=[1])
	def getJRCFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_JRC", self.propertyID], proxyArgumentIndices=[1])
	def getResidualFrictionAngleFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_FRICTION_ANGLE_RES_BARTON", self.propertyID], proxyArgumentIndices=[1])
	def getDilationAngleFactor(self) -> float:
		return self._callFunction("__getattribute__", ["m_dilation_angle"])
	def getJointPermeableFactor(self) -> bool:
		return self._callFunction("__getattribute__", ["m_joint_permeable_factor"])
class BartonBandisMaterialDefinedStageFactor(BartonBandisMaterialStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setJCSFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_JCS", value, self.propertyID], proxyArgumentIndices=[2])
	def setJRCFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_JRC", value, self.propertyID], proxyArgumentIndices=[2])
	def setResidualFrictionAngleFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_FRICTION_ANGLE_RES_BARTON", value, self.propertyID], proxyArgumentIndices=[2])
	def setDilationAngleFactor(self, dilationAngleFactor: float):
		return self._callFunction("setDilationAngle", [dilationAngleFactor])
	def setJointPermeableFactor(self, Permeable: bool):
		return self._callFunction("setJointPermeableFactor", [Permeable])
class BartonBandisMaterial(PropertyProxy):
	"""
	Attributes:
		stageFactorInterface (AbsoluteStageFactorInterface[BartonBandisMaterialDefinedStageFactor, BartonBandisMaterialStageFactor]): Reference object for modifying stage factor property.

	Examples:
		:ref:`Material Joint Stage Factor Example`
	
	"""
	def __init__(self, client : Client, ID, documentProxyID):
		super().__init__(client, ID, documentProxyID)
		stageFactorInterfaceID = self._callFunction("getStageFactorInterface", [], keepReturnValueReference=True)
		self.stageFactorInterface = AbsoluteStageFactorInterface[BartonBandisMaterialDefinedStageFactor, BartonBandisMaterialStageFactor](self._client, stageFactorInterfaceID, ID, BartonBandisMaterialDefinedStageFactor, BartonBandisMaterialStageFactor)
	def getJCS(self) -> float:
		return self._getDoubleProperty("JP_JCS")
	def setJCS(self, value: float):
		return self._setDoubleProperty("JP_JCS", value)
	def getJRC(self) -> float:
		return self._getDoubleProperty("JP_JRC")
	def setJRC(self, value: float):
		return self._setDoubleProperty("JP_JRC", value)
	def getResidualFrictionAngle(self) -> float:
		return self._getDoubleProperty("JP_FRICTION_ANGLE_RES_BARTON")
	def setResidualFrictionAngle(self, value: float):
		return self._setDoubleProperty("JP_FRICTION_ANGLE_RES_BARTON", value)
	def getResidualStrength(self) -> bool:
		return self._getBoolProperty("JP_USE_RES_STRENGTH_BARTON")
	def setResidualStrength(self, value: bool):
		return self._setBoolProperty("JP_USE_RES_STRENGTH_BARTON", value)
	def getApplyStageFactors(self) -> bool:
		return self._getBoolProperty("JP_USE_STAGE_JOINT_PROPERTIES")
	def setApplyStageFactors(self, value: bool):
		return self._setBoolProperty("JP_USE_STAGE_JOINT_PROPERTIES", value)
	def setDilationAngle(self, dilationAngle: float):
		return self._callFunction("setMohrDilationAngle", [dilationAngle])
	def getDilationAngle(self) -> float:
		return self._callFunction("__getattribute__", ["mohr_dilation_angle"])
	def setProperties(self, JCS : float = None, JRC : float = None, ResidualFrictionAngle : float = None, ResidualStrength : bool = None, ApplyStageFactors : bool = None):
		if JCS is not None:
			self._setDoubleProperty("JP_JCS", JCS)
		if JRC is not None:
			self._setDoubleProperty("JP_JRC", JRC)
		if ResidualFrictionAngle is not None:
			self._setDoubleProperty("JP_FRICTION_ANGLE_RES_BARTON", ResidualFrictionAngle)
		if ResidualStrength is not None:
			self._setBoolProperty("JP_USE_RES_STRENGTH_BARTON", ResidualStrength)
		if ApplyStageFactors is not None:
			self._setBoolProperty("JP_USE_STAGE_JOINT_PROPERTIES", ApplyStageFactors)
	def getProperties(self):
		return {
		"JCS" : self.getJCS(), 
		"JRC" : self.getJRC(), 
		"ResidualFrictionAngle" : self.getResidualFrictionAngle(), 
		"ResidualStrength" : self.getResidualStrength(), 
		"ApplyStageFactors" : self.getApplyStageFactors(), 
		}
