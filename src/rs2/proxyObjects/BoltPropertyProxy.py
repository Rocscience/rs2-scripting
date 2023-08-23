from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
from .EndAnchored import EndAnchored
from .FullyBonded import FullyBonded
from .PlainStrandCable import PlainStrandCable
from .Swellex import Swellex
from .Tieback import Tieback
class BoltProperty(PropertyProxy):
	"""
	:ref:`Bolt Example`
	"""
	def __init__(self, server : Client, ID, documentProxyID):
		self.EndAnchored = EndAnchored(server, ID, documentProxyID)
		self.FullyBonded = FullyBonded(server, ID, documentProxyID)
		self.PlainStrandCable = PlainStrandCable(server, ID, documentProxyID)
		self.Swellex = Swellex(server, ID, documentProxyID)
		self.Tieback = Tieback(server, ID, documentProxyID)
		super().__init__(server, ID, documentProxyID)
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
