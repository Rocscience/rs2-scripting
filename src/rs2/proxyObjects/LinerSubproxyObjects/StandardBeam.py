from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
from rs2.ProxyObject import ProxyObject
class StandardBeamStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, property : PropertyProxy):
		super().__init__(client, ID)
		self.property = property
	def getThicknessFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_THICKNESS", self.property._ID], proxyArgumentIndices=[1])
	def setThicknessFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_THICKNESS", value, self.property._ID], proxyArgumentIndices=[2])
	def getAreaFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_AREA", self.property._ID], proxyArgumentIndices=[1])
	def setAreaFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_AREA", value, self.property._ID], proxyArgumentIndices=[2])
	def getMomentOfInertiaFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_MOMENT_OF_INERTIA", self.property._ID], proxyArgumentIndices=[1])
	def setMomentOfInertiaFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_MOMENT_OF_INERTIA", value, self.property._ID], proxyArgumentIndices=[2])
	def getYoungsModulusFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_YOUNGS_MODULUS", self.property._ID], proxyArgumentIndices=[1])
	def setYoungsModulusFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_YOUNGS_MODULUS", value, self.property._ID], proxyArgumentIndices=[2])
	def getPoissonsRatioFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_POISSONS_RATIO", self.property._ID], proxyArgumentIndices=[1])
	def setPoissonsRatioFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_POISSONS_RATIO", value, self.property._ID], proxyArgumentIndices=[2])
	def getAxialStrainExpansionFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_AXIAL_STRAIN", self.property._ID], proxyArgumentIndices=[1])
	def setAxialStrainExpansionFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_AXIAL_STRAIN", value, self.property._ID], proxyArgumentIndices=[2])
	def getCompressiveStrengthPeakFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_COMPRESSIVE_STRENGTH", self.property._ID], proxyArgumentIndices=[1])
	def setCompressiveStrengthPeakFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_COMPRESSIVE_STRENGTH", value, self.property._ID], proxyArgumentIndices=[2])
	def getCompressiveStrengthResidualFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_COMPRESSIVE_STRENGTH_RES", self.property._ID], proxyArgumentIndices=[1])
	def setCompressiveStrengthResidualFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_COMPRESSIVE_STRENGTH_RES", value, self.property._ID], proxyArgumentIndices=[2])
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
class StandardBeam(PropertyProxy):
	def getUnitWeight(self) -> float:
		return self._getDoubleProperty("LNP_UNIT_WEIGHT")
	def setUnitWeight(self, value: float):
		return self._setDoubleProperty("LNP_UNIT_WEIGHT", value)
	def getIncludeWeightInStressAnalysis(self) -> bool:
		return self._getBoolProperty("LNP_USE_WEIGHT")
	def setIncludeWeightInStressAnalysis(self, value: bool):
		return self._setBoolProperty("LNP_USE_WEIGHT", value)
	def getMethod(self) -> GeometryChoice:
		return GeometryChoice(self._getEnumEGeometryChoiceProperty("LNP_GEOMETRY_CHOICE"))
	def setMethod(self, value: GeometryChoice):
		return self._setEnumEGeometryChoiceProperty("LNP_GEOMETRY_CHOICE", value)
	def getThickness(self) -> float:
		return self._getDoubleProperty("LNP_THICKNESS")
	def setThickness(self, value: float):
		return self._setDoubleProperty("LNP_THICKNESS", value)
	def getArea(self) -> float:
		return self._getDoubleProperty("LNP_AREA")
	def setArea(self, value: float):
		return self._setDoubleProperty("LNP_AREA", value)
	def getMomentOfInertia(self) -> float:
		return self._getDoubleProperty("LNP_MOMENT_OF_INERTIA")
	def setMomentOfInertia(self, value: float):
		return self._setDoubleProperty("LNP_MOMENT_OF_INERTIA", value)
	def getYoungsModulus(self) -> float:
		return self._getDoubleProperty("LNP_YOUNGS_MODULUS")
	def setYoungsModulus(self, value: float):
		return self._setDoubleProperty("LNP_YOUNGS_MODULUS", value)
	def getPoissonsRatio(self) -> float:
		return self._getDoubleProperty("LNP_POISSONS_RATIO")
	def setPoissonsRatio(self, value: float):
		return self._setDoubleProperty("LNP_POISSONS_RATIO", value)
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
	def getStageFactors(self) -> List[StandardBeamStageFactor]:
		"""
		Returns the defined stage factors in a list, in order from stage 1 to n.
		"""
		stageFactorReferenceIds = self._callFunction('getStageFactors', [], keepReturnValueReference=True)
		stageFactors = []
		for stageFactorID in stageFactorReferenceIds :
			stageFactors.append(StandardBeamStageFactor(self._client, stageFactorID, self))
		return stageFactors
	def setProperties(self, UnitWeight : float = None, IncludeWeightInStressAnalysis : bool = None, Method : GeometryChoice = None, Thickness : float = None, Area : float = None, MomentOfInertia : float = None, YoungsModulus : float = None, PoissonsRatio : float = None, MaterialType : MaterialType = None, CompressiveStrengthPeak : float = None, CompressiveStrengthResidual : float = None, TensileStrengthPeak : float = None, TensileStrengthResidual : float = None, SlidingGap : bool = None, StrainAtLocking : float = None, BeamElementFormulation : LinerFormulation = None, ActivateThermal : bool = None, StaticTemperatureMode : StaticWaterModes = None, StaticTemperature : float = None, Conductivity : float = None, SpecificHeatCapacity : float = None, ThermalExpansion : bool = None, ExpansionCoefficient : float = None, StageLinerProperties : bool = None):
		if UnitWeight is not None:
			self._setDoubleProperty("LNP_UNIT_WEIGHT", UnitWeight)
		if IncludeWeightInStressAnalysis is not None:
			self._setBoolProperty("LNP_USE_WEIGHT", IncludeWeightInStressAnalysis)
		if Method is not None:
			self._setEnumEGeometryChoiceProperty("LNP_GEOMETRY_CHOICE", Method)
		if Thickness is not None:
			self._setDoubleProperty("LNP_THICKNESS", Thickness)
		if Area is not None:
			self._setDoubleProperty("LNP_AREA", Area)
		if MomentOfInertia is not None:
			self._setDoubleProperty("LNP_MOMENT_OF_INERTIA", MomentOfInertia)
		if YoungsModulus is not None:
			self._setDoubleProperty("LNP_YOUNGS_MODULUS", YoungsModulus)
		if PoissonsRatio is not None:
			self._setDoubleProperty("LNP_POISSONS_RATIO", PoissonsRatio)
		if MaterialType is not None:
			self._setEnumEMaterialAnalysisTypesProperty("LNP_MATERIAL_TYPE", MaterialType)
		if CompressiveStrengthPeak is not None:
			self._setDoubleProperty("LNP_COMPRESSIVE_STRENGTH", CompressiveStrengthPeak)
		if CompressiveStrengthResidual is not None:
			self._setDoubleProperty("LNP_COMPRESSIVE_STRENGTH_RES", CompressiveStrengthResidual)
		if TensileStrengthPeak is not None:
			self._setDoubleProperty("LNP_TENSILE_STRENGTH", TensileStrengthPeak)
		if TensileStrengthResidual is not None:
			self._setDoubleProperty("LNP_TENSILE_STRENGTH_RES", TensileStrengthResidual)
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
		if StageLinerProperties is not None:
			self._setBoolProperty("LNP_USE_STAGE_LINER", StageLinerProperties)
	def getProperties(self):
		return {
		"UnitWeight" : self.getUnitWeight(), 
		"IncludeWeightInStressAnalysis" : self.getIncludeWeightInStressAnalysis(), 
		"Method" : self.getMethod(), 
		"Thickness" : self.getThickness(), 
		"Area" : self.getArea(), 
		"MomentOfInertia" : self.getMomentOfInertia(), 
		"YoungsModulus" : self.getYoungsModulus(), 
		"PoissonsRatio" : self.getPoissonsRatio(), 
		"MaterialType" : self.getMaterialType(), 
		"CompressiveStrengthPeak" : self.getCompressiveStrengthPeak(), 
		"CompressiveStrengthResidual" : self.getCompressiveStrengthResidual(), 
		"TensileStrengthPeak" : self.getTensileStrengthPeak(), 
		"TensileStrengthResidual" : self.getTensileStrengthResidual(), 
		"SlidingGap" : self.getSlidingGap(), 
		"StrainAtLocking" : self.getStrainAtLocking(), 
		"BeamElementFormulation" : self.getBeamElementFormulation(), 
		"ActivateThermal" : self.getActivateThermal(), 
		"StaticTemperatureMode" : self.getStaticTemperatureMode(), 
		"StaticTemperature" : self.getStaticTemperature(), 
		"Conductivity" : self.getConductivity(), 
		"SpecificHeatCapacity" : self.getSpecificHeatCapacity(), 
		"ThermalExpansion" : self.getThermalExpansion(), 
		"ExpansionCoefficient" : self.getExpansionCoefficient(), 
		"StageLinerProperties" : self.getStageLinerProperties(), 
		}
