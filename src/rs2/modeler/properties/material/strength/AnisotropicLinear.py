from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class AnisotropicLinear(PropertyProxy):
	def getMaterialType(self) -> MaterialType:
		return MaterialType(self._getEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE"))
	def setMaterialType(self, value: MaterialType):
		return self._setEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE", value)
	def getA1Parameter(self) -> float:
		return self._getDoubleProperty("MP_A1")
	def setA1Parameter(self, value: float):
		return self._setDoubleProperty("MP_A1", value)
	def getB1Parameter(self) -> float:
		return self._getDoubleProperty("MP_B1")
	def setB1Parameter(self, value: float):
		return self._setDoubleProperty("MP_B1", value)
	def getUseTensileStrength(self) -> bool:
		return self._getBoolProperty("MP_USE_TENSILE_STRENGTH")
	def setUseTensileStrength(self, value: bool):
		return self._setBoolProperty("MP_USE_TENSILE_STRENGTH", value)
	def getCohesion1(self) -> float:
		return self._getDoubleProperty("MP_COHESION_1")
	def setCohesion1(self, value: float):
		return self._setDoubleProperty("MP_COHESION_1", value)
	def getCohesion2(self) -> float:
		return self._getDoubleProperty("MP_COHESION_2")
	def setCohesion2(self, value: float):
		return self._setDoubleProperty("MP_COHESION_2", value)
	def getFrictionAngle1(self) -> float:
		return self._getDoubleProperty("MP_PHI_1")
	def setFrictionAngle1(self, value: float):
		return self._setDoubleProperty("MP_PHI_1", value)
	def getFrictionAngle2(self) -> float:
		return self._getDoubleProperty("MP_PHI_2")
	def setFrictionAngle2(self, value: float):
		return self._setDoubleProperty("MP_PHI_2", value)
	def getPeakTensileStrength(self) -> float:
		return self._getDoubleProperty("MP_PEAK_TENSILE_STRENGTH")
	def setPeakTensileStrength(self, value: float):
		return self._setDoubleProperty("MP_PEAK_TENSILE_STRENGTH", value)
	def getResidualCohesion1(self) -> float:
		return self._getDoubleProperty("MP_COHESION_1_RES")
	def setResidualCohesion1(self, value: float):
		return self._setDoubleProperty("MP_COHESION_1_RES", value)
	def getResidualCohesion2(self) -> float:
		return self._getDoubleProperty("MP_COHESION_2_RES")
	def setResidualCohesion2(self, value: float):
		return self._setDoubleProperty("MP_COHESION_2_RES", value)
	def getResidualFrictionAngle1(self) -> float:
		return self._getDoubleProperty("MP_PHI_1_RES")
	def setResidualFrictionAngle1(self, value: float):
		return self._setDoubleProperty("MP_PHI_1_RES", value)
	def getResidualFrictionAngle2(self) -> float:
		return self._getDoubleProperty("MP_PHI_2_RES")
	def setResidualFrictionAngle2(self, value: float):
		return self._setDoubleProperty("MP_PHI_2_RES", value)
	def getDilationAngle1(self) -> float:
		return self._getDoubleProperty("MP_DILATION_ANGLE_1")
	def setDilationAngle1(self, value: float):
		return self._setDoubleProperty("MP_DILATION_ANGLE_1", value)
	def getDilationAngle2(self) -> float:
		return self._getDoubleProperty("MP_DILATION_ANGLE_2")
	def setDilationAngle2(self, value: float):
		return self._setDoubleProperty("MP_DILATION_ANGLE_2", value)
	def getResidualTensileStrength(self) -> float:
		return self._getDoubleProperty("MP_TENSILE_STRENGTH_RES")
	def setResidualTensileStrength(self, value: float):
		return self._setDoubleProperty("MP_TENSILE_STRENGTH_RES", value)
	def getApplySSRShearStrengthReduction(self) -> bool:
		return self._getBoolProperty("MP_APPLY_SSR")
	def setApplySSRShearStrengthReduction(self, value: bool):
		return self._setBoolProperty("MP_APPLY_SSR", value)
	def getAnisotropyDefinition(self) -> AnisotropyDefinitions:
		return AnisotropyDefinitions(self._getEnumEAnisotropyDefinitionsProperty("MP_ANISOTROPY_DEFINITION"))
	def setAnisotropyDefinition(self, value: AnisotropyDefinitions):
		return self._setEnumEAnisotropyDefinitionsProperty("MP_ANISOTROPY_DEFINITION", value)
	def getAngleCcwTo1(self) -> float:
		return self._getDoubleProperty("MP_ANISOTROPY_ANGLE")
	def setAngleCcwTo1(self, value: float):
		return self._setDoubleProperty("MP_ANISOTROPY_ANGLE", value)
	def setAnisotropicSurfaceByName(self, surfaceName: str):
		"""
		Sets the anisotropic surface by name. The surface must be defined in the model.
		"""
		return self._callFunction("setAnisotropicSurfaceByName", [surfaceName])
	def getAnisotropicSurfaceName(self) -> str:
		return self._callFunction("getAnisotropicSurfaceName", [])
	def setProperties(self, MaterialType : MaterialType = None, A1Parameter : float = None, B1Parameter : float = None, UseTensileStrength : bool = None, Cohesion1 : float = None, Cohesion2 : float = None, FrictionAngle1 : float = None, FrictionAngle2 : float = None, PeakTensileStrength : float = None, ResidualCohesion1 : float = None, ResidualCohesion2 : float = None, ResidualFrictionAngle1 : float = None, ResidualFrictionAngle2 : float = None, DilationAngle1 : float = None, DilationAngle2 : float = None, ResidualTensileStrength : float = None, ApplySSRShearStrengthReduction : bool = None, AnisotropyDefinition : AnisotropyDefinitions = None, AngleCcwTo1 : float = None):
		if MaterialType is not None:
			self._setEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE", MaterialType)
		if A1Parameter is not None:
			self._setDoubleProperty("MP_A1", A1Parameter)
		if B1Parameter is not None:
			self._setDoubleProperty("MP_B1", B1Parameter)
		if UseTensileStrength is not None:
			self._setBoolProperty("MP_USE_TENSILE_STRENGTH", UseTensileStrength)
		if Cohesion1 is not None:
			self._setDoubleProperty("MP_COHESION_1", Cohesion1)
		if Cohesion2 is not None:
			self._setDoubleProperty("MP_COHESION_2", Cohesion2)
		if FrictionAngle1 is not None:
			self._setDoubleProperty("MP_PHI_1", FrictionAngle1)
		if FrictionAngle2 is not None:
			self._setDoubleProperty("MP_PHI_2", FrictionAngle2)
		if PeakTensileStrength is not None:
			self._setDoubleProperty("MP_PEAK_TENSILE_STRENGTH", PeakTensileStrength)
		if ResidualCohesion1 is not None:
			self._setDoubleProperty("MP_COHESION_1_RES", ResidualCohesion1)
		if ResidualCohesion2 is not None:
			self._setDoubleProperty("MP_COHESION_2_RES", ResidualCohesion2)
		if ResidualFrictionAngle1 is not None:
			self._setDoubleProperty("MP_PHI_1_RES", ResidualFrictionAngle1)
		if ResidualFrictionAngle2 is not None:
			self._setDoubleProperty("MP_PHI_2_RES", ResidualFrictionAngle2)
		if DilationAngle1 is not None:
			self._setDoubleProperty("MP_DILATION_ANGLE_1", DilationAngle1)
		if DilationAngle2 is not None:
			self._setDoubleProperty("MP_DILATION_ANGLE_2", DilationAngle2)
		if ResidualTensileStrength is not None:
			self._setDoubleProperty("MP_TENSILE_STRENGTH_RES", ResidualTensileStrength)
		if ApplySSRShearStrengthReduction is not None:
			self._setBoolProperty("MP_APPLY_SSR", ApplySSRShearStrengthReduction)
		if AnisotropyDefinition is not None:
			self._setEnumEAnisotropyDefinitionsProperty("MP_ANISOTROPY_DEFINITION", AnisotropyDefinition)
		if AngleCcwTo1 is not None:
			self._setDoubleProperty("MP_ANISOTROPY_ANGLE", AngleCcwTo1)
	def getProperties(self):
		return {
		"MaterialType" : self.getMaterialType(), 
		"A1Parameter" : self.getA1Parameter(), 
		"B1Parameter" : self.getB1Parameter(), 
		"UseTensileStrength" : self.getUseTensileStrength(), 
		"Cohesion1" : self.getCohesion1(), 
		"Cohesion2" : self.getCohesion2(), 
		"FrictionAngle1" : self.getFrictionAngle1(), 
		"FrictionAngle2" : self.getFrictionAngle2(), 
		"PeakTensileStrength" : self.getPeakTensileStrength(), 
		"ResidualCohesion1" : self.getResidualCohesion1(), 
		"ResidualCohesion2" : self.getResidualCohesion2(), 
		"ResidualFrictionAngle1" : self.getResidualFrictionAngle1(), 
		"ResidualFrictionAngle2" : self.getResidualFrictionAngle2(), 
		"DilationAngle1" : self.getDilationAngle1(), 
		"DilationAngle2" : self.getDilationAngle2(), 
		"ResidualTensileStrength" : self.getResidualTensileStrength(), 
		"ApplySSRShearStrengthReduction" : self.getApplySSRShearStrengthReduction(), 
		"AnisotropyDefinition" : self.getAnisotropyDefinition(), 
		"AngleCcwTo1" : self.getAngleCcwTo1(), 
		}
