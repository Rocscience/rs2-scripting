from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class CableTruss(PropertyProxy):
	def getTensileStrengthPeak(self) -> float:
		return self._getDoubleProperty("LNP_TENSILE_STRENGTH")
	def setTensileStrengthPeak(self, value: float):
		return self._setDoubleProperty("LNP_TENSILE_STRENGTH", value)
	def getOutofplaneSpacing(self) -> float:
		return self._getDoubleProperty("LNP_CABLE_OUT_OF_PLANE_SPACING")
	def setOutofplaneSpacing(self, value: float):
		return self._setDoubleProperty("LNP_CABLE_OUT_OF_PLANE_SPACING", value)
	def getUnitWeight(self) -> float:
		return self._getDoubleProperty("LNP_UNIT_WEIGHT")
	def setUnitWeight(self, value: float):
		return self._setDoubleProperty("LNP_UNIT_WEIGHT", value)
	def getCableDiameter(self) -> float:
		return self._getDoubleProperty("LNP_CABLE_DIAMETER")
	def setCableDiameter(self, value: float):
		return self._setDoubleProperty("LNP_CABLE_DIAMETER", value)
	def getIncludeWeightInAnalysis(self) -> bool:
		return self._getBoolProperty("LNP_DISABLED_USE_WEIGHT")
	def setIncludeWeightInAnalysis(self, value: bool):
		return self._setBoolProperty("LNP_DISABLED_USE_WEIGHT", value)
	def getYoungsModulus(self) -> float:
		return self._getDoubleProperty("LNP_YOUNGS_MODULUS")
	def setYoungsModulus(self, value: float):
		return self._setDoubleProperty("LNP_YOUNGS_MODULUS", value)
	def getMaterialType(self) -> MaterialType:
		return MaterialType(self._getEnumEMaterialAnalysisTypesProperty("LNP_MATERIAL_TYPE"))
	def setMaterialType(self, value: MaterialType):
		return self._setEnumEMaterialAnalysisTypesProperty("LNP_MATERIAL_TYPE", value)
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
		"""
		Grids "None" and "Default Grid" available by default.
		"""
		return self._callFunction("getStaticTemperatureGridToUse", [])
	def setStaticTemperatureGridToUse(self, gridName: str):
		return self._callFunction("setStaticTemperatureGridToUse", [gridName ])
