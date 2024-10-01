from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.properties.liner.StandardBeam import StandardBeam
from rs2.modeler.properties.liner.Geosynthetic import Geosynthetic
from rs2.modeler.properties.liner.ReinforcedConcrete import ReinforcedConcrete
from rs2.modeler.properties.liner.CableTruss import CableTruss
class LinerProperty(PropertyProxy):
	"""
	Attributes:
		StandardBeam (StandardBeam): Reference object for modifying property.
		Geosynthetic (Geosynthetic): Reference object for modifying property.
		ReinforcedConcrete (ReinforcedConcrete): Reference object for modifying property.
		CableTruss (CableTruss): Reference object for modifying property.

	Examples:
		:ref:`Liner Stage Factor Example`
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
