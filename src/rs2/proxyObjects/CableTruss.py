from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class CableTruss(PropertyProxy):
	def getCableDiameter(self) -> float:
		return self._getDoubleProperty("LNP_CABLE_DIAMETER")
	def setCableDiameter(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_CABLE_DIAMETER", value)
	def getTensileStrengthPeak(self) -> float:
		return self._getDoubleProperty("LNP_TENSILE_STRENGTH")
	def setTensileStrengthPeak(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_TENSILE_STRENGTH", value)
	def getOutofplaneSpacing(self) -> float:
		return self._getDoubleProperty("LNP_CABLE_OUT_OF_PLANE_SPACING")
	def setOutofplaneSpacing(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_CABLE_OUT_OF_PLANE_SPACING", value)
	def getPreTensioningForce(self) -> float:
		return self._getDoubleProperty("LNP_PRE_TENSIONING")
	def setPreTensioningForce(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_PRE_TENSIONING", value)
	def getYoungsModulus(self) -> float:
		return self._getDoubleProperty("LNP_YOUNGS_MODULUS")
	def setYoungsModulus(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_YOUNGS_MODULUS", value)
	def getMaterialType(self) -> MaterialType:
		return MaterialType(self._getEnumEMaterialAnalysisTypesProperty("LNP_MATERIAL_TYPE"))
	def setMaterialType(self, value: MaterialType):
		return self._validateAndSetEnumEMaterialAnalysisTypesProperty("LNP_MATERIAL_TYPE", value)
	def getPreTensioning(self) -> bool:
		return self._getBoolProperty("LNP_USE_PRE_TENSIONING")
	def setPreTensioning(self, value: bool):
		return self._validateAndSetBoolProperty("LNP_USE_PRE_TENSIONING", value)
	def getTensileStrengthResidual(self) -> float:
		return self._getDoubleProperty("LNP_TENSILE_STRENGTH_RES")
	def setTensileStrengthResidual(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_TENSILE_STRENGTH_RES", value)
	def getActivateThermal(self) -> bool:
		return self._getBoolProperty("LNP_THERAMAL_ACTIVATE")
	def setActivateThermal(self, value: bool):
		return self._validateAndSetBoolProperty("LNP_THERAMAL_ACTIVATE", value)
	def getStaticTemperatureMode(self) -> StaticWaterModes:
		return StaticWaterModes(self._getEnumEStaticWaterModesProperty("LNP_STATIC_TEMPERATURE_METHOD"))
	def setStaticTemperatureMode(self, value: StaticWaterModes):
		return self._validateAndSetEnumEStaticWaterModesProperty("LNP_STATIC_TEMPERATURE_METHOD", value)
	def getStaticTemperature(self) -> float:
		return self._getDoubleProperty("LNP_STATIC_TEMPERATURE_CONST")
	def setStaticTemperature(self, value: float):
		return self._validateAndSetDoubleProperty("LNP_STATIC_TEMPERATURE_CONST", value)
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
	def getStageCableProperties(self) -> bool:
		return self._getBoolProperty("LNP_USE_STAGE_CABLE")
	def setStageCableProperties(self, value: bool):
		return self._validateAndSetBoolProperty("LNP_USE_STAGE_CABLE", value)
	def getStaticTemperatureGridToUse(self) -> str:
		return self._callFunction("getStaticTemperatureGridToUse", [])
	def setStaticTemperatureGridToUse(self, gridName: str):
		"""
		Grids "None" and "Default Grid" available by default.
		"""
		return self._callFunction("setStaticTemperatureGridToUse", [gridName ])
	def setProperties(self, CableDiameter : float = None, TensileStrengthPeak : float = None, OutofplaneSpacing : float = None, PreTensioningForce : float = None, YoungsModulus : float = None, MaterialType : MaterialType = None, PreTensioning : bool = None, TensileStrengthResidual : float = None, ActivateThermal : bool = None, StaticTemperatureMode : StaticWaterModes = None, StaticTemperature : float = None, Conductivity : float = None, SpecificHeatCapacity : float = None, ThermalExpansion : bool = None, ExpansionCoefficient : float = None, StageCableProperties : bool = None):
		if CableDiameter is not None:
			self._validateAndSetDoubleProperty("LNP_CABLE_DIAMETER", CableDiameter)
		if TensileStrengthPeak is not None:
			self._validateAndSetDoubleProperty("LNP_TENSILE_STRENGTH", TensileStrengthPeak)
		if OutofplaneSpacing is not None:
			self._validateAndSetDoubleProperty("LNP_CABLE_OUT_OF_PLANE_SPACING", OutofplaneSpacing)
		if PreTensioningForce is not None:
			self._validateAndSetDoubleProperty("LNP_PRE_TENSIONING", PreTensioningForce)
		if YoungsModulus is not None:
			self._validateAndSetDoubleProperty("LNP_YOUNGS_MODULUS", YoungsModulus)
		if MaterialType is not None:
			self._validateAndSetEnumEMaterialAnalysisTypesProperty("LNP_MATERIAL_TYPE", MaterialType)
		if PreTensioning is not None:
			self._validateAndSetBoolProperty("LNP_USE_PRE_TENSIONING", PreTensioning)
		if TensileStrengthResidual is not None:
			self._validateAndSetDoubleProperty("LNP_TENSILE_STRENGTH_RES", TensileStrengthResidual)
		if ActivateThermal is not None:
			self._validateAndSetBoolProperty("LNP_THERAMAL_ACTIVATE", ActivateThermal)
		if StaticTemperatureMode is not None:
			self._validateAndSetEnumEStaticWaterModesProperty("LNP_STATIC_TEMPERATURE_METHOD", StaticTemperatureMode)
		if StaticTemperature is not None:
			self._validateAndSetDoubleProperty("LNP_STATIC_TEMPERATURE_CONST", StaticTemperature)
		if Conductivity is not None:
			self._validateAndSetDoubleProperty("LNP_THERAMAL_CONDUCTIVITY", Conductivity)
		if SpecificHeatCapacity is not None:
			self._validateAndSetDoubleProperty("LNP_THERAMAL_SPECIFIC_HEAT_CAPACITY", SpecificHeatCapacity)
		if ThermalExpansion is not None:
			self._validateAndSetBoolProperty("LNP_THERAMAL_EXPANSION_IS_ON", ThermalExpansion)
		if ExpansionCoefficient is not None:
			self._validateAndSetDoubleProperty("LNP_THERAMAL_EXPANSION_ALPHA", ExpansionCoefficient)
		if StageCableProperties is not None:
			self._validateAndSetBoolProperty("LNP_USE_STAGE_CABLE", StageCableProperties)