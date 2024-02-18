from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class BoundingSurfacePlasticity(PropertyProxy):
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
	def getCriticalFrictionAngleZeroDilation(self) -> float:
		return self._getDoubleProperty("MP_CRITICAL_FRICTION_ANGLE")
	def setCriticalFrictionAngleZeroDilation(self, value: float):
		return self._setDoubleProperty("MP_CRITICAL_FRICTION_ANGLE", value)
	def getHardeningProperty(self) -> float:
		return self._getDoubleProperty("MP_HARDENING_PROPERTY")
	def setHardeningProperty(self, value: float):
		return self._setDoubleProperty("MP_HARDENING_PROPERTY", value)
	def getUnloadingToLoadingPlasticModulusRatio(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_TO_LOADING_MODULUS_RATIO")
	def setUnloadingToLoadingPlasticModulusRatio(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_TO_LOADING_MODULUS_RATIO", value)
	def getPowerTerm(self) -> float:
		return self._getDoubleProperty("MP_POWER_TERM")
	def setPowerTerm(self, value: float):
		return self._setDoubleProperty("MP_POWER_TERM", value)
	def getApplySSRShearStrengthReduction(self) -> bool:
		return self._getBoolProperty("MP_APPLY_SSR")
	def setApplySSRShearStrengthReduction(self, value: bool):
		return self._setBoolProperty("MP_APPLY_SSR", value)
	def setProperties(self, PeakTensileStrength : float = None, PeakFrictionAngle : float = None, PeakCohesion : float = None, CriticalFrictionAngleZeroDilation : float = None, HardeningProperty : float = None, UnloadingToLoadingPlasticModulusRatio : float = None, PowerTerm : float = None, ApplySSRShearStrengthReduction : bool = None):
		if PeakTensileStrength is not None:
			self._setDoubleProperty("MP_PEAK_TENSILE_STRENGTH", PeakTensileStrength)
		if PeakFrictionAngle is not None:
			self._setDoubleProperty("MP_PEAK_FRICTION_ANGLE", PeakFrictionAngle)
		if PeakCohesion is not None:
			self._setDoubleProperty("MP_PEAK_COHESION", PeakCohesion)
		if CriticalFrictionAngleZeroDilation is not None:
			self._setDoubleProperty("MP_CRITICAL_FRICTION_ANGLE", CriticalFrictionAngleZeroDilation)
		if HardeningProperty is not None:
			self._setDoubleProperty("MP_HARDENING_PROPERTY", HardeningProperty)
		if UnloadingToLoadingPlasticModulusRatio is not None:
			self._setDoubleProperty("MP_UNLOADING_TO_LOADING_MODULUS_RATIO", UnloadingToLoadingPlasticModulusRatio)
		if PowerTerm is not None:
			self._setDoubleProperty("MP_POWER_TERM", PowerTerm)
		if ApplySSRShearStrengthReduction is not None:
			self._setBoolProperty("MP_APPLY_SSR", ApplySSRShearStrengthReduction)
	def getProperties(self):
		return {
		"PeakTensileStrength" : self.getPeakTensileStrength(), 
		"PeakFrictionAngle" : self.getPeakFrictionAngle(), 
		"PeakCohesion" : self.getPeakCohesion(), 
		"CriticalFrictionAngleZeroDilation" : self.getCriticalFrictionAngleZeroDilation(), 
		"HardeningProperty" : self.getHardeningProperty(), 
		"UnloadingToLoadingPlasticModulusRatio" : self.getUnloadingToLoadingPlasticModulusRatio(), 
		"PowerTerm" : self.getPowerTerm(), 
		"ApplySSRShearStrengthReduction" : self.getApplySSRShearStrengthReduction(), 
		}
