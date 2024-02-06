from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class CamClay(PropertyProxy):
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
