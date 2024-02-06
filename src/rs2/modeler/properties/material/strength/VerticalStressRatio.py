from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class VerticalStressRatio(PropertyProxy):
	def getMaterialType(self) -> MaterialType:
		return MaterialType(self._getEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE"))
	def setMaterialType(self, value: MaterialType):
		return self._setEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE", value)
	def getUseMaximumShearStrength(self) -> bool:
		return self._getBoolProperty("MP_USE_MAX_SHEAR_STRENGTH")
	def setUseMaximumShearStrength(self, value: bool):
		return self._setBoolProperty("MP_USE_MAX_SHEAR_STRENGTH", value)
	def getUseTensileStrength(self) -> bool:
		return self._getBoolProperty("MP_USE_TENSILE_STRENGTH")
	def setUseTensileStrength(self, value: bool):
		return self._setBoolProperty("MP_USE_TENSILE_STRENGTH", value)
	def getVerticalStressRatio(self) -> float:
		return self._getDoubleProperty("MP_VERTICAL_STRESS_RATIO")
	def setVerticalStressRatio(self, value: float):
		return self._setDoubleProperty("MP_VERTICAL_STRESS_RATIO", value)
	def getMinimumShearStrength(self) -> float:
		return self._getDoubleProperty("MP_MIN_SHEAR_STRENGTH")
	def setMinimumShearStrength(self, value: float):
		return self._setDoubleProperty("MP_MIN_SHEAR_STRENGTH", value)
	def getMaximumShearStrength(self) -> float:
		return self._getDoubleProperty("MP_MAX_SHEAR_STRENGTH")
	def setMaximumShearStrength(self, value: float):
		return self._setDoubleProperty("MP_MAX_SHEAR_STRENGTH", value)
	def getPeakTensileStrength(self) -> float:
		return self._getDoubleProperty("MP_PEAK_TENSILE_STRENGTH")
	def setPeakTensileStrength(self, value: float):
		return self._setDoubleProperty("MP_PEAK_TENSILE_STRENGTH", value)
	def getResidualVerticalStressRatio(self) -> float:
		return self._getDoubleProperty("MP_VERTICAL_STRESS_RATIO_RES")
	def setResidualVerticalStressRatio(self, value: float):
		return self._setDoubleProperty("MP_VERTICAL_STRESS_RATIO_RES", value)
	def getResidualMinimumShearStrength(self) -> float:
		return self._getDoubleProperty("MP_MIN_SHEAR_STRENGTH_RES")
	def setResidualMinimumShearStrength(self, value: float):
		return self._setDoubleProperty("MP_MIN_SHEAR_STRENGTH_RES", value)
	def getResidualMaximumShearStrength(self) -> float:
		return self._getDoubleProperty("MP_MAX_SHEAR_STRENGTH_RES")
	def setResidualMaximumShearStrength(self, value: float):
		return self._setDoubleProperty("MP_MAX_SHEAR_STRENGTH_RES", value)
	def getResidualTensileStrength(self) -> float:
		return self._getDoubleProperty("MP_TENSILE_STRENGTH_RES")
	def setResidualTensileStrength(self, value: float):
		return self._setDoubleProperty("MP_TENSILE_STRENGTH_RES", value)
	def getApplySSRShearStrengthReduction(self) -> bool:
		return self._getBoolProperty("MP_APPLY_SSR")
	def setApplySSRShearStrengthReduction(self, value: bool):
		return self._setBoolProperty("MP_APPLY_SSR", value)
	def setProperties(self, MaterialType : MaterialType = None, UseMaximumShearStrength : bool = None, UseTensileStrength : bool = None, VerticalStressRatio : float = None, MinimumShearStrength : float = None, MaximumShearStrength : float = None, PeakTensileStrength : float = None, ResidualVerticalStressRatio : float = None, ResidualMinimumShearStrength : float = None, ResidualMaximumShearStrength : float = None, ResidualTensileStrength : float = None, ApplySSRShearStrengthReduction : bool = None):
		if MaterialType is not None:
			self._setEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE", MaterialType)
		if UseMaximumShearStrength is not None:
			self._setBoolProperty("MP_USE_MAX_SHEAR_STRENGTH", UseMaximumShearStrength)
		if UseTensileStrength is not None:
			self._setBoolProperty("MP_USE_TENSILE_STRENGTH", UseTensileStrength)
		if VerticalStressRatio is not None:
			self._setDoubleProperty("MP_VERTICAL_STRESS_RATIO", VerticalStressRatio)
		if MinimumShearStrength is not None:
			self._setDoubleProperty("MP_MIN_SHEAR_STRENGTH", MinimumShearStrength)
		if MaximumShearStrength is not None:
			self._setDoubleProperty("MP_MAX_SHEAR_STRENGTH", MaximumShearStrength)
		if PeakTensileStrength is not None:
			self._setDoubleProperty("MP_PEAK_TENSILE_STRENGTH", PeakTensileStrength)
		if ResidualVerticalStressRatio is not None:
			self._setDoubleProperty("MP_VERTICAL_STRESS_RATIO_RES", ResidualVerticalStressRatio)
		if ResidualMinimumShearStrength is not None:
			self._setDoubleProperty("MP_MIN_SHEAR_STRENGTH_RES", ResidualMinimumShearStrength)
		if ResidualMaximumShearStrength is not None:
			self._setDoubleProperty("MP_MAX_SHEAR_STRENGTH_RES", ResidualMaximumShearStrength)
		if ResidualTensileStrength is not None:
			self._setDoubleProperty("MP_TENSILE_STRENGTH_RES", ResidualTensileStrength)
		if ApplySSRShearStrengthReduction is not None:
			self._setBoolProperty("MP_APPLY_SSR", ApplySSRShearStrengthReduction)
	def getProperties(self):
		return {
		"MaterialType" : self.getMaterialType(), 
		"UseMaximumShearStrength" : self.getUseMaximumShearStrength(), 
		"UseTensileStrength" : self.getUseTensileStrength(), 
		"VerticalStressRatio" : self.getVerticalStressRatio(), 
		"MinimumShearStrength" : self.getMinimumShearStrength(), 
		"MaximumShearStrength" : self.getMaximumShearStrength(), 
		"PeakTensileStrength" : self.getPeakTensileStrength(), 
		"ResidualVerticalStressRatio" : self.getResidualVerticalStressRatio(), 
		"ResidualMinimumShearStrength" : self.getResidualMinimumShearStrength(), 
		"ResidualMaximumShearStrength" : self.getResidualMaximumShearStrength(), 
		"ResidualTensileStrength" : self.getResidualTensileStrength(), 
		"ApplySSRShearStrengthReduction" : self.getApplySSRShearStrengthReduction(), 
		}
