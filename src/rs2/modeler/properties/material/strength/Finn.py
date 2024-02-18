from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class Finn(PropertyProxy):
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
	def getResidualTensileStrength(self) -> float:
		return self._getDoubleProperty("MP_TENSILE_STRENGTH_RES")
	def setResidualTensileStrength(self, value: float):
		return self._setDoubleProperty("MP_TENSILE_STRENGTH_RES", value)
	def getResidualFrictionAngle(self) -> float:
		return self._getDoubleProperty("MP_FRICTION_ANGLE_RES")
	def setResidualFrictionAngle(self, value: float):
		return self._setDoubleProperty("MP_FRICTION_ANGLE_RES", value)
	def getResidualCohesion(self) -> float:
		return self._getDoubleProperty("MP_COHESION_RES")
	def setResidualCohesion(self, value: float):
		return self._setDoubleProperty("MP_COHESION_RES", value)
	def getDilationAngle(self) -> float:
		return self._getDoubleProperty("MP_DILATION_ANGLE")
	def setDilationAngle(self, value: float):
		return self._setDoubleProperty("MP_DILATION_ANGLE", value)
	def getApplySSRShearStrengthReduction(self) -> bool:
		return self._getBoolProperty("MP_APPLY_SSR")
	def setApplySSRShearStrengthReduction(self, value: bool):
		return self._setBoolProperty("MP_APPLY_SSR", value)
	def getFinnFormulation(self) -> FinnFormula:
		return FinnFormula(self._getEnumEFinnFormulaProperty("MP_FINN_FORMULA"))
	def setFinnFormulation(self, value: FinnFormula):
		return self._setEnumEFinnFormulaProperty("MP_FINN_FORMULA", value)
	def getC1Parameter(self) -> float:
		return self._getDoubleProperty("MP_FINN_C1")
	def setC1Parameter(self, value: float):
		return self._setDoubleProperty("MP_FINN_C1", value)
	def getC2Parameter(self) -> float:
		return self._getDoubleProperty("MP_FINN_C2")
	def setC2Parameter(self, value: float):
		return self._setDoubleProperty("MP_FINN_C2", value)
	def getC3Parameter(self) -> float:
		return self._getDoubleProperty("MP_FINN_C3")
	def setC3Parameter(self, value: float):
		return self._setDoubleProperty("MP_FINN_C3", value)
	def getC4Parameter(self) -> float:
		return self._getDoubleProperty("MP_FINN_C4")
	def setC4Parameter(self, value: float):
		return self._setDoubleProperty("MP_FINN_C4", value)
	def getByrneDefinition(self) -> FinnByrneDefinition:
		return FinnByrneDefinition(self._getEnumEFinnByrneDefinitionProperty("MP_FINN_BYRNE_DEFINITION"))
	def setByrneDefinition(self, value: FinnByrneDefinition):
		return self._setEnumEFinnByrneDefinitionProperty("MP_FINN_BYRNE_DEFINITION", value)
	def getFinnByrneC1Parameter(self) -> float:
		return self._getDoubleProperty("MP_FINN_BYRNE_C1")
	def setFinnByrneC1Parameter(self, value: float):
		return self._setDoubleProperty("MP_FINN_BYRNE_C1", value)
	def getFinnByrneC2Parameter(self) -> float:
		return self._getDoubleProperty("MP_FINN_BYRNE_C2")
	def setFinnByrneC2Parameter(self, value: float):
		return self._setDoubleProperty("MP_FINN_BYRNE_C2", value)
	def getN160(self) -> int:
		return self._getIntProperty("MP_FINN_BYRNE_N1")
	def setN160(self, value: int):
		return self._setIntProperty("MP_FINN_BYRNE_N1", value)
	def setProperties(self, PeakTensileStrength : float = None, PeakFrictionAngle : float = None, PeakCohesion : float = None, ResidualTensileStrength : float = None, ResidualFrictionAngle : float = None, ResidualCohesion : float = None, DilationAngle : float = None, ApplySSRShearStrengthReduction : bool = None, FinnFormulation : FinnFormula = None, C1Parameter : float = None, C2Parameter : float = None, C3Parameter : float = None, C4Parameter : float = None, ByrneDefinition : FinnByrneDefinition = None, FinnByrneC1Parameter : float = None, FinnByrneC2Parameter : float = None, N160 : int = None):
		if PeakTensileStrength is not None:
			self._setDoubleProperty("MP_PEAK_TENSILE_STRENGTH", PeakTensileStrength)
		if PeakFrictionAngle is not None:
			self._setDoubleProperty("MP_PEAK_FRICTION_ANGLE", PeakFrictionAngle)
		if PeakCohesion is not None:
			self._setDoubleProperty("MP_PEAK_COHESION", PeakCohesion)
		if ResidualTensileStrength is not None:
			self._setDoubleProperty("MP_TENSILE_STRENGTH_RES", ResidualTensileStrength)
		if ResidualFrictionAngle is not None:
			self._setDoubleProperty("MP_FRICTION_ANGLE_RES", ResidualFrictionAngle)
		if ResidualCohesion is not None:
			self._setDoubleProperty("MP_COHESION_RES", ResidualCohesion)
		if DilationAngle is not None:
			self._setDoubleProperty("MP_DILATION_ANGLE", DilationAngle)
		if ApplySSRShearStrengthReduction is not None:
			self._setBoolProperty("MP_APPLY_SSR", ApplySSRShearStrengthReduction)
		if FinnFormulation is not None:
			self._setEnumEFinnFormulaProperty("MP_FINN_FORMULA", FinnFormulation)
		if C1Parameter is not None:
			self._setDoubleProperty("MP_FINN_C1", C1Parameter)
		if C2Parameter is not None:
			self._setDoubleProperty("MP_FINN_C2", C2Parameter)
		if C3Parameter is not None:
			self._setDoubleProperty("MP_FINN_C3", C3Parameter)
		if C4Parameter is not None:
			self._setDoubleProperty("MP_FINN_C4", C4Parameter)
		if ByrneDefinition is not None:
			self._setEnumEFinnByrneDefinitionProperty("MP_FINN_BYRNE_DEFINITION", ByrneDefinition)
		if FinnByrneC1Parameter is not None:
			self._setDoubleProperty("MP_FINN_BYRNE_C1", FinnByrneC1Parameter)
		if FinnByrneC2Parameter is not None:
			self._setDoubleProperty("MP_FINN_BYRNE_C2", FinnByrneC2Parameter)
		if N160 is not None:
			self._setIntProperty("MP_FINN_BYRNE_N1", N160)
	def getProperties(self):
		return {
		"PeakTensileStrength" : self.getPeakTensileStrength(), 
		"PeakFrictionAngle" : self.getPeakFrictionAngle(), 
		"PeakCohesion" : self.getPeakCohesion(), 
		"ResidualTensileStrength" : self.getResidualTensileStrength(), 
		"ResidualFrictionAngle" : self.getResidualFrictionAngle(), 
		"ResidualCohesion" : self.getResidualCohesion(), 
		"DilationAngle" : self.getDilationAngle(), 
		"ApplySSRShearStrengthReduction" : self.getApplySSRShearStrengthReduction(), 
		"FinnFormulation" : self.getFinnFormulation(), 
		"C1Parameter" : self.getC1Parameter(), 
		"C2Parameter" : self.getC2Parameter(), 
		"C3Parameter" : self.getC3Parameter(), 
		"C4Parameter" : self.getC4Parameter(), 
		"ByrneDefinition" : self.getByrneDefinition(), 
		"FinnByrneC1Parameter" : self.getFinnByrneC1Parameter(), 
		"FinnByrneC2Parameter" : self.getFinnByrneC2Parameter(), 
		"N160" : self.getN160(), 
		}
