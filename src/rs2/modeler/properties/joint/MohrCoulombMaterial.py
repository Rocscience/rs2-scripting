from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.AbsoluteStageFactorInterface import AbsoluteStageFactorInterface
class MohrCoulombMaterialStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getTensileStrengthFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_TENSILE_STRENGTH", self.propertyID], proxyArgumentIndices=[1])
	def getPeakFrictionAngleFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_PEAK_FRICTION_ANGLE", self.propertyID], proxyArgumentIndices=[1])
	def getPeakCohesionFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_PEAK_COHESION", self.propertyID], proxyArgumentIndices=[1])
	def getResTensileStrengthFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_TENSILE_STRENGTH_RES", self.propertyID], proxyArgumentIndices=[1])
	def getResCohesionFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_COHESION_RES", self.propertyID], proxyArgumentIndices=[1])
	def getResFrictionAngleFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_FRICTION_ANGLE_RES", self.propertyID], proxyArgumentIndices=[1])
	def getDilationAngleFactor(self) -> float:
		return self._callFunction("__getattribute__", ["m_dilation_angle"])
	def getJointPermeableFactor(self) -> bool:
		return self._callFunction("__getattribute__", ["m_joint_permeable_factor"])
class MohrCoulombMaterialDefinedStageFactor(MohrCoulombMaterialStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setTensileStrengthFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_TENSILE_STRENGTH", value, self.propertyID], proxyArgumentIndices=[2])
	def setPeakFrictionAngleFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_PEAK_FRICTION_ANGLE", value, self.propertyID], proxyArgumentIndices=[2])
	def setPeakCohesionFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_PEAK_COHESION", value, self.propertyID], proxyArgumentIndices=[2])
	def setResTensileStrengthFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_TENSILE_STRENGTH_RES", value, self.propertyID], proxyArgumentIndices=[2])
	def setResCohesionFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_COHESION_RES", value, self.propertyID], proxyArgumentIndices=[2])
	def setResFrictionAngleFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_FRICTION_ANGLE_RES", value, self.propertyID], proxyArgumentIndices=[2])
	def setDilationAngleFactor(self, dilationAngleFactor: float):
		return self._callFunction("setDilationAngle", [dilationAngleFactor])
	def setJointPermeableFactor(self, Permeable: bool):
		return self._callFunction("setJointPermeableFactor", [Permeable])
class MohrCoulombMaterial(PropertyProxy):
	"""
	Attributes:
		stageFactorInterface (AbsoluteStageFactorInterface[MohrCoulombMaterialDefinedStageFactor, MohrCoulombMaterialStageFactor]): Reference object for modifying stage factor property.

	Examples:
		:ref:`Material Joint Stage Factor Example`
	
	"""
	def __init__(self, client : Client, ID, documentProxyID):
		super().__init__(client, ID, documentProxyID)
		stageFactorInterfaceID = self._callFunction("getStageFactorInterface", [], keepReturnValueReference=True)
		self.stageFactorInterface = AbsoluteStageFactorInterface[MohrCoulombMaterialDefinedStageFactor, MohrCoulombMaterialStageFactor](self._client, stageFactorInterfaceID, ID, MohrCoulombMaterialDefinedStageFactor, MohrCoulombMaterialStageFactor)
	def getTensileStrength(self) -> float:
		return self._getDoubleProperty("JP_TENSILE_STRENGTH")
	def setTensileStrength(self, value: float):
		return self._setDoubleProperty("JP_TENSILE_STRENGTH", value)
	def getPeakFrictionAngle(self) -> float:
		return self._getDoubleProperty("JP_PEAK_FRICTION_ANGLE")
	def setPeakFrictionAngle(self, value: float):
		return self._setDoubleProperty("JP_PEAK_FRICTION_ANGLE", value)
	def getPeakCohesion(self) -> float:
		return self._getDoubleProperty("JP_PEAK_COHESION")
	def setPeakCohesion(self, value: float):
		return self._setDoubleProperty("JP_PEAK_COHESION", value)
	def getResidualStrength(self) -> bool:
		return self._getBoolProperty("JP_USE_RES_STRENGTH")
	def setResidualStrength(self, value: bool):
		return self._setBoolProperty("JP_USE_RES_STRENGTH", value)
	def getResTensileStrength(self) -> float:
		return self._getDoubleProperty("JP_TENSILE_STRENGTH_RES")
	def setResTensileStrength(self, value: float):
		return self._setDoubleProperty("JP_TENSILE_STRENGTH_RES", value)
	def getResCohesion(self) -> float:
		return self._getDoubleProperty("JP_COHESION_RES")
	def setResCohesion(self, value: float):
		return self._setDoubleProperty("JP_COHESION_RES", value)
	def getResFrictionAngle(self) -> float:
		return self._getDoubleProperty("JP_FRICTION_ANGLE_RES")
	def setResFrictionAngle(self, value: float):
		return self._setDoubleProperty("JP_FRICTION_ANGLE_RES", value)
	def getApplyStageFactors(self) -> bool:
		return self._getBoolProperty("JP_USE_STAGE_JOINT_PROPERTIES")
	def setApplyStageFactors(self, value: bool):
		return self._setBoolProperty("JP_USE_STAGE_JOINT_PROPERTIES", value)
	def setDilationAngle(self, dilationAngle: float):
		return self._callFunction("setMohrDilationAngle", [dilationAngle])
	def getDilationAngle(self) -> float:
		return self._callFunction("__getattribute__", ["mohr_dilation_angle"])
	def setProperties(self, TensileStrength : float = None, PeakFrictionAngle : float = None, PeakCohesion : float = None, ResidualStrength : bool = None, ResTensileStrength : float = None, ResCohesion : float = None, ResFrictionAngle : float = None, ApplyStageFactors : bool = None):
		if TensileStrength is not None:
			self._setDoubleProperty("JP_TENSILE_STRENGTH", TensileStrength)
		if PeakFrictionAngle is not None:
			self._setDoubleProperty("JP_PEAK_FRICTION_ANGLE", PeakFrictionAngle)
		if PeakCohesion is not None:
			self._setDoubleProperty("JP_PEAK_COHESION", PeakCohesion)
		if ResidualStrength is not None:
			self._setBoolProperty("JP_USE_RES_STRENGTH", ResidualStrength)
		if ResTensileStrength is not None:
			self._setDoubleProperty("JP_TENSILE_STRENGTH_RES", ResTensileStrength)
		if ResCohesion is not None:
			self._setDoubleProperty("JP_COHESION_RES", ResCohesion)
		if ResFrictionAngle is not None:
			self._setDoubleProperty("JP_FRICTION_ANGLE_RES", ResFrictionAngle)
		if ApplyStageFactors is not None:
			self._setBoolProperty("JP_USE_STAGE_JOINT_PROPERTIES", ApplyStageFactors)
	def getProperties(self):
		return {
		"TensileStrength" : self.getTensileStrength(), 
		"PeakFrictionAngle" : self.getPeakFrictionAngle(), 
		"PeakCohesion" : self.getPeakCohesion(), 
		"ResidualStrength" : self.getResidualStrength(), 
		"ResTensileStrength" : self.getResTensileStrength(), 
		"ResCohesion" : self.getResCohesion(), 
		"ResFrictionAngle" : self.getResFrictionAngle(), 
		"ApplyStageFactors" : self.getApplyStageFactors(), 
		}
