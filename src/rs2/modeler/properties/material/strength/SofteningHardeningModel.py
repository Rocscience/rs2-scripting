from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.AbsoluteStageFactorGettersInterface import AbsoluteStageFactorGettersInterface
class SofteningHardeningModelStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getHardeningPropertyFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_HARDENING_PROPERTY", self.propertyID], proxyArgumentIndices=[1])
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
	def getDilationAngleFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_SOFT_HARD_DILATION_ANGLE", self.propertyID], proxyArgumentIndices=[1])
class SofteningHardeningModelDefinedStageFactor(SofteningHardeningModelStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setHardeningPropertyFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_HARDENING_PROPERTY", value, self.propertyID], proxyArgumentIndices=[2])
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
	def setDilationAngleFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_SOFT_HARD_DILATION_ANGLE", value, self.propertyID], proxyArgumentIndices=[2])
class SofteningHardeningModel(PropertyProxy):
	"""
	Attributes:
		stageFactorInterface (AbsoluteStageFactorGettersInterface[SofteningHardeningModelDefinedStageFactor, SofteningHardeningModelStageFactor]): Reference object for modifying stage factor property.

	Examples:
		:ref:`Material Property Strength Example`
	
	"""
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		super().__init__(client, ID, documentProxyID)
		self.stageFactorInterface = AbsoluteStageFactorGettersInterface[SofteningHardeningModelDefinedStageFactor, SofteningHardeningModelStageFactor](self._client, stageFactorInterfaceID, ID, SofteningHardeningModelDefinedStageFactor, SofteningHardeningModelStageFactor)
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
	def getConeHardeningType(self) -> ConeHardeningTypes:
		return ConeHardeningTypes(self._getEnumEConeHardeningTypesProperty("MP_CONE_HARDENING_TYPE"))
	def setConeHardeningType(self, value: ConeHardeningTypes):
		return self._setEnumEConeHardeningTypesProperty("MP_CONE_HARDENING_TYPE", value)
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
	def getCapHardeningType(self) -> CapHardeningTypes:
		return CapHardeningTypes(self._getEnumECapHardeningTypesProperty("MP_SH_CAP_HARDENING_TYPE"))
	def setCapHardeningType(self, value: CapHardeningTypes):
		return self._setEnumECapHardeningTypesProperty("MP_SH_CAP_HARDENING_TYPE", value)
	def getInitialMeanStress(self) -> float:
		return self._getDoubleProperty("MP_INITIAL_MEAN_STRESS")
	def setInitialMeanStress(self, value: float):
		return self._setDoubleProperty("MP_INITIAL_MEAN_STRESS", value)
	def getLambdaKappa(self) -> float:
		return self._getDoubleProperty("MP_LAMBDA_KAPPA")
	def setLambdaKappa(self, value: float):
		return self._setDoubleProperty("MP_LAMBDA_KAPPA", value)
	def setSHConeHardening(self, plasticStrainVsFrictionAngle: list[tuple[float,float]], plasticStrainVsCohesion: list[tuple[float,float]]):
		"""
		plasticStrainVsFrictionAngle: list of tuples, (plainStrain, frictionAngle)
		plasticStrainVsCohesion: list of tuples, (plasticStrain, Cohesion)
		"""
		return self._callFunction("setSHConeHardening", [plasticStrainVsFrictionAngle, plasticStrainVsCohesion])
	def getSHConeHardening(self) -> tuple[list[tuple[float,float]],list[tuple[float,float]]]:
		"""
		returns a tuple of (plasticStrainVsFrictionAngle, plasticStrainVsCohesion), where
		plasticStrainVsFrictionAngle: list of tuples, (plainStrain, frictionAngle)
		plasticStrainVsCohesion: list of tuples, (plasticStrain, Cohesion)
		"""
		return self._callFunction("getSHConeHardening", [])
	def setSHCapMeanStress(self, meanStress: list[tuple[float,float]]):
		"""
		meanStress is a list of (x,y) tuples.
		"""
		return self._callFunction("setSHCapMeanStress", [meanStress])
	def getSHCapMeanStress(self) -> list[tuple[float,float]]:
		"""
		returns a list of (x,y) tuples.
		"""
		return self._callFunction("getSHCapMeanStress", [])
	def setProperties(self, PeakTensileStrength : float = None, PeakFrictionAngle : float = None, PeakCohesion : float = None, ConeHardeningType : ConeHardeningTypes = None, HardeningProperty : float = None, DilationAngle : float = None, ConeDilationType : DilationTypes = None, CapType : CapTypes = None, CapHardeningType : CapHardeningTypes = None, InitialMeanStress : float = None, LambdaKappa : float = None):
		if PeakTensileStrength is not None:
			self._setDoubleProperty("MP_PEAK_TENSILE_STRENGTH", PeakTensileStrength)
		if PeakFrictionAngle is not None:
			self._setDoubleProperty("MP_PEAK_FRICTION_ANGLE", PeakFrictionAngle)
		if PeakCohesion is not None:
			self._setDoubleProperty("MP_PEAK_COHESION", PeakCohesion)
		if ConeHardeningType is not None:
			self._setEnumEConeHardeningTypesProperty("MP_CONE_HARDENING_TYPE", ConeHardeningType)
		if HardeningProperty is not None:
			self._setDoubleProperty("MP_HARDENING_PROPERTY", HardeningProperty)
		if DilationAngle is not None:
			self._setDoubleProperty("MP_SOFT_HARD_DILATION_ANGLE", DilationAngle)
		if ConeDilationType is not None:
			self._setEnumEDilationTypesProperty("MP_CONE_DILATION", ConeDilationType)
		if CapType is not None:
			self._setEnumECapTypesProperty("MP_SH_CAP_TYPE", CapType)
		if CapHardeningType is not None:
			self._setEnumECapHardeningTypesProperty("MP_SH_CAP_HARDENING_TYPE", CapHardeningType)
		if InitialMeanStress is not None:
			self._setDoubleProperty("MP_INITIAL_MEAN_STRESS", InitialMeanStress)
		if LambdaKappa is not None:
			self._setDoubleProperty("MP_LAMBDA_KAPPA", LambdaKappa)
	def getProperties(self):
		return {
		"PeakTensileStrength" : self.getPeakTensileStrength(), 
		"PeakFrictionAngle" : self.getPeakFrictionAngle(), 
		"PeakCohesion" : self.getPeakCohesion(), 
		"ConeHardeningType" : self.getConeHardeningType(), 
		"HardeningProperty" : self.getHardeningProperty(), 
		"DilationAngle" : self.getDilationAngle(), 
		"ConeDilationType" : self.getConeDilationType(), 
		"CapType" : self.getCapType(), 
		"CapHardeningType" : self.getCapHardeningType(), 
		"InitialMeanStress" : self.getInitialMeanStress(), 
		"LambdaKappa" : self.getLambdaKappa(), 
		}
