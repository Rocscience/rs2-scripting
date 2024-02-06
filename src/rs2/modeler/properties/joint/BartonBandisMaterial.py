from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class BartonBandisMaterial(PropertyProxy):
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
