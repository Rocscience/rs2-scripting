from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class GeneralizedAnisotropic(PropertyProxy):
	def setGeneralizedAnisotropicFunction(self, generalizedFunction: list[tuple[float,str]]):
		"""
		Takes a list of tuples (angle, materialPropertyName). First angle must be greater than -90. Last angle must be exactly 90.
		"""
		return self._callFunction("setGeneralizedAnisotropicFunction", [generalizedFunction])
	def getGeneralizedAnisotropicFunction(self) -> list[tuple[float,str]]:
		"""
		Returns a list of tuples (angle, materialPropertyName)
		"""
		return self._callFunction("getGeneralizedAnisotropicFunction", [])
	def setBaseMaterialByName(self, materialName: str):
		return self._callFunction("setBaseMaterialByName", [materialName])
	def getBaseMaterialName(self) -> str:
		return self._callFunction("getBaseMaterialName", [])
