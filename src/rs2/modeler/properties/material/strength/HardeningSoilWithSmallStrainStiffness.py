from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class HardeningSoilWithSmallStrainStiffness(PropertyProxy):
	def getFrictionAngle(self) -> float:
		return self._getDoubleProperty("MP_HS_FRIC_ANGLE")
	def setFrictionAngle(self, value: float):
		return self._setDoubleProperty("MP_HS_FRIC_ANGLE", value)
	def getCohesion(self) -> float:
		return self._getDoubleProperty("MP_HS_COHESION")
	def setCohesion(self, value: float):
		return self._setDoubleProperty("MP_HS_COHESION", value)
	def getFailureRatio(self) -> float:
		return self._getDoubleProperty("MP_HS_FAILURE_RATIO")
	def setFailureRatio(self, value: float):
		return self._setDoubleProperty("MP_HS_FAILURE_RATIO", value)
	def getTensileStrength(self) -> float:
		return self._getDoubleProperty("MP_HS_TENSILE")
	def setTensileStrength(self, value: float):
		return self._setDoubleProperty("MP_HS_TENSILE", value)
	def getDilationAngle(self) -> float:
		return self._getDoubleProperty("MP_HS_DILATION_ANGLE")
	def setDilationAngle(self, value: float):
		return self._setDoubleProperty("MP_HS_DILATION_ANGLE", value)
	def getDilationOption(self) -> DilationOption:
		return DilationOption(self._getEnumEDilationOptionProperty("MP_HS_DILATION_OPTION"))
	def setDilationOption(self, value: DilationOption):
		return self._setEnumEDilationOptionProperty("MP_HS_DILATION_OPTION", value)
	def getDilatancyCutoff(self) -> Dilatancy:
		return Dilatancy(self._getEnumEDilatancyProperty("MP_HS_DILATANCY"))
	def setDilatancyCutoff(self, value: Dilatancy):
		return self._setEnumEDilatancyProperty("MP_HS_DILATANCY", value)
	def getE0(self) -> float:
		return self._getDoubleProperty("MP_HS_E_0")
	def setE0(self, value: float):
		return self._setDoubleProperty("MP_HS_E_0", value)
	def getEmax(self) -> float:
		return self._getDoubleProperty("MP_HS_E_MAX")
	def setEmax(self, value: float):
		return self._setDoubleProperty("MP_HS_E_MAX", value)
	def getK0NormalConsolidation(self) -> float:
		return self._getDoubleProperty("MP_HS_K0_NORM_CONSOL")
	def setK0NormalConsolidation(self, value: float):
		return self._setDoubleProperty("MP_HS_K0_NORM_CONSOL", value)
	def getInitialConsolidationCondition(self) -> InitialConsolidation:
		return InitialConsolidation(self._getEnumEInitialConsolidationProperty("MP_HS_INIT_CONSOL"))
	def setInitialConsolidationCondition(self, value: InitialConsolidation):
		return self._setEnumEInitialConsolidationProperty("MP_HS_INIT_CONSOL", value)
	def getOCRStress(self) -> float:
		return self._getDoubleProperty("MP_HS_OCR_STRESS")
	def setOCRStress(self, value: float):
		return self._setDoubleProperty("MP_HS_OCR_STRESS", value)
	def getInitialMeanStress(self) -> float:
		return self._getDoubleProperty("MP_HS_INIT_MEAN_STRESS")
	def setInitialMeanStress(self, value: float):
		return self._setDoubleProperty("MP_HS_INIT_MEAN_STRESS", value)
	def setProperties(self, FrictionAngle : float = None, Cohesion : float = None, FailureRatio : float = None, TensileStrength : float = None, DilationAngle : float = None, DilationOption : DilationOption = None, DilatancyCutoff : Dilatancy = None, E0 : float = None, Emax : float = None, K0NormalConsolidation : float = None, InitialConsolidationCondition : InitialConsolidation = None, OCRStress : float = None, InitialMeanStress : float = None):
		if FrictionAngle is not None:
			self._setDoubleProperty("MP_HS_FRIC_ANGLE", FrictionAngle)
		if Cohesion is not None:
			self._setDoubleProperty("MP_HS_COHESION", Cohesion)
		if FailureRatio is not None:
			self._setDoubleProperty("MP_HS_FAILURE_RATIO", FailureRatio)
		if TensileStrength is not None:
			self._setDoubleProperty("MP_HS_TENSILE", TensileStrength)
		if DilationAngle is not None:
			self._setDoubleProperty("MP_HS_DILATION_ANGLE", DilationAngle)
		if DilationOption is not None:
			self._setEnumEDilationOptionProperty("MP_HS_DILATION_OPTION", DilationOption)
		if DilatancyCutoff is not None:
			self._setEnumEDilatancyProperty("MP_HS_DILATANCY", DilatancyCutoff)
		if E0 is not None:
			self._setDoubleProperty("MP_HS_E_0", E0)
		if Emax is not None:
			self._setDoubleProperty("MP_HS_E_MAX", Emax)
		if K0NormalConsolidation is not None:
			self._setDoubleProperty("MP_HS_K0_NORM_CONSOL", K0NormalConsolidation)
		if InitialConsolidationCondition is not None:
			self._setEnumEInitialConsolidationProperty("MP_HS_INIT_CONSOL", InitialConsolidationCondition)
		if OCRStress is not None:
			self._setDoubleProperty("MP_HS_OCR_STRESS", OCRStress)
		if InitialMeanStress is not None:
			self._setDoubleProperty("MP_HS_INIT_MEAN_STRESS", InitialMeanStress)
	def getProperties(self):
		return {
		"FrictionAngle" : self.getFrictionAngle(), 
		"Cohesion" : self.getCohesion(), 
		"FailureRatio" : self.getFailureRatio(), 
		"TensileStrength" : self.getTensileStrength(), 
		"DilationAngle" : self.getDilationAngle(), 
		"DilationOption" : self.getDilationOption(), 
		"DilatancyCutoff" : self.getDilatancyCutoff(), 
		"E0" : self.getE0(), 
		"Emax" : self.getEmax(), 
		"K0NormalConsolidation" : self.getK0NormalConsolidation(), 
		"InitialConsolidationCondition" : self.getInitialConsolidationCondition(), 
		"OCRStress" : self.getOCRStress(), 
		"InitialMeanStress" : self.getInitialMeanStress(), 
		}
