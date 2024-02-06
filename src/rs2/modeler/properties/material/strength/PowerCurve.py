from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class PowerCurve(PropertyProxy):
	def getMaterialType(self) -> MaterialType:
		return MaterialType(self._getEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE"))
	def setMaterialType(self, value: MaterialType):
		return self._setEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE", value)
	def getAParameter(self) -> float:
		return self._getDoubleProperty("MP_PC_A")
	def setAParameter(self, value: float):
		return self._setDoubleProperty("MP_PC_A", value)
	def getBParameter(self) -> float:
		return self._getDoubleProperty("MP_PC_B")
	def setBParameter(self, value: float):
		return self._setDoubleProperty("MP_PC_B", value)
	def getCParameter(self) -> float:
		return self._getDoubleProperty("MP_PC_C")
	def setCParameter(self, value: float):
		return self._setDoubleProperty("MP_PC_C", value)
	def getDParameter(self) -> float:
		return self._getDoubleProperty("MP_PC_D")
	def setDParameter(self, value: float):
		return self._setDoubleProperty("MP_PC_D", value)
	def getWaviness(self) -> float:
		return self._getDoubleProperty("MP_PC_WAVINESS")
	def setWaviness(self, value: float):
		return self._setDoubleProperty("MP_PC_WAVINESS", value)
	def getResidualAParameter(self) -> float:
		return self._getDoubleProperty("MP_PC_A_RES")
	def setResidualAParameter(self, value: float):
		return self._setDoubleProperty("MP_PC_A_RES", value)
	def getResidualBParameter(self) -> float:
		return self._getDoubleProperty("MP_PC_B_RES")
	def setResidualBParameter(self, value: float):
		return self._setDoubleProperty("MP_PC_B_RES", value)
	def getResidualCParameter(self) -> float:
		return self._getDoubleProperty("MP_PC_C_RES")
	def setResidualCParameter(self, value: float):
		return self._setDoubleProperty("MP_PC_C_RES", value)
	def getResidualDParameter(self) -> float:
		return self._getDoubleProperty("MP_PC_D_RES")
	def setResidualDParameter(self, value: float):
		return self._setDoubleProperty("MP_PC_D_RES", value)
	def getResidualWaviness(self) -> float:
		return self._getDoubleProperty("MP_PC_WAVINESS_RES")
	def setResidualWaviness(self, value: float):
		return self._setDoubleProperty("MP_PC_WAVINESS_RES", value)
	def getDilationRatio(self) -> float:
		return self._getDoubleProperty("MP_DILATION_RATIO")
	def setDilationRatio(self, value: float):
		return self._setDoubleProperty("MP_DILATION_RATIO", value)
	def getApplySSRShearStrengthReduction(self) -> bool:
		return self._getBoolProperty("MP_APPLY_SSR")
	def setApplySSRShearStrengthReduction(self, value: bool):
		return self._setBoolProperty("MP_APPLY_SSR", value)
	def setProperties(self, MaterialType : MaterialType = None, AParameter : float = None, BParameter : float = None, CParameter : float = None, DParameter : float = None, Waviness : float = None, ResidualAParameter : float = None, ResidualBParameter : float = None, ResidualCParameter : float = None, ResidualDParameter : float = None, ResidualWaviness : float = None, DilationRatio : float = None, ApplySSRShearStrengthReduction : bool = None):
		if MaterialType is not None:
			self._setEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE", MaterialType)
		if AParameter is not None:
			self._setDoubleProperty("MP_PC_A", AParameter)
		if BParameter is not None:
			self._setDoubleProperty("MP_PC_B", BParameter)
		if CParameter is not None:
			self._setDoubleProperty("MP_PC_C", CParameter)
		if DParameter is not None:
			self._setDoubleProperty("MP_PC_D", DParameter)
		if Waviness is not None:
			self._setDoubleProperty("MP_PC_WAVINESS", Waviness)
		if ResidualAParameter is not None:
			self._setDoubleProperty("MP_PC_A_RES", ResidualAParameter)
		if ResidualBParameter is not None:
			self._setDoubleProperty("MP_PC_B_RES", ResidualBParameter)
		if ResidualCParameter is not None:
			self._setDoubleProperty("MP_PC_C_RES", ResidualCParameter)
		if ResidualDParameter is not None:
			self._setDoubleProperty("MP_PC_D_RES", ResidualDParameter)
		if ResidualWaviness is not None:
			self._setDoubleProperty("MP_PC_WAVINESS_RES", ResidualWaviness)
		if DilationRatio is not None:
			self._setDoubleProperty("MP_DILATION_RATIO", DilationRatio)
		if ApplySSRShearStrengthReduction is not None:
			self._setBoolProperty("MP_APPLY_SSR", ApplySSRShearStrengthReduction)
	def getProperties(self):
		return {
		"MaterialType" : self.getMaterialType(), 
		"AParameter" : self.getAParameter(), 
		"BParameter" : self.getBParameter(), 
		"CParameter" : self.getCParameter(), 
		"DParameter" : self.getDParameter(), 
		"Waviness" : self.getWaviness(), 
		"ResidualAParameter" : self.getResidualAParameter(), 
		"ResidualBParameter" : self.getResidualBParameter(), 
		"ResidualCParameter" : self.getResidualCParameter(), 
		"ResidualDParameter" : self.getResidualDParameter(), 
		"ResidualWaviness" : self.getResidualWaviness(), 
		"DilationRatio" : self.getDilationRatio(), 
		"ApplySSRShearStrengthReduction" : self.getApplySSRShearStrengthReduction(), 
		}
