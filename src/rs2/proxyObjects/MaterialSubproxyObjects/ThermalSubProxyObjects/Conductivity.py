from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
from rs2.proxyObjects.MaterialSubproxyObjects.ThermalSubProxyObjects.ConductivityProxies.ConstantConductivity import ConstantConductivity
from rs2.proxyObjects.MaterialSubproxyObjects.ThermalSubProxyObjects.ConductivityProxies.Johansen import Johansen
from rs2.proxyObjects.MaterialSubproxyObjects.ThermalSubProxyObjects.ConductivityProxies.JohansenLu import JohansenLu
from rs2.proxyObjects.MaterialSubproxyObjects.ThermalSubProxyObjects.ConductivityProxies.Derives import Derives
from rs2.proxyObjects.MaterialSubproxyObjects.ThermalSubProxyObjects.ConductivityProxies.CoteAndKonrad import CoteAndKonrad
from rs2.proxyObjects.MaterialSubproxyObjects.ThermalSubProxyObjects.ConductivityProxies.Tabular import Tabular
class Conductivity(PropertyProxy):
	"""
	:ref:`Material Property Thermal Conductivity Example`
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
