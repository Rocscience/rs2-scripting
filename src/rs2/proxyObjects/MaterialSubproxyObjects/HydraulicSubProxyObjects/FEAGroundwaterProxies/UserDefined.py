from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class UserDefined(PropertyProxy):
	def getUserDefinedPermeabilityAndWaterContent(self) -> int:
		return int(self._getIntProperty("MP_USER_DEFINED_SELECTION"))
	def setUserDefinedPermeabilityAndWaterContent(self, value: int):
		return self._setIntProperty("MP_USER_DEFINED_SELECTION", value)
	def setProperties(self, UserDefinedPermeabilityAndWaterContent : int = None):
		if UserDefinedPermeabilityAndWaterContent is not None:
			self._setIntProperty("MP_USER_DEFINED_SELECTION", UserDefinedPermeabilityAndWaterContent)
	def getProperties(self):
		return {
		"UserDefinedPermeabilityAndWaterContent" : self.getUserDefinedPermeabilityAndWaterContent(), 
		}
