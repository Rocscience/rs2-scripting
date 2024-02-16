from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.AbsoluteStageFactorInterface import AbsoluteStageFactorInterface
class BoundingSurfacePlasticityStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getHardeningPropertyFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_HARDENING_PROPERTY", self.propertyID], proxyArgumentIndices=[1])
	def getPeakCohesionFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_PEAK_COHESION", self.propertyID], proxyArgumentIndices=[1])
	def getPeakFrictionAngleFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_PEAK_FRICTION_ANGLE", self.propertyID], proxyArgumentIndices=[1])
	def getPeakTensileStrengthFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_PEAK_TENSILE_STRENGTH", self.propertyID], proxyArgumentIndices=[1])
class BoundingSurfacePlasticityDefinedStageFactor(BoundingSurfacePlasticityStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setHardeningPropertyFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_HARDENING_PROPERTY", value, self.propertyID], proxyArgumentIndices=[2])
	def setPeakCohesionFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_PEAK_COHESION", value, self.propertyID], proxyArgumentIndices=[2])
	def setPeakFrictionAngleFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_PEAK_FRICTION_ANGLE", value, self.propertyID], proxyArgumentIndices=[2])
	def setPeakTensileStrengthFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_PEAK_TENSILE_STRENGTH", value, self.propertyID], proxyArgumentIndices=[2])
class BoundingSurfacePlasticity(PropertyProxy):
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		super().__init__(client, ID, documentProxyID)
		self.stageFactorInterface = AbsoluteStageFactorInterface[BoundingSurfacePlasticityDefinedStageFactor, BoundingSurfacePlasticityStageFactor](self._client, stageFactorInterfaceID, ID, BoundingSurfacePlasticityDefinedStageFactor, BoundingSurfacePlasticityStageFactor)
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
