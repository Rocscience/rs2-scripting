from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class Shansep(PropertyProxy):
	def getMaterialType(self) -> MaterialType:
		return MaterialType(self._getEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE"))
	def setMaterialType(self, value: MaterialType):
		return self._setEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE", value)
	def getUseMaterialDependentStress(self) -> bool:
		return self._getBoolProperty("MP_USE_MATERIAL_DEPENDENT_STRESS")
	def setUseMaterialDependentStress(self, value: bool):
		return self._setBoolProperty("MP_USE_MATERIAL_DEPENDENT_STRESS", value)
	def getUseMaximumShearStrength(self) -> bool:
		return self._getBoolProperty("MP_USE_MAX_SHEAR_STRENGTH")
	def setUseMaximumShearStrength(self, value: bool):
		return self._setBoolProperty("MP_USE_MAX_SHEAR_STRENGTH", value)
	def getUseTensileStrength(self) -> bool:
		return self._getBoolProperty("MP_USE_TENSILE_STRENGTH")
	def setUseTensileStrength(self, value: bool):
		return self._setBoolProperty("MP_USE_TENSILE_STRENGTH", value)
	def getAParameter(self) -> float:
		return self._getDoubleProperty("MP_SHANSEP_A")
	def setAParameter(self, value: float):
		return self._setDoubleProperty("MP_SHANSEP_A", value)
	def getSParameter(self) -> float:
		return self._getDoubleProperty("MP_SHANSEP_S")
	def setSParameter(self, value: float):
		return self._setDoubleProperty("MP_SHANSEP_S", value)
	def getMParameter(self) -> float:
		return self._getDoubleProperty("MP_SHANSEP_M")
	def setMParameter(self, value: float):
		return self._setDoubleProperty("MP_SHANSEP_M", value)
	def getMaximumShearStrength(self) -> float:
		return self._getDoubleProperty("MP_MAX_SHEAR_STRENGTH")
	def setMaximumShearStrength(self, value: float):
		return self._setDoubleProperty("MP_MAX_SHEAR_STRENGTH", value)
	def getPeakTensileStrength(self) -> float:
		return self._getDoubleProperty("MP_PEAK_TENSILE_STRENGTH")
	def setPeakTensileStrength(self, value: float):
		return self._setDoubleProperty("MP_PEAK_TENSILE_STRENGTH", value)
	def getResidualAParameter(self) -> float:
		return self._getDoubleProperty("MP_SHANSEP_A_RES")
	def setResidualAParameter(self, value: float):
		return self._setDoubleProperty("MP_SHANSEP_A_RES", value)
	def getResidualSParameter(self) -> float:
		return self._getDoubleProperty("MP_SHANSEP_S_RES")
	def setResidualSParameter(self, value: float):
		return self._setDoubleProperty("MP_SHANSEP_S_RES", value)
	def getResidualMParameter(self) -> float:
		return self._getDoubleProperty("MP_SHANSEP_M_RES")
	def setResidualMParameter(self, value: float):
		return self._setDoubleProperty("MP_SHANSEP_M_RES", value)
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
	def getStressHistoryType(self) -> StressHistoryTypes:
		return StressHistoryTypes(self._getEnumEStressHistoryTypesProperty("MP_STRESS_HISTORY_TYPE"))
	def setStressHistoryType(self, value: StressHistoryTypes):
		return self._setEnumEStressHistoryTypesProperty("MP_STRESS_HISTORY_TYPE", value)
	def getOCRDefinitionMethod(self) -> StressHistoryDefinitionMethods:
		return StressHistoryDefinitionMethods(self._getEnumEStressHistoryDefinitionMethodsProperty("MP_OCR_DEFINITION"))
	def setOCRDefinitionMethod(self, value: StressHistoryDefinitionMethods):
		return self._setEnumEStressHistoryDefinitionMethodsProperty("MP_OCR_DEFINITION", value)
	def getOCR(self) -> float:
		return self._getDoubleProperty("MP_OCR_CONSTANT")
	def setOCR(self, value: float):
		return self._setDoubleProperty("MP_OCR_CONSTANT", value)
	def getPcDefinitionMethod(self) -> StressHistoryDefinitionMethods:
		return StressHistoryDefinitionMethods(self._getEnumEStressHistoryDefinitionMethodsProperty("MP_PC_DEFINITION"))
	def setPcDefinitionMethod(self, value: StressHistoryDefinitionMethods):
		return self._setEnumEStressHistoryDefinitionMethodsProperty("MP_PC_DEFINITION", value)
	def getPc(self) -> float:
		return self._getDoubleProperty("MP_PC_CONSTANT")
	def setPc(self, value: float):
		return self._setDoubleProperty("MP_PC_CONSTANT", value)
	def setShansepMaterialDependentVerticalStress(self, materialDependentVerticalStress: list[tuple[str,float]]):
		"""
		materialDependentVerticalStress is a list of (materialName,verticalStressFactor) pairs.
		 A factor of 1 means that the entire weight is used in the vertical stress computation.  A factor of 0 means no weight is used.  If a material is not provided, it automatically has a factor of 1.
		"""
		return self._callFunction("setShansepMaterialDependentVerticalStress", [materialDependentVerticalStress])
	def getShansepMaterialDependentVerticalStress(self) -> list[tuple[str,float]]:
		"""
		returns a list of (materialName,verticalStressFactor) pairs.
		 A factor of 1 means that the entire weight is used in the vertical stress computation.  A factor of 0 means no weight is used.  If a material is not listed below it automatically has a factor of 1.
		"""
		return self._callFunction("getShansepMaterialDependentVerticalStress", [])
	def setShansepStressHistory(self, stressHistory: list[tuple[float,float]]):
		"""
		Depending on the stressHistory type and definition method, stressHistory is specified as (Depth or Elevation, OCR or Pc).
		"""
		return self._callFunction("setShansepStressHistory", [stressHistory])
	def getShansepStressHistory(self) -> list[tuple[float,float]]:
		"""
		Returns the Stress History. Depending on the stressHistory type and definition method, stressHistory is specified as a list of tuples (Depth or Elevation, OCR or Pc).
		"""
		return self._callFunction("__getattribute__", ["arStressHistoryType"])
	def setProperties(self, MaterialType : MaterialType = None, UseMaterialDependentStress : bool = None, UseMaximumShearStrength : bool = None, UseTensileStrength : bool = None, AParameter : float = None, SParameter : float = None, MParameter : float = None, MaximumShearStrength : float = None, PeakTensileStrength : float = None, ResidualAParameter : float = None, ResidualSParameter : float = None, ResidualMParameter : float = None, ResidualMaximumShearStrength : float = None, ResidualTensileStrength : float = None, ApplySSRShearStrengthReduction : bool = None, StressHistoryType : StressHistoryTypes = None, OCRDefinitionMethod : StressHistoryDefinitionMethods = None, OCR : float = None, PcDefinitionMethod : StressHistoryDefinitionMethods = None, Pc : float = None):
		if MaterialType is not None:
			self._setEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE", MaterialType)
		if UseMaterialDependentStress is not None:
			self._setBoolProperty("MP_USE_MATERIAL_DEPENDENT_STRESS", UseMaterialDependentStress)
		if UseMaximumShearStrength is not None:
			self._setBoolProperty("MP_USE_MAX_SHEAR_STRENGTH", UseMaximumShearStrength)
		if UseTensileStrength is not None:
			self._setBoolProperty("MP_USE_TENSILE_STRENGTH", UseTensileStrength)
		if AParameter is not None:
			self._setDoubleProperty("MP_SHANSEP_A", AParameter)
		if SParameter is not None:
			self._setDoubleProperty("MP_SHANSEP_S", SParameter)
		if MParameter is not None:
			self._setDoubleProperty("MP_SHANSEP_M", MParameter)
		if MaximumShearStrength is not None:
			self._setDoubleProperty("MP_MAX_SHEAR_STRENGTH", MaximumShearStrength)
		if PeakTensileStrength is not None:
			self._setDoubleProperty("MP_PEAK_TENSILE_STRENGTH", PeakTensileStrength)
		if ResidualAParameter is not None:
			self._setDoubleProperty("MP_SHANSEP_A_RES", ResidualAParameter)
		if ResidualSParameter is not None:
			self._setDoubleProperty("MP_SHANSEP_S_RES", ResidualSParameter)
		if ResidualMParameter is not None:
			self._setDoubleProperty("MP_SHANSEP_M_RES", ResidualMParameter)
		if ResidualMaximumShearStrength is not None:
			self._setDoubleProperty("MP_MAX_SHEAR_STRENGTH_RES", ResidualMaximumShearStrength)
		if ResidualTensileStrength is not None:
			self._setDoubleProperty("MP_TENSILE_STRENGTH_RES", ResidualTensileStrength)
		if ApplySSRShearStrengthReduction is not None:
			self._setBoolProperty("MP_APPLY_SSR", ApplySSRShearStrengthReduction)
		if StressHistoryType is not None:
			self._setEnumEStressHistoryTypesProperty("MP_STRESS_HISTORY_TYPE", StressHistoryType)
		if OCRDefinitionMethod is not None:
			self._setEnumEStressHistoryDefinitionMethodsProperty("MP_OCR_DEFINITION", OCRDefinitionMethod)
		if OCR is not None:
			self._setDoubleProperty("MP_OCR_CONSTANT", OCR)
		if PcDefinitionMethod is not None:
			self._setEnumEStressHistoryDefinitionMethodsProperty("MP_PC_DEFINITION", PcDefinitionMethod)
		if Pc is not None:
			self._setDoubleProperty("MP_PC_CONSTANT", Pc)
	def getProperties(self):
		return {
		"MaterialType" : self.getMaterialType(), 
		"UseMaterialDependentStress" : self.getUseMaterialDependentStress(), 
		"UseMaximumShearStrength" : self.getUseMaximumShearStrength(), 
		"UseTensileStrength" : self.getUseTensileStrength(), 
		"AParameter" : self.getAParameter(), 
		"SParameter" : self.getSParameter(), 
		"MParameter" : self.getMParameter(), 
		"MaximumShearStrength" : self.getMaximumShearStrength(), 
		"PeakTensileStrength" : self.getPeakTensileStrength(), 
		"ResidualAParameter" : self.getResidualAParameter(), 
		"ResidualSParameter" : self.getResidualSParameter(), 
		"ResidualMParameter" : self.getResidualMParameter(), 
		"ResidualMaximumShearStrength" : self.getResidualMaximumShearStrength(), 
		"ResidualTensileStrength" : self.getResidualTensileStrength(), 
		"ApplySSRShearStrengthReduction" : self.getApplySSRShearStrengthReduction(), 
		"StressHistoryType" : self.getStressHistoryType(), 
		"OCRDefinitionMethod" : self.getOCRDefinitionMethod(), 
		"OCR" : self.getOCR(), 
		"PcDefinitionMethod" : self.getPcDefinitionMethod(), 
		"Pc" : self.getPc(), 
		}
