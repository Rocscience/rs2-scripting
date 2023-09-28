from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
from rs2.proxyObjects.PileSubproxyObjects.Elastic import Elastic
from rs2.proxyObjects.PileSubproxyObjects.MohrCoulombPile import MohrCoulombPile
from rs2.proxyObjects.PileSubproxyObjects.Linear import Linear
from rs2.proxyObjects.PileSubproxyObjects.MultiLinear import MultiLinear
from rs2.proxyObjects.PileSubproxyObjects.MaterialDependentPile import MaterialDependentPile
from rs2.proxyObjects.PileSubproxyObjects.Beam import Beam
from rs2.proxyObjects.PileSubproxyObjects.ForceDisplacement import ForceDisplacement
class PileProperty(PropertyProxy):
	"""
	:ref:`Pile Example`
	"""
	def __init__(self, server : Client, ID, documentProxyID):
		self.Elastic = Elastic(server, ID, documentProxyID)
		self.MohrCoulombPile = MohrCoulombPile(server, ID, documentProxyID)
		self.Linear = Linear(server, ID, documentProxyID)
		self.MultiLinear = MultiLinear(server, ID, documentProxyID)
		self.MaterialDependentPile = MaterialDependentPile(server, ID, documentProxyID)
		self.Beam = Beam(server, ID, documentProxyID)
		self.ForceDisplacement = ForceDisplacement(server, ID, documentProxyID)
		super().__init__(server, ID, documentProxyID)
	def getPileName(self) -> str:
		return self._getCStringProperty("PFP_NAME")
	def setPileName(self, value: str):
		return self._setCStringProperty("PFP_NAME", value)
	def getPileColor(self) -> int:
		return self._getUnsignedLongProperty("PFP_COLOR")
	def setPileColor(self, value: int):
		return self._setUnsignedLongProperty("PFP_COLOR", value)
	def getConnectionType(self) -> PileConnectionType:
		return PileConnectionType(self._getEnumEPileConnectionTypeProperty("PFP_TYPE"))
	def setConnectionType(self, value: PileConnectionType):
		return self._setEnumEPileConnectionTypeProperty("PFP_TYPE", value)
	def getSkinResistance(self) -> PileSkinResistanceType:
		return PileSkinResistanceType(self._getEnumEPileSkinResistanceTypeProperty("PFP_SKIN_RESISTANCE_METHOD"))
	def setSkinResistance(self, value: PileSkinResistanceType):
		return self._setEnumEPileSkinResistanceTypeProperty("PFP_SKIN_RESISTANCE_METHOD", value)
	def getMMax(self) -> float:
		return self._callFunction("getMMax", [])
	def setMMax(self, MMax: float):
		return self._callFunction("setMMax", [MMax])
	def getOutOfPlaneSpacing(self) -> float:
		return self._callFunction("getOutOfPlaneSpacing", [])
	def setOutOfPlaneSpacing(self, outOfPlaneSpacing: float):
		return self._callFunction("setOutOfPlaneSpacing", [outOfPlaneSpacing])
	def getLength(self) -> float:
		return self._callFunction("getLength", [])
	def setLength(self, Length: float):
		return self._callFunction("setLength", [Length])
