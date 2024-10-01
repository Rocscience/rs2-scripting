from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.AbsoluteStageFactorGettersInterface import AbsoluteStageFactorGettersInterface
class CamClayStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getCriticalStateSlopeFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_CRITICAL_STATE_SLOPE", self.propertyID], proxyArgumentIndices=[1])
	def getGammaFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_GAMMA", self.propertyID], proxyArgumentIndices=[1])
	def getKappaFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_KAPPA", self.propertyID], proxyArgumentIndices=[1])
	def getLambdaFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_LAMBDA", self.propertyID], proxyArgumentIndices=[1])
	def getNParameterFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_N", self.propertyID], proxyArgumentIndices=[1])
	def getOverconsolidationRatioFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_OVERCONSOLIDATION_RATIO", self.propertyID], proxyArgumentIndices=[1])
	def getPreconsolidationStressFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_PRECONSOLIDATION_STRESS", self.propertyID], proxyArgumentIndices=[1])
class CamClayDefinedStageFactor(CamClayStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setCriticalStateSlopeFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_CRITICAL_STATE_SLOPE", value, self.propertyID], proxyArgumentIndices=[2])
	def setGammaFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_GAMMA", value, self.propertyID], proxyArgumentIndices=[2])
	def setKappaFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_KAPPA", value, self.propertyID], proxyArgumentIndices=[2])
	def setLambdaFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_LAMBDA", value, self.propertyID], proxyArgumentIndices=[2])
	def setNParameterFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_N", value, self.propertyID], proxyArgumentIndices=[2])
	def setOverconsolidationRatioFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_OVERCONSOLIDATION_RATIO", value, self.propertyID], proxyArgumentIndices=[2])
	def setPreconsolidationStressFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_PRECONSOLIDATION_STRESS", value, self.propertyID], proxyArgumentIndices=[2])
class CamClay(PropertyProxy):
	"""
	Attributes:
		stageFactorInterface (AbsoluteStageFactorGettersInterface[CamClayDefinedStageFactor, CamClayStageFactor]): Reference object for modifying stage factor property.

	Examples:
		:ref:`Material Property Strength Example`
	
	"""
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		super().__init__(client, ID, documentProxyID)
		self.stageFactorInterface = AbsoluteStageFactorGettersInterface[CamClayDefinedStageFactor, CamClayStageFactor](self._client, stageFactorInterfaceID, ID, CamClayDefinedStageFactor, CamClayStageFactor)
	def getCriticalStateSlope(self) -> float:
		return self._getDoubleProperty("MP_CRITICAL_STATE_SLOPE")
	def setCriticalStateSlope(self, value: float):
		return self._setDoubleProperty("MP_CRITICAL_STATE_SLOPE", value)
	def getSpecificVolumeAtUnitPressure(self) -> SpecificVolumeAtUnitPressure:
		return SpecificVolumeAtUnitPressure(self._getEnumESpecificVolumeAtUnitPressureProperty("MP_SPECIFIC_VOLUME_AT_UNIT_PRESSURE"))
	def setSpecificVolumeAtUnitPressure(self, value: SpecificVolumeAtUnitPressure):
		return self._setEnumESpecificVolumeAtUnitPressureProperty("MP_SPECIFIC_VOLUME_AT_UNIT_PRESSURE", value)
	def getNParameter(self) -> float:
		return self._getDoubleProperty("MP_N")
	def setNParameter(self, value: float):
		return self._setDoubleProperty("MP_N", value)
	def getGamma(self) -> float:
		return self._getDoubleProperty("MP_GAMMA")
	def setGamma(self, value: float):
		return self._setDoubleProperty("MP_GAMMA", value)
	def getKappa(self) -> float:
		return self._getDoubleProperty("MP_KAPPA")
	def setKappa(self, value: float):
		return self._setDoubleProperty("MP_KAPPA", value)
	def getInitialStateOfConsolidation(self) -> InitialStateOfConsolidation:
		return InitialStateOfConsolidation(self._getEnumEInitialStateOfConsolidationProperty("MP_INITIAL_STATE_OF_CONSOLIDATION"))
	def setInitialStateOfConsolidation(self, value: InitialStateOfConsolidation):
		return self._setEnumEInitialStateOfConsolidationProperty("MP_INITIAL_STATE_OF_CONSOLIDATION", value)
	def getOverconsolidationRatio(self) -> float:
		return self._getDoubleProperty("MP_OVERCONSOLIDATION_RATIO")
	def setOverconsolidationRatio(self, value: float):
		return self._setDoubleProperty("MP_OVERCONSOLIDATION_RATIO", value)
	def getPreconsolidationStress(self) -> float:
		return self._getDoubleProperty("MP_PRECONSOLIDATION_STRESS")
	def setPreconsolidationStress(self, value: float):
		return self._setDoubleProperty("MP_PRECONSOLIDATION_STRESS", value)
	def getLambda(self) -> float:
		return self._getDoubleProperty("MP_LAMBDA")
	def setLambda(self, value: float):
		return self._setDoubleProperty("MP_LAMBDA", value)
	def setProperties(self, CriticalStateSlope : float = None, SpecificVolumeAtUnitPressure : SpecificVolumeAtUnitPressure = None, NParameter : float = None, Gamma : float = None, Kappa : float = None, InitialStateOfConsolidation : InitialStateOfConsolidation = None, OverconsolidationRatio : float = None, PreconsolidationStress : float = None, Lambda : float = None):
		if CriticalStateSlope is not None:
			self._setDoubleProperty("MP_CRITICAL_STATE_SLOPE", CriticalStateSlope)
		if SpecificVolumeAtUnitPressure is not None:
			self._setEnumESpecificVolumeAtUnitPressureProperty("MP_SPECIFIC_VOLUME_AT_UNIT_PRESSURE", SpecificVolumeAtUnitPressure)
		if NParameter is not None:
			self._setDoubleProperty("MP_N", NParameter)
		if Gamma is not None:
			self._setDoubleProperty("MP_GAMMA", Gamma)
		if Kappa is not None:
			self._setDoubleProperty("MP_KAPPA", Kappa)
		if InitialStateOfConsolidation is not None:
			self._setEnumEInitialStateOfConsolidationProperty("MP_INITIAL_STATE_OF_CONSOLIDATION", InitialStateOfConsolidation)
		if OverconsolidationRatio is not None:
			self._setDoubleProperty("MP_OVERCONSOLIDATION_RATIO", OverconsolidationRatio)
		if PreconsolidationStress is not None:
			self._setDoubleProperty("MP_PRECONSOLIDATION_STRESS", PreconsolidationStress)
		if Lambda is not None:
			self._setDoubleProperty("MP_LAMBDA", Lambda)
	def getProperties(self):
		return {
		"CriticalStateSlope" : self.getCriticalStateSlope(), 
		"SpecificVolumeAtUnitPressure" : self.getSpecificVolumeAtUnitPressure(), 
		"NParameter" : self.getNParameter(), 
		"Gamma" : self.getGamma(), 
		"Kappa" : self.getKappa(), 
		"InitialStateOfConsolidation" : self.getInitialStateOfConsolidation(), 
		"OverconsolidationRatio" : self.getOverconsolidationRatio(), 
		"PreconsolidationStress" : self.getPreconsolidationStress(), 
		"Lambda" : self.getLambda(), 
		}
