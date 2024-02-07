from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class CustomWaterContent(PropertyProxy):
	def setTemperatureVsUnfrozenWaterContentValues(self, temperature: list[float], unfrozenWaterContent: list[float]):
		return self._callFunction("setTemperatureVsUnfrozenWaterContentValues", [temperature, unfrozenWaterContent])
	def getTemperatureVsUnfrozenWaterContentValues(self) -> tuple[list[float],list[float]]:
		"""
		Returns a tuple of lists [[temperature],[unfrozenWaterContent]]
		"""
		return self._callFunction("getTemperatureVsUnfrozenWaterContentValues", [])
