from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class BrooksWaterContent(PropertyProxy):
	def getPoreSizeIndex(self) -> float:
		return self._getDoubleProperty("MP_PORE_SIZE_INDEX_THERMAL")
	def setPoreSizeIndex(self, value: float):
		return self._setDoubleProperty("MP_PORE_SIZE_INDEX_THERMAL", value)
	def getBubblingPressure(self) -> float:
		return self._getDoubleProperty("MP_BUBBLING_PRESSURE_THERMAL")
	def setBubblingPressure(self, value: float):
		return self._setDoubleProperty("MP_BUBBLING_PRESSURE_THERMAL", value)
	def setProperties(self, PoreSizeIndex : float = None, BubblingPressure : float = None):
		if PoreSizeIndex is not None:
			self._setDoubleProperty("MP_PORE_SIZE_INDEX_THERMAL", PoreSizeIndex)
		if BubblingPressure is not None:
			self._setDoubleProperty("MP_BUBBLING_PRESSURE_THERMAL", BubblingPressure)
	def getProperties(self):
		return {
		"PoreSizeIndex" : self.getPoreSizeIndex(), 
		"BubblingPressure" : self.getBubblingPressure(), 
		}
