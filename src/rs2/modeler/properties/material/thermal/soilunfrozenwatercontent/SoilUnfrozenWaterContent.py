from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.properties.material.thermal.soilunfrozenwatercontent.Konrad import Konrad
from rs2.modeler.properties.material.thermal.soilunfrozenwatercontent.TiceAnderson import TiceAnderson
from rs2.modeler.properties.material.thermal.soilunfrozenwatercontent.CustomWaterContent import CustomWaterContent
from rs2.modeler.properties.material.thermal.soilunfrozenwatercontent.hydraulic.HydraulicModel import HydraulicModel
class SoilUnfrozenWaterContent(PropertyProxy):
	"""
	Attributes:
		Konrad (Konrad): Reference object for modifying property.
		TiceAnderson (TiceAnderson): Reference object for modifying property.
		CustomWaterContent (CustomWaterContent): Reference object for modifying property.
		HydraulicModel (HydraulicModel): Reference object for modifying property.

	Examples:
		:ref:`Material Property Thermal Example`
	"""
	def __init__(self, client : Client, ID, documentProxyID):
		self.Konrad = Konrad(client, ID, documentProxyID)
		self.TiceAnderson = TiceAnderson(client, ID, documentProxyID)
		self.CustomWaterContent = CustomWaterContent(client, ID, documentProxyID)
		self.HydraulicModel = HydraulicModel(client, ID, documentProxyID)
		super().__init__(client, ID, documentProxyID)
	def getType(self) -> ThermalWaterContentType:
		return ThermalWaterContentType(self._getEnumEThermalWaterContentTypeProperty("MP_THERMAL_WATER_CONTENT_TYPE"))
	def setType(self, value: ThermalWaterContentType):
		return self._setEnumEThermalWaterContentTypeProperty("MP_THERMAL_WATER_CONTENT_TYPE", value)
