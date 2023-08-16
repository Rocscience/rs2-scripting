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
		return self._callFunction("getStaticTemperatureGridToUse", [])
	def setStaticTemperatureGridToUse(self, gridName: str):
		"""
		Grids "None" and "Default Grid" available by default.
		"""
		return self._callFunction("setStaticTemperatureGridToUse", [gridName ])
	def setProperties(self, Reinforcement : bool = None, IncludeWeightInAnalysis : bool = None, ConcreteUnitWeight : float = None, Spacing : float = None, SectionDepth : float = None, ConcreteYoungsModulus : float = None, Area : float = None, MomentOfInertia : float = None, ConcreteCompressiveStrength : float = None, ConcreteTensileStrength : float = None, Weight : float = None, Concrete : bool = None, Thickness : float = None, YoungsModulus : float = None, PoissonRatio : float = None, CompressiveStrength : float = None, TensileStrength : float = None, MaterialType : MaterialType = None, SlidingGap : bool = None, StrainAtLocking : float = None, BeamElementFormulation : LinerFormulation = None, ActivateThermal : bool = None, StaticTemperatureMode : StaticWaterModes = None, StaticTemperature : float = None, Conductivity : float = None, SpecificHeatCapacity : float = None, ThermalExpansion : bool = None, ExpansionCoefficient : float = None, StageConcreteProperties : bool = None):
		if Reinforcement is not None:
			self._setBoolProperty("LNP_USE_REINFORCEMENT", Reinforcement)
		if IncludeWeightInAnalysis is not None:
			self._setBoolProperty("LNP_USE_WEIGHT", IncludeWeightInAnalysis)
		if ConcreteUnitWeight is not None:
			self._setDoubleProperty("LNP_UNIT_WEIGTH_CONCRETE", ConcreteUnitWeight)
		if Spacing is not None:
			self._setDoubleProperty("LNP_SPACING", Spacing)
		if SectionDepth is not None:
			self._setDoubleProperty("LNP_SECTION_DEPTH", SectionDepth)
		if ConcreteYoungsModulus is not None:
			self._setDoubleProperty("LNP_YOUNGS_MODULUS_REIN", ConcreteYoungsModulus)
		if Area is not None:
			self._setDoubleProperty("LNP_AREA", Area)
		if MomentOfInertia is not None:
			self._setDoubleProperty("LNP_MOMENT_OF_INERTIA", MomentOfInertia)
		if ConcreteCompressiveStrength is not None:
			self._setDoubleProperty("LNP_COMPRESSIVE_STRENGTH_REIN", ConcreteCompressiveStrength)
		if ConcreteTensileStrength is not None:
			self._setDoubleProperty("LNP_TENSILE_STRENGTH_REIN", ConcreteTensileStrength)
		if Weight is not None:
			self._setDoubleProperty("LNP_WEIGHT_REIN", Weight)
		if Concrete is not None:
			self._setBoolProperty("LNP_USE_CONCRETE", Concrete)
		if Thickness is not None:
			self._setDoubleProperty("LNP_THICKNESS_CONCRETE", Thickness)
		if YoungsModulus is not None:
			self._setDoubleProperty("LNP_YOUNGS_MODULUS_CONCRETE", YoungsModulus)
		if PoissonRatio is not None:
			self._setDoubleProperty("LNP_POISSONS_RATIO_CONCRETE", PoissonRatio)
		if CompressiveStrength is not None:
			self._setDoubleProperty("LNP_COMPRESSIVE_STRENGTH_CONCRETE", CompressiveStrength)
		if TensileStrength is not None:
			self._setDoubleProperty("LNP_TENSILE_STRENGTH_CONCRETE", TensileStrength)
		if MaterialType is not None:
			self._setEnumEMaterialAnalysisTypesProperty("LNP_MATERIAL_TYPE", MaterialType)
		if SlidingGap is not None:
			self._setBoolProperty("LNP_USE_SLIDING_GAP", SlidingGap)
		if StrainAtLocking is not None:
			self._setDoubleProperty("LNP_STRAIN_AT_LOCKING", StrainAtLocking)
		if BeamElementFormulation is not None:
			self._setEnumELinerFormulationProperty("LNP_BEAM_ELEMENT_FORMULATION", BeamElementFormulation)
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
		if StageConcreteProperties is not None:
			self._setBoolProperty("LNP_USE_STAGE_CONCRETE", StageConcreteProperties)