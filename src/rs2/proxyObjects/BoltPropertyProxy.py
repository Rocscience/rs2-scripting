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
		return self._validateAndSetCStringProperty("BP_NAME", value)
	def getBoltColor(self) -> int:
		return self._getUnsignedLongProperty("BP_COLOR")
	def setBoltColor(self, value: int):
		return self._validateAndSetUnsignedLongProperty("BP_COLOR", value)
	def getBoltType(self) -> BoltTypes:
		return BoltTypes(self._getEnumEBoltTypesProperty("BP_TYPE"))
	def setBoltType(self, value: BoltTypes):
		return self._validateAndSetEnumEBoltTypesProperty("BP_TYPE", value)
