from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class GeneralizedAnisotropic(PropertyProxy):
	def getBaseMaterial(self) -> int:
		return int(self._getIntProperty("MP_BASE_MATERIAL"))
	def setBaseMaterial(self, value: int):
		return self._setIntProperty("MP_BASE_MATERIAL", value)
	def setProperties(self, BaseMaterial : int = None):
		if BaseMaterial is not None:
			self._setIntProperty("MP_BASE_MATERIAL", BaseMaterial)
	def getProperties(self):
		return {
		"BaseMaterial" : self.getBaseMaterial(), 
		}
