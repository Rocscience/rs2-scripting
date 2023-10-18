from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
from rs2.proxyObjects.MaterialSubproxyObjects.ThermalSubProxyObjects.SoilUnfrozenWaterContentProxies.Konrad import Konrad
from rs2.proxyObjects.MaterialSubproxyObjects.ThermalSubProxyObjects.SoilUnfrozenWaterContentProxies.TiceAnderson import TiceAnderson
from rs2.proxyObjects.MaterialSubproxyObjects.ThermalSubProxyObjects.SoilUnfrozenWaterContentProxies.HydraulicModel import HydraulicModel
class SoilUnfrozenWaterContent(PropertyProxy):
	"""
	:ref:`Material Property Thermal SoilUnfrozenWaterContent Example`
	"""
	def __init__(self, server : Client, ID, documentProxyID):
		self.Konrad = Konrad(server, ID, documentProxyID)
		self.TiceAnderson = TiceAnderson(server, ID, documentProxyID)
		self.HydraulicModel = HydraulicModel(server, ID, documentProxyID)
		super().__init__(server, ID, documentProxyID)
	def getType(self) -> ThermalType:
		return ThermalType(self._getEnumEThermalTypeProperty("MP_THERMAL_WATER_CONTENT_TYPE"))
	def setType(self, value: ThermalType):
		return self._setEnumEThermalTypeProperty("MP_THERMAL_WATER_CONTENT_TYPE", value)
