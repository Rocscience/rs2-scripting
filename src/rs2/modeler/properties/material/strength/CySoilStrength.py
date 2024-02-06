from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class CySoilStrength(PropertyProxy):
	def getCap(self) -> CySoilCapOption:
		return CySoilCapOption(self._getEnumECySoilCapOptionProperty("MP_CYS_CAP"))
	def setCap(self, value: CySoilCapOption):
		return self._setEnumECySoilCapOptionProperty("MP_CYS_CAP", value)
	def getAlfaCap(self) -> float:
		return self._getDoubleProperty("MP_CYS_ALFA_CAP")
	def setAlfaCap(self, value: float):
		return self._setDoubleProperty("MP_CYS_ALFA_CAP", value)
	def getNormallyConsolidatedCapPressure(self) -> float:
		return self._getDoubleProperty("MP_CYS_NORM_CONSOL_CAP_PRESSURE")
	def setNormallyConsolidatedCapPressure(self, value: float):
		return self._setDoubleProperty("MP_CYS_NORM_CONSOL_CAP_PRESSURE", value)
	def getFrictionAngleFailure(self) -> float:
		return self._getDoubleProperty("MP_CYS_FRIC_ANGLE_FAILURE")
	def setFrictionAngleFailure(self, value: float):
		return self._setDoubleProperty("MP_CYS_FRIC_ANGLE_FAILURE", value)
	def getCohesion(self) -> float:
		return self._getDoubleProperty("MP_CYS_COHESION")
	def setCohesion(self, value: float):
		return self._setDoubleProperty("MP_CYS_COHESION", value)
	def getFailureRatio(self) -> float:
		return self._getDoubleProperty("MP_CYS_FAILURE_RATIO")
	def setFailureRatio(self, value: float):
		return self._setDoubleProperty("MP_CYS_FAILURE_RATIO", value)
	def getFrictionAngleNormallyConsolidated(self) -> float:
		return self._getDoubleProperty("MP_CYS_FRIC_ANGLE_NORM_CONSOL")
	def setFrictionAngleNormallyConsolidated(self, value: float):
		return self._setDoubleProperty("MP_CYS_FRIC_ANGLE_NORM_CONSOL", value)
	def getBetaShearCalibrationFactor(self) -> float:
		return self._getDoubleProperty("MP_CYS_BETA")
	def setBetaShearCalibrationFactor(self, value: float):
		return self._setDoubleProperty("MP_CYS_BETA", value)
	def getTensileStrength(self) -> float:
		return self._getDoubleProperty("MP_CYS_TENSILE")
	def setTensileStrength(self, value: float):
		return self._setDoubleProperty("MP_CYS_TENSILE", value)
	def getDilationAngle(self) -> float:
		return self._getDoubleProperty("MP_CYS_DILATION_ANGLE")
	def setDilationAngle(self, value: float):
		return self._setDoubleProperty("MP_CYS_DILATION_ANGLE", value)
	def getDilationOption(self) -> DilationOption:
		return DilationOption(self._getEnumEDilationOptionProperty("MP_CYS_DILATION_OPTION"))
	def setDilationOption(self, value: DilationOption):
		return self._setEnumEDilationOptionProperty("MP_CYS_DILATION_OPTION", value)
	def getConstantVolumeFrictionAngle(self) -> float:
		return self._getDoubleProperty("MP_CYS_CONST_V_FRIC_ANGLE")
	def setConstantVolumeFrictionAngle(self, value: float):
		return self._setDoubleProperty("MP_CYS_CONST_V_FRIC_ANGLE", value)
	def setProperties(self, Cap : CySoilCapOption = None, AlfaCap : float = None, NormallyConsolidatedCapPressure : float = None, FrictionAngleFailure : float = None, Cohesion : float = None, FailureRatio : float = None, FrictionAngleNormallyConsolidated : float = None, BetaShearCalibrationFactor : float = None, TensileStrength : float = None, DilationAngle : float = None, DilationOption : DilationOption = None, ConstantVolumeFrictionAngle : float = None):
		if Cap is not None:
			self._setEnumECySoilCapOptionProperty("MP_CYS_CAP", Cap)
		if AlfaCap is not None:
			self._setDoubleProperty("MP_CYS_ALFA_CAP", AlfaCap)
		if NormallyConsolidatedCapPressure is not None:
			self._setDoubleProperty("MP_CYS_NORM_CONSOL_CAP_PRESSURE", NormallyConsolidatedCapPressure)
		if FrictionAngleFailure is not None:
			self._setDoubleProperty("MP_CYS_FRIC_ANGLE_FAILURE", FrictionAngleFailure)
		if Cohesion is not None:
			self._setDoubleProperty("MP_CYS_COHESION", Cohesion)
		if FailureRatio is not None:
			self._setDoubleProperty("MP_CYS_FAILURE_RATIO", FailureRatio)
		if FrictionAngleNormallyConsolidated is not None:
			self._setDoubleProperty("MP_CYS_FRIC_ANGLE_NORM_CONSOL", FrictionAngleNormallyConsolidated)
		if BetaShearCalibrationFactor is not None:
			self._setDoubleProperty("MP_CYS_BETA", BetaShearCalibrationFactor)
		if TensileStrength is not None:
			self._setDoubleProperty("MP_CYS_TENSILE", TensileStrength)
		if DilationAngle is not None:
			self._setDoubleProperty("MP_CYS_DILATION_ANGLE", DilationAngle)
		if DilationOption is not None:
			self._setEnumEDilationOptionProperty("MP_CYS_DILATION_OPTION", DilationOption)
		if ConstantVolumeFrictionAngle is not None:
			self._setDoubleProperty("MP_CYS_CONST_V_FRIC_ANGLE", ConstantVolumeFrictionAngle)
	def getProperties(self):
		return {
		"Cap" : self.getCap(), 
		"AlfaCap" : self.getAlfaCap(), 
		"NormallyConsolidatedCapPressure" : self.getNormallyConsolidatedCapPressure(), 
		"FrictionAngleFailure" : self.getFrictionAngleFailure(), 
		"Cohesion" : self.getCohesion(), 
		"FailureRatio" : self.getFailureRatio(), 
		"FrictionAngleNormallyConsolidated" : self.getFrictionAngleNormallyConsolidated(), 
		"BetaShearCalibrationFactor" : self.getBetaShearCalibrationFactor(), 
		"TensileStrength" : self.getTensileStrength(), 
		"DilationAngle" : self.getDilationAngle(), 
		"DilationOption" : self.getDilationOption(), 
		"ConstantVolumeFrictionAngle" : self.getConstantVolumeFrictionAngle(), 
		}
