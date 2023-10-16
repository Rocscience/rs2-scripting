from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class BartonBandis(PropertyProxy):
	def getMaterialType(self) -> MaterialType:
		return MaterialType(self._getEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE"))
	def setMaterialType(self, value: MaterialType):
		return self._setEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE", value)
	def getPhiR(self) -> float:
		return self._getDoubleProperty("MP_PHI_R")
	def setPhiR(self, value: float):
		return self._setDoubleProperty("MP_PHI_R", value)
	def getJRC(self) -> float:
		return self._getDoubleProperty("MP_JRC")
	def setJRC(self, value: float):
		return self._setDoubleProperty("MP_JRC", value)
	def getJCS(self) -> float:
		return self._getDoubleProperty("MP_JCS")
	def setJCS(self, value: float):
		return self._setDoubleProperty("MP_JCS", value)
	def getDilationRatio(self) -> float:
		return self._getDoubleProperty("MP_DILATION_RATIO")
	def setDilationRatio(self, value: float):
		return self._setDoubleProperty("MP_DILATION_RATIO", value)
	def getResidualStrength(self) -> bool:
		return self._getBoolProperty("MP_RESIDUAL_STRENGTH")
	def setResidualStrength(self, value: bool):
		return self._setBoolProperty("MP_RESIDUAL_STRENGTH", value)
	def getApplySSRShearStrengthReduction(self) -> bool:
		return self._getBoolProperty("MP_APPLY_SSR")
	def setApplySSRShearStrengthReduction(self, value: bool):
		return self._setBoolProperty("MP_APPLY_SSR", value)
	def setProperties(self, MaterialType : MaterialType = None, PhiR : float = None, JRC : float = None, JCS : float = None, DilationRatio : float = None, ResidualStrength : bool = None, ApplySSRShearStrengthReduction : bool = None):
		if MaterialType is not None:
			self._setEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE", MaterialType)
		if PhiR is not None:
			self._setDoubleProperty("MP_PHI_R", PhiR)
		if JRC is not None:
			self._setDoubleProperty("MP_JRC", JRC)
		if JCS is not None:
			self._setDoubleProperty("MP_JCS", JCS)
		if DilationRatio is not None:
			self._setDoubleProperty("MP_DILATION_RATIO", DilationRatio)
		if ResidualStrength is not None:
			self._setBoolProperty("MP_RESIDUAL_STRENGTH", ResidualStrength)
		if ApplySSRShearStrengthReduction is not None:
			self._setBoolProperty("MP_APPLY_SSR", ApplySSRShearStrengthReduction)
	def getProperties(self):
		return {
		"MaterialType" : self.getMaterialType(), 
		"PhiR" : self.getPhiR(), 
		"JRC" : self.getJRC(), 
		"JCS" : self.getJCS(), 
		"DilationRatio" : self.getDilationRatio(), 
		"ResidualStrength" : self.getResidualStrength(), 
		"ApplySSRShearStrengthReduction" : self.getApplySSRShearStrengthReduction(), 
		}
