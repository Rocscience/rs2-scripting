from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class JohansenLu(PropertyProxy):
	def getSoilType(self) -> ThermalSoilType:
		return ThermalSoilType(self._getEnumEThermalSoilTypeProperty("MP_THERMAL_SOIL_TYPE_JOHANSEN_LU"))
	def setSoilType(self, value: ThermalSoilType):
		return self._setEnumEThermalSoilTypeProperty("MP_THERMAL_SOIL_TYPE_JOHANSEN_LU", value)
	def getQuartzContent(self) -> float:
		return self._getDoubleProperty("MP_THERMAL_QUARTZ_CONTENT")
	def setQuartzContent(self, value: float):
		return self._setDoubleProperty("MP_THERMAL_QUARTZ_CONTENT", value)
	def setProperties(self, SoilType : ThermalSoilType = None, QuartzContent : float = None):
		if SoilType is not None:
			self._setEnumEThermalSoilTypeProperty("MP_THERMAL_SOIL_TYPE_JOHANSEN_LU", SoilType)
		if QuartzContent is not None:
			self._setDoubleProperty("MP_THERMAL_QUARTZ_CONTENT", QuartzContent)
	def getProperties(self):
		return {
		"SoilType" : self.getSoilType(), 
		"QuartzContent" : self.getQuartzContent(), 
		}
