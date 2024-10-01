from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.RelativeStageFactorInterface import RelativeStageFactorInterface
class ReinforcedConcreteStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getConcreteUnitWeightFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_UNIT_WEIGTH_CONCRETE", self.propertyID], proxyArgumentIndices=[1])
	def getAreaFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_AREA", self.propertyID], proxyArgumentIndices=[1])
	def getWeightFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_WEIGHT_REIN", self.propertyID], proxyArgumentIndices=[1])
	def getThicknessFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_THICKNESS_CONCRETE", self.propertyID], proxyArgumentIndices=[1])
	def getConcreteYoungsModulusFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_YOUNGS_MODULUS_CONCRETE", self.propertyID], proxyArgumentIndices=[1])
	def getConcreteCompressiveStrengthFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_COMPRESSIVE_STRENGTH_CONCRETE", self.propertyID], proxyArgumentIndices=[1])
	def getConcreteTensileStrengthFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_TENSILE_STRENGTH_CONCRETE", self.propertyID], proxyArgumentIndices=[1])
	def getAxialStrainExpansionFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_AXIAL_STRAIN", self.propertyID], proxyArgumentIndices=[1])
	def getConductivityFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_THERAMAL_CONDUCTIVITY", self.propertyID], proxyArgumentIndices=[1])
	def getSpecificHeatCapacityFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_THERAMAL_SPECIFIC_HEAT_CAPACITY", self.propertyID], proxyArgumentIndices=[1])
	def getExpansionCoefficientFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_THERAMAL_EXPANSION_ALPHA", self.propertyID], proxyArgumentIndices=[1])
