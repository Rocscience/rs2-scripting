from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class Johansen(PropertyProxy):
	def getSoilType(self) -> ThermalSoilType:
		return ThermalSoilType(self._getEnumEThermalSoilTypeProperty("MP_THERMAL_SOIL_TYPE_JOHANSEN"))
	def setSoilType(self, value: ThermalSoilType):
		return self._setEnumEThermalSoilTypeProperty("MP_THERMAL_SOIL_TYPE_JOHANSEN", value)
	def getQuartzContent(self) -> float:
		return self._getDoubleProperty("MP_THERMAL_QUARTZ_CONTENT")
	def setQuartzContent(self, value: float):
		return self._setDoubleProperty("MP_THERMAL_QUARTZ_CONTENT", value)
	def getDryConductivity(self) -> float:
		return self._getDoubleProperty("MP_THERMAL_DRY_CONDUCTIVITY")
	def setDryConductivity(self, value: float):
		return self._setDoubleProperty("MP_THERMAL_DRY_CONDUCTIVITY", value)
	def getSaturatedUnfrozenConductivity(self) -> float:
		return self._getDoubleProperty("MP_THERMAL_SATURATED_CONDUCTIVITY")
	def setSaturatedUnfrozenConductivity(self, value: float):
		return self._setDoubleProperty("MP_THERMAL_SATURATED_CONDUCTIVITY", value)
	def getSaturatedFrozenConductivity(self) -> float:
		return self._getDoubleProperty("MP_THERMAL_SATURATED_FROZEN_CONDUCTIVITY")
	def setSaturatedFrozenConductivity(self, value: float):
		return self._setDoubleProperty("MP_THERMAL_SATURATED_FROZEN_CONDUCTIVITY", value)
	def setProperties(self, SoilType : ThermalSoilType = None, QuartzContent : float = None, DryConductivity : float = None, SaturatedUnfrozenConductivity : float = None, SaturatedFrozenConductivity : float = None):
		if SoilType is not None:
			self._setEnumEThermalSoilTypeProperty("MP_THERMAL_SOIL_TYPE_JOHANSEN", SoilType)
		if QuartzContent is not None:
			self._setDoubleProperty("MP_THERMAL_QUARTZ_CONTENT", QuartzContent)
		if DryConductivity is not None:
			self._setDoubleProperty("MP_THERMAL_DRY_CONDUCTIVITY", DryConductivity)
		if SaturatedUnfrozenConductivity is not None:
			self._setDoubleProperty("MP_THERMAL_SATURATED_CONDUCTIVITY", SaturatedUnfrozenConductivity)
		if SaturatedFrozenConductivity is not None:
			self._setDoubleProperty("MP_THERMAL_SATURATED_FROZEN_CONDUCTIVITY", SaturatedFrozenConductivity)
	def getProperties(self):
		return {
		"SoilType" : self.getSoilType(), 
		"QuartzContent" : self.getQuartzContent(), 
		"DryConductivity" : self.getDryConductivity(), 
		"SaturatedUnfrozenConductivity" : self.getSaturatedUnfrozenConductivity(), 
		"SaturatedFrozenConductivity" : self.getSaturatedFrozenConductivity(), 
		}
