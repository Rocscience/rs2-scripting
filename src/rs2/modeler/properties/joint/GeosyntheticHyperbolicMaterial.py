from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.AbsoluteStageFactorInterface import AbsoluteStageFactorInterface
class GeosyntheticHyperbolicMaterialStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getPeakAdhesionAtSigninfFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_PEAK_ADHESION", self.propertyID], proxyArgumentIndices=[1])
	def getPeakFrictionAngleAtSign0Factor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_PEAK_FRICTION_ANGLE_GEOSYN", self.propertyID], proxyArgumentIndices=[1])
	def getResAdhesionAtSigninfFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_ADHESION_RES", self.propertyID], proxyArgumentIndices=[1])
	def getResFrictionAngleAtSign0Factor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_FRICTION_ANGLE_RES_GEOSYN", self.propertyID], proxyArgumentIndices=[1])
	def getDilationRatioFactor(self) -> float:
		return self._callFunction("__getattribute__", ["m_dilation_ratio"])
	def getJointPermeableFactor(self) -> bool:
		return self._callFunction("__getattribute__", ["m_joint_permeable_factor"])
class GeosyntheticHyperbolicMaterialDefinedStageFactor(GeosyntheticHyperbolicMaterialStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setPeakAdhesionAtSigninfFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_PEAK_ADHESION", value, self.propertyID], proxyArgumentIndices=[2])
	def setPeakFrictionAngleAtSign0Factor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_PEAK_FRICTION_ANGLE_GEOSYN", value, self.propertyID], proxyArgumentIndices=[2])
	def setResAdhesionAtSigninfFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_ADHESION_RES", value, self.propertyID], proxyArgumentIndices=[2])
	def setResFrictionAngleAtSign0Factor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_FRICTION_ANGLE_RES_GEOSYN", value, self.propertyID], proxyArgumentIndices=[2])
	def setDilationRatioFactor(self, dilationRatioFactor: float):
		return self._callFunction("setDilationRatio", [dilationRatioFactor])
	def setJointPermeableFactor(self, Permeable: bool):
		return self._callFunction("setJointPermeableFactor", [Permeable])
class GeosyntheticHyperbolicMaterial(PropertyProxy):
	"""
	Attributes:
		stageFactorInterface (AbsoluteStageFactorInterface[GeosyntheticHyperbolicMaterialDefinedStageFactor, GeosyntheticHyperbolicMaterialStageFactor]): Reference object for modifying stage factor property.

	Examples:
		:ref:`Material Joint Stage Factor Example`
	
	"""
	def __init__(self, client : Client, ID, documentProxyID):
		super().__init__(client, ID, documentProxyID)
		stageFactorInterfaceID = self._callFunction("getStageFactorInterface", [], keepReturnValueReference=True)
		self.stageFactorInterface = AbsoluteStageFactorInterface[GeosyntheticHyperbolicMaterialDefinedStageFactor, GeosyntheticHyperbolicMaterialStageFactor](self._client, stageFactorInterfaceID, ID, GeosyntheticHyperbolicMaterialDefinedStageFactor, GeosyntheticHyperbolicMaterialStageFactor)
	def getPeakAdhesionAtSigninf(self) -> float:
		return self._getDoubleProperty("JP_PEAK_ADHESION")
	def setPeakAdhesionAtSigninf(self, value: float):
		return self._setDoubleProperty("JP_PEAK_ADHESION", value)
	def getPeakFrictionAngleAtSign0(self) -> float:
		return self._getDoubleProperty("JP_PEAK_FRICTION_ANGLE_GEOSYN")
	def setPeakFrictionAngleAtSign0(self, value: float):
		return self._setDoubleProperty("JP_PEAK_FRICTION_ANGLE_GEOSYN", value)
	def getResAdhesionAtSigninf(self) -> float:
		return self._getDoubleProperty("JP_ADHESION_RES")
	def setResAdhesionAtSigninf(self, value: float):
		return self._setDoubleProperty("JP_ADHESION_RES", value)
	def getResFrictionAngleAtSign0(self) -> float:
		return self._getDoubleProperty("JP_FRICTION_ANGLE_RES_GEOSYN")
	def setResFrictionAngleAtSign0(self, value: float):
		return self._setDoubleProperty("JP_FRICTION_ANGLE_RES_GEOSYN", value)
	def getApplyStageFactors(self) -> bool:
		return self._getBoolProperty("JP_USE_STAGE_JOINT_PROPERTIES")
	def setApplyStageFactors(self, value: bool):
		return self._setBoolProperty("JP_USE_STAGE_JOINT_PROPERTIES", value)
	def getTensileStrength(self) -> float:
		return self._getDoubleProperty("JP_TENSILE_GEOSYN")
	def setTensileStrength(self, value: float):
		return self._setDoubleProperty("JP_TENSILE_GEOSYN", value)
	def setDilationRatio(self, dilationRatio: float):
		return self._callFunction("setDilationRatio", [dilationRatio])
	def getDilationRatio(self) -> float:
		return self._callFunction("__getattribute__", ["dilation_ratio"])
	def setProperties(self, PeakAdhesionAtSigninf : float = None, PeakFrictionAngleAtSign0 : float = None, ResAdhesionAtSigninf : float = None, ResFrictionAngleAtSign0 : float = None, ApplyStageFactors : bool = None, TensileStrength : float = None):
		if PeakAdhesionAtSigninf is not None:
			self._setDoubleProperty("JP_PEAK_ADHESION", PeakAdhesionAtSigninf)
		if PeakFrictionAngleAtSign0 is not None:
			self._setDoubleProperty("JP_PEAK_FRICTION_ANGLE_GEOSYN", PeakFrictionAngleAtSign0)
		if ResAdhesionAtSigninf is not None:
			self._setDoubleProperty("JP_ADHESION_RES", ResAdhesionAtSigninf)
		if ResFrictionAngleAtSign0 is not None:
			self._setDoubleProperty("JP_FRICTION_ANGLE_RES_GEOSYN", ResFrictionAngleAtSign0)
		if ApplyStageFactors is not None:
			self._setBoolProperty("JP_USE_STAGE_JOINT_PROPERTIES", ApplyStageFactors)
		if TensileStrength is not None:
			self._setDoubleProperty("JP_TENSILE_GEOSYN", TensileStrength)
	def getProperties(self):
		return {
		"PeakAdhesionAtSigninf" : self.getPeakAdhesionAtSigninf(), 
		"PeakFrictionAngleAtSign0" : self.getPeakFrictionAngleAtSign0(), 
		"ResAdhesionAtSigninf" : self.getResAdhesionAtSigninf(), 
		"ResFrictionAngleAtSign0" : self.getResFrictionAngleAtSign0(), 
		"ApplyStageFactors" : self.getApplyStageFactors(), 
		"TensileStrength" : self.getTensileStrength(), 
		}
