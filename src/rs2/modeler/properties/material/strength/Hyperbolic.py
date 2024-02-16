from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.AbsoluteStageFactorInterface import AbsoluteStageFactorInterface
class HyperbolicStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getResidualCohesionFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_COHESION_RES", self.propertyID], proxyArgumentIndices=[1])
	def getResidualFrictionAngleFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_FRICTION_ANGLE_RES", self.propertyID], proxyArgumentIndices=[1])
	def getPeakCohesionFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_PEAK_COHESION", self.propertyID], proxyArgumentIndices=[1])
	def getPeakFrictionAngleFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_PEAK_FRICTION_ANGLE", self.propertyID], proxyArgumentIndices=[1])
class HyperbolicDefinedStageFactor(HyperbolicStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setResidualCohesionFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_COHESION_RES", value, self.propertyID], proxyArgumentIndices=[2])
	def setResidualFrictionAngleFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_FRICTION_ANGLE_RES", value, self.propertyID], proxyArgumentIndices=[2])
	def setPeakCohesionFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_PEAK_COHESION", value, self.propertyID], proxyArgumentIndices=[2])
	def setPeakFrictionAngleFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_PEAK_FRICTION_ANGLE", value, self.propertyID], proxyArgumentIndices=[2])
class Hyperbolic(PropertyProxy):
	def __init__(self, client : Client, ID, documentProxyID):
		super().__init__(client, ID, documentProxyID)
		stageFactorInterfaceID = self._callFunction("getStageFactorInterface", [], keepReturnValueReference=True)
		self.stageFactorInterface = AbsoluteStageFactorInterface[HyperbolicDefinedStageFactor, HyperbolicStageFactor](self._client, stageFactorInterfaceID, ID, HyperbolicDefinedStageFactor, HyperbolicStageFactor)
	def getMaterialType(self) -> MaterialType:
		return MaterialType(self._getEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE"))
	def setMaterialType(self, value: MaterialType):
		return self._setEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE", value)
	def getPeakFrictionAngle(self) -> float:
		return self._getDoubleProperty("MP_PEAK_FRICTION_ANGLE")
	def setPeakFrictionAngle(self, value: float):
		return self._setDoubleProperty("MP_PEAK_FRICTION_ANGLE", value)
	def getPeakCohesion(self) -> float:
		return self._getDoubleProperty("MP_PEAK_COHESION")
	def setPeakCohesion(self, value: float):
		return self._setDoubleProperty("MP_PEAK_COHESION", value)
	def getResidualFrictionAngle(self) -> float:
		return self._getDoubleProperty("MP_FRICTION_ANGLE_RES")
	def setResidualFrictionAngle(self, value: float):
		return self._setDoubleProperty("MP_FRICTION_ANGLE_RES", value)
	def getResidualCohesion(self) -> float:
		return self._getDoubleProperty("MP_COHESION_RES")
	def setResidualCohesion(self, value: float):
		return self._setDoubleProperty("MP_COHESION_RES", value)
	def getDilationRatio(self) -> float:
		return self._getDoubleProperty("MP_DILATION_RATIO")
	def setDilationRatio(self, value: float):
		return self._setDoubleProperty("MP_DILATION_RATIO", value)
	def getApplySSRShearStrengthReduction(self) -> bool:
		return self._getBoolProperty("MP_APPLY_SSR")
	def setApplySSRShearStrengthReduction(self, value: bool):
		return self._setBoolProperty("MP_APPLY_SSR", value)
	def setProperties(self, MaterialType : MaterialType = None, PeakFrictionAngle : float = None, PeakCohesion : float = None, ResidualFrictionAngle : float = None, ResidualCohesion : float = None, DilationRatio : float = None, ApplySSRShearStrengthReduction : bool = None):
		if MaterialType is not None:
			self._setEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE", MaterialType)
		if PeakFrictionAngle is not None:
			self._setDoubleProperty("MP_PEAK_FRICTION_ANGLE", PeakFrictionAngle)
		if PeakCohesion is not None:
			self._setDoubleProperty("MP_PEAK_COHESION", PeakCohesion)
		if ResidualFrictionAngle is not None:
			self._setDoubleProperty("MP_FRICTION_ANGLE_RES", ResidualFrictionAngle)
		if ResidualCohesion is not None:
			self._setDoubleProperty("MP_COHESION_RES", ResidualCohesion)
		if DilationRatio is not None:
			self._setDoubleProperty("MP_DILATION_RATIO", DilationRatio)
		if ApplySSRShearStrengthReduction is not None:
			self._setBoolProperty("MP_APPLY_SSR", ApplySSRShearStrengthReduction)
	def getProperties(self):
		return {
		"MaterialType" : self.getMaterialType(), 
		"PeakFrictionAngle" : self.getPeakFrictionAngle(), 
		"PeakCohesion" : self.getPeakCohesion(), 
		"ResidualFrictionAngle" : self.getResidualFrictionAngle(), 
		"ResidualCohesion" : self.getResidualCohesion(), 
		"DilationRatio" : self.getDilationRatio(), 
		"ApplySSRShearStrengthReduction" : self.getApplySSRShearStrengthReduction(), 
		}
