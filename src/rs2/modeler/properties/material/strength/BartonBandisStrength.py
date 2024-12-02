from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class BartonBandisStrength(PropertyProxy):
	def getMaterialType(self) -> MaterialType:
		return MaterialType(self._getEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE"))
	def setMaterialType(self, value: MaterialType):
		return self._setEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE", value)
	def getPhiR(self) -> float:
		return self._getDoubleProperty("MP_FRICTION_ANGLE_RES")
	def setPhiR(self, value: float):
		return self._setDoubleProperty("MP_FRICTION_ANGLE_RES", value)
	def getJRC(self) -> float:
		return self._getDoubleProperty("MP_JRC")
	def setJRC(self, value: float):
		return self._setDoubleProperty("MP_JRC", value)
	def getJCS(self) -> float:
		return self._getDoubleProperty("MP_JCS")
	def setJCS(self, value: float):
		return self._setDoubleProperty("MP_JCS", value)
	def getDilationAngle(self) -> float:
		return self._getDoubleProperty("MP_DILATION_ANGLE")
	def setDilationAngle(self, value: float):
		return self._setDoubleProperty("MP_DILATION_ANGLE", value)
	def getResidualStrength(self) -> bool:
		return self._getBoolProperty("MP_RESIDUAL_STRENGTH")
	def setResidualStrength(self, value: bool):
		return self._setBoolProperty("MP_RESIDUAL_STRENGTH", value)
	def getApplySSRShearStrengthReduction(self) -> bool:
		return self._getBoolProperty("MP_APPLY_SSR")
	def setApplySSRShearStrengthReduction(self, value: bool):
		return self._setBoolProperty("MP_APPLY_SSR", value)
	def setProperties(self, MaterialType : MaterialType = None, PhiR : float = None, JRC : float = None, JCS : float = None, DilationAngle : float = None, ResidualStrength : bool = None, ApplySSRShearStrengthReduction : bool = None):
		if MaterialType is not None:
			self._setEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE", MaterialType)
		if PhiR is not None:
			self._setDoubleProperty("MP_FRICTION_ANGLE_RES", PhiR)
		if JRC is not None:
			self._setDoubleProperty("MP_JRC", JRC)
		if JCS is not None:
			self._setDoubleProperty("MP_JCS", JCS)
		if DilationAngle is not None:
			self._setDoubleProperty("MP_DILATION_ANGLE", DilationAngle)
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
		"DilationAngle" : self.getDilationAngle(), 
		"ResidualStrength" : self.getResidualStrength(), 
		"ApplySSRShearStrengthReduction" : self.getApplySSRShearStrengthReduction(), 
		}
