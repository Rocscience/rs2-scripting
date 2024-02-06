from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class SoftSoilStrength(PropertyProxy):
	def getFrictionAngle(self) -> float:
		return self._getDoubleProperty("MP_SS_FRICTION_ANGLE")
	def setFrictionAngle(self, value: float):
		return self._setDoubleProperty("MP_SS_FRICTION_ANGLE", value)
	def getCohesion(self) -> float:
		return self._getDoubleProperty("MP_SS_COHESION")
	def setCohesion(self, value: float):
		return self._setDoubleProperty("MP_SS_COHESION", value)
	def getTensileStrength(self) -> float:
		return self._getDoubleProperty("MP_SS_TENSILE")
	def setTensileStrength(self, value: float):
		return self._setDoubleProperty("MP_SS_TENSILE", value)
	def getDilationAngle(self) -> float:
		return self._getDoubleProperty("MP_SS_DILATION_ANGLE")
	def setDilationAngle(self, value: float):
		return self._setDoubleProperty("MP_SS_DILATION_ANGLE", value)
	def getLambda(self) -> float:
		return self._getDoubleProperty("MP_SS_LAMBDA")
	def setLambda(self, value: float):
		return self._setDoubleProperty("MP_SS_LAMBDA", value)
	def getKappa(self) -> float:
		return self._getDoubleProperty("MP_SS_KAPPA")
	def setKappa(self, value: float):
		return self._setDoubleProperty("MP_SS_KAPPA", value)
	def getK0NormalConsolidation(self) -> float:
		return self._getDoubleProperty("MP_SS_K0_NORM_CONSOL")
	def setK0NormalConsolidation(self, value: float):
		return self._setDoubleProperty("MP_SS_K0_NORM_CONSOL", value)
	def getInitialConsolidationCondition(self) -> InitialConsolidation:
		return InitialConsolidation(self._getEnumEInitialConsolidationProperty("MP_SS_INIT_CONSOL"))
	def setInitialConsolidationCondition(self, value: InitialConsolidation):
		return self._setEnumEInitialConsolidationProperty("MP_SS_INIT_CONSOL", value)
	def getOCRStress(self) -> float:
		return self._getDoubleProperty("MP_SS_OCR_STRESS")
	def setOCRStress(self, value: float):
		return self._setDoubleProperty("MP_SS_OCR_STRESS", value)
	def getInitialMeanStress(self) -> float:
		return self._getDoubleProperty("MP_SS_INIT_MEAN_STRESS")
	def setInitialMeanStress(self, value: float):
		return self._setDoubleProperty("MP_SS_INIT_MEAN_STRESS", value)
	def setProperties(self, FrictionAngle : float = None, Cohesion : float = None, TensileStrength : float = None, DilationAngle : float = None, Lambda : float = None, Kappa : float = None, K0NormalConsolidation : float = None, InitialConsolidationCondition : InitialConsolidation = None, OCRStress : float = None, InitialMeanStress : float = None):
		if FrictionAngle is not None:
			self._setDoubleProperty("MP_SS_FRICTION_ANGLE", FrictionAngle)
		if Cohesion is not None:
			self._setDoubleProperty("MP_SS_COHESION", Cohesion)
		if TensileStrength is not None:
			self._setDoubleProperty("MP_SS_TENSILE", TensileStrength)
		if DilationAngle is not None:
			self._setDoubleProperty("MP_SS_DILATION_ANGLE", DilationAngle)
		if Lambda is not None:
			self._setDoubleProperty("MP_SS_LAMBDA", Lambda)
		if Kappa is not None:
			self._setDoubleProperty("MP_SS_KAPPA", Kappa)
		if K0NormalConsolidation is not None:
			self._setDoubleProperty("MP_SS_K0_NORM_CONSOL", K0NormalConsolidation)
		if InitialConsolidationCondition is not None:
			self._setEnumEInitialConsolidationProperty("MP_SS_INIT_CONSOL", InitialConsolidationCondition)
		if OCRStress is not None:
			self._setDoubleProperty("MP_SS_OCR_STRESS", OCRStress)
		if InitialMeanStress is not None:
			self._setDoubleProperty("MP_SS_INIT_MEAN_STRESS", InitialMeanStress)
	def getProperties(self):
		return {
		"FrictionAngle" : self.getFrictionAngle(), 
		"Cohesion" : self.getCohesion(), 
		"TensileStrength" : self.getTensileStrength(), 
		"DilationAngle" : self.getDilationAngle(), 
		"Lambda" : self.getLambda(), 
		"Kappa" : self.getKappa(), 
		"K0NormalConsolidation" : self.getK0NormalConsolidation(), 
		"InitialConsolidationCondition" : self.getInitialConsolidationCondition(), 
		"OCRStress" : self.getOCRStress(), 
		"InitialMeanStress" : self.getInitialMeanStress(), 
		}
