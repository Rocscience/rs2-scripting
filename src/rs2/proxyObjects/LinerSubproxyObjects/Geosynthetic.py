from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
from rs2.ProxyObject import ProxyObject
class GeosyntheticStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, property : PropertyProxy):
		super().__init__(client, ID)
		self.property = property
	def getTensileModulusFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_TENSILE_MODULUS", self.property._ID], proxyArgumentIndices=[1])
	def setTensileModulusFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_TENSILE_MODULUS", value, self.property._ID], proxyArgumentIndices=[2])
	def getAxialStrainExpansionFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_AXIAL_STRAIN", self.property._ID], proxyArgumentIndices=[1])
	def setAxialStrainExpansionFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_AXIAL_STRAIN", value, self.property._ID], proxyArgumentIndices=[2])
	def getTensileStrengthPeakFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_TENSILE_STRENGTH", self.property._ID], proxyArgumentIndices=[1])
	def setTensileStrengthPeakFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_TENSILE_STRENGTH", value, self.property._ID], proxyArgumentIndices=[2])
	def getTensileStrengthResidualFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_TENSILE_STRENGTH_RES", self.property._ID], proxyArgumentIndices=[1])
	def setTensileStrengthResidualFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_TENSILE_STRENGTH_RES", value, self.property._ID], proxyArgumentIndices=[2])
	def getStagesAfterInstallation(self) -> int:
		return self._callFunction("getIntFactor", ["LNP_RELATIVE_STAGE_FACTOR", self.property._ID], proxyArgumentIndices=[1])
	def setStagesAfterInstallation(self, relativeStage: int):
		return self._callFunction("setIntFactor", ["LNP_RELATIVE_STAGE_FACTOR", relativeStage, self.property._ID], proxyArgumentIndices = [2])
