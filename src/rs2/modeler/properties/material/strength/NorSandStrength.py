from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class NorSandStrength(PropertyProxy):
	def getMTCCriticalFrictionRatio(self) -> float:
		return self._getDoubleProperty("MP_NS_MTC")
	def setMTCCriticalFrictionRatio(self, value: float):
		return self._setDoubleProperty("MP_NS_MTC", value)
	def getLambdaSlopeOfCSLNaturalLog(self) -> float:
		return self._getDoubleProperty("MP_NS_LAMBDA")
	def setLambdaSlopeOfCSLNaturalLog(self, value: float):
		return self._setDoubleProperty("MP_NS_LAMBDA", value)
	def getH0PlasticHardeningModulus(self) -> float:
		return self._getDoubleProperty("MP_NS_H0")
	def setH0PlasticHardeningModulus(self, value: float):
		return self._setDoubleProperty("MP_NS_H0", value)
	def getChiTCDilationCoefficient(self) -> float:
		return self._getDoubleProperty("MP_NS_CHITC")
	def setChiTCDilationCoefficient(self, value: float):
		return self._setDoubleProperty("MP_NS_CHITC", value)
	def getNVolumetricCouplingCoefficient(self) -> float:
		return self._getDoubleProperty("MP_NS_N")
	def setNVolumetricCouplingCoefficient(self, value: float):
		return self._setDoubleProperty("MP_NS_N", value)
	def getHyChangeInHardeningModulus(self) -> float:
		return self._getDoubleProperty("MP_NS_HY")
	def setHyChangeInHardeningModulus(self, value: float):
		return self._setDoubleProperty("MP_NS_HY", value)
	def getPsi0InitialStateParameter(self) -> float:
		return self._getDoubleProperty("MP_NS_PSI0")
	def setPsi0InitialStateParameter(self, value: float):
		return self._setDoubleProperty("MP_NS_PSI0", value)
	def getGamaAltitudeOfCSLAt1KPa(self) -> float:
		return self._getDoubleProperty("MP_NS_GAMA")
	def setGamaAltitudeOfCSLAt1KPa(self, value: float):
		return self._setDoubleProperty("MP_NS_GAMA", value)
	def getInitialConsolidationCondition(self) -> NorSandInitialConsolidationCondition:
		return NorSandInitialConsolidationCondition(self._getEnumENorSandInitialConsolidationConditionProperty("MP_NS_INTIIAL_CONSOLIDATION_CONDITION"))
	def setInitialConsolidationCondition(self, value: NorSandInitialConsolidationCondition):
		return self._setEnumENorSandInitialConsolidationConditionProperty("MP_NS_INTIIAL_CONSOLIDATION_CONDITION", value)
	def getOCR(self) -> float:
		return self._getDoubleProperty("MP_NS_OCR")
	def setOCR(self, value: float):
		return self._setDoubleProperty("MP_NS_OCR", value)
	def getInitialMeanStress(self) -> float:
		return self._getDoubleProperty("MP_NS_INITIAL_MEAN_STRESS")
	def setInitialMeanStress(self, value: float):
		return self._setDoubleProperty("MP_NS_INITIAL_MEAN_STRESS", value)
	def getCapSoftening(self) -> bool:
		return self._getBoolProperty("MP_NS_CAP_SOFTENING")
	def setCapSoftening(self, value: bool):
		return self._setBoolProperty("MP_NS_CAP_SOFTENING", value)
	def getNorSandFluidBulkModulus(self) -> float:
		return self._getDoubleProperty("MP_NS_FLUID_BULK_MODULUS")
	def setNorSandFluidBulkModulus(self, value: float):
		return self._setDoubleProperty("MP_NS_FLUID_BULK_MODULUS", value)
	def setProperties(self, MTCCriticalFrictionRatio : float = None, LambdaSlopeOfCSLNaturalLog : float = None, H0PlasticHardeningModulus : float = None, ChiTCDilationCoefficient : float = None, NVolumetricCouplingCoefficient : float = None, HyChangeInHardeningModulus : float = None, Psi0InitialStateParameter : float = None, GamaAltitudeOfCSLAt1KPa : float = None, InitialConsolidationCondition : NorSandInitialConsolidationCondition = None, OCR : float = None, InitialMeanStress : float = None, CapSoftening : bool = None, NorSandFluidBulkModulus : float = None):
		if MTCCriticalFrictionRatio is not None:
			self._setDoubleProperty("MP_NS_MTC", MTCCriticalFrictionRatio)
		if LambdaSlopeOfCSLNaturalLog is not None:
			self._setDoubleProperty("MP_NS_LAMBDA", LambdaSlopeOfCSLNaturalLog)
		if H0PlasticHardeningModulus is not None:
			self._setDoubleProperty("MP_NS_H0", H0PlasticHardeningModulus)
		if ChiTCDilationCoefficient is not None:
			self._setDoubleProperty("MP_NS_CHITC", ChiTCDilationCoefficient)
		if NVolumetricCouplingCoefficient is not None:
			self._setDoubleProperty("MP_NS_N", NVolumetricCouplingCoefficient)
		if HyChangeInHardeningModulus is not None:
			self._setDoubleProperty("MP_NS_HY", HyChangeInHardeningModulus)
		if Psi0InitialStateParameter is not None:
			self._setDoubleProperty("MP_NS_PSI0", Psi0InitialStateParameter)
		if GamaAltitudeOfCSLAt1KPa is not None:
			self._setDoubleProperty("MP_NS_GAMA", GamaAltitudeOfCSLAt1KPa)
		if InitialConsolidationCondition is not None:
			self._setEnumENorSandInitialConsolidationConditionProperty("MP_NS_INTIIAL_CONSOLIDATION_CONDITION", InitialConsolidationCondition)
		if OCR is not None:
			self._setDoubleProperty("MP_NS_OCR", OCR)
		if InitialMeanStress is not None:
			self._setDoubleProperty("MP_NS_INITIAL_MEAN_STRESS", InitialMeanStress)
		if CapSoftening is not None:
			self._setBoolProperty("MP_NS_CAP_SOFTENING", CapSoftening)
		if NorSandFluidBulkModulus is not None:
			self._setDoubleProperty("MP_NS_FLUID_BULK_MODULUS", NorSandFluidBulkModulus)
	def getProperties(self):
		return {
		"MTCCriticalFrictionRatio" : self.getMTCCriticalFrictionRatio(), 
		"LambdaSlopeOfCSLNaturalLog" : self.getLambdaSlopeOfCSLNaturalLog(), 
		"H0PlasticHardeningModulus" : self.getH0PlasticHardeningModulus(), 
		"ChiTCDilationCoefficient" : self.getChiTCDilationCoefficient(), 
		"NVolumetricCouplingCoefficient" : self.getNVolumetricCouplingCoefficient(), 
		"HyChangeInHardeningModulus" : self.getHyChangeInHardeningModulus(), 
		"Psi0InitialStateParameter" : self.getPsi0InitialStateParameter(), 
		"GamaAltitudeOfCSLAt1KPa" : self.getGamaAltitudeOfCSLAt1KPa(), 
		"InitialConsolidationCondition" : self.getInitialConsolidationCondition(), 
		"OCR" : self.getOCR(), 
		"InitialMeanStress" : self.getInitialMeanStress(), 
		"CapSoftening" : self.getCapSoftening(), 
		"NorSandFluidBulkModulus" : self.getNorSandFluidBulkModulus(), 
		}
