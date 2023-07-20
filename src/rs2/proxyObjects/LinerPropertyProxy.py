from rs2.proxyObjects.propertyProxy import PropertyProxy
from enum import Enum, auto
from typing import List
class LinerProperty(PropertyProxy):
	class LinerTypes(Enum):
		P2_LINER_STANDARD_BEAM = "P2_LINER_STANDARD_BEAM"
		P2_LINER_GEOSYNTHETIC = "P2_LINER_GEOSYNTHETIC"
		P2_LINER_REINFORCED_CONCRETE = "P2_LINER_REINFORCED_CONCRETE"
		P2_LINER_CABLE_TRUSS = "P2_LINER_CABLE_TRUSS"
	class LinerFormulation(Enum):
		P2_LINER_FORMULATION_BERNOULLI = "P2_LINER_FORMULATION_BERNOULLI"
		P2_LINER_FORMULATION_TIMOSHENKO = "P2_LINER_FORMULATION_TIMOSHENKO"
	class MaterialType(Enum):
		ELASTIC = "ELASTIC"
		PLASTIC = "PLASTIC"
	class GeometryChoice(Enum):
		LNP_USE_AREA = "LNP_USE_AREA"
		LNP_USE_THICKNESS = "LNP_USE_THICKNESS"
	class StaticWaterModes(Enum):
		SWM_PWP = "SWM_PWP"
		SWM_GRID = "SWM_GRID"
	def getLinerName(self) -> str:
		return self._getCStringProperty("LNP_NAME")
	def setLinerName(self, value: str):
		return self._validateAndSetCStringProperty("LNP_NAME", value)
	def getLinerColor(self) -> int:
		return self._getUnsignedLongProperty("LNP_COLOR")
	def setLinerColor(self, value: int):
		return self._validateAndSetUnsignedLongProperty("LNP_COLOR", value)
	def getLinerType(self) -> LinerTypes:
		return self.LinerTypes(self._getEnumELinerTypesProperty("LNP_LINER_TYPE"))
	def setLinerType(self, value: LinerTypes):
		return self._validateAndSetEnumELinerTypesProperty("LNP_LINER_TYPE", value)
	def getYoungsModulus(self) -> float:
		return self._getDoubleProperty("LNP_YOUNGS_MODULUS")
	def setYoungsModulus(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_YOUNGS_MODULUS", value)
	def getTensileModulus(self) -> float:
		return self._getDoubleProperty("LNP_TENSILE_MODULUS")
	def setTensileModulus(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_TENSILE_MODULUS", value)
	def getPoissonsRatio(self) -> float:
		return self._getDoubleProperty("LNP_POISSONS_RATIO")
	def setPoissonsRatio(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_POISSONS_RATIO", value)
	def getMaterialType(self) -> MaterialType:
		return self.MaterialType(self._getEnumEMaterialAnalysisTypesProperty("LNP_MATERIAL_TYPE"))
	def setMaterialType(self, value: MaterialType):
		return self._validateAndSetEnumEMaterialAnalysisTypesProperty("LNP_MATERIAL_TYPE", value)
	def getCompressiveStrengthPeak(self) -> float:
		return self._getDoubleProperty("LNP_COMPRESSIVE_STRENGTH")
	def setCompressiveStrengthPeak(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_COMPRESSIVE_STRENGTH", value)
	def getCompressiveStrengthResidual(self) -> float:
		return self._getDoubleProperty("LNP_COMPRESSIVE_STRENGTH_RES")
	def setCompressiveStrengthResidual(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_COMPRESSIVE_STRENGTH_RES", value)
	def getTensileStrengthPeak(self) -> float:
		return self._getDoubleProperty("LNP_TENSILE_STRENGTH")
	def setTensileStrengthPeak(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_TENSILE_STRENGTH", value)
	def getTensileStrengthResidual(self) -> float:
		return self._getDoubleProperty("LNP_TENSILE_STRENGTH_RES")
	def setTensileStrengthResidual(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_TENSILE_STRENGTH_RES", value)
	def getMethod(self) -> GeometryChoice:
		return self.GeometryChoice(self._getEnumEGeometryChoiceProperty("LNP_GEOMETRY_CHOICE"))
	def setMethod(self, value: GeometryChoice):
		return self._validateAndSetEnumEGeometryChoiceProperty("LNP_GEOMETRY_CHOICE", value)
	def getThickness(self) -> float:
		return self._getDoubleProperty("LNP_THICKNESS")
	def setThickness(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_THICKNESS", value)
	def getArea(self) -> float:
		return self._getDoubleProperty("LNP_AREA")
	def setArea(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_AREA", value)
	def getMomentOfInertia(self) -> float:
		return self._getDoubleProperty("LNP_MOMENT_OF_INERTIA")
	def setMomentOfInertia(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_MOMENT_OF_INERTIA", value)
	def getIncludeWeightInAnalysis(self) -> bool:
		return self._getBoolProperty("LNP_USE_WEIGHT")
	def setIncludeWeightInAnalysis(self, value: bool):
		return self._validateAndSetBoolProperty("LNP_USE_WEIGHT", value)
	def getUnitWeight(self) -> float:
		return self._getDoubleProperty("LNP_UNIT_WEIGHT")
	def setUnitWeight(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_UNIT_WEIGHT", value)
	def getPreTensioning(self) -> bool:
		return self._getBoolProperty("LNP_USE_PRE_TENSIONING")
	def setPreTensioning(self, value: bool):
		return self._validateAndSetBoolProperty("LNP_USE_PRE_TENSIONING", value)
	def getPreTensioningForce(self) -> float:
		return self._getDoubleProperty("LNP_PRE_TENSIONING")
	def setPreTensioningForce(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_PRE_TENSIONING", value)
	def getSlidingGap(self) -> bool:
		return self._getBoolProperty("LNP_USE_SLIDING_GAP")
	def setSlidingGap(self, value: bool):
		return self._validateAndSetBoolProperty("LNP_USE_SLIDING_GAP", value)
	def getStrainAtLocking(self) -> float:
		return self._getDoubleProperty("LNP_STRAIN_AT_LOCKING")
	def setStrainAtLocking(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_STRAIN_AT_LOCKING", value)
	def getBeamElementFormulation(self) -> LinerFormulation:
		return self.LinerFormulation(self._getEnumELinerFormulationProperty("LNP_BEAM_ELEMENT_FORMULATION"))
	def setBeamElementFormulation(self, value: LinerFormulation):
		return self._validateAndSetEnumELinerFormulationProperty("LNP_BEAM_ELEMENT_FORMULATION", value)
	def getReinforcement(self) -> bool:
		return self._getBoolProperty("LNP_USE_REINFORCEMENT")
	def setReinforcement(self, value: bool):
		return self._validateAndSetBoolProperty("LNP_USE_REINFORCEMENT", value)
	def getConcrete(self) -> bool:
		return self._getBoolProperty("LNP_USE_CONCRETE")
	def setConcrete(self, value: bool):
		return self._validateAndSetBoolProperty("LNP_USE_CONCRETE", value)
	def getSpacing(self) -> float:
		return self._getDoubleProperty("LNP_SPACING")
	def setSpacing(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_SPACING", value)
	def getSectionDepth(self) -> float:
		return self._getDoubleProperty("LNP_SECTION_DEPTH")
	def setSectionDepth(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_SECTION_DEPTH", value)
	def getConcreteYoungsModulus(self) -> float:
		return self._getDoubleProperty("LNP_YOUNGS_MODULUS_REIN")
	def setConcreteYoungsModulus(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_YOUNGS_MODULUS_REIN", value)
	def getConcretePoissonsRatio(self) -> float:
		return self._getDoubleProperty("LNP_POISSON_RATIO_REIN")
	def setConcretePoissonsRatio(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_POISSON_RATIO_REIN", value)
	def getConcreteCompressiveStrength(self) -> float:
		return self._getDoubleProperty("LNP_COMPRESSIVE_STRENGTH_REIN")
	def setConcreteCompressiveStrength(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_COMPRESSIVE_STRENGTH_REIN", value)
	def getConcreteTensileStrength(self) -> float:
		return self._getDoubleProperty("LNP_TENSILE_STRENGTH_REIN")
	def setConcreteTensileStrength(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_TENSILE_STRENGTH_REIN", value)
	def getWeight(self) -> float:
		return self._getDoubleProperty("LNP_WEIGHT_REIN")
	def setWeight(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_WEIGHT_REIN", value)
	def getConcreteThickness(self) -> float:
		return self._getDoubleProperty("LNP_THICKNESS_CONCRETE")
	def setConcreteThickness(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_THICKNESS_CONCRETE", value)
	def getYoungsModulus(self) -> float:
		return self._getDoubleProperty("LNP_YOUNGS_MODULUS_CONCRETE")
	def setYoungsModulus(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_YOUNGS_MODULUS_CONCRETE", value)
	def getPoissonRatio(self) -> float:
		return self._getDoubleProperty("LNP_POISSONS_RATIO_CONCRETE")
	def setPoissonRatio(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_POISSONS_RATIO_CONCRETE", value)
	def getCompressiveStrength(self) -> float:
		return self._getDoubleProperty("LNP_COMPRESSIVE_STRENGTH_CONCRETE")
	def setCompressiveStrength(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_COMPRESSIVE_STRENGTH_CONCRETE", value)
	def getTensileStrength(self) -> float:
		return self._getDoubleProperty("LNP_TENSILE_STRENGTH_CONCRETE")
	def setTensileStrength(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_TENSILE_STRENGTH_CONCRETE", value)
	def getConcreteUnitWeight(self) -> float:
		return self._getDoubleProperty("LNP_UNIT_WEIGTH_CONCRETE")
	def setConcreteUnitWeight(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_UNIT_WEIGTH_CONCRETE", value)
	def getCableDiameter(self) -> float:
		return self._getDoubleProperty("LNP_CABLE_DIAMETER")
	def setCableDiameter(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_CABLE_DIAMETER", value)
	def getOutofplaneSpacing(self) -> float:
		return self._getDoubleProperty("LNP_CABLE_OUT_OF_PLANE_SPACING")
	def setOutofplaneSpacing(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_CABLE_OUT_OF_PLANE_SPACING", value)
	def getStageStandardBeamProperties(self) -> bool:
		return self._getBoolProperty("LNP_USE_STAGE_LINER")
	def setStageStandardBeamProperties(self, value: bool):
		return self._validateAndSetBoolProperty("LNP_USE_STAGE_LINER", value)
	def getStageGeosyntheticProperties(self) -> bool:
		return self._getBoolProperty("LNP_USE_STAGE_GEOSYN")
	def setStageGeosyntheticProperties(self, value: bool):
		return self._validateAndSetBoolProperty("LNP_USE_STAGE_GEOSYN", value)
	def getStageConcreteProperties(self) -> bool:
		return self._getBoolProperty("LNP_USE_STAGE_CONCRETE")
	def setStageConcreteProperties(self, value: bool):
		return self._validateAndSetBoolProperty("LNP_USE_STAGE_CONCRETE", value)
	def getStageCableProperties(self) -> bool:
		return self._getBoolProperty("LNP_USE_STAGE_CABLE")
	def setStageCableProperties(self, value: bool):
		return self._validateAndSetBoolProperty("LNP_USE_STAGE_CABLE", value)
	def getActivateThermal(self) -> bool:
		return self._getBoolProperty("LNP_THERAMAL_ACTIVATE")
	def setActivateThermal(self, value: bool):
		return self._validateAndSetBoolProperty("LNP_THERAMAL_ACTIVATE", value)
	def getConductivity(self) -> float:
		return self._getDoubleProperty("LNP_THERAMAL_CONDUCTIVITY")
	def setConductivity(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_THERAMAL_CONDUCTIVITY", value)
	def getSpecificHeatCapacity(self) -> float:
		return self._getDoubleProperty("LNP_THERAMAL_SPECIFIC_HEAT_CAPACITY")
	def setSpecificHeatCapacity(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_THERAMAL_SPECIFIC_HEAT_CAPACITY", value)
	def getThermalExpansion(self) -> bool:
		return self._getBoolProperty("LNP_THERAMAL_EXPANSION_IS_ON")
	def setThermalExpansion(self, value: bool):
		return self._validateAndSetBoolProperty("LNP_THERAMAL_EXPANSION_IS_ON", value)
	def getExpansionCoefficient(self) -> float:
		return self._getDoubleProperty("LNP_THERAMAL_EXPANSION_ALPHA")
	def setExpansionCoefficient(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_THERAMAL_EXPANSION_ALPHA", value)
	def getInitialTemperature(self) -> float:
		return self._getDoubleProperty("LNP_THERAMAL_INITIAL_TEMPERATURE")
	def setInitialTemperature(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_THERAMAL_INITIAL_TEMPERATURE", value)
	def getGeosyntheticUnitWeight(self) -> float:
		return self._getDoubleProperty("LNP_UNIT_WEIGTH_GEOSYNTHETIC")
	def setGeosyntheticUnitWeight(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_UNIT_WEIGTH_GEOSYNTHETIC", value)
	def getStaticTemperatureMode(self) -> StaticWaterModes:
		return self.StaticWaterModes(self._getEnumEStaticWaterModesProperty("LNP_STATIC_TEMPERATURE_METHOD"))
	def setStaticTemperatureMode(self, value: StaticWaterModes):
		return self._validateAndSetEnumEStaticWaterModesProperty("LNP_STATIC_TEMPERATURE_METHOD", value)
	def getStaticTemperature(self) -> float:
		return self._getDoubleProperty("LNP_STATIC_TEMPERATURE_CONST")
	def setStaticTemperature(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_STATIC_TEMPERATURE_CONST", value)
	
	def getStaticTemperatureGridToUse(self) -> str:
		"""
		Grids "None" and "Default Grid" available by default.
		"""
		return self._callFunction("getStaticTemperatureGridToUse")

	def setStaticTemperatureGridToUse(self, gridName: str):
		return self._callFunction("setStaticTemperatureGridToUse", [gridName])
