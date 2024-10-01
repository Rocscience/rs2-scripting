from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.properties.material.thermal.conductivity.ConstantConductivity import ConstantConductivity
from rs2.modeler.properties.material.thermal.conductivity.Johansen import Johansen
from rs2.modeler.properties.material.thermal.conductivity.JohansenLu import JohansenLu
from rs2.modeler.properties.material.thermal.conductivity.Derives import Derives
from rs2.modeler.properties.material.thermal.conductivity.CoteAndKonrad import CoteAndKonrad
from rs2.modeler.properties.material.thermal.conductivity.Tabular import Tabular
class Conductivity(PropertyProxy):
	"""
	Attributes:
		ConstantConductivity (ConstantConductivity): Reference object for modifying property.
		Johansen (Johansen): Reference object for modifying property.
		JohansenLu (JohansenLu): Reference object for modifying property.
		Derives (Derives): Reference object for modifying property.
		CoteAndKonrad (CoteAndKonrad): Reference object for modifying property.
		Tabular (Tabular): Reference object for modifying property.

	Examples:
		:ref:`Material Property Thermal Example`
	"""
	def __init__(self, client : Client, ID, documentProxyID):
		self.ConstantConductivity = ConstantConductivity(client, ID, documentProxyID)
		self.Johansen = Johansen(client, ID, documentProxyID)
		self.JohansenLu = JohansenLu(client, ID, documentProxyID)
		self.Derives = Derives(client, ID, documentProxyID)
		self.CoteAndKonrad = CoteAndKonrad(client, ID, documentProxyID)
		self.Tabular = Tabular(client, ID, documentProxyID)
		super().__init__(client, ID, documentProxyID)
	def getMethod(self) -> ThermalType:
		return ThermalType(self._getEnumEThermalTypeProperty("MP_THERMAL_TYPE"))
	def setMethod(self, value: ThermalType):
		return self._setEnumEThermalTypeProperty("MP_THERMAL_TYPE", value)
