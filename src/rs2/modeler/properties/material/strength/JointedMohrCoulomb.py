from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.properties.MaterialJointOptions import MaterialJointOptions
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.AbsoluteStageFactorGettersInterface import AbsoluteStageFactorGettersInterface
class JointedMohrCoulombStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getResidualCohesionFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_COHESION_RES", self.propertyID], proxyArgumentIndices=[1])
	def getDilationAngleFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_DILATION_ANGLE", self.propertyID], proxyArgumentIndices=[1])
	def getResidualFrictionAngleFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_FRICTION_ANGLE_RES", self.propertyID], proxyArgumentIndices=[1])
	def getPeakCohesionFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_PEAK_COHESION", self.propertyID], proxyArgumentIndices=[1])
	def getPeakFrictionAngleFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_PEAK_FRICTION_ANGLE", self.propertyID], proxyArgumentIndices=[1])
	def getPeakTensileStrengthFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_PEAK_TENSILE_STRENGTH", self.propertyID], proxyArgumentIndices=[1])
	def getResidualTensileStrengthFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_TENSILE_STRENGTH_RES", self.propertyID], proxyArgumentIndices=[1])
class JointedMohrCoulombDefinedStageFactor(JointedMohrCoulombStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setResidualCohesionFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_COHESION_RES", value, self.propertyID], proxyArgumentIndices=[2])
	def setDilationAngleFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_DILATION_ANGLE", value, self.propertyID], proxyArgumentIndices=[2])
	def setResidualFrictionAngleFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_FRICTION_ANGLE_RES", value, self.propertyID], proxyArgumentIndices=[2])
	def setPeakCohesionFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_PEAK_COHESION", value, self.propertyID], proxyArgumentIndices=[2])
	def setPeakFrictionAngleFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_PEAK_FRICTION_ANGLE", value, self.propertyID], proxyArgumentIndices=[2])
	def setPeakTensileStrengthFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_PEAK_TENSILE_STRENGTH", value, self.propertyID], proxyArgumentIndices=[2])
	def setResidualTensileStrengthFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_TENSILE_STRENGTH_RES", value, self.propertyID], proxyArgumentIndices=[2])
class JointedMohrCoulomb(PropertyProxy):
	"""
	Attributes:
		stageFactorInterface (AbsoluteStageFactorGettersInterface[JointedMohrCoulombDefinedStageFactor, JointedMohrCoulombStageFactor]): Reference object for modifying stage factor property.

	Examples:
		:ref:`Material Property Strength Example`
	
	"""
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		super().__init__(client, ID, documentProxyID)
		self.stageFactorInterface = AbsoluteStageFactorGettersInterface[JointedMohrCoulombDefinedStageFactor, JointedMohrCoulombStageFactor](self._client, stageFactorInterfaceID, ID, JointedMohrCoulombDefinedStageFactor, JointedMohrCoulombStageFactor)
	def getMaterialType(self) -> MaterialType:
		return MaterialType(self._getEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE"))
	def setMaterialType(self, value: MaterialType):
		return self._setEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE", value)
	def getPeakTensileStrength(self) -> float:
		return self._getDoubleProperty("MP_PEAK_TENSILE_STRENGTH")
	def setPeakTensileStrength(self, value: float):
		return self._setDoubleProperty("MP_PEAK_TENSILE_STRENGTH", value)
	def getPeakFrictionAngle(self) -> float:
		return self._getDoubleProperty("MP_PEAK_FRICTION_ANGLE")
	def setPeakFrictionAngle(self, value: float):
		return self._setDoubleProperty("MP_PEAK_FRICTION_ANGLE", value)
	def getPeakCohesion(self) -> float:
		return self._getDoubleProperty("MP_PEAK_COHESION")
	def setPeakCohesion(self, value: float):
		return self._setDoubleProperty("MP_PEAK_COHESION", value)
	def getResidualTensileStrength(self) -> float:
		return self._getDoubleProperty("MP_TENSILE_STRENGTH_RES")
	def setResidualTensileStrength(self, value: float):
		return self._setDoubleProperty("MP_TENSILE_STRENGTH_RES", value)
	def getResidualFrictionAngle(self) -> float:
		return self._getDoubleProperty("MP_FRICTION_ANGLE_RES")
	def setResidualFrictionAngle(self, value: float):
		return self._setDoubleProperty("MP_FRICTION_ANGLE_RES", value)
	def getResidualCohesion(self) -> float:
		return self._getDoubleProperty("MP_COHESION_RES")
	def setResidualCohesion(self, value: float):
		return self._setDoubleProperty("MP_COHESION_RES", value)
	def getDilationAngle(self) -> float:
		return self._getDoubleProperty("MP_DILATION_ANGLE")
	def setDilationAngle(self, value: float):
		return self._setDoubleProperty("MP_DILATION_ANGLE", value)
	def getApplySSRShearStrengthReduction(self) -> bool:
		return self._getBoolProperty("MP_APPLY_SSR")
	def setApplySSRShearStrengthReduction(self, value: bool):
		return self._setBoolProperty("MP_APPLY_SSR", value)
	def getJointOptions(self) -> MaterialJointOptions:
		return MaterialJointOptions(self._client, self._callFunction("getJointOptions", [], keepReturnValueReference = True), self.documentProxyID)
	def setProperties(self, MaterialType : MaterialType = None, PeakTensileStrength : float = None, PeakFrictionAngle : float = None, PeakCohesion : float = None, ResidualTensileStrength : float = None, ResidualFrictionAngle : float = None, ResidualCohesion : float = None, DilationAngle : float = None, ApplySSRShearStrengthReduction : bool = None):
		if MaterialType is not None:
			self._setEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE", MaterialType)
		if PeakTensileStrength is not None:
			self._setDoubleProperty("MP_PEAK_TENSILE_STRENGTH", PeakTensileStrength)
		if PeakFrictionAngle is not None:
			self._setDoubleProperty("MP_PEAK_FRICTION_ANGLE", PeakFrictionAngle)
		if PeakCohesion is not None:
			self._setDoubleProperty("MP_PEAK_COHESION", PeakCohesion)
		if ResidualTensileStrength is not None:
			self._setDoubleProperty("MP_TENSILE_STRENGTH_RES", ResidualTensileStrength)
		if ResidualFrictionAngle is not None:
			self._setDoubleProperty("MP_FRICTION_ANGLE_RES", ResidualFrictionAngle)
		if ResidualCohesion is not None:
			self._setDoubleProperty("MP_COHESION_RES", ResidualCohesion)
		if DilationAngle is not None:
			self._setDoubleProperty("MP_DILATION_ANGLE", DilationAngle)
		if ApplySSRShearStrengthReduction is not None:
			self._setBoolProperty("MP_APPLY_SSR", ApplySSRShearStrengthReduction)
	def getProperties(self):
		return {
		"MaterialType" : self.getMaterialType(), 
		"PeakTensileStrength" : self.getPeakTensileStrength(), 
		"PeakFrictionAngle" : self.getPeakFrictionAngle(), 
		"PeakCohesion" : self.getPeakCohesion(), 
		"ResidualTensileStrength" : self.getResidualTensileStrength(), 
		"ResidualFrictionAngle" : self.getResidualFrictionAngle(), 
		"ResidualCohesion" : self.getResidualCohesion(), 
		"DilationAngle" : self.getDilationAngle(), 
		"ApplySSRShearStrengthReduction" : self.getApplySSRShearStrengthReduction(), 
		}
