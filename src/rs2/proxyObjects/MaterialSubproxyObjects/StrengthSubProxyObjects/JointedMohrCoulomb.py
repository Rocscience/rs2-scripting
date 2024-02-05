from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
from rs2.proxyObjects.MaterialJointOptions import MaterialJointOptions
class JointedMohrCoulomb(PropertyProxy):
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
