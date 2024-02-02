from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class GeosyntheticHyperbolicMaterial(PropertyProxy):
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
