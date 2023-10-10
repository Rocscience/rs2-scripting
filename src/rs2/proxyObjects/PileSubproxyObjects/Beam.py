from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class Beam(PropertyProxy):
	def getApplication(self) -> PileApplicationType:
		return PileApplicationType(self._getEnumEPileApplicationTypeProperty("PFP_BEAM_APPLICATION"))
	def setApplication(self, value: PileApplicationType):
		return self._setEnumEPileApplicationTypeProperty("PFP_BEAM_APPLICATION", value)
	def getLinerProperty(self) -> str:
		return self._callFunction("getBeamLinerProperty", [])
	def setLinerProperty(self, linerName: str):
		return self._callFunction("setBeamLinerProperty", [linerName])
	def getBeamSegment(self) -> tuple[list[float], list[str]]:
		return self._callFunction("getBeamSegment", [])
	def defineBeamSegment(self, Locations: list[float], Liners: list[str]):
		return self._callFunction("defineBeamSegment", [Locations, Liners])
	def setProperties(self, Application : PileApplicationType = None):
		if Application is not None:
			self._setEnumEPileApplicationTypeProperty("PFP_BEAM_APPLICATION", Application)
	def getProperties(self):
		return {
		"Application" : self.getApplication(), 
		}
