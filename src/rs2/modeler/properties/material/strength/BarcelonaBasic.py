from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class BarcelonaBasic(PropertyProxy):
	def getSlopeOfCriticalStateLines(self) -> float:
		return self._getDoubleProperty("MP_M_SLOPE")
	def setSlopeOfCriticalStateLines(self, value: float):
		return self._setDoubleProperty("MP_M_SLOPE", value)
	def getIncludeTheEffectOfLodesAngle(self) -> bool:
		return self._getBoolProperty("MP_USE_LODE")
	def setIncludeTheEffectOfLodesAngle(self, value: bool):
		return self._setBoolProperty("MP_USE_LODE", value)
	def getLambda(self) -> float:
		return self._getDoubleProperty("MP_BB_LAMBDA")
	def setLambda(self, value: float):
		return self._setDoubleProperty("MP_BB_LAMBDA", value)
	def getKappa(self) -> float:
		return self._getDoubleProperty("MP_BB_KAPPA")
	def setKappa(self, value: float):
		return self._setDoubleProperty("MP_BB_KAPPA", value)
	def getSpecificVolumeAtUnitPressure(self) -> float:
		return self._getDoubleProperty("MP_BB_N")
	def setSpecificVolumeAtUnitPressure(self, value: float):
		return self._setDoubleProperty("MP_BB_N", value)
	def getInitialStateOfConsolidation(self) -> InitialStateOfConsolidation:
		return InitialStateOfConsolidation(self._getEnumEInitialStateOfConsolidationProperty("MP_INITIAL_CONSOLIDATION_STATE"))
	def setInitialStateOfConsolidation(self, value: InitialStateOfConsolidation):
		return self._setEnumEInitialStateOfConsolidationProperty("MP_INITIAL_CONSOLIDATION_STATE", value)
	def getOverConsolidationRatio(self) -> float:
		return self._getDoubleProperty("MP_BB_OCR")
	def setOverConsolidationRatio(self, value: float):
		return self._setDoubleProperty("MP_BB_OCR", value)
	def getPreconsolidationPressure(self) -> float:
		return self._getDoubleProperty("MP_BB_PC")
	def setPreconsolidationPressure(self, value: float):
		return self._setDoubleProperty("MP_BB_PC", value)
	def getElasticParameters(self) -> ElasticParameters:
		return ElasticParameters(self._getEnumEElasticParametersProperty("MP_ELASTIC_PARAMETERS"))
	def setElasticParameters(self, value: ElasticParameters):
		return self._setEnumEElasticParametersProperty("MP_ELASTIC_PARAMETERS", value)
	def getAutoCalculateAlfaFactor(self) -> bool:
		return self._getBoolProperty("MP_USE_AUTO_ALFA")
	def setAutoCalculateAlfaFactor(self, value: bool):
		return self._setBoolProperty("MP_USE_AUTO_ALFA", value)
	def getAlfaFactor(self) -> float:
		return self._getDoubleProperty("MP_ALFA")
	def setAlfaFactor(self, value: float):
		return self._setDoubleProperty("MP_ALFA", value)
	def getMinimumBulkModulus(self) -> float:
		return self._getDoubleProperty("MP_MIN_BULK_MODULUS")
	def setMinimumBulkModulus(self, value: float):
		return self._setDoubleProperty("MP_MIN_BULK_MODULUS", value)
	def getKTensionSuction(self) -> float:
		return self._getDoubleProperty("MP_K_TENSION_SUCTION")
	def setKTensionSuction(self, value: float):
		return self._setDoubleProperty("MP_K_TENSION_SUCTION", value)
	def getKapaSuction(self) -> float:
		return self._getDoubleProperty("MP_KAPA_SUCTION")
	def setKapaSuction(self, value: float):
		return self._setDoubleProperty("MP_KAPA_SUCTION", value)
	def getRParameter(self) -> float:
		return self._getDoubleProperty("MP_BB_R")
	def setRParameter(self, value: float):
		return self._setDoubleProperty("MP_BB_R", value)
	def getBetaParameter(self) -> float:
		return self._getDoubleProperty("MP_BB_BETA")
	def setBetaParameter(self, value: float):
		return self._setDoubleProperty("MP_BB_BETA", value)
	def getReferenceMeanStress(self) -> float:
		return self._getDoubleProperty("MP_REF_PRESSURE")
	def setReferenceMeanStress(self, value: float):
		return self._setDoubleProperty("MP_REF_PRESSURE", value)
	def getAtmosphericPressure(self) -> float:
		return self._getDoubleProperty("MP_P_ATM")
	def setAtmosphericPressure(self, value: float):
		return self._setDoubleProperty("MP_P_ATM", value)
	def setProperties(self, SlopeOfCriticalStateLines : float = None, IncludeTheEffectOfLodesAngle : bool = None, Lambda : float = None, Kappa : float = None, SpecificVolumeAtUnitPressure : float = None, InitialStateOfConsolidation : InitialStateOfConsolidation = None, OverConsolidationRatio : float = None, PreconsolidationPressure : float = None, ElasticParameters : ElasticParameters = None, AutoCalculateAlfaFactor : bool = None, AlfaFactor : float = None, MinimumBulkModulus : float = None, KTensionSuction : float = None, KapaSuction : float = None, RParameter : float = None, BetaParameter : float = None, ReferenceMeanStress : float = None, AtmosphericPressure : float = None):
		if SlopeOfCriticalStateLines is not None:
			self._setDoubleProperty("MP_M_SLOPE", SlopeOfCriticalStateLines)
		if IncludeTheEffectOfLodesAngle is not None:
			self._setBoolProperty("MP_USE_LODE", IncludeTheEffectOfLodesAngle)
		if Lambda is not None:
			self._setDoubleProperty("MP_BB_LAMBDA", Lambda)
		if Kappa is not None:
			self._setDoubleProperty("MP_BB_KAPPA", Kappa)
		if SpecificVolumeAtUnitPressure is not None:
			self._setDoubleProperty("MP_BB_N", SpecificVolumeAtUnitPressure)
		if InitialStateOfConsolidation is not None:
			self._setEnumEInitialStateOfConsolidationProperty("MP_INITIAL_CONSOLIDATION_STATE", InitialStateOfConsolidation)
		if OverConsolidationRatio is not None:
			self._setDoubleProperty("MP_BB_OCR", OverConsolidationRatio)
		if PreconsolidationPressure is not None:
			self._setDoubleProperty("MP_BB_PC", PreconsolidationPressure)
		if ElasticParameters is not None:
			self._setEnumEElasticParametersProperty("MP_ELASTIC_PARAMETERS", ElasticParameters)
		if AutoCalculateAlfaFactor is not None:
			self._setBoolProperty("MP_USE_AUTO_ALFA", AutoCalculateAlfaFactor)
		if AlfaFactor is not None:
			self._setDoubleProperty("MP_ALFA", AlfaFactor)
		if MinimumBulkModulus is not None:
			self._setDoubleProperty("MP_MIN_BULK_MODULUS", MinimumBulkModulus)
		if KTensionSuction is not None:
			self._setDoubleProperty("MP_K_TENSION_SUCTION", KTensionSuction)
		if KapaSuction is not None:
			self._setDoubleProperty("MP_KAPA_SUCTION", KapaSuction)
		if RParameter is not None:
			self._setDoubleProperty("MP_BB_R", RParameter)
		if BetaParameter is not None:
			self._setDoubleProperty("MP_BB_BETA", BetaParameter)
		if ReferenceMeanStress is not None:
			self._setDoubleProperty("MP_REF_PRESSURE", ReferenceMeanStress)
		if AtmosphericPressure is not None:
			self._setDoubleProperty("MP_P_ATM", AtmosphericPressure)
	def getProperties(self):
		return {
		"SlopeOfCriticalStateLines" : self.getSlopeOfCriticalStateLines(), 
		"IncludeTheEffectOfLodesAngle" : self.getIncludeTheEffectOfLodesAngle(), 
		"Lambda" : self.getLambda(), 
		"Kappa" : self.getKappa(), 
		"SpecificVolumeAtUnitPressure" : self.getSpecificVolumeAtUnitPressure(), 
		"InitialStateOfConsolidation" : self.getInitialStateOfConsolidation(), 
		"OverConsolidationRatio" : self.getOverConsolidationRatio(), 
		"PreconsolidationPressure" : self.getPreconsolidationPressure(), 
		"ElasticParameters" : self.getElasticParameters(), 
		"AutoCalculateAlfaFactor" : self.getAutoCalculateAlfaFactor(), 
		"AlfaFactor" : self.getAlfaFactor(), 
		"MinimumBulkModulus" : self.getMinimumBulkModulus(), 
		"KTensionSuction" : self.getKTensionSuction(), 
		"KapaSuction" : self.getKapaSuction(), 
		"RParameter" : self.getRParameter(), 
		"BetaParameter" : self.getBetaParameter(), 
		"ReferenceMeanStress" : self.getReferenceMeanStress(), 
		"AtmosphericPressure" : self.getAtmosphericPressure(), 
		}
