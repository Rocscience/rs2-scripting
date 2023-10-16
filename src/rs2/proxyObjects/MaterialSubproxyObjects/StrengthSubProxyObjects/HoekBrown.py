from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class HoekBrown(PropertyProxy):
	def getMaterialType(self) -> MaterialType:
		return MaterialType(self._getEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE"))
	def setMaterialType(self, value: MaterialType):
		return self._setEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE", value)
	def getCompressiveStrength(self) -> float:
		return self._getDoubleProperty("MP_COMPRESSIVE_STRENGTH")
	def setCompressiveStrength(self, value: float):
		return self._setDoubleProperty("MP_COMPRESSIVE_STRENGTH", value)
	def getMbParameter(self) -> float:
		return self._getDoubleProperty("MP_MB_PARAMETER")
	def setMbParameter(self, value: float):
		return self._setDoubleProperty("MP_MB_PARAMETER", value)
	def getSParameter(self) -> float:
		return self._getDoubleProperty("MP_S_PARAMETER")
	def setSParameter(self, value: float):
		return self._setDoubleProperty("MP_S_PARAMETER", value)
	def getResidualMbParameter(self) -> float:
		return self._getDoubleProperty("MP_MB_PARAMETER_RES")
	def setResidualMbParameter(self, value: float):
		return self._setDoubleProperty("MP_MB_PARAMETER_RES", value)
	def getResidualSParameter(self) -> float:
		return self._getDoubleProperty("MP_S_PARAMETER_RES")
	def setResidualSParameter(self, value: float):
		return self._setDoubleProperty("MP_S_PARAMETER_RES", value)
	def getDilationParameter(self) -> float:
		return self._getDoubleProperty("MP_DILATION_PARAMETER")
	def setDilationParameter(self, value: float):
		return self._setDoubleProperty("MP_DILATION_PARAMETER", value)
	def getApplySSRShearStrengthReduction(self) -> bool:
		return self._getBoolProperty("MP_APPLY_SSR")
	def setApplySSRShearStrengthReduction(self, value: bool):
		return self._setBoolProperty("MP_APPLY_SSR", value)
	def setProperties(self, MaterialType : MaterialType = None, CompressiveStrength : float = None, MbParameter : float = None, SParameter : float = None, ResidualMbParameter : float = None, ResidualSParameter : float = None, DilationParameter : float = None, ApplySSRShearStrengthReduction : bool = None):
		if MaterialType is not None:
			self._setEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE", MaterialType)
		if CompressiveStrength is not None:
			self._setDoubleProperty("MP_COMPRESSIVE_STRENGTH", CompressiveStrength)
		if MbParameter is not None:
			self._setDoubleProperty("MP_MB_PARAMETER", MbParameter)
		if SParameter is not None:
			self._setDoubleProperty("MP_S_PARAMETER", SParameter)
		if ResidualMbParameter is not None:
			self._setDoubleProperty("MP_MB_PARAMETER_RES", ResidualMbParameter)
		if ResidualSParameter is not None:
			self._setDoubleProperty("MP_S_PARAMETER_RES", ResidualSParameter)
		if DilationParameter is not None:
			self._setDoubleProperty("MP_DILATION_PARAMETER", DilationParameter)
		if ApplySSRShearStrengthReduction is not None:
			self._setBoolProperty("MP_APPLY_SSR", ApplySSRShearStrengthReduction)
	def getProperties(self):
		return {
		"MaterialType" : self.getMaterialType(), 
		"CompressiveStrength" : self.getCompressiveStrength(), 
		"MbParameter" : self.getMbParameter(), 
		"SParameter" : self.getSParameter(), 
		"ResidualMbParameter" : self.getResidualMbParameter(), 
		"ResidualSParameter" : self.getResidualSParameter(), 
		"DilationParameter" : self.getDilationParameter(), 
		"ApplySSRShearStrengthReduction" : self.getApplySSRShearStrengthReduction(), 
		}
