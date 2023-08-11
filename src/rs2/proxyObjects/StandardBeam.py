from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class StandardBeam(PropertyProxy):
	def getUnitWeight(self) -> float:
		return self._getDoubleProperty("LNP_UNIT_WEIGHT")
	def setUnitWeight(self, value: float):
		return self._setDoubleProperty("LNP_UNIT_WEIGHT", value)
	def getIncludeWeightInAnalysis(self) -> bool:
		return self._getBoolProperty("LNP_USE_WEIGHT")
	def setIncludeWeightInAnalysis(self, value: bool):
		return self._setBoolProperty("LNP_USE_WEIGHT", value)
	def getYoungsModulus(self) -> float:
		return self._getDoubleProperty("LNP_YOUNGS_MODULUS")
	def setYoungsModulus(self, value: float):
		return self._setDoubleProperty("LNP_YOUNGS_MODULUS", value)
	def getMethod(self) -> GeometryChoice:
		return GeometryChoice(self._getEnumEGeometryChoiceProperty("LNP_GEOMETRY_CHOICE"))
	def setMethod(self, value: GeometryChoice):
		return self._setEnumEGeometryChoiceProperty("LNP_GEOMETRY_CHOICE", value)
	def getThickness(self) -> float:
		return self._getDoubleProperty("LNP_THICKNESS")
	def setThickness(self, value: float):
		return self._setDoubleProperty("LNP_THICKNESS", value)
	def getPoissonsRatio(self) -> float:
		return self._getDoubleProperty("LNP_POISSONS_RATIO")
	def setPoissonsRatio(self, value: float):
		return self._setDoubleProperty("LNP_POISSONS_RATIO", value)
	def getArea(self) -> float:
		return self._getDoubleProperty("LNP_AREA")
	def setArea(self, value: float):
		return self._setDoubleProperty("LNP_AREA", value)
	def getMomentOfInertia(self) -> float:
		return self._getDoubleProperty("LNP_MOMENT_OF_INERTIA")
	def setMomentOfInertia(self, value: float):
		return self._setDoubleProperty("LNP_MOMENT_OF_INERTIA", value)
	def getMaterialType(self) -> MaterialType:
		return MaterialType(self._getEnumEMaterialAnalysisTypesProperty("LNP_MATERIAL_TYPE"))
	def setMaterialType(self, value: MaterialType):
		return self._setEnumEMaterialAnalysisTypesProperty("LNP_MATERIAL_TYPE", value)
	def getCompressiveStrengthPeak(self) -> float:
		return self._getDoubleProperty("LNP_COMPRESSIVE_STRENGTH")
	def setCompressiveStrengthPeak(self, value: float):
		return self._setDoubleProperty("LNP_COMPRESSIVE_STRENGTH", value)
	def getCompressiveStrengthResidual(self) -> float:
		return self._getDoubleProperty("LNP_COMPRESSIVE_STRENGTH_RES")
	def setCompressiveStrengthResidual(self, value: float):
		return self._setDoubleProperty("LNP_COMPRESSIVE_STRENGTH_RES", value)
	def getTensileStrengthPeak(self) -> float:
		return self._getDoubleProperty("LNP_TENSILE_STRENGTH")
	def setTensileStrengthPeak(self, value: float):
		return self._setDoubleProperty("LNP_TENSILE_STRENGTH", value)
	def getTensileStrengthResidual(self) -> float:
		return self._getDoubleProperty("LNP_TENSILE_STRENGTH_RES")
	def setTensileStrengthResidual(self, value: float):
		return self._setDoubleProperty("LNP_TENSILE_STRENGTH_RES", value)
	def getSlidingGap(self) -> bool:
		return self._getBoolProperty("LNP_USE_SLIDING_GAP")
	def setSlidingGap(self, value: bool):
		return self._setBoolProperty("LNP_USE_SLIDING_GAP", value)
	def getStrainAtLocking(self) -> float:
		return self._getDoubleProperty("LNP_STRAIN_AT_LOCKING")
	def setStrainAtLocking(self, value: float):
		return self._setDoubleProperty("LNP_STRAIN_AT_LOCKING", value)
	def getBeamElementFormulation(self) -> LinerFormulation:
		return LinerFormulation(self._getEnumELinerFormulationProperty("LNP_BEAM_ELEMENT_FORMULATION"))
	def setBeamElementFormulation(self, value: LinerFormulation):
		return self._setEnumELinerFormulationProperty("LNP_BEAM_ELEMENT_FORMULATION", value)
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
	def getStageLinerProperties(self) -> bool:
		return self._getBoolProperty("LNP_USE_STAGE_LINER")
	def setStageLinerProperties(self, value: bool):
		return self._setBoolProperty("LNP_USE_STAGE_LINER", value)
	def getStaticTemperatureGridToUse(self) -> str:
		"""
		Grids "None" and "Default Grid" available by default.
		"""
		return self._callFunction("getStaticTemperatureGridToUse", [])
	def setStaticTemperatureGridToUse(self, gridName: str):
		return self._callFunction("setStaticTemperatureGridToUse", [gridName ])
