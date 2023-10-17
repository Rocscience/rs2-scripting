from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class UserDefined(PropertyProxy):
	def getWCInputType(self) -> WCInputType:
		return WCInputType(self._getEnumEWCInputTypeProperty("MP_WC_INPUT_TYPE"))
	def setWCInputType(self, value: WCInputType):
		return self._setEnumEWCInputTypeProperty("MP_WC_INPUT_TYPE", value)
	def getUserDefinedPermeabilityAndWaterContent(self) -> int:
		return int(self._getIntProperty("MP_USER_DEFINED_SELECTION"))
	def setUserDefinedPermeabilityAndWaterContent(self, value: int):
		return self._setIntProperty("MP_USER_DEFINED_SELECTION", value)
	def setProperties(self, WCInputType : WCInputType = None, UserDefinedPermeabilityAndWaterContent : int = None):
		if WCInputType is not None:
			self._setEnumEWCInputTypeProperty("MP_WC_INPUT_TYPE", WCInputType)
		if UserDefinedPermeabilityAndWaterContent is not None:
			self._setIntProperty("MP_USER_DEFINED_SELECTION", UserDefinedPermeabilityAndWaterContent)
	def getProperties(self):
		return {
		"WCInputType" : self.getWCInputType(), 
		"UserDefinedPermeabilityAndWaterContent" : self.getUserDefinedPermeabilityAndWaterContent(), 
		}
