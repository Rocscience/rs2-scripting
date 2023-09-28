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
	def getLinerProperties(self) -> int:
		return int(self._getIntProperty("PFP_CONSTANT_LINER_PROPERTIES"))
	def setLinerProperties(self, value: int):
		return self._setIntProperty("PFP_CONSTANT_LINER_PROPERTIES", value)
	def setProperties(self, Application : PileApplicationType = None, LinerProperties : int = None):
		if Application is not None:
			self._setEnumEPileApplicationTypeProperty("PFP_BEAM_APPLICATION", Application)
		if LinerProperties is not None:
			self._setIntProperty("PFP_CONSTANT_LINER_PROPERTIES", LinerProperties)
	def getProperties(self):
		return {
		"Application" : self.getApplication(), 
		"LinerProperties" : self.getLinerProperties(), 
		}
