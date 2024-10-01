from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.properties.material.thermal.heatcapacity.ConstantHeatCapacity import ConstantHeatCapacity
from rs2.modeler.properties.material.thermal.heatcapacity.JameNewman import JameNewman
from rs2.modeler.properties.material.thermal.heatcapacity.CustomHeatCapacity import CustomHeatCapacity
class HeatCapacity(PropertyProxy):
	"""
	Attributes:
		ConstantHeatCapacity (ConstantHeatCapacity): Reference object for modifying property.
		JameNewman (JameNewman): Reference object for modifying property.
		CustomHeatCapacity (CustomHeatCapacity): Reference object for modifying property.

	Examples:
		:ref:`Material Property Thermal Example`
	"""
	def __init__(self, client : Client, ID, documentProxyID):
		self.ConstantHeatCapacity = ConstantHeatCapacity(client, ID, documentProxyID)
		self.JameNewman = JameNewman(client, ID, documentProxyID)
		self.CustomHeatCapacity = CustomHeatCapacity(client, ID, documentProxyID)
		super().__init__(client, ID, documentProxyID)
	def getType(self) -> ThermalHeatCapacityType:
		return ThermalHeatCapacityType(self._getEnumEThermalHeatCapacityTypeProperty("MP_THERMAL_HEAT_CAPACITY_TYPE"))
	def setType(self, value: ThermalHeatCapacityType):
		return self._setEnumEThermalHeatCapacityTypeProperty("MP_THERMAL_HEAT_CAPACITY_TYPE", value)
