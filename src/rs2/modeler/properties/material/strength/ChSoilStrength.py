from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class ChSoilStrength(PropertyProxy):
	def getFrictionAngleFailure(self) -> float:
		return self._getDoubleProperty("MP_CHS_FRIC_ANGLE_FAILURE")
	def setFrictionAngleFailure(self, value: float):
		return self._setDoubleProperty("MP_CHS_FRIC_ANGLE_FAILURE", value)
	def getCohesion(self) -> float:
		return self._getDoubleProperty("MP_CHS_COHESION")
	def setCohesion(self, value: float):
		return self._setDoubleProperty("MP_CHS_COHESION", value)
	def getFailureRatio(self) -> float:
		return self._getDoubleProperty("MP_CHS_FAILURE_RATIO")
	def setFailureRatio(self, value: float):
		return self._setDoubleProperty("MP_CHS_FAILURE_RATIO", value)
	def getFrictionAngleNormallyConsolidated(self) -> float:
		return self._getDoubleProperty("MP_CHS_REIC_ANGLE_CONSOL")
	def setFrictionAngleNormallyConsolidated(self, value: float):
		return self._setDoubleProperty("MP_CHS_REIC_ANGLE_CONSOL", value)
	def getTensileStrength(self) -> float:
		return self._getDoubleProperty("MP_CHS_TENSILE")
	def setTensileStrength(self, value: float):
		return self._setDoubleProperty("MP_CHS_TENSILE", value)
	def getDilationAngle(self) -> float:
		return self._getDoubleProperty("MP_CHS_DILATION_ANGLE")
	def setDilationAngle(self, value: float):
		return self._setDoubleProperty("MP_CHS_DILATION_ANGLE", value)
	def getDilationOption(self) -> DilationOption:
		return DilationOption(self._getEnumEDilationOptionProperty("MP_CHS_DILATION_OPTION"))
	def setDilationOption(self, value: DilationOption):
		return self._setEnumEDilationOptionProperty("MP_CHS_DILATION_OPTION", value)
	def getConstantVolumeFrictionAngle(self) -> float:
		return self._getDoubleProperty("MP_CHS_CONST_V_FRIC_ANGLE")
	def setConstantVolumeFrictionAngle(self, value: float):
		return self._setDoubleProperty("MP_CHS_CONST_V_FRIC_ANGLE", value)
	def setProperties(self, FrictionAngleFailure : float = None, Cohesion : float = None, FailureRatio : float = None, FrictionAngleNormallyConsolidated : float = None, TensileStrength : float = None, DilationAngle : float = None, DilationOption : DilationOption = None, ConstantVolumeFrictionAngle : float = None):
		if FrictionAngleFailure is not None:
			self._setDoubleProperty("MP_CHS_FRIC_ANGLE_FAILURE", FrictionAngleFailure)
		if Cohesion is not None:
			self._setDoubleProperty("MP_CHS_COHESION", Cohesion)
		if FailureRatio is not None:
			self._setDoubleProperty("MP_CHS_FAILURE_RATIO", FailureRatio)
		if FrictionAngleNormallyConsolidated is not None:
			self._setDoubleProperty("MP_CHS_REIC_ANGLE_CONSOL", FrictionAngleNormallyConsolidated)
		if TensileStrength is not None:
			self._setDoubleProperty("MP_CHS_TENSILE", TensileStrength)
		if DilationAngle is not None:
			self._setDoubleProperty("MP_CHS_DILATION_ANGLE", DilationAngle)
		if DilationOption is not None:
			self._setEnumEDilationOptionProperty("MP_CHS_DILATION_OPTION", DilationOption)
		if ConstantVolumeFrictionAngle is not None:
			self._setDoubleProperty("MP_CHS_CONST_V_FRIC_ANGLE", ConstantVolumeFrictionAngle)
	def getProperties(self):
		return {
		"FrictionAngleFailure" : self.getFrictionAngleFailure(), 
		"Cohesion" : self.getCohesion(), 
		"FailureRatio" : self.getFailureRatio(), 
		"FrictionAngleNormallyConsolidated" : self.getFrictionAngleNormallyConsolidated(), 
		"TensileStrength" : self.getTensileStrength(), 
		"DilationAngle" : self.getDilationAngle(), 
		"DilationOption" : self.getDilationOption(), 
		"ConstantVolumeFrictionAngle" : self.getConstantVolumeFrictionAngle(), 
		}
