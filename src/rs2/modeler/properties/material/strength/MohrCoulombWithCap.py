from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class MohrCoulombWithCap(PropertyProxy):
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
	def getDilationAngle(self) -> float:
		return self._getDoubleProperty("MP_DILATION_ANGLE")
	def setDilationAngle(self, value: float):
		return self._setDoubleProperty("MP_DILATION_ANGLE", value)
	def getCapType(self) -> MCCapType:
		return MCCapType(self._getEnumEMCCapTypeProperty("MP_CAP_TYPE"))
	def setCapType(self, value: MCCapType):
		return self._setEnumEMCCapTypeProperty("MP_CAP_TYPE", value)
	def getCapHardeningType(self) -> CapHardeningTypes:
		return CapHardeningTypes(self._getEnumECapHardeningTypesProperty("MP_CAP_HARDENING_TYPE"))
	def setCapHardeningType(self, value: CapHardeningTypes):
		return self._setEnumECapHardeningTypesProperty("MP_CAP_HARDENING_TYPE", value)
	def getInitialMeanStress(self) -> float:
		return self._getDoubleProperty("MP_INITIAL_MEAN_STRESS")
	def setInitialMeanStress(self, value: float):
		return self._setDoubleProperty("MP_INITIAL_MEAN_STRESS", value)
	def getLambdaKappa(self) -> float:
		return self._getDoubleProperty("MP_LAMBDA_KAPPA")
	def setLambdaKappa(self, value: float):
		return self._setDoubleProperty("MP_LAMBDA_KAPPA", value)
	def setMohrCoulombCapMeanStress(self, meanStress: list[tuple[float,float]]):
		"""
		meanStress is a list of (x,y) tuples.
		"""
		return self._callFunction("setMohrCoulombCapMeanStress", [meanStress])
	def getMohrCoulombCapMeanStress(self) -> list[tuple[float,float]]:
		"""
		returns a list of (x,y) tuples.
		"""
		return self._callFunction("getMohrCoulombCapMeanStress", [])
	def setProperties(self, PeakTensileStrength : float = None, PeakFrictionAngle : float = None, PeakCohesion : float = None, DilationAngle : float = None, CapType : MCCapType = None, CapHardeningType : CapHardeningTypes = None, InitialMeanStress : float = None, LambdaKappa : float = None):
		if PeakTensileStrength is not None:
			self._setDoubleProperty("MP_PEAK_TENSILE_STRENGTH", PeakTensileStrength)
		if PeakFrictionAngle is not None:
			self._setDoubleProperty("MP_PEAK_FRICTION_ANGLE", PeakFrictionAngle)
		if PeakCohesion is not None:
			self._setDoubleProperty("MP_PEAK_COHESION", PeakCohesion)
		if DilationAngle is not None:
			self._setDoubleProperty("MP_DILATION_ANGLE", DilationAngle)
		if CapType is not None:
			self._setEnumEMCCapTypeProperty("MP_CAP_TYPE", CapType)
		if CapHardeningType is not None:
			self._setEnumECapHardeningTypesProperty("MP_CAP_HARDENING_TYPE", CapHardeningType)
		if InitialMeanStress is not None:
			self._setDoubleProperty("MP_INITIAL_MEAN_STRESS", InitialMeanStress)
		if LambdaKappa is not None:
			self._setDoubleProperty("MP_LAMBDA_KAPPA", LambdaKappa)
	def getProperties(self):
		return {
		"PeakTensileStrength" : self.getPeakTensileStrength(), 
		"PeakFrictionAngle" : self.getPeakFrictionAngle(), 
		"PeakCohesion" : self.getPeakCohesion(), 
		"DilationAngle" : self.getDilationAngle(), 
		"CapType" : self.getCapType(), 
		"CapHardeningType" : self.getCapHardeningType(), 
		"InitialMeanStress" : self.getInitialMeanStress(), 
		"LambdaKappa" : self.getLambdaKappa(), 
		}
