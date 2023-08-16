from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class ReinforcedConcrete(PropertyProxy):
	def getReinforcement(self) -> bool:
		return self._getBoolProperty("LNP_USE_REINFORCEMENT")
	def setReinforcement(self, value: bool):
		return self._setBoolProperty("LNP_USE_REINFORCEMENT", value)
	def getIncludeWeightInAnalysis(self) -> bool:
		return self._getBoolProperty("LNP_USE_WEIGHT")
	def setIncludeWeightInAnalysis(self, value: bool):
		return self._setBoolProperty("LNP_USE_WEIGHT", value)
	def getConcreteUnitWeight(self) -> float:
		return self._getDoubleProperty("LNP_UNIT_WEIGTH_CONCRETE")
	def setConcreteUnitWeight(self, value: float):
		return self._setDoubleProperty("LNP_UNIT_WEIGTH_CONCRETE", value)
	def getSpacing(self) -> float:
		return self._getDoubleProperty("LNP_SPACING")
	def setSpacing(self, value: float):
		return self._setDoubleProperty("LNP_SPACING", value)
	def getSectionDepth(self) -> float:
		return self._getDoubleProperty("LNP_SECTION_DEPTH")
	def setSectionDepth(self, value: float):
		return self._setDoubleProperty("LNP_SECTION_DEPTH", value)
	def getYoungsModulus(self) -> float:
		return self._getDoubleProperty("LNP_YOUNGS_MODULUS_REIN")
	def setYoungsModulus(self, value: float):
		return self._setDoubleProperty("LNP_YOUNGS_MODULUS_REIN", value)
	def getArea(self) -> float:
		return self._getDoubleProperty("LNP_AREA")
	def setArea(self, value: float):
		return self._setDoubleProperty("LNP_AREA", value)
	def getMomentOfInertia(self) -> float:
		return self._getDoubleProperty("LNP_MOMENT_OF_INERTIA")
	def setMomentOfInertia(self, value: float):
		return self._setDoubleProperty("LNP_MOMENT_OF_INERTIA", value)
	def getCompressiveStrength(self) -> float:
		return self._getDoubleProperty("LNP_COMPRESSIVE_STRENGTH_REIN")
	def setCompressiveStrength(self, value: float):
		return self._setDoubleProperty("LNP_COMPRESSIVE_STRENGTH_REIN", value)
	def getTensileStrength(self) -> float:
		return self._getDoubleProperty("LNP_TENSILE_STRENGTH_REIN")
	def setTensileStrength(self, value: float):
		return self._setDoubleProperty("LNP_TENSILE_STRENGTH_REIN", value)
	def getWeight(self) -> float:
		return self._getDoubleProperty("LNP_WEIGHT_REIN")
	def setWeight(self, value: float):
		return self._setDoubleProperty("LNP_WEIGHT_REIN", value)
	def getConcrete(self) -> bool:
		return self._getBoolProperty("LNP_USE_CONCRETE")
	def setConcrete(self, value: bool):
		return self._setBoolProperty("LNP_USE_CONCRETE", value)
	def getThickness(self) -> float:
		return self._getDoubleProperty("LNP_THICKNESS_CONCRETE")
	def setThickness(self, value: float):
		return self._setDoubleProperty("LNP_THICKNESS_CONCRETE", value)
	def getYoungsModulus(self) -> float:
		return self._getDoubleProperty("LNP_YOUNGS_MODULUS_CONCRETE")
	def setYoungsModulus(self, value: float):
		return self._setDoubleProperty("LNP_YOUNGS_MODULUS_CONCRETE", value)
	def getPoissonRatio(self) -> float:
		return self._getDoubleProperty("LNP_POISSONS_RATIO_CONCRETE")
	def setPoissonRatio(self, value: float):
		return self._setDoubleProperty("LNP_POISSONS_RATIO_CONCRETE", value)
	def getCompressiveStrength(self) -> float:
		return self._getDoubleProperty("LNP_COMPRESSIVE_STRENGTH_CONCRETE")
	def setCompressiveStrength(self, value: float):
		return self._setDoubleProperty("LNP_COMPRESSIVE_STRENGTH_CONCRETE", value)
	def getTensileStrength(self) -> float:
		return self._getDoubleProperty("LNP_TENSILE_STRENGTH_CONCRETE")
	def setTensileStrength(self, value: float):
		return self._setDoubleProperty("LNP_TENSILE_STRENGTH_CONCRETE", value)
	def getMaterialType(self) -> MaterialType:
		return MaterialType(self._getEnumEMaterialAnalysisTypesProperty("LNP_MATERIAL_TYPE"))
	def setMaterialType(self, value: MaterialType):
		return self._setEnumEMaterialAnalysisTypesProperty("LNP_MATERIAL_TYPE", value)
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
	def getStageConcreteProperties(self) -> bool:
		return self._getBoolProperty("LNP_USE_STAGE_CONCRETE")
	def setStageConcreteProperties(self, value: bool):
		return self._setBoolProperty("LNP_USE_STAGE_CONCRETE", value)
	def getStaticTemperatureGridToUse(self) -> str:
		"""
		Grids "None" and "Default Grid" available by default.
		"""
		return self._callFunction("getStaticTemperatureGridToUse", [])
	def setStaticTemperatureGridToUse(self, gridName: str):
		return self._callFunction("setStaticTemperatureGridToUse", [gridName ])
