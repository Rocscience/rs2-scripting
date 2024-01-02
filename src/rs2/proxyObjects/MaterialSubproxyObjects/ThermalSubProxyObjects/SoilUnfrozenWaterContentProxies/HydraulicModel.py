from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
from rs2.proxyObjects.MaterialSubproxyObjects.ThermalSubProxyObjects.SoilUnfrozenWaterContentProxies.HydraulicModelProxies.SimpleWaterContent import SimpleWaterContent
from rs2.proxyObjects.MaterialSubproxyObjects.ThermalSubProxyObjects.SoilUnfrozenWaterContentProxies.HydraulicModelProxies.FredlundWaterContent import FredlundWaterContent
from rs2.proxyObjects.MaterialSubproxyObjects.ThermalSubProxyObjects.SoilUnfrozenWaterContentProxies.HydraulicModelProxies.GenuchtenWaterContent import GenuchtenWaterContent
from rs2.proxyObjects.MaterialSubproxyObjects.ThermalSubProxyObjects.SoilUnfrozenWaterContentProxies.HydraulicModelProxies.BrooksWaterContent import BrooksWaterContent
from rs2.proxyObjects.MaterialSubproxyObjects.ThermalSubProxyObjects.SoilUnfrozenWaterContentProxies.HydraulicModelProxies.GardnerWaterContent import GardnerWaterContent
class HydraulicModel(PropertyProxy):
	"""
	:ref:`Material Property Thermal SoilUnfrozenWaterContent HydraulicModel Example`
	"""
	def __init__(self, client : Client, ID, documentProxyID):
		self.SimpleWaterContent = SimpleWaterContent(client, ID, documentProxyID)
		self.FredlundWaterContent = FredlundWaterContent(client, ID, documentProxyID)
		self.GenuchtenWaterContent = GenuchtenWaterContent(client, ID, documentProxyID)
		self.BrooksWaterContent = BrooksWaterContent(client, ID, documentProxyID)
		self.GardnerWaterContent = GardnerWaterContent(client, ID, documentProxyID)
		super().__init__(client, ID, documentProxyID)
	def getFrozenTemperature(self) -> float:
		return self._getDoubleProperty("MP_THERMAL_WATER_CONTENT_FROZEN_TEMPERATURE")
	def setFrozenTemperature(self, value: float):
		return self._setDoubleProperty("MP_THERMAL_WATER_CONTENT_FROZEN_TEMPERATURE", value)
	def getSelectHydraulicModel(self) -> GroundWaterModes:
		return GroundWaterModes(self._getEnumEGroundWaterModesProperty("MP_THERMAL_SELECT_HYDRAULIC_MODEL"))
	def setSelectHydraulicModel(self, value: GroundWaterModes):
		return self._setEnumEGroundWaterModesProperty("MP_THERMAL_SELECT_HYDRAULIC_MODEL", value)
	def getWCSat(self) -> float:
		return self._getDoubleProperty("MP_WC_SAT_THERMAL")
	def setWCSat(self, value: float):
		return self._setDoubleProperty("MP_WC_SAT_THERMAL", value)
	def getWCRes(self) -> float:
		return self._getDoubleProperty("MP_WC_RES_THERMAL")
	def setWCRes(self, value: float):
		return self._setDoubleProperty("MP_WC_RES_THERMAL", value)
