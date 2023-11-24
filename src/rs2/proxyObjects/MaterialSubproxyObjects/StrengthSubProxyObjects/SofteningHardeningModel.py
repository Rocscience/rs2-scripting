from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class SofteningHardeningModel(PropertyProxy):
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
	def getHardeningProperty(self) -> float:
		return self._getDoubleProperty("MP_HARDENING_PROPERTY")
	def setHardeningProperty(self, value: float):
		return self._setDoubleProperty("MP_HARDENING_PROPERTY", value)
	def getDilationAngle(self) -> float:
		return self._getDoubleProperty("MP_SOFT_HARD_DILATION_ANGLE")
	def setDilationAngle(self, value: float):
		return self._setDoubleProperty("MP_SOFT_HARD_DILATION_ANGLE", value)
	def getConeDilationType(self) -> DilationTypes:
		return DilationTypes(self._getEnumEDilationTypesProperty("MP_CONE_DILATION"))
	def setConeDilationType(self, value: DilationTypes):
		return self._setEnumEDilationTypesProperty("MP_CONE_DILATION", value)
	def getCapType(self) -> CapTypes:
		return CapTypes(self._getEnumECapTypesProperty("MP_SH_CAP_TYPE"))
	def setCapType(self, value: CapTypes):
		return self._setEnumECapTypesProperty("MP_SH_CAP_TYPE", value)
	def getInitialMeanStress(self) -> float:
		return self._getDoubleProperty("MP_INITIAL_MEAN_STRESS")
	def setInitialMeanStress(self, value: float):
		return self._setDoubleProperty("MP_INITIAL_MEAN_STRESS", value)
	def getLambdaKappa(self) -> float:
		return self._getDoubleProperty("MP_LAMBDA_KAPPA")
	def setLambdaKappa(self, value: float):
		return self._setDoubleProperty("MP_LAMBDA_KAPPA", value)
	def setProperties(self, PeakTensileStrength : float = None, PeakFrictionAngle : float = None, PeakCohesion : float = None, HardeningProperty : float = None, DilationAngle : float = None, ConeDilationType : DilationTypes = None, CapType : CapTypes = None, InitialMeanStress : float = None, LambdaKappa : float = None):
		if PeakTensileStrength is not None:
			self._setDoubleProperty("MP_PEAK_TENSILE_STRENGTH", PeakTensileStrength)
		if PeakFrictionAngle is not None:
			self._setDoubleProperty("MP_PEAK_FRICTION_ANGLE", PeakFrictionAngle)
		if PeakCohesion is not None:
			self._setDoubleProperty("MP_PEAK_COHESION", PeakCohesion)
		if HardeningProperty is not None:
			self._setDoubleProperty("MP_HARDENING_PROPERTY", HardeningProperty)
		if DilationAngle is not None:
			self._setDoubleProperty("MP_SOFT_HARD_DILATION_ANGLE", DilationAngle)
		if ConeDilationType is not None:
			self._setEnumEDilationTypesProperty("MP_CONE_DILATION", ConeDilationType)
		if CapType is not None:
			self._setEnumECapTypesProperty("MP_SH_CAP_TYPE", CapType)
		if InitialMeanStress is not None:
			self._setDoubleProperty("MP_INITIAL_MEAN_STRESS", InitialMeanStress)
		if LambdaKappa is not None:
			self._setDoubleProperty("MP_LAMBDA_KAPPA", LambdaKappa)
	def getProperties(self):
		return {
		"PeakTensileStrength" : self.getPeakTensileStrength(), 
		"PeakFrictionAngle" : self.getPeakFrictionAngle(), 
		"PeakCohesion" : self.getPeakCohesion(), 
		"HardeningProperty" : self.getHardeningProperty(), 
		"DilationAngle" : self.getDilationAngle(), 
		"ConeDilationType" : self.getConeDilationType(), 
		"CapType" : self.getCapType(), 
		"InitialMeanStress" : self.getInitialMeanStress(), 
		"LambdaKappa" : self.getLambdaKappa(), 
		}