class ReinforcedConcreteDefinedStageFactor(ReinforcedConcreteStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setConcreteUnitWeightFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_UNIT_WEIGTH_CONCRETE", value, self.propertyID], proxyArgumentIndices=[2])
	def setAreaFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_AREA", value, self.propertyID], proxyArgumentIndices=[2])
	def setWeightFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_WEIGHT_REIN", value, self.propertyID], proxyArgumentIndices=[2])
	def setThicknessFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_THICKNESS_CONCRETE", value, self.propertyID], proxyArgumentIndices=[2])
	def setConcreteYoungsModulusFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_YOUNGS_MODULUS_CONCRETE", value, self.propertyID], proxyArgumentIndices=[2])
	def setConcreteCompressiveStrengthFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_COMPRESSIVE_STRENGTH_CONCRETE", value, self.propertyID], proxyArgumentIndices=[2])
	def setConcreteTensileStrengthFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_TENSILE_STRENGTH_CONCRETE", value, self.propertyID], proxyArgumentIndices=[2])
	def setAxialStrainExpansionFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_AXIAL_STRAIN", value, self.propertyID], proxyArgumentIndices=[2])
	def setConductivityFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_THERAMAL_CONDUCTIVITY", value, self.propertyID], proxyArgumentIndices=[2])
	def setSpecificHeatCapacityFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_THERAMAL_SPECIFIC_HEAT_CAPACITY", value, self.propertyID], proxyArgumentIndices=[2])
	def setExpansionCoefficientFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_THERAMAL_EXPANSION_ALPHA", value, self.propertyID], proxyArgumentIndices=[2])
class ReinforcedConcrete(PropertyProxy):
	"""
	Attributes:
		stageFactorInterface (RelativeStageFactorInterface[ReinforcedConcreteDefinedStageFactor, ReinforcedConcreteStageFactor]): Reference object for modifying stage factor property.

	Examples:
		:ref:`Liner Stage Factor Example`
	
	"""
	def __init__(self, client : Client, ID, documentProxyID):
		super().__init__(client, ID, documentProxyID)
		stageFactorInterfaceID = self._callFunction("getStageFactorInterface", [], keepReturnValueReference=True)
		self.stageFactorInterface = RelativeStageFactorInterface[ReinforcedConcreteDefinedStageFactor, ReinforcedConcreteStageFactor](self._client, stageFactorInterfaceID, ID, ReinforcedConcreteDefinedStageFactor, ReinforcedConcreteStageFactor)
	def getConcreteUnitWeight(self) -> float:
		return self._getDoubleProperty("LNP_UNIT_WEIGTH_CONCRETE")
	def setConcreteUnitWeight(self, value: float):
		return self._setDoubleProperty("LNP_UNIT_WEIGTH_CONCRETE", value)
	def getIncludeWeightInStressAnalysis(self) -> bool:
		return self._getBoolProperty("LNP_USE_WEIGHT")
	def setIncludeWeightInStressAnalysis(self, value: bool):
		return self._setBoolProperty("LNP_USE_WEIGHT", value)
	def getInitialTemperature(self) -> float:
		return self._getDoubleProperty("LNP_THERAMAL_INITIAL_TEMPERATURE")
	def setInitialTemperature(self, value: float):
		return self._setDoubleProperty("LNP_THERAMAL_INITIAL_TEMPERATURE", value)
	def getReinforcement(self) -> bool:
		return self._getBoolProperty("LNP_USE_REINFORCEMENT")
	def setReinforcement(self, value: bool):
		return self._setBoolProperty("LNP_USE_REINFORCEMENT", value)
	def getSpacing(self) -> float:
		return self._getDoubleProperty("LNP_SPACING")
	def setSpacing(self, value: float):
		return self._setDoubleProperty("LNP_SPACING", value)
	def getSectionDepth(self) -> float:
		return self._getDoubleProperty("LNP_SECTION_DEPTH")
	def setSectionDepth(self, value: float):
		return self._setDoubleProperty("LNP_SECTION_DEPTH", value)
	def getArea(self) -> float:
		return self._getDoubleProperty("LNP_STEELSET_AREA")
	def setArea(self, value: float):
		return self._setDoubleProperty("LNP_STEELSET_AREA", value)
	def getMomentOfInertia(self) -> float:
		return self._getDoubleProperty("LNP_MOMENT_OF_INERTIA")
	def setMomentOfInertia(self, value: float):
		return self._setDoubleProperty("LNP_MOMENT_OF_INERTIA", value)
	def getYoungsModulus(self) -> float:
		return self._getDoubleProperty("LNP_YOUNGS_MODULUS_REIN")
	def setYoungsModulus(self, value: float):
		return self._setDoubleProperty("LNP_YOUNGS_MODULUS_REIN", value)
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
	def getConcreteYoungsModulus(self) -> float:
		return self._getDoubleProperty("LNP_YOUNGS_MODULUS_CONCRETE")
	def setConcreteYoungsModulus(self, value: float):
		return self._setDoubleProperty("LNP_YOUNGS_MODULUS_CONCRETE", value)
	def getPoissonRatio(self) -> float:
		return self._getDoubleProperty("LNP_POISSONS_RATIO_CONCRETE")
	def setPoissonRatio(self, value: float):
		return self._setDoubleProperty("LNP_POISSONS_RATIO_CONCRETE", value)
	def getConcreteCompressiveStrength(self) -> float:
		return self._getDoubleProperty("LNP_COMPRESSIVE_STRENGTH_CONCRETE")
	def setConcreteCompressiveStrength(self, value: float):
		return self._setDoubleProperty("LNP_COMPRESSIVE_STRENGTH_CONCRETE", value)
	def getConcreteTensileStrength(self) -> float:
		return self._getDoubleProperty("LNP_TENSILE_STRENGTH_CONCRETE")
	def setConcreteTensileStrength(self, value: float):
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
	def getAxialStrainExpansion(self) -> float:
		return self._getDoubleProperty("LNP_AXIAL_STRAIN")
	def setAxialStrainExpansion(self, value: float):
		return self._setDoubleProperty("LNP_AXIAL_STRAIN", value)
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
		return self._callFunction("setStaticTemperatureGridToUse", [gridName])
	def setProperties(self, ConcreteUnitWeight : float = None, IncludeWeightInStressAnalysis : bool = None, InitialTemperature : float = None, Reinforcement : bool = None, Spacing : float = None, SectionDepth : float = None, Area : float = None, MomentOfInertia : float = None, YoungsModulus : float = None, CompressiveStrength : float = None, TensileStrength : float = None, Weight : float = None, Concrete : bool = None, Thickness : float = None, ConcreteYoungsModulus : float = None, PoissonRatio : float = None, ConcreteCompressiveStrength : float = None, ConcreteTensileStrength : float = None, MaterialType : MaterialType = None, SlidingGap : bool = None, StrainAtLocking : float = None, BeamElementFormulation : LinerFormulation = None, AxialStrainExpansion : float = None, ActivateThermal : bool = None, StaticTemperatureMode : StaticWaterModes = None, StaticTemperature : float = None, Conductivity : float = None, SpecificHeatCapacity : float = None, ThermalExpansion : bool = None, ExpansionCoefficient : float = None, StageConcreteProperties : bool = None):
		if ConcreteUnitWeight is not None:
			self._setDoubleProperty("LNP_UNIT_WEIGTH_CONCRETE", ConcreteUnitWeight)
		if IncludeWeightInStressAnalysis is not None:
			self._setBoolProperty("LNP_USE_WEIGHT", IncludeWeightInStressAnalysis)
		if InitialTemperature is not None:
			self._setDoubleProperty("LNP_THERAMAL_INITIAL_TEMPERATURE", InitialTemperature)
		if Reinforcement is not None:
			self._setBoolProperty("LNP_USE_REINFORCEMENT", Reinforcement)
		if Spacing is not None:
			self._setDoubleProperty("LNP_SPACING", Spacing)
		if SectionDepth is not None:
			self._setDoubleProperty("LNP_SECTION_DEPTH", SectionDepth)
		if Area is not None:
			self._setDoubleProperty("LNP_STEELSET_AREA", Area)
		if MomentOfInertia is not None:
			self._setDoubleProperty("LNP_MOMENT_OF_INERTIA", MomentOfInertia)
		if YoungsModulus is not None:
			self._setDoubleProperty("LNP_YOUNGS_MODULUS_REIN", YoungsModulus)
		if CompressiveStrength is not None:
			self._setDoubleProperty("LNP_COMPRESSIVE_STRENGTH_REIN", CompressiveStrength)
		if TensileStrength is not None:
			self._setDoubleProperty("LNP_TENSILE_STRENGTH_REIN", TensileStrength)
		if Weight is not None:
			self._setDoubleProperty("LNP_WEIGHT_REIN", Weight)
		if Concrete is not None:
			self._setBoolProperty("LNP_USE_CONCRETE", Concrete)
		if Thickness is not None:
			self._setDoubleProperty("LNP_THICKNESS_CONCRETE", Thickness)
		if ConcreteYoungsModulus is not None:
			self._setDoubleProperty("LNP_YOUNGS_MODULUS_CONCRETE", ConcreteYoungsModulus)
		if PoissonRatio is not None:
			self._setDoubleProperty("LNP_POISSONS_RATIO_CONCRETE", PoissonRatio)
		if ConcreteCompressiveStrength is not None:
			self._setDoubleProperty("LNP_COMPRESSIVE_STRENGTH_CONCRETE", ConcreteCompressiveStrength)
		if ConcreteTensileStrength is not None:
			self._setDoubleProperty("LNP_TENSILE_STRENGTH_CONCRETE", ConcreteTensileStrength)
		if MaterialType is not None:
			self._setEnumEMaterialAnalysisTypesProperty("LNP_MATERIAL_TYPE", MaterialType)
		if SlidingGap is not None:
			self._setBoolProperty("LNP_USE_SLIDING_GAP", SlidingGap)
		if StrainAtLocking is not None:
			self._setDoubleProperty("LNP_STRAIN_AT_LOCKING", StrainAtLocking)
		if BeamElementFormulation is not None:
			self._setEnumELinerFormulationProperty("LNP_BEAM_ELEMENT_FORMULATION", BeamElementFormulation)
		if AxialStrainExpansion is not None:
			self._setDoubleProperty("LNP_AXIAL_STRAIN", AxialStrainExpansion)
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
	def getProperties(self):
		return {
		"ConcreteUnitWeight" : self.getConcreteUnitWeight(), 
		"IncludeWeightInStressAnalysis" : self.getIncludeWeightInStressAnalysis(), 
		"InitialTemperature" : self.getInitialTemperature(), 
		"Reinforcement" : self.getReinforcement(), 
		"Spacing" : self.getSpacing(), 
		"SectionDepth" : self.getSectionDepth(), 
		"Area" : self.getArea(), 
		"MomentOfInertia" : self.getMomentOfInertia(), 
		"YoungsModulus" : self.getYoungsModulus(), 
		"CompressiveStrength" : self.getCompressiveStrength(), 
		"TensileStrength" : self.getTensileStrength(), 
		"Weight" : self.getWeight(), 
		"Concrete" : self.getConcrete(), 
		"Thickness" : self.getThickness(), 
		"ConcreteYoungsModulus" : self.getConcreteYoungsModulus(), 
		"PoissonRatio" : self.getPoissonRatio(), 
		"ConcreteCompressiveStrength" : self.getConcreteCompressiveStrength(), 
		"ConcreteTensileStrength" : self.getConcreteTensileStrength(), 
		"MaterialType" : self.getMaterialType(), 
		"SlidingGap" : self.getSlidingGap(), 
		"StrainAtLocking" : self.getStrainAtLocking(), 
		"BeamElementFormulation" : self.getBeamElementFormulation(), 
		"AxialStrainExpansion" : self.getAxialStrainExpansion(), 
		"ActivateThermal" : self.getActivateThermal(), 
		"StaticTemperatureMode" : self.getStaticTemperatureMode(), 
		"StaticTemperature" : self.getStaticTemperature(), 
		"Conductivity" : self.getConductivity(), 
		"SpecificHeatCapacity" : self.getSpecificHeatCapacity(), 
		"ThermalExpansion" : self.getThermalExpansion(), 
		"ExpansionCoefficient" : self.getExpansionCoefficient(), 
		"StageConcreteProperties" : self.getStageConcreteProperties(), 
		}
