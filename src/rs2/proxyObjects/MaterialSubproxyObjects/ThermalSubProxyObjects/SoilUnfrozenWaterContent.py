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
	def __init__(self, client : Client, ID, documentProxyID):
		self.Konrad = Konrad(client, ID, documentProxyID)
		self.TiceAnderson = TiceAnderson(client, ID, documentProxyID)
		self.HydraulicModel = HydraulicModel(client, ID, documentProxyID)
		super().__init__(client, ID, documentProxyID)
	def getType(self) -> ThermalWaterContentType:
		return ThermalWaterContentType(self._getEnumEThermalWaterContentTypeProperty("MP_THERMAL_WATER_CONTENT_TYPE"))
	def setType(self, value: ThermalWaterContentType):
		return self._setEnumEThermalWaterContentTypeProperty("MP_THERMAL_WATER_CONTENT_TYPE", value)
