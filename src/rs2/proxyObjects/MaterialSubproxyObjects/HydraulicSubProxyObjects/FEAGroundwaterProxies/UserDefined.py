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
	def setUserDefinedPermeabilityAndWaterContentFunction(self, functionName: str):
		return self._callFunction("setUserDefinedPermeabilityAndWaterContentFunction", [functionName])
	def getUserDefinedPermeabilityAndWaterContentFunction(self) -> str:
		return self._callFunction("getUserDefinedPermeabilityAndWaterContentFunction", [])
	def setProperties(self, WCInputType : WCInputType = None):
		if WCInputType is not None:
			self._setEnumEWCInputTypeProperty("MP_WC_INPUT_TYPE", WCInputType)
	def getProperties(self):
		return {
		"WCInputType" : self.getWCInputType(), 
		}
