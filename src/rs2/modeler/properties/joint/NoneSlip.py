from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.AbsoluteStageFactorInterface import AbsoluteStageFactorInterface
class NoneSlipStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getNormalStiffnessFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_NORMAL_STIFFNESS", self.propertyID], proxyArgumentIndices=[1])
	def getShearStiffnessFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_SHEAR_STIFFNESS", self.propertyID], proxyArgumentIndices=[1])
	def getAdditionalPressureInsideJointFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_ADDITIONAL_PRESSURE", self.propertyID], proxyArgumentIndices=[1])
	def getGroundwaterPressureFactor(self) -> float:
		return self._callFunction("__getattribute__", ["m_groundwater_pressure_factor"])
	def getJointPermeableFactor(self) -> bool:
		return self._callFunction("__getattribute__", ["m_joint_permeable_factor"])
class NoneSlipDefinedStageFactor(NoneSlipStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setNormalStiffnessFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_NORMAL_STIFFNESS", value, self.propertyID], proxyArgumentIndices=[2])
	def setShearStiffnessFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_SHEAR_STIFFNESS", value, self.propertyID], proxyArgumentIndices=[2])
	def setAdditionalPressureInsideJointFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_ADDITIONAL_PRESSURE", value, self.propertyID], proxyArgumentIndices=[2])
	def setGroundwaterPressureFactor(self, GroundWaterPressure: float):
		return self._callFunction("setGroundwaterPressureFactor", [GroundWaterPressure])
	def setJointPermeableFactor(self, Permeable: bool):
		return self._callFunction("setJointPermeableFactor", [Permeable])
class NoneSlip(PropertyProxy):
	"""
	Attributes:
		stageFactorInterface (AbsoluteStageFactorInterface[NoneSlipDefinedStageFactor, NoneSlipStageFactor]): Reference object for modifying stage factor property.

	Examples:
		:ref:`Joint Stage Factor Example`
	
	"""
	def __init__(self, client : Client, ID, documentProxyID):
		super().__init__(client, ID, documentProxyID)
		stageFactorInterfaceID = self._callFunction("getStageFactorInterface", [], keepReturnValueReference=True)
		self.stageFactorInterface = AbsoluteStageFactorInterface[NoneSlipDefinedStageFactor, NoneSlipStageFactor](self._client, stageFactorInterfaceID, ID, NoneSlipDefinedStageFactor, NoneSlipStageFactor)
	def getNormalStiffness(self) -> float:
		return self._getDoubleProperty("JP_NORMAL_STIFFNESS")
	def setNormalStiffness(self, value: float):
		return self._setDoubleProperty("JP_NORMAL_STIFFNESS", value)
	def getShearStiffness(self) -> float:
		return self._getDoubleProperty("JP_SHEAR_STIFFNESS")
	def setShearStiffness(self, value: float):
		return self._setDoubleProperty("JP_SHEAR_STIFFNESS", value)
	def getApplyPorePressure(self) -> bool:
		return self._getBoolProperty("JP_USE_GROUNDWATER_PORE_PRESSURE")
	def setApplyPorePressure(self, value: bool):
		return self._setBoolProperty("JP_USE_GROUNDWATER_PORE_PRESSURE", value)
	def getApplyAdditionalPressureInsideJoint(self) -> bool:
		return self._getBoolProperty("JP_USE_ADDITIONAL_PRESSURE")
	def setApplyAdditionalPressureInsideJoint(self, value: bool):
		return self._setBoolProperty("JP_USE_ADDITIONAL_PRESSURE", value)
	def getAdditionalPressureType(self) -> AdditionalPressureType:
		return AdditionalPressureType(self._getEnumEJointWaterPressureTypeProperty("JP_ADDITIONAL_TYPE"))
	def setAdditionalPressureType(self, value: AdditionalPressureType):
		return self._setEnumEJointWaterPressureTypeProperty("JP_ADDITIONAL_TYPE", value)
	def getAdditionalPressureInsideJoint(self) -> float:
		return self._getDoubleProperty("JP_ADDITIONAL_PRESSURE")
	def setAdditionalPressureInsideJoint(self, value: float):
		return self._setDoubleProperty("JP_ADDITIONAL_PRESSURE", value)
	def getApplyPressureToLinerSideOnly(self) -> bool:
		return self._getBoolProperty("JP_USE_PRESSURE_TO_LINER_SIDE_ONLY")
	def setApplyPressureToLinerSideOnly(self, value: bool):
		return self._setBoolProperty("JP_USE_PRESSURE_TO_LINER_SIDE_ONLY", value)
	def getApplyStageFactors(self) -> bool:
		return self._getBoolProperty("JP_USE_STAGE_JOINT_PROPERTIES")
	def setApplyStageFactors(self, value: bool):
		return self._setBoolProperty("JP_USE_STAGE_JOINT_PROPERTIES", value)
	def setPiezoID(self, piezoName: str):
		return self._callFunction("python_setPiezoPressureID", [piezoName])
	def getPiezoID(self):
		return self._callFunction("python_getPiezoPressureID", [])
	def setProperties(self, NormalStiffness : float = None, ShearStiffness : float = None, ApplyPorePressure : bool = None, ApplyAdditionalPressureInsideJoint : bool = None, AdditionalPressureType : AdditionalPressureType = None, AdditionalPressureInsideJoint : float = None, ApplyPressureToLinerSideOnly : bool = None, ApplyStageFactors : bool = None):
		if NormalStiffness is not None:
			self._setDoubleProperty("JP_NORMAL_STIFFNESS", NormalStiffness)
		if ShearStiffness is not None:
			self._setDoubleProperty("JP_SHEAR_STIFFNESS", ShearStiffness)
		if ApplyPorePressure is not None:
			self._setBoolProperty("JP_USE_GROUNDWATER_PORE_PRESSURE", ApplyPorePressure)
		if ApplyAdditionalPressureInsideJoint is not None:
			self._setBoolProperty("JP_USE_ADDITIONAL_PRESSURE", ApplyAdditionalPressureInsideJoint)
		if AdditionalPressureType is not None:
			self._setEnumEJointWaterPressureTypeProperty("JP_ADDITIONAL_TYPE", AdditionalPressureType)
		if AdditionalPressureInsideJoint is not None:
			self._setDoubleProperty("JP_ADDITIONAL_PRESSURE", AdditionalPressureInsideJoint)
		if ApplyPressureToLinerSideOnly is not None:
			self._setBoolProperty("JP_USE_PRESSURE_TO_LINER_SIDE_ONLY", ApplyPressureToLinerSideOnly)
		if ApplyStageFactors is not None:
			self._setBoolProperty("JP_USE_STAGE_JOINT_PROPERTIES", ApplyStageFactors)
	def getProperties(self):
		return {
		"NormalStiffness" : self.getNormalStiffness(), 
		"ShearStiffness" : self.getShearStiffness(), 
		"ApplyPorePressure" : self.getApplyPorePressure(), 
		"ApplyAdditionalPressureInsideJoint" : self.getApplyAdditionalPressureInsideJoint(), 
		"AdditionalPressureType" : self.getAdditionalPressureType(), 
		"AdditionalPressureInsideJoint" : self.getAdditionalPressureInsideJoint(), 
		"ApplyPressureToLinerSideOnly" : self.getApplyPressureToLinerSideOnly(), 
		"ApplyStageFactors" : self.getApplyStageFactors(), 
		}
