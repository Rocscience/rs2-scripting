from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
from rs2.proxyObjects.MaterialSubproxyObjects.ThermalSubProxyObjects.ConductivityProxies.Constant import Constant
from rs2.proxyObjects.MaterialSubproxyObjects.ThermalSubProxyObjects.ConductivityProxies.Johansen import Johansen
from rs2.proxyObjects.MaterialSubproxyObjects.ThermalSubProxyObjects.ConductivityProxies.JohansenLu import JohansenLu
from rs2.proxyObjects.MaterialSubproxyObjects.ThermalSubProxyObjects.ConductivityProxies.Derives import Derives
from rs2.proxyObjects.MaterialSubproxyObjects.ThermalSubProxyObjects.ConductivityProxies.CoteAndKonrad import CoteAndKonrad
from rs2.proxyObjects.MaterialSubproxyObjects.ThermalSubProxyObjects.ConductivityProxies.Tabular import Tabular
class Conductivity(PropertyProxy):
	"""
	:ref:`Material Property Thermal Conductivity Example`
	"""
	def __init__(self, server : Client, ID, documentProxyID):
		self.Constant = Constant(server, ID, documentProxyID)
		self.Johansen = Johansen(server, ID, documentProxyID)
		self.JohansenLu = JohansenLu(server, ID, documentProxyID)
		self.Derives = Derives(server, ID, documentProxyID)
		self.CoteAndKonrad = CoteAndKonrad(server, ID, documentProxyID)
		self.Tabular = Tabular(server, ID, documentProxyID)
		super().__init__(server, ID, documentProxyID)
	def getMethod(self) -> ThermalType:
		return ThermalType(self._getEnumEThermalTypeProperty("MP_THERMAL_TYPE"))
	def setMethod(self, value: ThermalType):
		return self._setEnumEThermalTypeProperty("MP_THERMAL_TYPE", value)
