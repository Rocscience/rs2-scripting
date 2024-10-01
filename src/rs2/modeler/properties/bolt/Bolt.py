from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.properties.bolt.EndAnchored import EndAnchored
from rs2.modeler.properties.bolt.FullyBonded import FullyBonded
from rs2.modeler.properties.bolt.PlainStrandCable import PlainStrandCable
from rs2.modeler.properties.bolt.Swellex import Swellex
from rs2.modeler.properties.bolt.Tieback import Tieback
class BoltProperty(PropertyProxy):
	"""
	Attributes:
		EndAnchored (EndAnchored): Reference object for modifying property.
		FullyBonded (FullyBonded): Reference object for modifying property.
		PlainStrandCable (PlainStrandCable): Reference object for modifying property.
		Swellex (Swellex): Reference object for modifying property.
		Tieback (Tieback): Reference object for modifying property.

	Examples:
		:ref:`Bolt Script Example`
	"""
	def __init__(self, client : Client, ID, documentProxyID):
		self.EndAnchored = EndAnchored(client, ID, documentProxyID)
		self.FullyBonded = FullyBonded(client, ID, documentProxyID)
		self.PlainStrandCable = PlainStrandCable(client, ID, documentProxyID)
		self.Swellex = Swellex(client, ID, documentProxyID)
		self.Tieback = Tieback(client, ID, documentProxyID)
		super().__init__(client, ID, documentProxyID)
	def getBoltName(self) -> str:
		return self._getCStringProperty("BP_NAME")
	def setBoltName(self, value: str):
		return self._setCStringProperty("BP_NAME", value)
	def getBoltColor(self) -> int:
		return self._getUnsignedLongProperty("BP_COLOR")
	def setBoltColor(self, value: int):
		return self._setUnsignedLongProperty("BP_COLOR", value)
	def getBoltType(self) -> BoltTypes:
		return BoltTypes(self._getEnumEBoltTypesProperty("BP_TYPE"))
	def setBoltType(self, value: BoltTypes):
		return self._setEnumEBoltTypesProperty("BP_TYPE", value)
