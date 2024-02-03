from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class UserDefined(PropertyProxy):
	def setUserDefinedPermeabilityAndWaterContentFunction(self, functionName: str):
		return self._callFunction("setUserDefinedPermeabilityAndWaterContentFunction", [functionName])
	def getUserDefinedPermeabilityAndWaterContentFunction(self) -> str:
		return self._callFunction("getUserDefinedPermeabilityAndWaterContentFunction", [])
