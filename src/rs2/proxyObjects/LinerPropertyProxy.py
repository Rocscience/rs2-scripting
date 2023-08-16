from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
from .StandardBeam import StandardBeam
from .Geosynthetic import Geosynthetic
from .ReinforcedConcrete import ReinforcedConcrete
from .CableTruss import CableTruss
class LinerProperty(PropertyProxy):
	def __init__(self, server : Client, ID, documentProxyID):
		self.StandardBeam = StandardBeam(server, ID, documentProxyID)
		self.Geosynthetic = Geosynthetic(server, ID, documentProxyID)
		self.ReinforcedConcrete = ReinforcedConcrete(server, ID, documentProxyID)
		self.CableTruss = CableTruss(server, ID, documentProxyID)
		super().__init__(server, ID, documentProxyID)
	def getLinerName(self) -> str:
		return self._getCStringProperty("LNP_NAME")
	def setLinerName(self, value: str):
		return self._validateAndSetCStringProperty("LNP_NAME", value)
	def getLinerColor(self) -> int:
		return self._getUnsignedLongProperty("LNP_COLOR")
	def setLinerColor(self, value: int):
		return self._validateAndSetUnsignedLongProperty("LNP_COLOR", value)
	def getLinerType(self) -> LinerTypes:
		return LinerTypes(self._getEnumELinerTypesProperty("LNP_LINER_TYPE"))
	def setLinerType(self, value: LinerTypes):
		return self._validateAndSetEnumELinerTypesProperty("LNP_LINER_TYPE", value)
