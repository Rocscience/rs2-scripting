from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
from rs2.proxyObjects.MaterialSubproxyObjects.ThermalSubProxyObjects.HeatCapacityProxies.ConstantHeatCapacity import ConstantHeatCapacity
from rs2.proxyObjects.MaterialSubproxyObjects.ThermalSubProxyObjects.HeatCapacityProxies.JameNewman import JameNewman
from rs2.proxyObjects.MaterialSubproxyObjects.ThermalSubProxyObjects.HeatCapacityProxies.CustomHeatCapacity import CustomHeatCapacity
class HeatCapacity(PropertyProxy):
	"""
	:ref:`Material Property Thermal HeatCapacity Example`
	"""
	def __init__(self, server : Client, ID, documentProxyID):
		self.ConstantHeatCapacity = ConstantHeatCapacity(server, ID, documentProxyID)
		self.JameNewman = JameNewman(server, ID, documentProxyID)
		self.CustomHeatCapacity = CustomHeatCapacity(server, ID, documentProxyID)
		super().__init__(server, ID, documentProxyID)
	def getType(self) -> ThermalHeatCapacityType:
		return ThermalHeatCapacityType(self._getEnumEThermalHeatCapacityTypeProperty("MP_THERMAL_HEAT_CAPACITY_TYPE"))
	def setType(self, value: ThermalHeatCapacityType):
		return self._setEnumEThermalHeatCapacityTypeProperty("MP_THERMAL_HEAT_CAPACITY_TYPE", value)
