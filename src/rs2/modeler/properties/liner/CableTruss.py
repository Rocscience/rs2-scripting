from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.RelativeStageFactorInterface import RelativeStageFactorInterface
class CableTrussStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getUnitWeightFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_UNIT_WEIGHT", self.propertyID], proxyArgumentIndices=[1])
	def getCableDiameterFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_CABLE_DIAMETER", self.propertyID], proxyArgumentIndices=[1])
	def getYoungsModulusFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_YOUNGS_MODULUS", self.propertyID], proxyArgumentIndices=[1])
	def getAxialStrainExpansionFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_AXIAL_STRAIN", self.propertyID], proxyArgumentIndices=[1])
	def getTensileStrengthPeakFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_TENSILE_STRENGTH", self.propertyID], proxyArgumentIndices=[1])
	def getTensileStrengthResidualFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_TENSILE_STRENGTH_RES", self.propertyID], proxyArgumentIndices=[1])
	def getConductivityFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_THERAMAL_CONDUCTIVITY", self.propertyID], proxyArgumentIndices=[1])
	def getSpecificHeatCapacityFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_THERAMAL_SPECIFIC_HEAT_CAPACITY", self.propertyID], proxyArgumentIndices=[1])
	def getExpansionCoefficientFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["LNP_THERAMAL_EXPANSION_ALPHA", self.propertyID], proxyArgumentIndices=[1])
class CableTrussDefinedStageFactor(CableTrussStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setUnitWeightFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_UNIT_WEIGHT", value, self.propertyID], proxyArgumentIndices=[2])
	def setCableDiameterFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_CABLE_DIAMETER", value, self.propertyID], proxyArgumentIndices=[2])
	def setYoungsModulusFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_YOUNGS_MODULUS", value, self.propertyID], proxyArgumentIndices=[2])
	def setAxialStrainExpansionFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_AXIAL_STRAIN", value, self.propertyID], proxyArgumentIndices=[2])
	def setTensileStrengthPeakFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_TENSILE_STRENGTH", value, self.propertyID], proxyArgumentIndices=[2])
	def setTensileStrengthResidualFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_TENSILE_STRENGTH_RES", value, self.propertyID], proxyArgumentIndices=[2])
	def setConductivityFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_THERAMAL_CONDUCTIVITY", value, self.propertyID], proxyArgumentIndices=[2])
	def setSpecificHeatCapacityFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_THERAMAL_SPECIFIC_HEAT_CAPACITY", value, self.propertyID], proxyArgumentIndices=[2])
	def setExpansionCoefficientFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["LNP_THERAMAL_EXPANSION_ALPHA", value, self.propertyID], proxyArgumentIndices=[2])
