from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class CustomWaterContent(PropertyProxy):
	def setTemperatureVsUnfrozenWaterContentValues(self, temperature: list[float], unfrozenWaterContent: list[float]):
		return self._callFunction("setTemperatureVsUnfrozenWaterContentValues", [temperature, unfrozenWaterContent])
	def getTemperatureVsUnfrozenWaterContentValues(self) -> list[tuple[float,float]]:
		"""
		The first element in each tuple is the temperature.
		The second element in each tuple is the unfrozen water content.
		"""
		return self._callFunction("getTemperatureVsUnfrozenWaterContentValues", [])
