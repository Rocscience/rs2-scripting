from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.properties.SnowdenAnisotropicFunction import SnowdenAnisotropicFunction
class SnowdenModAnisotropicLinear(PropertyProxy):
	def getMaterialType(self) -> MaterialType:
		return MaterialType(self._getEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE"))
	def setMaterialType(self, value: MaterialType):
		return self._setEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE", value)
	def getA1Parameter(self) -> float:
		return self._getDoubleProperty("MP_A1")
	def setA1Parameter(self, value: float):
		return self._setDoubleProperty("MP_A1", value)
	def getA2Parameter(self) -> float:
		return self._getDoubleProperty("MP_A2")
	def setA2Parameter(self, value: float):
		return self._setDoubleProperty("MP_A2", value)
	def getB1Parameter(self) -> float:
		return self._getDoubleProperty("MP_B1")
	def setB1Parameter(self, value: float):
		return self._setDoubleProperty("MP_B1", value)
	def getB2Parameter(self) -> float:
		return self._getDoubleProperty("MP_B2")
	def setB2Parameter(self, value: float):
		return self._setDoubleProperty("MP_B2", value)
	def getAnisotropyDefinition(self) -> AnisotropyDefinitions:
		return AnisotropyDefinitions(self._getEnumEAnisotropyDefinitionsProperty("MP_ANISOTROPY_DEFINITION"))
	def setAnisotropyDefinition(self, value: AnisotropyDefinitions):
		return self._setEnumEAnisotropyDefinitionsProperty("MP_ANISOTROPY_DEFINITION", value)
	def getAngleCcwTo1(self) -> float:
		return self._getDoubleProperty("MP_ANISOTROPY_ANGLE")
	def setAngleCcwTo1(self, value: float):
		return self._setDoubleProperty("MP_ANISOTROPY_ANGLE", value)
	def getApplySSRShearStrengthReduction(self) -> bool:
		return self._getBoolProperty("MP_APPLY_SSR")
	def setApplySSRShearStrengthReduction(self, value: bool):
		return self._setBoolProperty("MP_APPLY_SSR", value)
	def setAnisotropicSurfaceByName(self, surfaceName: str):
		"""
		Sets the anisotropic surface by name. The surface must be defined in the model.
		"""
		return self._callFunction("setAnisotropicSurfaceByName", [surfaceName])
	def getAnisotropicSurfaceName(self) -> str:
		return self._callFunction("getAnisotropicSurfaceName", [])
	def getBeddingStrengthFunction(self) -> SnowdenAnisotropicFunction:
		return SnowdenAnisotropicFunction(self._client, self._callFunction("getBeddingStrengthFunction", keepReturnValueReference=True))
	def getRockMassStrengthFunction(self) -> SnowdenAnisotropicFunction:
		return SnowdenAnisotropicFunction(self._client, self._callFunction("getRockMassStrengthFunction", keepReturnValueReference=True))
	def setProperties(self, MaterialType : MaterialType = None, A1Parameter : float = None, A2Parameter : float = None, B1Parameter : float = None, B2Parameter : float = None, AnisotropyDefinition : AnisotropyDefinitions = None, AngleCcwTo1 : float = None, ApplySSRShearStrengthReduction : bool = None):
		if MaterialType is not None:
			self._setEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE", MaterialType)
		if A1Parameter is not None:
			self._setDoubleProperty("MP_A1", A1Parameter)
		if A2Parameter is not None:
			self._setDoubleProperty("MP_A2", A2Parameter)
		if B1Parameter is not None:
			self._setDoubleProperty("MP_B1", B1Parameter)
		if B2Parameter is not None:
			self._setDoubleProperty("MP_B2", B2Parameter)
		if AnisotropyDefinition is not None:
			self._setEnumEAnisotropyDefinitionsProperty("MP_ANISOTROPY_DEFINITION", AnisotropyDefinition)
		if AngleCcwTo1 is not None:
			self._setDoubleProperty("MP_ANISOTROPY_ANGLE", AngleCcwTo1)
		if ApplySSRShearStrengthReduction is not None:
			self._setBoolProperty("MP_APPLY_SSR", ApplySSRShearStrengthReduction)
	def getProperties(self):
		return {
		"MaterialType" : self.getMaterialType(), 
		"A1Parameter" : self.getA1Parameter(), 
		"A2Parameter" : self.getA2Parameter(), 
		"B1Parameter" : self.getB1Parameter(), 
		"B2Parameter" : self.getB2Parameter(), 
		"AnisotropyDefinition" : self.getAnisotropyDefinition(), 
		"AngleCcwTo1" : self.getAngleCcwTo1(), 
		"ApplySSRShearStrengthReduction" : self.getApplySSRShearStrengthReduction(), 
		}
