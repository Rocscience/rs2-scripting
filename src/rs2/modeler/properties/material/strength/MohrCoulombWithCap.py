from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.AbsoluteStageFactorGettersInterface import AbsoluteStageFactorGettersInterface
class MohrCoulombWithCapStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getDilationAngleFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_DILATION_ANGLE", self.propertyID], proxyArgumentIndices=[1])
	def getInitialMeanStressFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_INITIAL_MEAN_STRESS", self.propertyID], proxyArgumentIndices=[1])
	def getLambdaKappaFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_LAMBDA_KAPPA", self.propertyID], proxyArgumentIndices=[1])
	def getPeakCohesionFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_PEAK_COHESION", self.propertyID], proxyArgumentIndices=[1])
	def getPeakFrictionAngleFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_PEAK_FRICTION_ANGLE", self.propertyID], proxyArgumentIndices=[1])
	def getPeakTensileStrengthFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_PEAK_TENSILE_STRENGTH", self.propertyID], proxyArgumentIndices=[1])
class MohrCoulombWithCapDefinedStageFactor(MohrCoulombWithCapStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setDilationAngleFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_DILATION_ANGLE", value, self.propertyID], proxyArgumentIndices=[2])
	def setInitialMeanStressFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_INITIAL_MEAN_STRESS", value, self.propertyID], proxyArgumentIndices=[2])
	def setLambdaKappaFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_LAMBDA_KAPPA", value, self.propertyID], proxyArgumentIndices=[2])
	def setPeakCohesionFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_PEAK_COHESION", value, self.propertyID], proxyArgumentIndices=[2])
	def setPeakFrictionAngleFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_PEAK_FRICTION_ANGLE", value, self.propertyID], proxyArgumentIndices=[2])
	def setPeakTensileStrengthFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_PEAK_TENSILE_STRENGTH", value, self.propertyID], proxyArgumentIndices=[2])
class MohrCoulombWithCap(PropertyProxy):
	"""
	Attributes:
		stageFactorInterface (AbsoluteStageFactorGettersInterface[MohrCoulombWithCapDefinedStageFactor, MohrCoulombWithCapStageFactor]): Reference object for modifying stage factor property.

	Examples:
		:ref:`Material Property Strength Example`
	
	"""
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		super().__init__(client, ID, documentProxyID)
		self.stageFactorInterface = AbsoluteStageFactorGettersInterface[MohrCoulombWithCapDefinedStageFactor, MohrCoulombWithCapStageFactor](self._client, stageFactorInterfaceID, ID, MohrCoulombWithCapDefinedStageFactor, MohrCoulombWithCapStageFactor)
	def getPeakTensileStrength(self) -> float:
		return self._getDoubleProperty("MP_PEAK_TENSILE_STRENGTH")
	def setPeakTensileStrength(self, value: float):
		return self._setDoubleProperty("MP_PEAK_TENSILE_STRENGTH", value)
	def getPeakFrictionAngle(self) -> float:
		return self._getDoubleProperty("MP_FRICTION_ANGLE_RES")
	def setPeakFrictionAngle(self, value: float):
		return self._setDoubleProperty("MP_FRICTION_ANGLE_RES", value)
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
			self._setDoubleProperty("MP_FRICTION_ANGLE_RES", PeakFrictionAngle)
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
