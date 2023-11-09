from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
from rs2.proxyObjects.MaterialSubproxyObjects.ThermalSubProxyObjects.Conductivity import Conductivity
from rs2.proxyObjects.MaterialSubproxyObjects.ThermalSubProxyObjects.HeatCapacity import HeatCapacity
from rs2.proxyObjects.MaterialSubproxyObjects.ThermalSubProxyObjects.SoilUnfrozenWaterContent import SoilUnfrozenWaterContent
class Thermal(PropertyProxy):
	"""
	:ref:`Material Property Thermal Example`
	"""
	def __init__(self, server : Client, ID, documentProxyID):
		self.Conductivity = Conductivity(server, ID, documentProxyID)
		self.HeatCapacity = HeatCapacity(server, ID, documentProxyID)
		self.SoilUnfrozenWaterContent = SoilUnfrozenWaterContent(server, ID, documentProxyID)
		super().__init__(server, ID, documentProxyID)
	def getStaticTemperatureMode(self) -> StaticWaterModes:
		return StaticWaterModes(self._getEnumEStaticWaterModesProperty("MP_STATIC_TEMPERATURE_METHOD"))
	def setStaticTemperatureMode(self, value: StaticWaterModes):
		return self._setEnumEStaticWaterModesProperty("MP_STATIC_TEMPERATURE_METHOD", value)
	def getStaticTemperature(self) -> float:
		return self._getDoubleProperty("MP_STATIC_TEMPERATURE_CONST")
	def setStaticTemperature(self, value: float):
		return self._setDoubleProperty("MP_STATIC_TEMPERATURE_CONST", value)
	def getWaterContent(self) -> ThermalWaterContentMethodType:
		return ThermalWaterContentMethodType(self._getEnumEThermalWaterContentMethodTypeProperty("MP_THERMAL_WATER_CONTENT_METHOD"))
	def setWaterContent(self, value: ThermalWaterContentMethodType):
		return self._setEnumEThermalWaterContentMethodTypeProperty("MP_THERMAL_WATER_CONTENT_METHOD", value)
	def getWaterContentValue(self) -> float:
		return self._getDoubleProperty("MP_THERMAL_WATER_CONTENT_VALUE")
	def setWaterContentValue(self, value: float):
		return self._setDoubleProperty("MP_THERMAL_WATER_CONTENT_VALUE", value)
	def getThermalExpansion(self) -> bool:
		return self._getBoolProperty("MP_THERMAL_EXPANSION_IS_ON")
	def setThermalExpansion(self, value: bool):
		return self._setBoolProperty("MP_THERMAL_EXPANSION_IS_ON", value)
	def getExpansionCoefficient(self) -> float:
		return self._getDoubleProperty("MP_THERMAL_EXPANSION_ALPHA")
	def setExpansionCoefficient(self, value: float):
		return self._setDoubleProperty("MP_THERMAL_EXPANSION_ALPHA", value)
	def getDispersivity(self) -> bool:
		return self._getBoolProperty("MP_THERMAL_DISPERSIVITY_IS_ON")
	def setDispersivity(self, value: bool):
		return self._setBoolProperty("MP_THERMAL_DISPERSIVITY_IS_ON", value)
	def getLongitudinalDispersivity(self) -> float:
		return self._getDoubleProperty("MP_THERMAL_DISPERSIVITY_LONGITUDINAL")
	def setLongitudinalDispersivity(self, value: float):
		return self._setDoubleProperty("MP_THERMAL_DISPERSIVITY_LONGITUDINAL", value)
	def getTransverseDispersivity(self) -> float:
		return self._getDoubleProperty("MP_THERMAL_DISPERSIVITY_TRANSVERSE")
	def setTransverseDispersivity(self, value: float):
		return self._setDoubleProperty("MP_THERMAL_DISPERSIVITY_TRANSVERSE", value)
	def setStaticTemperatureGridToUseByName(self, gridName: str):
		"""
		gridName is the name of the grid to be used. "None" and "Default Grid" are available by default.
		"""
		return self._callFunction("setStaticTemperatureGridToUseByName", [gridName])
	def getStaticTemperatureGridToUse(self) -> str:
		return self._callFunction("getStaticTemperatureGridToUse", [])
