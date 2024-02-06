from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.properties.material.InitialConditions import InitialConditions
from rs2.modeler.properties.material.stiffness.Stiffness import Stiffness
from rs2.modeler.properties.material.strength.Strength import Strength
from rs2.modeler.properties.material.hydraulic.Hydraulic import Hydraulic
from rs2.modeler.properties.material.thermal.Thermal import Thermal
from rs2.modeler.properties.material.datum.Datum import Datum
class MaterialProperty(PropertyProxy):
	"""
	:ref:`Material Example`
	"""
	def __init__(self, client : Client, ID, documentProxyID):
		self.InitialConditions = InitialConditions(client, ID, documentProxyID)
		self.Stiffness = Stiffness(client, ID, documentProxyID)
		self.Strength = Strength(client, ID, documentProxyID)
		self.Hydraulic = Hydraulic(client, ID, documentProxyID)
		self.Thermal = Thermal(client, ID, documentProxyID)
		self.Datum = Datum(client, ID, documentProxyID)
		super().__init__(client, ID, documentProxyID)
	def getMaterialName(self) -> str:
		return self._getCStringProperty("MP_NAME")
	def setMaterialName(self, value: str):
		return self._setCStringProperty("MP_NAME", value)
	def getMaterialColor(self) -> int:
		return self._getUnsignedLongProperty("MP_COLOUR")
	def setMaterialColor(self, value: int):
		return self._setUnsignedLongProperty("MP_COLOUR", value)
	def getHatch(self) -> bool:
		return self._getBoolProperty("MP_USE_HATCH")
	def setHatch(self, value: bool):
		return self._setBoolProperty("MP_USE_HATCH", value)
	def getHatchStyle(self) -> HatchStyle:
		return HatchStyle(self._getEnumGdiplusHatchStyleProperty("MP_HATCH_STYLE"))
	def setHatchStyle(self, value: HatchStyle):
		return self._setEnumGdiplusHatchStyleProperty("MP_HATCH_STYLE", value)
	def getHatchColour(self) -> int:
		return self._getUnsignedLongProperty("MP_HATCH_COLOR")
	def setHatchColour(self, value: int):
		return self._setUnsignedLongProperty("MP_HATCH_COLOR", value)
