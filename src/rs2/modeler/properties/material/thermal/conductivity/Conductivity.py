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
	Examples:
		:ref:`Material Property Thermal Example`

	Attributes:
		ConstantConductivity (ConstantConductivity) : Reference object for modifying constant conductivity properties
		Johansen (Johansen) : Reference object for modifying johansen conductivity properties
		JohansenLu (JohansenLu) : Reference object for modifying johansen lu conductivity properties
		Derives (Derives) : Reference object for modifying derives conductivity properties
		CoteAndKonrad (CoteAndKonrad) : Reference object for modifying cote and kondrad conductivity properties
		Tabular (Tabular) : Reference object for modifying tabular conductivity properties
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
