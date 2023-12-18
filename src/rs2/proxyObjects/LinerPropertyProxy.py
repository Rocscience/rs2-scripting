from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
from rs2.proxyObjects.LinerSubproxyObjects.StandardBeam import StandardBeam
from rs2.proxyObjects.LinerSubproxyObjects.Geosynthetic import Geosynthetic
from rs2.proxyObjects.LinerSubproxyObjects.ReinforcedConcrete import ReinforcedConcrete
from rs2.proxyObjects.LinerSubproxyObjects.CableTruss import CableTruss
class LinerProperty(PropertyProxy):
	"""
	:ref:`Liner Example`
	"""
	def __init__(self, client : Client, ID, documentProxyID):
		self.StandardBeam = StandardBeam(client, ID, documentProxyID)
		self.Geosynthetic = Geosynthetic(client, ID, documentProxyID)
		self.ReinforcedConcrete = ReinforcedConcrete(client, ID, documentProxyID)
		self.CableTruss = CableTruss(client, ID, documentProxyID)
		super().__init__(client, ID, documentProxyID)
	def getLinerName(self) -> str:
		return self._getCStringProperty("LNP_NAME")
	def setLinerName(self, value: str):
		return self._setCStringProperty("LNP_NAME", value)
	def getLinerColor(self) -> int:
		return self._getUnsignedLongProperty("LNP_COLOR")
	def setLinerColor(self, value: int):
		return self._setUnsignedLongProperty("LNP_COLOR", value)
	def getLinerType(self) -> LinerTypes:
		return LinerTypes(self._getEnumELinerTypesProperty("LNP_LINER_TYPE"))
	def setLinerType(self, value: LinerTypes):
		return self._setEnumELinerTypesProperty("LNP_LINER_TYPE", value)