class CableTruss(PropertyProxy):
	def __init__(self, client : Client, ID, documentProxyID):
		super().__init__(client, ID, documentProxyID)
		stageFactorInterfaceID = self._callFunction("getStageFactorInterface", [], keepReturnValueReference=True)
		self.stageFactorInterface = RelativeStageFactorInterface[CableTrussDefinedStageFactor, CableTrussStageFactor](self._client, stageFactorInterfaceID, ID, CableTrussDefinedStageFactor, CableTrussStageFactor)
	def getUnitWeight(self) -> float:
		return self._getDoubleProperty("LNP_UNIT_WEIGHT")
	def setUnitWeight(self, value: float):
		return self._setDoubleProperty("LNP_UNIT_WEIGHT", value)
	def getInitialTemperature(self) -> float:
		return self._getDoubleProperty("LNP_THERAMAL_INITIAL_TEMPERATURE")
	def setInitialTemperature(self, value: float):
		return self._setDoubleProperty("LNP_THERAMAL_INITIAL_TEMPERATURE", value)
	def getCableDiameter(self) -> float:
		return self._getDoubleProperty("LNP_CABLE_DIAMETER")
	def setCableDiameter(self, value: float):
		return self._setDoubleProperty("LNP_CABLE_DIAMETER", value)
	def getOutofplaneSpacing(self) -> float:
		return self._getDoubleProperty("LNP_CABLE_OUT_OF_PLANE_SPACING")
	def setOutofplaneSpacing(self, value: float):
		return self._setDoubleProperty("LNP_CABLE_OUT_OF_PLANE_SPACING", value)
	def getYoungsModulus(self) -> float:
		return self._getDoubleProperty("LNP_YOUNGS_MODULUS")
	def setYoungsModulus(self, value: float):
		return self._setDoubleProperty("LNP_YOUNGS_MODULUS", value)
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
	def getPreTensioning(self) -> bool:
		return self._getBoolProperty("LNP_USE_PRE_TENSIONING")
	def setPreTensioning(self, value: bool):
		return self._setBoolProperty("LNP_USE_PRE_TENSIONING", value)
	def getPreTensioningForce(self) -> float:
		return self._getDoubleProperty("LNP_PRE_TENSIONING")
	def setPreTensioningForce(self, value: float):
		return self._setDoubleProperty("LNP_PRE_TENSIONING", value)
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
	def getStageCableProperties(self) -> bool:
		return self._getBoolProperty("LNP_USE_STAGE_CABLE")
	def setStageCableProperties(self, value: bool):
		return self._setBoolProperty("LNP_USE_STAGE_CABLE", value)
	def getStaticTemperatureGridToUse(self) -> str:
		return self._callFunction("getStaticTemperatureGridToUse", [])
	def setStaticTemperatureGridToUse(self, gridName: str):
		"""
		Grids "None" and "Default Grid" available by default.
		"""
		return self._callFunction("setStaticTemperatureGridToUse", [gridName])
	def setProperties(self, UnitWeight : float = None, InitialTemperature : float = None, CableDiameter : float = None, OutofplaneSpacing : float = None, YoungsModulus : float = None, MaterialType : MaterialType = None, TensileStrengthPeak : float = None, TensileStrengthResidual : float = None, PreTensioning : bool = None, PreTensioningForce : float = None, AxialStrainExpansion : float = None, ActivateThermal : bool = None, StaticTemperatureMode : StaticWaterModes = None, StaticTemperature : float = None, Conductivity : float = None, SpecificHeatCapacity : float = None, ThermalExpansion : bool = None, ExpansionCoefficient : float = None, StageCableProperties : bool = None):
		if UnitWeight is not None:
			self._setDoubleProperty("LNP_UNIT_WEIGHT", UnitWeight)
		if InitialTemperature is not None:
			self._setDoubleProperty("LNP_THERAMAL_INITIAL_TEMPERATURE", InitialTemperature)
		if CableDiameter is not None:
			self._setDoubleProperty("LNP_CABLE_DIAMETER", CableDiameter)
		if OutofplaneSpacing is not None:
			self._setDoubleProperty("LNP_CABLE_OUT_OF_PLANE_SPACING", OutofplaneSpacing)
		if YoungsModulus is not None:
			self._setDoubleProperty("LNP_YOUNGS_MODULUS", YoungsModulus)
		if MaterialType is not None:
			self._setEnumEMaterialAnalysisTypesProperty("LNP_MATERIAL_TYPE", MaterialType)
		if TensileStrengthPeak is not None:
			self._setDoubleProperty("LNP_TENSILE_STRENGTH", TensileStrengthPeak)
		if TensileStrengthResidual is not None:
			self._setDoubleProperty("LNP_TENSILE_STRENGTH_RES", TensileStrengthResidual)
		if PreTensioning is not None:
			self._setBoolProperty("LNP_USE_PRE_TENSIONING", PreTensioning)
		if PreTensioningForce is not None:
			self._setDoubleProperty("LNP_PRE_TENSIONING", PreTensioningForce)
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
		if StageCableProperties is not None:
			self._setBoolProperty("LNP_USE_STAGE_CABLE", StageCableProperties)
	def getProperties(self):
		return {
		"UnitWeight" : self.getUnitWeight(), 
		"InitialTemperature" : self.getInitialTemperature(), 
		"CableDiameter" : self.getCableDiameter(), 
		"OutofplaneSpacing" : self.getOutofplaneSpacing(), 
		"YoungsModulus" : self.getYoungsModulus(), 
		"MaterialType" : self.getMaterialType(), 
		"TensileStrengthPeak" : self.getTensileStrengthPeak(), 
		"TensileStrengthResidual" : self.getTensileStrengthResidual(), 
		"PreTensioning" : self.getPreTensioning(), 
		"PreTensioningForce" : self.getPreTensioningForce(), 
		"AxialStrainExpansion" : self.getAxialStrainExpansion(), 
		"ActivateThermal" : self.getActivateThermal(), 
		"StaticTemperatureMode" : self.getStaticTemperatureMode(), 
		"StaticTemperature" : self.getStaticTemperature(), 
		"Conductivity" : self.getConductivity(), 
		"SpecificHeatCapacity" : self.getSpecificHeatCapacity(), 
		"ThermalExpansion" : self.getThermalExpansion(), 
		"ExpansionCoefficient" : self.getExpansionCoefficient(), 
		"StageCableProperties" : self.getStageCableProperties(), 
		}