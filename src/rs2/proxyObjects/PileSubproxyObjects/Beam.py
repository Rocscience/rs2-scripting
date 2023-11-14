from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class Beam(PropertyProxy):
	def getLinerProperty(self) -> str:
		return self._callFunction("getBeamLinerProperty", [])
	def setLinerProperty(self, linerName: str):
		return self._callFunction("setBeamLinerProperty", [linerName, self.documentProxyID], proxyArgumentIndices=[1])
	def getBeamSegment(self) -> tuple[list[float], list[str]]:
		return self._callFunction("getBeamSegment", [])
	def defineBeamSegment(self, Locations: list[float], Liners: list[str]):
		return self._callFunction("defineBeamSegment", [Locations, Liners, self.documentProxyID], proxyArgumentIndices=[2])
	def setApplication(self, method: PileApplicationType):
		return self._callFunction("setBeamApplication", [method.value, self.documentProxyID], proxyArgumentIndices=[1])
	def getApplication(self) -> PileApplicationType:
		return PileApplicationType(self._callFunction("getBeamApplication", []))