class Geosynthetic(PropertyProxy):
	def getInitialTemperature(self) -> float:
		return self._getDoubleProperty("LNP_THERAMAL_INITIAL_TEMPERATURE")
	def setInitialTemperature(self, value: float):
		return self._setDoubleProperty("LNP_THERAMAL_INITIAL_TEMPERATURE", value)
	def getTensileModulus(self) -> float:
		return self._getDoubleProperty("LNP_TENSILE_MODULUS")
	def setTensileModulus(self, value: float):
		return self._setDoubleProperty("LNP_TENSILE_MODULUS", value)
	def getMaterialType(self) -> MaterialType:
		return MaterialType(self._getEnumEMaterialAnalysisTypesProperty("LNP_MATERIAL_TYPE"))
	def setMaterialType(self, value: MaterialType):
		return self._setEnumEMaterialAnalysisTypesProperty("LNP_MATERIAL_TYPE", value)
	def getTensileStrengthPeak(self) -> float:
		return self._getDoubleProperty("LNP_TENSILE_STRENGTH")
	def setTensileStrengthPeak(self, value: float):
		return self._setDoubleProperty("LNP_TENSILE_STRENGTH", value)
	def getTensileStrengthResidual(self) -> float:
		return self._getDoubleProperty("LNP_TENSILE_STRENGTH_RES")
	def setTensileStrengthResidual(self, value: float):
		return self._setDoubleProperty("LNP_TENSILE_STRENGTH_RES", value)
	def getActivateThermal(self) -> bool:
		return self._getBoolProperty("LNP_THERAMAL_ACTIVATE")
	def setActivateThermal(self, value: bool):
		return self._setBoolProperty("LNP_THERAMAL_ACTIVATE", value)
	def getStaticTemperatureMode(self) -> StaticWaterModes:
		return StaticWaterModes(self._getEnumEStaticWaterModesProperty("LNP_STATIC_TEMPERATURE_METHOD"))
	def setStaticTemperatureMode(self, value: StaticWaterModes):
		return self._setEnumEStaticWaterModesProperty("LNP_STATIC_TEMPERATURE_METHOD", value)
	def getStaticTemperature(self) -> float:
		return self._getDoubleProperty("LNP_STATIC_TEMPERATURE_CONST")
	def setStaticTemperature(self, value: float):
		return self._setDoubleProperty("LNP_STATIC_TEMPERATURE_CONST", value)
	def getConductivity(self) -> float:
		return self._getDoubleProperty("LNP_THERAMAL_CONDUCTIVITY")
	def setConductivity(self, value: float):
		return self._setDoubleProperty("LNP_THERAMAL_CONDUCTIVITY", value)
	def getSpecificHeatCapacity(self) -> float:
		return self._getDoubleProperty("LNP_THERAMAL_SPECIFIC_HEAT_CAPACITY")
	def setSpecificHeatCapacity(self, value: float):
		return self._setDoubleProperty("LNP_THERAMAL_SPECIFIC_HEAT_CAPACITY", value)
	def getThermalExpansion(self) -> bool:
		return self._getBoolProperty("LNP_THERAMAL_EXPANSION_IS_ON")
	def setThermalExpansion(self, value: bool):
		return self._setBoolProperty("LNP_THERAMAL_EXPANSION_IS_ON", value)
	def getExpansionCoefficient(self) -> float:
		return self._getDoubleProperty("LNP_THERAMAL_EXPANSION_ALPHA")
	def setExpansionCoefficient(self, value: float):
		return self._setDoubleProperty("LNP_THERAMAL_EXPANSION_ALPHA", value)
	def getStageGeosyntheticProperties(self) -> bool:
		return self._getBoolProperty("LNP_USE_STAGE_GEOSYN")
	def setStageGeosyntheticProperties(self, value: bool):
		return self._setBoolProperty("LNP_USE_STAGE_GEOSYN", value)
	def getStaticTemperatureGridToUse(self) -> str:
		return self._callFunction("getStaticTemperatureGridToUse", [])
	def setStaticTemperatureGridToUse(self, gridName: str):
		"""
		Grids "None" and "Default Grid" available by default.
		"""
		return self._callFunction("setStaticTemperatureGridToUse", [gridName])
	def getDefineRelativeStageFactors(self) -> bool:
		return self._callFunction("getUseRelativeStageFactors", [])
	def setDefineRelativeStageFactors(self, useStagesAfterInstallation: bool):
		"""
		Choose to define relative stage factors based on the installation stage.
		If true, set the relative stage of each stage factor using setStagesAfterInstallation.
		If false, each stage factor is returned in order from 1 to n from getStageFactors().
		"""
		return self._callFunction("setUseRelativeStageFactors", [useStagesAfterInstallation])
	def getStageFactors(self) -> dict[int, GeosyntheticStageFactor]:
		"""
		Returns a map of stage factors. The key is the absolute or relative stage at which the stage factor is applied. The value is the stage factor object
		"""
		stageFactorReferenceIds = self._callFunction('getStageFactors', [], keepReturnValueReference=True)
		stageFactors = {}
		for stageKey in stageFactorReferenceIds :
			stageFactors[stageKey] = GeosyntheticStageFactor(self._client, stageFactorReferenceIds[stageKey], self)
		return stageFactors
	def setProperties(self, InitialTemperature : float = None, TensileModulus : float = None, MaterialType : MaterialType = None, TensileStrengthPeak : float = None, TensileStrengthResidual : float = None, ActivateThermal : bool = None, StaticTemperatureMode : StaticWaterModes = None, StaticTemperature : float = None, Conductivity : float = None, SpecificHeatCapacity : float = None, ThermalExpansion : bool = None, ExpansionCoefficient : float = None, StageGeosyntheticProperties : bool = None):
		if InitialTemperature is not None:
			self._setDoubleProperty("LNP_THERAMAL_INITIAL_TEMPERATURE", InitialTemperature)
		if TensileModulus is not None:
			self._setDoubleProperty("LNP_TENSILE_MODULUS", TensileModulus)
		if MaterialType is not None:
			self._setEnumEMaterialAnalysisTypesProperty("LNP_MATERIAL_TYPE", MaterialType)
		if TensileStrengthPeak is not None:
			self._setDoubleProperty("LNP_TENSILE_STRENGTH", TensileStrengthPeak)
		if TensileStrengthResidual is not None:
			self._setDoubleProperty("LNP_TENSILE_STRENGTH_RES", TensileStrengthResidual)
		if ActivateThermal is not None:
			self._setBoolProperty("LNP_THERAMAL_ACTIVATE", ActivateThermal)
		if StaticTemperatureMode is not None:
			self._setEnumEStaticWaterModesProperty("LNP_STATIC_TEMPERATURE_METHOD", StaticTemperatureMode)
		if StaticTemperature is not None:
			self._setDoubleProperty("LNP_STATIC_TEMPERATURE_CONST", StaticTemperature)
		if Conductivity is not None:
			self._setDoubleProperty("LNP_THERAMAL_CONDUCTIVITY", Conductivity)
		if SpecificHeatCapacity is not None:
			self._setDoubleProperty("LNP_THERAMAL_SPECIFIC_HEAT_CAPACITY", SpecificHeatCapacity)
		if ThermalExpansion is not None:
			self._setBoolProperty("LNP_THERAMAL_EXPANSION_IS_ON", ThermalExpansion)
		if ExpansionCoefficient is not None:
			self._setDoubleProperty("LNP_THERAMAL_EXPANSION_ALPHA", ExpansionCoefficient)
		if StageGeosyntheticProperties is not None:
			self._setBoolProperty("LNP_USE_STAGE_GEOSYN", StageGeosyntheticProperties)
	def getProperties(self):
		return {
		"InitialTemperature" : self.getInitialTemperature(), 
		"TensileModulus" : self.getTensileModulus(), 
		"MaterialType" : self.getMaterialType(), 
		"TensileStrengthPeak" : self.getTensileStrengthPeak(), 
		"TensileStrengthResidual" : self.getTensileStrengthResidual(), 
		"ActivateThermal" : self.getActivateThermal(), 
		"StaticTemperatureMode" : self.getStaticTemperatureMode(), 
		"StaticTemperature" : self.getStaticTemperature(), 
		"Conductivity" : self.getConductivity(), 
		"SpecificHeatCapacity" : self.getSpecificHeatCapacity(), 
		"ThermalExpansion" : self.getThermalExpansion(), 
		"ExpansionCoefficient" : self.getExpansionCoefficient(), 
		"StageGeosyntheticProperties" : self.getStageGeosyntheticProperties(), 
		}
