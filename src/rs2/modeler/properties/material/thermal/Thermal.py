from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.AbsoluteStageFactorGettersInterface import AbsoluteStageFactorGettersInterface
class ThermalStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getThermalGridFactor(self) -> str:
		return self._callFunction("getThermalGridFactor", [self.propertyID], proxyArgumentIndices=[0])
class ThermalDefinedStageFactor(ThermalStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setThermalGridFactor(self, thermalGridName: str):
		return self._callFunction("setThermalGridFactor", [thermalGridName, self.propertyID], proxyArgumentIndices=[1])
from rs2.modeler.properties.material.thermal.conductivity.Conductivity import Conductivity
from rs2.modeler.properties.material.thermal.heatcapacity.HeatCapacity import HeatCapacity
from rs2.modeler.properties.material.thermal.soilunfrozenwatercontent.SoilUnfrozenWaterContent import SoilUnfrozenWaterContent
class Thermal(PropertyProxy):
	"""
	Attributes:
		stageFactorInterface (AbsoluteStageFactorGettersInterface[ThermalDefinedStageFactor, ThermalStageFactor]): Reference object for modifying stage factor property.
		Conductivity (Conductivity): Reference object for modifying property.
		HeatCapacity (HeatCapacity): Reference object for modifying property.
		SoilUnfrozenWaterContent (SoilUnfrozenWaterContent): Reference object for modifying property.

	Examples:
		:ref:`Material Property Thermal Example`
	"""
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		super().__init__(client, ID, documentProxyID)
		self.stageFactorInterface = AbsoluteStageFactorGettersInterface[ThermalDefinedStageFactor, ThermalStageFactor](self._client, stageFactorInterfaceID, ID, ThermalDefinedStageFactor, ThermalStageFactor)
		self.Conductivity = Conductivity(client, ID, documentProxyID)
		self.HeatCapacity = HeatCapacity(client, ID, documentProxyID)
		self.SoilUnfrozenWaterContent = SoilUnfrozenWaterContent(client, ID, documentProxyID)
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
