from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class BartonBandisMaterial(PropertyProxy):
	def getDilationAngle(self) -> float:
		return self._getDoubleProperty("JP_DILATION_ANGLE")
	def setDilationAngle(self, value: float):
		return self._setDoubleProperty("JP_DILATION_ANGLE", value)
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
	def setProperties(self, DilationAngle : float = None, JCS : float = None, JRC : float = None, ResidualFrictionAngle : float = None, ResidualStrength : bool = None, ApplyStageFactors : bool = None):
		if DilationAngle is not None:
			self._setDoubleProperty("JP_DILATION_ANGLE", DilationAngle)
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
		"DilationAngle" : self.getDilationAngle(), 
		"JCS" : self.getJCS(), 
		"JRC" : self.getJRC(), 
		"ResidualFrictionAngle" : self.getResidualFrictionAngle(), 
		"ResidualStrength" : self.getResidualStrength(), 
		"ApplyStageFactors" : self.getApplyStageFactors(), 
		}
