from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class MohrCoulombMaterial(PropertyProxy):
	def getDilationAngle(self) -> float:
		return self._getDoubleProperty("JP_DILATION_ANGLE")
	def setDilationAngle(self, value: float):
		return self._setDoubleProperty("JP_DILATION_ANGLE", value)
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
	def setProperties(self, DilationAngle : float = None, TensileStrength : float = None, PeakFrictionAngle : float = None, PeakCohesion : float = None, ResidualStrength : bool = None, ResTensileStrength : float = None, ResCohesion : float = None, ResFrictionAngle : float = None, ApplyStageFactors : bool = None):
		if DilationAngle is not None:
			self._setDoubleProperty("JP_DILATION_ANGLE", DilationAngle)
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
		"DilationAngle" : self.getDilationAngle(), 
		"TensileStrength" : self.getTensileStrength(), 
		"PeakFrictionAngle" : self.getPeakFrictionAngle(), 
		"PeakCohesion" : self.getPeakCohesion(), 
		"ResidualStrength" : self.getResidualStrength(), 
		"ResTensileStrength" : self.getResTensileStrength(), 
		"ResCohesion" : self.getResCohesion(), 
		"ResFrictionAngle" : self.getResFrictionAngle(), 
		"ApplyStageFactors" : self.getApplyStageFactors(), 
		}
